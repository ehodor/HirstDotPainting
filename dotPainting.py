import colorgram
from random import choice
import turtle

pointer = turtle.Turtle()
screen = turtle.Screen()
pointer.speed('fastest')
pointer.penup()
pointer.setpos(-300, -300)
pointer.pendown()
screen.colormode(255)

pos_list = [-300, -300]
colors = colorgram.extract('HirstArt.jpg', 20)

list_of_colors = []
for color in colors:
    rgb = color.rgb
    color_tuple = (rgb[0], rgb[1], rgb[2])
    list_of_colors.append(color_tuple)

print(list_of_colors)
for i in range(10):
    for j in range(10):
        pointer.pendown()
        pointer.color(choice(list_of_colors))
        pointer.begin_fill()
        pointer.circle(10)
        pointer.end_fill()
        pointer.penup()
        pointer.forward(50)
    pos_list[1] += 50
    pointer.setpos(pos_list[0], pos_list[1])

screen.exitonclick()
