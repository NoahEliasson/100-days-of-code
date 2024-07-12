from turtle import Turtle, Screen 
import random 
t = Turtle()
t.shape("turtle")
colors = ["red", "green", "blue", "orange", "purple", "yellow", "pink", "#00FF00", "#FF5733", (0, 0, 255)]

def shape(angles):
    for steps in range(angles):
        t.forward(100)
        t.right(360/angles)


for i in range(3, 11):
    t.color(random.choice(colors))
    shape(i,)


screen = Screen()
screen.exitonclick()

