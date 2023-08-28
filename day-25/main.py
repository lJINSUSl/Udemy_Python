# with open('weather_data.csv') as file:
#     print(file.readlines())
#
# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     num = 0
#     for row in data:
#         if num >0:
#             temperatures.append(int(row[1]))
#         num +=1
#     print(temperatures)

import pandas as pd

# data = pd.read_csv('weather_data.csv')
#
#
# # print(data['temp'])
# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == 'Monday']
# print(monday.temp)
# temp = float(monday.temp)
# fahrenheit = (temp *9/5) + 32
# print(fahrenheit)

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
x= data["Primary Fur Color"].value_counts()
p= pd.DataFrame(x)
print(p)