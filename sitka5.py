import csv
from datetime import datetime

valley_file=open('death_valley_2018_simple.csv','r')
sitka_file=open('sitka_weather_2018_simple.csv','r')

infile_valley=csv.reader(valley_file,delimiter=',')
infile_sitka=csv.reader(sitka_file,delimiter=',')

header_valley=next(infile_valley)
header_sitka=next(infile_sitka)

dates_valley=[]
highs_valley=[]
lows_valley=[]

dates_sitka=[]
highs_sitka=[]
lows_sitka=[]

for line in infile_valley:
    try:
        for index,col_head in enumerate(header_valley):
            if col_head == 'NAME':
                title_index=index
            if col_head == 'DATE':
                date=(datetime.strptime(line[index],'%Y-%m-%d'))
            if col_head=='TMAX':
                high=int(line[index])
            if col_head=='TMIN':
                low=int(line[index])
    except ValueError: #itll carry this out if its not one of the above, and if it passes first it passes control to else
        print(f'Missing data for {line}') #this works, and if we do 'date' well need to put ddate first in the order of the for loop
    else:
        title_valley=line[title_index]
        dates_valley.append(date)
        highs_valley.append(high)
        lows_valley.append(low)

for line in infile_sitka:
    try:
        for index,col_head in enumerate(header_sitka):
            if col_head == 'NAME':
                title_index=index
            if col_head == 'DATE':
                date=(datetime.strptime(line[index],'%Y-%m-%d'))
            if col_head=='TMAX':
                high=int(line[index])
            if col_head=='TMIN':
                low=int(line[index])
    except ValueError: #itll carry this out if its not one of the above, and if it passes first it passes control to else
        print(f'Missing data for {line}') #this works, and if we do 'date' well need to put ddate first in the order of the for loop
    else:
        title_sitka=line[title_index]
        dates_sitka.append(date)
        highs_sitka.append(high)
        lows_sitka.append(low)


import matplotlib.pyplot as plt

fig=plt.figure()

plt.subplot(2,1,1) 
plt.plot(dates_valley,highs_valley,c='red')
plt.plot(dates_valley,lows_valley,c='blue')
plt.fill_between(dates_valley,highs_valley,lows_valley,facecolor='blue',alpha=0.1)
plt.tick_params(axis="both",labelsize=10)
plt.title(title_valley)


plt.subplot(2,1,2)
plt.plot(dates_sitka,highs_sitka,c="red")
plt.plot(dates_sitka,lows_sitka,c='blue')
plt.fill_between(dates_sitka,highs_sitka,lows_sitka,facecolor='blue',alpha=0.1)
plt.tick_params(axis="both",labelsize=10)
plt.title(title_sitka)

plt.suptitle("Temperature Comparison Between DEATH VALLEY, CA US and SITKA AIRPORT, AK US")

fig.autofmt_xdate()
plt.show()