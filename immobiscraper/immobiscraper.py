__version__ = "0.1.1"

from io import BytesIO
from bs4 import BeautifulSoup
from collections import namedtuple
import requests
import re
import pandas as pd
import numpy as np
import time


class Immobiliare():
    
    def __init__(self, url, *,
                 verbose=True,
                 min_house_cost=10_000, # threshold below which the house price
                                        # is assumed to be guessed wrong
                 browse_all_pages=True, # keeps browsing all ads
                 
                 area_not_found =0, # sets the default value if parameter is not found
                 price_not_found=np.nan, # sets the default value if parameter is not found
                 floor_not_found=0,  # sets the default value if parameter is not found
                 car_not_found=0,  # sets the default value if parameter is not found
                 energy_not_found="n/a", # sets the default value if parameter is not found
                 invalid_price_per_area=0, # sets the default value if parameter is not found
                 wait=100, # milliseconds wait for each website query
    ):
        """ By default, if not found, only if the apartment price is not found
        that is set to np.nan, so that all useless entries can be removed by DataFrame.dropna().
        All other data is set to manageable entity so that the row is not dropped just because, for example,
        energy information is not retrievable/available.
        """
        
        self.url = url
        self.verbose = verbose
        self.min_house_cost = min_house_cost #below, we pulled the wrong house price
        self.browse_all_pages = browse_all_pages
        self.wait = wait/1000
        
        self.area_not_found  = area_not_found
        self.price_not_found = price_not_found
        self.floor_not_found = floor_not_found
        self.car_not_found   = car_not_found
        self.energy_not_found = energy_not_found
        self.invalid_price_per_area = invalid_price_per_area
        
    def _say(self, *args, **kwargs):
        if self.verbose:
            print(*args, **kwargs)


    def get_all_urls(self):
        pattern = re.compile("\d+\/$")
        urls_ = []
        
        # first page
        self._say("Processing page 1")
        page = self._get_page(self.url)
        
        page.seek(0)
        soup = BeautifulSoup(page, "html.parser")
        
        for link in soup.find_all("a"):
            time.sleep(self.wait)
            l = link.get("href")

            if l is None:
                continue

            if "https" in l and "annunci" in l:
                if pattern.search(l):
                    urls_.append(l)
                    
        if self.browse_all_pages:
            # trying other pages
            for i in range(2, 10_000): #that's enough of pages
                self._say(f"Processing page {i}")
                curr_url = self.url + f"&pag={i}"

                t = self._get_text(curr_url).lower()

                if "404 not found" in t:
                    self.urls_ = urls_
                    break

                else:
                    page = self._get_page(curr_url)
                    page.seek(0)
                    soup = BeautifulSoup(page, "html.parser")

                for link in soup.find_all("a"):
                    l = link.get("href")

                    if l is None:
                        continue

                    if "https" in l and "annunci" in l:
                        if pattern.search(l):
                            urls_.append(l)

        self.urls_ = urls_    
        self._say("All retrieved urls in attribute 'urls_'")
        self._say(f"Found {len(urls_)} houses matching criteria.")

    

    @staticmethod
    def _get_page(url):
        
        req = requests.get(url, allow_redirects=False)
        page = BytesIO()
        page.write(req.content)
        
        return page
    
    
    @staticmethod
    def _get_text(sub_url):

        req = requests.get(sub_url, allow_redirects=False)
        page = BytesIO()
        page.write(req.content)

        page.seek(0)
        soup = BeautifulSoup(page, "html.parser")
        
        text = soup.get_text() #?? OK on Mac, mayhem on Windows

        # compacting text
        t = text.replace("\n", "")
        for _ in range(50): # that would be sufficient..
            t = t.replace("  ", " ")
        
        return t
    
    
    def _get_data(self, sub_url):
        """ This gets data from *one* of the sub-urls
        """
        
        t = self._get_text(sub_url).lower()
        
        # costo appartamento ========== #
        # ============================= #
        cost_patterns = (
            "€ (\d+\.\d+\.\d+)", #if that's more than 1M €
            "€ (\d+\.\d+)",
        )
        
        for pattern in cost_patterns:
            cost_pattern = re.compile(pattern)
        
            try:
                cost = cost_pattern.search(t)
                cost = cost.group(1).replace(".", "")
                break
            
            except AttributeError:
                continue
            
        if cost is None:
            if "prezzo su richiesta" in t:
                self._say(f"Price available upon request for {sub_url}")
                cost = self.price_not_found
            else:
                self._say(f"Can't get price for {sub_url}")
                cost = self.price_not_found
        
        if cost is not None and cost is not self.price_not_found:
            # caso in cui ci siano le spese condominiali scambiate
            # per errore per costo della casa
            if int(cost) < self.min_house_cost:
                if "prezzo su richiesta" in t:
                    self._say(f"Price available upon request for {sub_url}")
                    cost = self.price_not_found
                else:
                    self._say(f"Too low house price: {int(cost)}? for {sub_url}")
                    cost = self.price_not_found

        
        # floor              ========== #
        # ============================= #
        floor_patterns = (
            "piano (\d{1,2})",
            "(\d{1,2}) piano",
            # if ultimo piano, floor number can be left out
            "(\d{1,2}) piani",
        )
        
        for pattern in floor_patterns:
            floor_pattern = re.compile(pattern)
            floor = floor_pattern.search(t)
            
            if floor is not None:
                floor = floor.group(1)
                break
        
        if "piano terra" in t:
            floor = 1 
        
        if "ultimo" in t:
            ultimo = True
        else:
            ultimo = False
        
        
        # square meters      ========== #
        # ============================= #
        area_pattern = re.compile("superficie(\d{1,4}) m")
        
        try:
            area = area_pattern.search(t)
            area = area.group(1)
        except AttributeError:
            area = self.area_not_found
            
            if "asta" in t:
                self._say(f"Auction house: no area info {sub_url}")
            else:
                self._say(f"Can't get area info from url {sub_url}")


        # classe energetica  ========== #
        # ============================= #
        energy_patterns = (
            "energetica ([a-z0-9+]{1,2}) ",
            "energetica([a-z0-9+]{1,2})",
        )
        
        def energy_acceptable(stringlike):
            if not stringlike.startswith(("A", "B", "C", "D", "E", "F", "G")):
                return False
            else:
                if len(stringlike) == 1:
                    return True
                else:
                    if not stringlike.endswith(
                        ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+")
                    ):
                        return False
                    else:
                        return True

        for i, pattern in enumerate(energy_patterns):
            energy_pattern = re.compile(pattern)
            matches = energy_pattern.findall(t)

            if matches is not None and len(matches) > 0:
                energy = matches[-1].upper()
                #print(f"**debug pattern {i}")
                #print(f"**debug match   {energy}")
                if energy_acceptable(energy):
                        break

        if energy is None or not energy_acceptable(energy): # in case everything fails
            if "in attesa di certificazione" in t:
                self._say(f"Energy efficiency still pending for {sub_url} ")
                energy = self.energy_not_found
            else:
                self._say(f"Can't get energy efficiency from {sub_url}")
                energy = self.energy_not_found
                
        
        # posto auto         ========== #
        # ============================= #
        car_patterns = (
        "post\S auto (\d{1,2})",
        )
        
        for pattern in car_patterns:
            car_pattern = re.compile(pattern)
            car = car_pattern.search(t)
            
            if car is not None:
                car = car.group(1)
                break
            
            if car is None:
                available_upon_request = re.compile("possibilit\S.{0,10}auto")
                if available_upon_request.search(t) is not None:
                    self._say(f"Car spot/box available upon request for {sub_url}")
                    car = 0
                else:
                    car = self.car_not_found
        
        
        # €/m²                      ========== #
        # ==================================== #
        try:
            price_per_area = round(int(cost) / int(area), 1)
        except:
            price_per_area = self.energy_not_found
        
        
        # packing the results       ========== #
        # ==================================== #
        House = namedtuple(
            "House", [
                "cost",
                "price_per_area",
                "floor",
                "area",
                "ultimo",
                "url",
                "energy",
                "posto_auto"
            ]
        )
        
        res = House(
            cost,
            price_per_area,
            floor,
            area,
            ultimo,
            sub_url,
            energy,
            car
        )

        return res
    
    
    def find_all_houses(self):
        
        if not hasattr(self, "urls_"):
            self.get_all_urls()
        
        all_results = []
        for url in self.urls_:
            try:
                all_results.append(self._get_data(url))
            except:
                print(f"offending_url='{url}'")
                raise
        
        
        self.df_ = pd.DataFrame(all_results)
        self._say("Results stored in attribute 'df_'")
