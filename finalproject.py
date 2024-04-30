###meteogram
#import modules and files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pygrib
import csv

#stream = 'VicksburgStrmFlow.txt'
#recordedsf = pd.read_csv('C:/Users/esega/Downloads/VicksburgStrmFlow.txt')
#median = pd.read_csv('C:/Users/esega/Downloads/VicksburgMedian.txt')
#vicks = pd.read_csv('C:/Users/esega/Downloads/Vicksburg_flow.xlsx')
#file_path = 'C:/Users/esega/Downloads/NewVicksburgStrmFlow.txt'
#file_path = 'C:/Users/esega/Downloads/NewVicksburgMedian.txt'

f4 = open('NewVicksburgStrmFlow.txt', 'r')
f5 = open('NewVicksburgMedian.txt', 'r')

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
    
#data = [eval(i) for i in data]
#daily = data.splice[0,528,23]
#date = [eval(i) for i in date]
    


#plot and label the graph
plt.figure(figsize=(10,10))
plt.plot(data)
plt.xlabel('Hours Since 5/07/11 0z')
plt.ylabel('Cubic Feet/Second')
plt.title('Vicksburg Streamflow 05/07 - 05/28')
plt.show()


