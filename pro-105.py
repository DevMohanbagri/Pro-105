import csv 
import math
with open('../csv/stdev-105.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#Removing the title from the dataset
data = file_data.pop(0)
print(data)

n = 0
def  mean(dataset):
    n = len(dataset)
    total = 0
    for x in dataset:
         total += float(x[1])
    
    mean = total/n
    return mean

# Squaring and getting the values
squared_list = []


for no in data:
    a = int(no)-mean(data)
    a = a**2
    squared_list.append(a)

#summing the squared list
sum = 0

for i in squared_list:
    sum += i

result = sum/(n-1)

standard_deviation = math.sqrt(result)

print("Standard Deviation = "+str(standard_deviation))