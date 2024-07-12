import turtle

# Set up the turtle
t = turtle.Turtle()
turtle.colormode(255)  # Set color mode to RGB tuples

# Lift the pen and move to a starting position
t.penup()
t.goto(-200, 0)
t.pendown()

# Function to draw the letter 'C'
def draw_C():
    t.penup()
    t.goto(-200, 50)
    t.pendown()
    t.circle(50, 180)
    t.left(90)
    t.penup()

# Function to draw the letter 'O'
def draw_O():
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.circle(50)
    t.penup()

# Function to draw the letter 'L'
def draw_L():
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.penup()

# Function to draw the letter 'I'
def draw_I():
    t.penup()
    t.goto(100, 50)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.penup()

# Function to draw the letter 'N'
def draw_N():
    t.penup()
    t.goto(200, -50)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(135)
    t.forward(140)
    t.left(135)
    t.forward(100)
    t.penup()

# Draw each letter
draw_C()
draw_O()
draw_L()
draw_I()
draw_N()

# Hide the turtle and finish
t.hideturtle()
turtle.done()