import turtle as tur
import colorsys as cs
from random import uniform 
tur.speed(5)
tur.bgcolor("black")
tur.tracer(10)
for i in range(360):
    tur.color(cs.hsv_to_rgb(i/30,uniform(0, 1),1))
    tur.pensize(2)
    tur.forward(150)
    tur.right(30)
    tur.forward(60)
    tur.left(90)
    tur.forward(60)
    tur.right(60)
    tur.penup()
    tur.setposition(0, 0)
    tur.pendown()
    tur.right(1)

tur.hideturtle()
tur.done()

# Follow My Page : https://instagram.com/web_coding_06?igshid=YmMyMTA2M2Y=
# Subscribe MY YouTube Chhanel : https://youtube.com/channel/UCH7szjqV-WvvZCJBm2x2H5w
