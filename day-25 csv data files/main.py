# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if data.line_num > 1:
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
import pandas
#
# data = pandas.read_csv("weather_data.csv")
# temperature = data["temp"].to_list()
#
# average_temp = sum(temperature) / len(temperature)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_fahr = (monday_temp * (9 / 2)) + 32
# print(monday_fahr)
#
# dict = {
#     "Names": ["Jonathan", "Joseph", "Jotaro", "Josuke", "Giorno"],
#     "Surnames": ["Joestar", "Joestar", "Kujo", "Higashikata", "Giovanna"]
# }
#
# data = pandas.DataFrame(dict)
# data.to_csv("jojo_db.csv")

squirrel_data = pandas.read_csv("Squirrel_Data.csv")

fur_color = squirrel_data["Primary Fur Color"]

cinnamon_amount = len(squirrel_data[fur_color == "Cinnamon"])
black_amount = len(squirrel_data[fur_color == "Black"])
gray_amount = len(squirrel_data[fur_color == "Gray"])

squirrel_count = {
    "Fur color": ["cinnamon","black","gray"],
    "count": [cinnamon_amount,black_amount,gray_amount]
}

count_data = pandas.DataFrame(squirrel_count)
count_data.to_csv("squirrel_count.csv")

print(cinnamon_amount)