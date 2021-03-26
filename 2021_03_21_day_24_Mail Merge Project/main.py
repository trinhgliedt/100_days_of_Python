#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open("./Input/Names/invited_names.txt") as file:
    contents = file.read()
    names = contents.split("\n")
    print(names)

with open("./Input/Letters/starting_letter.txt", "r") as file:
    raw_contents = file.read()

for name in names:
    if " " in name:
        formatted_name = name.replace(" ", "_")
    else:
        formatted_name = name
    file_path = f"./Output/ReadyToSend/letter_for_{formatted_name}.txt"

    with open(file_path, "w") as file:
        contents = raw_contents.replace("[name]", name)
        file.write(contents)




#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp