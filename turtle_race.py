from turtle import Turtle, Screen 

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)
    
def counter_clockwise():
    t.right(10)

def clock_wise():
    t.left(10)
                
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.exitonclick()
    
