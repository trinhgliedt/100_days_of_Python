from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "indigo"]
xCor = -240
yCors = [150, 100, 50, 0, -50, -100]
turtles = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(xCor, yCors[i])
    turtles.append(new_turtle)

is_raced_on = False
if user_bet:
    is_raced_on = True

while is_raced_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_raced_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()