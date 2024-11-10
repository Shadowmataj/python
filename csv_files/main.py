import csv
import statistics

import pandas

#USING FILE MANAGEMENT
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)

#USING CSV MODULE
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)


#USING PANDAS MODULE
# data = pandas.read_csv("weather_data.csv")

# print(data)
# data_list = data["temp"].to_list()
# print(data_list)
# average_temp = data["temp"].mean()
# print(round(average_temp, 2))
# max_temp = data["temp"].max()
# print(max_temp)

#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
#
# monday = data[data.day == "Monday"]
# monday_celsius = monday.temp[0]
# monday_fahrenheit = (monday_celsius * 9/5) + 32
# print(monday_fahrenheit)


#creating a Dataframe with pandas module
#
# data_dict =  {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
#
# data_csv = data.to_csv()
#
# print(data)
# print("\n")
# print(data_csv)


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241110.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

new_data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}

new_data = pandas.DataFrame(new_data_dict)
new_data.to_csv("squirrel_count.csv")