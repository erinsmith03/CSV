
import csv
from datetime import datetime

sitka_file=open('sitka_weather_2018_simple.csv','r')

infile_csv=csv.reader(sitka_file,delimiter=',')

header_row=next(infile_csv)
print(header_row)

for index,col_header in enumerate(header_row):
    print(index,col_header)

#extract max temp column into list
#for loop
dates=[]
max_temps=[]
min_temps=[]

#need to convert dates in csv file to date format
some_date=datetime.strptime('2018-07-01', '%Y-%m-%d')
print(type(some_date))


for line in infile_csv:
    dates.append(datetime.strptime(line[2],'%Y-%m-%d'))
    max_temps.append(int(line[5]))
    min_temps.append(int(line[6]))

    

import matplotlib.pyplot as plt

fig=plt.figure()

#figure is another thing we need besides the graph
#plt.plot is just graph
#have to match in terms of # of elements 
plt.plot(dates,max_temps,c='red',alpha=0.5) #this creates line chart, argument it needs is list of values, and it will create graph
plt.plot(dates,min_temps,c='blue',alpha=0.5) #the alpha makes it lighter

#this will create two lines on chart

plt.fill_between(dates,max_temps,min_temps,facecolor='blue',alpha=0.1) #this will fill in between 

plt.title("Daily low and high temps - 2018",fontsize=16)
plt.xlabel("Dates",fontsize=16)
plt.ylabel("Temps (F)",fontsize=16)
plt.tick_params(axis="both",which='major',labelsize=16) #tick marks, only want major dates not all


fig.autofmt_xdate() #creates date in diagnol format so they dotn overlap 
plt.show()

plt.subplot(2,1,1) #we want 2 rows, 1 column, and give it index value of chart we want to work on (there will be 2 charts)
plt.plot(dates,max_temps,c='red')
plt.title("Highs")


plt.subplot(2,1,2)
plt.plot(dates,min_temps,c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows for Sitka, Alaska")

plt.show()


