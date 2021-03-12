import turtle as t
import random
# import colorgram

tim = t.Turtle()
tim.shape("turtle")

# extract 10 colors from the image:
# extracted_colors = colorgram.extract("img.jpg", 30)
# colors = []
# for color in extracted_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors.append((r, g, b))
# print(colors)
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.goto(-230, 200)



color_list = [(236, 225, 202), (209, 155, 95), (187, 62, 29), (225, 213, 109), (236, 217, 226), (208, 148, 178), (223, 226, 238), (177, 157, 44), (223, 233, 225), (92, 104, 189), (79, 85, 145), (27, 27, 67), (37, 40, 19), (28, 45, 27), (191, 20, 7), (226, 168, 197), (146, 152, 187), (212, 85, 59), (45, 46, 104), (236, 172, 159), (143, 68, 79), (183, 15, 22), (156, 167, 158), (210, 77, 102), (82, 95, 84), (181, 183, 217), (45, 26, 45), (72, 72, 40), (222, 205, 26), (51, 72, 53)]
position = tim.pos()
for row in range(10):
    for column in range(10):
        color = random.choice(color_list)
        tim.dot(20, color)
        tim.color(color)
        tim.penup()
        tim.forward(50)
    tim.goto(position)
    tim.right(90)
    tim.forward(50*(row+1))
    tim.left(90)



screen = t.Screen()
screen.exitonclick()