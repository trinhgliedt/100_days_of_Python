import turtle as t
import random
t.colormode(255)

tim = t.Turtle()

tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def draw_spinograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.setheading(tim.heading()+size_of_gap)
        tim.circle(100)


draw_spinograph(10)

screen = t.Screen()
screen.exitonclick()