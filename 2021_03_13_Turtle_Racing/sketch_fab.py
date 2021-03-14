from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_counter_clockwise():
    tim.left(10)


def turn_clockwise():
    tim.left(-10)


def clear_drawing():
    tim.clear()
    tim.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=turn_counter_clockwise)
screen.onkeypress(key="c", fun=clear_drawing)
screen.exitonclick()