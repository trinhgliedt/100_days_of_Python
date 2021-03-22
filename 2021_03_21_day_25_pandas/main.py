# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperture = []
#     for row in data:
#         if row[1] != "temp":
#             temperture.append(int(row[1]))
#     print(temperture)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)

print(data["temp"].max())
print(data["temp"].max())
