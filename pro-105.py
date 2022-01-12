import csv 
import math
with open('../csv/stdev-105.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


    
data = file_data.pop(0)



n = len(data)
total = 0
for x in data:
    total += int(x[1])
    print(x)
mean = total/n
print(mean)

# Squaring and getting the values
squared_list = []
print(data)

for x in data:
    a = x-mean(data)
    a = a**2
    squared_list.append(a)

#summing the squared list
sum = 0

for i in squared_list:
    sum += i

result = sum/(n-1)

standard_deviation = math.sqrt(result)

print("Standard Deviation = "+str(standard_deviation))
