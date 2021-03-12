import turtle as t
import random

tim = t.Turtle()

tim.speed("fastest")



def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

# draw many shapes
colors = ["red", "orange", "darkGoldenrod", "green", "blue", "indigo", "violet"]
tim.penup()

tim.goto(0,140)
tim.pendown()
tim.circle(30)

tim.penup()
tim.goto(-50,200)
tim.pendown()


for sides in range(3,20):
    color = random.choice(colors)
    for side in range(sides):
        angle = 360/sides
        tim.color(color)
        tim.forward(100)
        tim.right(angle)

screen = t.Screen()
screen.exitonclick()