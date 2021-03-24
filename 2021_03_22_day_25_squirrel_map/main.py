import pandas

data = pandas.read_csv("squirrel_data.csv")
# print(type(data))
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")

squirrel_count = data.groupby(["Primary Fur Color"]).size().reset_index(name="Count")
squirrel_count = squirrel_count.rename(columns={"Primary Fur Color": "Fur Color"})
print(squirrel_count)

new_data = pandas.DataFrame(squirrel_count)
new_data.to_csv("squirrel_count.csv")
