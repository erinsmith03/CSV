import csv

sitka_file=open('sitka_weather_07-2018_simple.csv','r')

infile_csv=csv.reader(sitka_file,delimiter=',')

header_row=next(infile_csv)
print(header_row)

for index,col_header in enumerate(header_row):
    print(index,col_header)

#extract max temp column into list
#for loop
max_temps=[]
for line in infile_csv:
    max_temp=int(line[5])
    max_temps.append(max_temp)

print(max_temps[:5])
#function called 'enumerate': allows us to see index value along with value in list

import matplotlib.pyplot as plt

plt.plot(max_temps,c='red') #this creates line chart, argument it needs is list of values, and it will create graph
plt.title("Daily high temps, July 2018",fontsize=16)
plt.xlabel("")
plt.ylabel("Temps (F)",fontsize=16)
plt.tick_params(axis="both",which='major',labelsize=16) #tick marks, only want major wones

plt.show()




