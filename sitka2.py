import csv
from datetime import datetime

sitka_file=open('sitka_weather_07-2018_simple.csv','r')

infile_csv=csv.reader(sitka_file,delimiter=',')

header_row=next(infile_csv)
print(header_row)

for index,col_header in enumerate(header_row):
    print(index,col_header)

#extract max temp column into list
#for loop
max_temps=[]
dates=[]

#need to convert dates in csv file to date format
some_date=datetime.strptime('2018-07-01', '%Y-%m-%d')
print(type(some_date))


for line in infile_csv:
    dates.append(datetime.strptime(line[2],'%Y-%m-%d'))
    max_temps.append(int(line[5]))
print(dates)
print(max_temps)
    

import matplotlib.pyplot as plt

fig=plt.figure() 

#figure is another thing we need besides the graph
#plt.plot is just graph
#have to match in terms of # of elements 
plt.plot(dates,max_temps,c='red') #this creates line chart, argument it needs is list of values, and it will create graph
plt.title("Daily high temps, July 2018",fontsize=16)
plt.xlabel("Dates",fontsize=16)
plt.ylabel("Temps (F)",fontsize=16)
plt.tick_params(axis="both",which='major',labelsize=16) #tick marks, only want major dates not all


fig.autofmt_xdate() #creates date in diagnol format so they dotn overlap 
plt.show()




