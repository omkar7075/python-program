
#
import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Turtle()
s.bgcolor("black")
h=0
for i in range(460):
    c = colorsys.hsv_to_rgb(h,1,8,9)
    h+= 1/n
    t.color(c)
    t.left(145)
    for j in range(5):
        t.forward(300)
        t.left(150)


 #######
"""from turtle import *
#make a square
   for _ in range(4):
       forward(100)
       left(90)
   exitonclick()
"""
