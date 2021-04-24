import requests, csv
from bs4 import BeautifulSoup
import pandas as pd

userage = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

r = requests.get("https://www.yellowpages.com/los-angeles-ca/auto-repair",headers=userage)

soup = BeautifulSoup(r.text,'lxml')

listings = soup.find_all("div",class_="srp-listing")

tname = []
tcatego = []
tphonum = []
tstadr = []
tlocality = []

for listing in listings:

    try:
        name = listing.find("a",class_="business-name").span.text
        catego = listing.find("div",class_="categories").text
        phonum = listing.find("div",class_="phones phone primary").text
        stadr = listing.find("div",class_="street-address").text
        locality = listing.find("div",class_="locality").text

        tname.append(name)
        tcatego.append(catego)
        tphonum.append(phonum)
        tstadr.append(stadr)
        tlocality.append(locality)

    except:
        pass

data = {
    "Name":tname,
    "Category":tcatego,
    "Phone Number":tphonum,
    "Street Address":tstadr,
    "Locality":tlocality
}

df = pd.DataFrame(data)

df.to_csv('exported.csv',index=True)
print(df)
