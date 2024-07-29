from turtle import Turtle, Screen 
import random 
t = Turtle()
t.shape("turtle")
colors = ["red", "green", "blue", "orange", "purple", "yellow", "pink", "#00FF00", "#FF5733",]

# def shape(angles):
#     for steps in range(angles):
#         t.forward(100)
#         t.right(360/angles)


# for i in range(3, 11):
#    t.color(random.choice(colors))
#     shape(i,)


# screen = Screen()
# screen.exitonclick()
#turns()
screen = Screen()
screen.bgcolor("black")
turns = [0, 90 , 180, 270]
def random_turn():
    while True: 
        t.speed(0)
        i = random.randint(0,3)
        t.forward(20)
        t.right(turns[i])
        t.color(random.choice(colors))
        t.forward(20)
random_turn()