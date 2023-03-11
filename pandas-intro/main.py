import csv

# METHOD 1
with open('./weather_data.csv') as data_file:
    data = data_file.readlines()

# METHOD 2
with open('./weather_data.csv') as data_file2:
    data2 = csv.reader(data_file2)
    temperatures = []
    for row in data2:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

import pandas

# METHOD 3 (BEST!)
data3 = pandas.read_csv('./weather_data.csv')
# print(data3)
temp_list = data3['temp'].to_list()
# print(temp_list)
# print(data3['temp'].mean())
# print(data3[data3.temp == data3.temp.max()])
# print(data3[data3.temp == 12])
# print(data3[data3.temp > 20])

monday = data3[data3.day == 'Monday']
monday_temp = monday.temp
print(monday_temp)