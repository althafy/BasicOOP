import json
from this import d
import pandas as pd
import os

path = r"C:\Users\user\Downloads\Homework - Basic OOP\Modul6-Homework"

class Preprocessing:
   
    def __init__(self, path):
        self.path = path

    
    def listingFile(self):
        listfile = []
        for i in os.listdir(self.path):
            if "json" in i:                
                listfile.append(i)
    
        return listfile
    
    def listingData(self, listfile):
        listdata = []
        for j in listfile:
            with open(self.path+ "/" + j, "r") as file:
                data = json.load(file)
                listdata.append(data["data"])
                
        return listdata

    def transformData(self, listdata):
        totalsalesJakarta, totalsalesBalikpapan, totalsalesMedan   = 0, 0, 0

        for k in range(len(listdata)):
            if listdata[k]["lokasi"] == "Jakarta":
                totalsalesJakarta += listdata[k]["sales"]
            elif listdata[k]["lokasi"] == "Balikpapan":
                totalsalesBalikpapan += listdata[k]["sales"]
            else:
                totalsalesMedan += listdata[k]["sales"]
        

        dataframe = [["Jakarta", totalsalesJakarta], ["Balikpapan", totalsalesBalikpapan], 
                    ["Medan", totalsalesMedan]]
        df = pd.DataFrame(dataframe, columns=["Kota", "Total Sales"])
        df.to_csv(r"C:\Users\user\OneDrive\Documents\Homework Data Engineering 2\Basic OOP\Total Sales Final.csv",
                 index = False)

        return df


a = Preprocessing(path)
b = a.listingFile()
c = a.listingData(b)
d = a.transformData(c)
