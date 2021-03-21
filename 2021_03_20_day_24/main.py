

# with open("new_file.txt", mode="a") as file:
#     file.write("\nNew text.")

with open("../my_file.txt") as file:
    # if len(file.read()) == 0:
    #     print("empty file")
    # else:
    #     contents = file.read()
    #     print(contents)
    contents = file.read()
    print(contents)