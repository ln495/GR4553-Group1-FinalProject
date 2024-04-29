###meteogram

##Import modules and open files as variables
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pygrib
import csv

f4 = open("NewVicksburgStrmFlow.txt", 'r')
f5 = open("NewVicksburgMedian.txt", 'r')



##Read file lines and store as variable, then create empty arrays to store columns of data
lines = f4.readlines()
usgs = []
station = []
date = []
time =[]
timezone = []
data = []

##Split individual parts of each line into columns within the file, 
##then store items from each column into empty array
for i in range (len(lines)):
    num = lines[i]
    splitnum = num.split()
    usgs = np.append(usgs, splitnum[0])
    station = np.append(station, splitnum[1])
    date = np.append(date, splitnum[2])
    time = np.append(time, splitnum[3])
    timezone = np.append(timezone, splitnum[4])
    data = np.append(data, splitnum[5])
    
##Convert each item in the data array into usable, numeric values
data = [eval(i) for i in data]

##Create the stream flow figure (per hour from 5/7/11-5/28/11) and save it
plt.figure(figsize=(7,7))
plt.plot(data)
plt.xlabel('Hours since 5/7/2011')
plt.ylabel('Cubic Feet/Second')
plt.title('MS River Stream Flow (5/7 - 5/28/11)')
#plt.show()
plt.savefig('finalproject_strmflow.png')



##Read lines from next file and store as a variable, then create a new set of empty arrays
##to store the new file's columns as items
lines2 = f5.readlines()
usgs2 = []
station2 = []
arr1 = []
arr2 = []
month = []
day = []
year1 = []
year2 = []
arr4 = []
data2 = []

##Split individual parts of each line into columns within the second file, 
##then store items from each column into empty array
for i in range(len(lines2)):
    num = lines2[i]
    splitnum = num.split()
    usgs2 = np.append(usgs2, splitnum[0])
    station2 = np.append(station2, splitnum[1])
    arr1 = np.append(arr1, splitnum[2])
    arr2 = np.append(arr2, splitnum[3])
    month = np.append(month, splitnum[4])
    day = np.append(day, splitnum[5])
    year1 = np.append(year1, splitnum[6])
    year2 = np.append(year2, splitnum[7])
    arr4 = np.append(arr4, splitnum[8])
    data2 = np.append(data2, splitnum[9])

##Convert each item in the next array into usuable, numeric values
data2 = [eval(i) for i in data2]

##Split the first array into 24 smaller arrays (for 24hrs per day)
newData = np.array_split(data, len(data)/24)


##Create the stream flow vs median (per day) figure and save it 
plt.figure(figsize=(7,7))
plt.plot(newData)
plt.plot(data2, label='Median')
plt.xlabel('Days')
plt.ylabel('Cubic Feet/Second')
plt.legend()
plt.title('Median vs. 2011 Flooding Stream Flow')
#plt.show()
plt.savefig('finalproject_medianstrmflow.png')


##Close files
f4.close()
f5.close()

