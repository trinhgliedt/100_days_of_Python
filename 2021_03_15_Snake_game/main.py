from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

base_x_cor = 0
base_y_cor = 0

segments = []

for i in range(3):
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.setx(base_x_cor - 20 * i)
    new_segment.sety(base_y_cor)
    segments.append(new_segment)


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.8)
    for seg_num in range(len(segments)-1,0,-1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)


    segments[0].left(90)
    segments[0].forward(20)



screen.exitonclick()