''' Packages & Debugging
    (1) Python Packages & Core Packages
    (2) Package manager & 
    (3) Enum, map and filter
'''

# import turtle
# print("====== Python Packages & Core Packages =====")

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(2)
# t.circle(250)

# turtle.done()


import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
pizza = turtle.Turtle()
pizza.speed(2)

# Draw crust (outer circle)
pizza.penup()
pizza.goto(0, -150)
pizza.pendown()
pizza.color("#D2691E")  # brown crust
pizza.begin_fill()
pizza.circle(150)
pizza.end_fill()

# Draw cheese (inner circle)
pizza.penup()
pizza.goto(0, -130)
pizza.pendown()
pizza.color("#FFD700")  # yellow cheese
pizza.begin_fill()
pizza.circle(130)
pizza.end_fill()

# Draw slices (lines)
pizza.penup()
pizza.goto(0, 0)
pizza.pendown()
pizza.color("black")

for angle in range(0, 360, 45):  # 8 slices
    pizza.setheading(angle)
    pizza.forward(130)
    pizza.backward(130)

# Draw pepperoni
pizza.penup()
pizza.color("red")

pepperoni_positions = [
    (40, 40), (-40, 40), (60, -20), (-60, -20),
    (0, 70), (0, -60)
]

for pos in pepperoni_positions:
    pizza.goto(pos)
    pizza.begin_fill()
    pizza.circle(10)
    pizza.end_fill()

# Hide turtle and finish
pizza.hideturtle()
turtle.done()
