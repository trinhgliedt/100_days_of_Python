import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

directions = [0, 90, 180, 270]
tim.pensize(10)
distance = 30
tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)


for i in range(300):
    direction = random.choice(directions)
    tim.color(random_color())
    tim.forward(distance)
    tim.setheading(direction)

