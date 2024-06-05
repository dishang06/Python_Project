import turtle
from turtle import *

# Follow My Page : https://instagram.com/web_coding_06?igshid=YmMyMTA2M2Y=
# Subscribe MY YouTube Chhanel : https://youtube.com/channel/UCH7szjqV-WvvZCJBm2x2H5w

# Creating a screen instance
screen = turtle.Screen()

# Defining a turtle instance
t = turtle.Turtle()

# Setting turtle's speed
speed(3)

# Initially, penup()
t.penup()

# Moving turtle to the starting position for the orange rectangle
t.goto(-400, 250)

# Drawing the orange rectangle
t.pendown()
t.color("orange")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()

# Moving turtle to the starting position for the green rectangle
t.left(90)
t.forward(167)

# Drawing the green rectangle
t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()

# Moving turtle to the starting position for the big blue circle
t.penup()
t.goto(70, 0)

# Drawing the big blue circle
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()

# Moving turtle to the starting position for the big white circle
t.penup()
t.goto(60, 0)

# Drawing the big white circle
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()

# Drawing the mini blue circles
t.penup()
t.goto(-57, -8)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(15)
    t.right(15)
    t.pendown()

# Moving turtle to the starting position for the small blue circle
t.penup()
t.goto(20, 0)

# Drawing the small blue circle
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

# Drawing the spokes
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(60)
    t.backward(60)
    t.left(15)

# Closing the turtle window
turtle.done()

# Follow My Page : https://instagram.com/web_coding_06?igshid=YmMyMTA2M2Y=
# Subscribe MY YouTube Chhanel : https://youtube.com/channel/UCH7szjqV-WvvZCJBm2x2H5w