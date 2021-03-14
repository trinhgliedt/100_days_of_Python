from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)

# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "indigo"]
turtle_names = ["tim", "tom", "tam", "max", "cass", "trinh"]

tim = Turtle(shape="turtle")
tim.penup()
tim.goto(-240,0)

screen.exitonclick()