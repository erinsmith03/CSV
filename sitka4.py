
import csv
from datetime import datetime

sitka_file=open('death_valley_2018_simple.csv','r')

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

#we need to do try/except method for VALUE error
for line in infile_csv:
    try:
        high=int(line[4])
        low=int(line[5])
        date=(datetime.strptime(line[2],'%Y-%m-%d'))
    except ValueError: #itll carry this out if its not one of the above, and if it passes first it passes control to else
        print(f'Missing data for {line}') #this works, and if we do 'date' well need to put ddate first in the order of the for loop
    else:
        dates.append(datetime.strptime(line[2],'%Y-%m-%d'))
        max_temps.append(high)
        min_temps.append(int(line[5]))

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




