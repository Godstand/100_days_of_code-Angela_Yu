# import colorgram
#
# rgb_colors = []
# colors_list = colorgram.extract('Image.png', 30)
# for color in colors_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()
colors_list = [
    (199, 12, 32), (231, 250, 242), (250, 238, 17), (39, 76, 190),
    (38, 217, 69), (237, 226, 5), (229, 159, 46), (28, 39, 156), (215, 75, 13), (197, 15, 11), (15, 154, 15),
    (243, 34, 166), (230, 17, 122), (70, 10, 31), (241, 245, 251), (61, 15, 8), (224, 141, 209), (10, 97, 62),
    (222, 160, 9), (50, 213, 230), (18, 19, 44), (11, 227, 239), (237, 156, 218), (86, 75, 209), (79, 211, 162),
    (84, 234, 199), (59, 233, 242), (4, 67, 41)
]

tim.setheading(225)
tim.forward(350)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
