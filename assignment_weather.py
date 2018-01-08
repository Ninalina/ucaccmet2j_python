# -*- coding: utf-8 -*-
import json

with open ('precipitation.json') as precipitation_file:
   data = json.load(precipitation_file)
   
#looping over all the dictionary entries   
   for item in data:
       #datatype, date, station, value = item
#selecting the items with the seattle code
       if item["station"] == "GHCND:US1WAKG0038":
           print (item)

#creating a list with the months           
seattle_list = list()

#select the items in seattle and put them in the empty list
for item in data:
    if item["station"] == "GHCND:US1WAKG0038":
       seattle_list.append(item)

#create another list with the precipitations
seattle_monthly_totals = [0]*12    #create a list with 12 spots 
for item in seattle_list:
    month = int(item["date"][5:7]) #indicate the position of the month in each item
    seattle_monthly_totals[month-1] += item["value"] #add all the values for each month
print (seattle_monthly_totals)

seattle_total = sum(seattle_monthly_totals) #calculate the sum of the precipitation over the whole year

print (seattle_total)

for item in seattle_monthly_totals: 
    relative_precipitation_per_month = (item/seattle_total) * 100 #calculate the relative precipitation per month, *100 to make a percentage out of it
    print (relative_precipitation_per_month)
    

with open("file.json", "w") as file:
    json.dump({"Seattle": {"totalYearlyPrecipitation": seattle_total, "totalMonthlyPrecipitation": seattle_monthly_totals, "relativeMonthlyPrecipitation": relative_precipitation_per_month}}, file)
