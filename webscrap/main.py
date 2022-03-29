import requests
from bs4 import BeautifulSoup
from pandas import DataFrame

l = []
base_url="https://www.remax.gr/properties/1269-?Property_page="
for page in range(1,3,1):
    r=requests.get(base_url+str(page))
    print(base_url+str(page))
    c= r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div",{"class":"information-wrapper"})
    for item in all:
        d = {}
        try:
            d["Είδος ακινήτου"] = item.find("div",{"class":"property-type"}).text.replace("\n","")
        except:
            d["Είδος ακινήτου"] = None

        try:
            d["Τοποθεσία"] = item.find("div",{"class":"property-location"}).text.replace("\n","").replace(" ","")
        except:
            d["Τοποθεσία"] = None

        try:
            d["Τιμή"] = item.find("div",{"class":"property-price"}).text.replace("\n","").replace(" ","")
        except:
            d["Τιμή"] = None

        try:
            d["Δωμάτια"] = item.find("div",{"class":"rooms"}).text.replace("\n","").replace(" ","").replace("\t","")
        except:
            d["Δωμάτια"] = None

        try:
            d["Μπάνια"] = item.find("div",{"class":"bathrooms"}).text.replace("\n","").replace(" ","").replace("\t","")
        except:
            d["Μπάνια"] = None

        try:
            d["Όροφος"] = item.find("div",{"class":"floor"}).text.replace("\n","").replace(" ","").replace("\t","")
        except:
            d["Όροφος"] = None

        try:
            d["Εμβαδό"] = item.find("div",{"class":"area"}).text.replace("\n","").replace(" ","").replace("\t","")
        except:
            d["Εμβαδό"] = None
        l.append(d)




df = DataFrame(l)
df.to_csv("data.csv")
print(df)
