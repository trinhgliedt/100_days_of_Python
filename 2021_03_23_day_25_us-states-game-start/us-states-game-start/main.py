import turtle
import pandas
screen = turtle.Screen()
screen.screensize(1200,600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"]
# print(states.str.contains("Alaska").any())
correct_count = 0
correct_guesses = []
while correct_count < 50:
    answer_state = screen.textinput(title="Guess the State", prompt=f"{correct_count}/50 states correct.\n What's another state's name?")
    if answer_state.lower() == "exit":
        break
    formatted_answer = answer_state.title()


    if states.str.contains(formatted_answer).any():
        matched_row = data[data.state == formatted_answer]
        if formatted_answer not in correct_guesses:
            correct_guesses.append(formatted_answer)
            correct_count += 1

        if formatted_answer in correct_guesses:
            x_coor = int(matched_row.x)
            y_coor = int(matched_row.y)
            new_turtle = turtle.Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.goto(x_coor-15, y_coor)
            new_turtle.write(formatted_answer)
states_to_learn = []
for index, state in states.items():
    if state not in correct_guesses:
        states_to_learn.append(state)
states_to_learn_dict = {"states to learn": states_to_learn}
new_data = pandas.DataFrame(states_to_learn_dict)
new_data.to_csv("state_to_learn.csv")