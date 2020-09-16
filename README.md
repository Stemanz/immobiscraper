# immobiscraper
A simple scraper for the Italian Immobiliare.it website

Use like:

```Python
url = "https://www.immobiliare.it/vendita-case/milano/forlanini/?criterio=rilevanza"
case = Immobiliare(url)
case.find_all_houses()
df = case.df_
```

It defaults to verbose, telling you what it finds or fails to find.

Most likely, failing to find data depends on the data not being present in the page in the first place, even if I am aware that some data is still not being pulled and this is still a _work in progress_.

An example output (scroll down to the bottom to see the resulting ```DataFrame```).

```
Processing page 1
Processing page 2
Processing page 3
Processing page 4
Processing page 5
Processing page 6
Processing page 7
Processing page 8
Processing page 9
Processing page 10
Processing page 11
Processing page 12
Processing page 13
Processing page 14
All retrieved urls in attribute 'urls_'
Found 325 houses matching criteria.
Price available upon request for https://www.immobiliare.it/annunci/82648691/
Price available upon request for https://www.immobiliare.it/annunci/81423851/
Car spot/box available upon request for https://www.immobiliare.it/annunci/81652136/
Energy efficiency still pending for https://www.immobiliare.it/annunci/80742027/ 
Energy efficiency still pending for https://www.immobiliare.it/annunci/80748177/ 
Can't get energy efficiency from https://www.immobiliare.it/annunci/82320042/
Can't get energy efficiency from https://www.immobiliare.it/annunci/81933976/
Can't get energy efficiency from https://www.immobiliare.it/annunci/81933158/
Can't get energy efficiency from https://www.immobiliare.it/annunci/81674994/
Energy efficiency still pending for https://www.immobiliare.it/annunci/80603469/ 
Energy efficiency still pending for https://www.immobiliare.it/annunci/78653095/ 
Energy efficiency still pending for https://www.immobiliare.it/annunci/77597800/ 
Price available upon request for https://www.immobiliare.it/annunci/81171609/
Price available upon request for https://www.immobiliare.it/annunci/81761272/
Price available upon request for https://www.immobiliare.it/annunci/81729602/
Energy efficiency still pending for https://www.immobiliare.it/annunci/77772230/ 
Energy efficiency still pending for https://www.immobiliare.it/annunci/79773681/ 
Energy efficiency still pending for https://www.immobiliare.it/annunci/81455099/ 
Energy efficiency still pending for https://www.immobiliare.it/annunci/78414525/ 
Energy efficiency still pending for https://www.immobiliare.it/annunci/79877917/ 
Energy efficiency still pending for https://www.immobiliare.it/annunci/80756707/ 
Energy efficiency still pending for https://www.immobiliare.it/annunci/80312691/ 
Auction house: no area info https://www.immobiliare.it/annunci/81877556/
Can't get energy efficiency from https://www.immobiliare.it/annunci/81877556/
Energy efficiency still pending for https://www.immobiliare.it/annunci/80311011/ 
Energy efficiency still pending for https://www.immobiliare.it/annunci/81164299/ 
Energy efficiency still pending for https://www.immobiliare.it/annunci/80024333/ 
Energy efficiency still pending for https://www.immobiliare.it/annunci/80025535/ 
Energy efficiency still pending for https://www.immobiliare.it/annunci/80603915/ 
Price available upon request for https://www.immobiliare.it/annunci/81897014/
Price available upon request for https://www.immobiliare.it/annunci/81761274/
Energy efficiency still pending for https://www.immobiliare.it/annunci/81570145/ 
Can't get energy efficiency from https://www.immobiliare.it/annunci/78414923/
Energy efficiency still pending for https://www.immobiliare.it/annunci/81686758/ 
Price available upon request for https://www.immobiliare.it/annunci/81900548/
Can't get energy efficiency from https://www.immobiliare.it/annunci/82460368/
Can't get energy efficiency from https://www.immobiliare.it/annunci/81739222/
Can't get energy efficiency from https://www.immobiliare.it/annunci/81739116/
Can't get energy efficiency from https://www.immobiliare.it/annunci/78787755/
Can't get energy efficiency from https://www.immobiliare.it/annunci/82155458/
Can't get energy efficiency from https://www.immobiliare.it/annunci/82131788/
Can't get energy efficiency from https://www.immobiliare.it/annunci/81570629/
Can't get energy efficiency from https://www.immobiliare.it/annunci/82131834/
Can't get energy efficiency from https://www.immobiliare.it/annunci/82251622/
Can't get area info from url https://www.immobiliare.it/annunci/80856545/
Can't get energy efficiency from https://www.immobiliare.it/annunci/78834541/
Can't get energy efficiency from https://www.immobiliare.it/annunci/78968119/
Can't get energy efficiency from https://www.immobiliare.it/annunci/79232875/
Can't get energy efficiency from https://www.immobiliare.it/annunci/82642983/
Can't get energy efficiency from https://www.immobiliare.it/annunci/82351192/
Can't get energy efficiency from https://www.immobiliare.it/annunci/82642953/
Energy efficiency still pending for https://www.immobiliare.it/annunci/82643629/ 
Can't get energy efficiency from https://www.immobiliare.it/annunci/82305834/
Can't get area info from url https://www.immobiliare.it/annunci/p-153877/
Can't get area info from url https://www.immobiliare.it/annunci/p-148426/
Energy efficiency still pending for https://www.immobiliare.it/annunci/p-148426/ 
Price available upon request for https://www.immobiliare.it/annunci/p-146236/
Can't get area info from url https://www.immobiliare.it/annunci/p-146236/
Can't get area info from url https://www.immobiliare.it/annunci/p-154775/
Car spot/box available upon request for https://www.immobiliare.it/annunci/82583761/
Can't get area info from url https://www.immobiliare.it/annunci/p-148464/
Car spot/box available upon request for https://www.immobiliare.it/annunci/p-148464/
Can't get area info from url https://www.immobiliare.it/annunci/p-152658/
Can't get area info from url https://www.immobiliare.it/annunci/81570789/
Can't get area info from url https://www.immobiliare.it/annunci/p-146556/
Can't get area info from url https://www.immobiliare.it/annunci/p-154081/
Can't get area info from url https://www.immobiliare.it/annunci/p-155271/
Can't get area info from url https://www.immobiliare.it/annunci/p-155265/
Can't get area info from url https://www.immobiliare.it/annunci/p-153478/
Can't get area info from url https://www.immobiliare.it/annunci/p-155273/
Can't get area info from url https://www.immobiliare.it/annunci/p-135964/
Can't get area info from url https://www.immobiliare.it/annunci/p-154471/
Can't get area info from url https://www.immobiliare.it/annunci/p-149688/
Can't get area info from url https://www.immobiliare.it/annunci/p-152572/
Can't get energy efficiency from https://www.immobiliare.it/annunci/p-152572/
Car spot/box available upon request for https://www.immobiliare.it/annunci/82370712/
Car spot/box available upon request for https://www.immobiliare.it/annunci/82494528/
Can't get energy efficiency from https://www.immobiliare.it/annunci/68189575/
Can't get energy efficiency from https://www.immobiliare.it/annunci/80734569/
Can't get energy efficiency from https://www.immobiliare.it/annunci/80174869/
Can't get area info from url https://www.immobiliare.it/annunci/p-153797/
Can't get energy efficiency from https://www.immobiliare.it/annunci/81327473/
Price available upon request for https://www.immobiliare.it/annunci/66204875/
Price available upon request for https://www.immobiliare.it/annunci/72372656/
Can't get energy efficiency from https://www.immobiliare.it/annunci/80362037/
Price available upon request for https://www.immobiliare.it/annunci/62478258/
Can't get energy efficiency from https://www.immobiliare.it/annunci/82361386/
Can't get energy efficiency from https://www.immobiliare.it/annunci/79551681/
Price available upon request for https://www.immobiliare.it/annunci/71351380/
Price available upon request for https://www.immobiliare.it/annunci/77798194/
Can't get energy efficiency from https://www.immobiliare.it/annunci/81936810/
Can't get energy efficiency from https://www.immobiliare.it/annunci/76436520/
Can't get energy efficiency from https://www.immobiliare.it/annunci/76436370/
Can't get energy efficiency from https://www.immobiliare.it/annunci/76436446/
Can't get energy efficiency from https://www.immobiliare.it/annunci/76436448/
Can't get energy efficiency from https://www.immobiliare.it/annunci/76436522/
Price available upon request for https://www.immobiliare.it/annunci/80602305/
Can't get energy efficiency from https://www.immobiliare.it/annunci/78986891/
Can't get energy efficiency from https://www.immobiliare.it/annunci/80729327/
Price available upon request for https://www.immobiliare.it/annunci/71099174/
Price available upon request for https://www.immobiliare.it/annunci/60225598/
Can't get area info from url https://www.immobiliare.it/annunci/80419029/
Energy efficiency still pending for https://www.immobiliare.it/annunci/80419029/ 
Can't get area info from url https://www.immobiliare.it/annunci/78871661/
Energy efficiency still pending for https://www.immobiliare.it/annunci/78871661/ 
Results stored in attribute 'df_'
```
(https://github.com/Stemanz/immobiscraper/raw/master/img/Screenshot%202020-09-16%20at%2010.50.08.png)
