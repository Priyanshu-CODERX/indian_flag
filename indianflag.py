import turtle

# Creating Canvas
w = turtle.Screen()
w.bgcolor("#b3daff")
w.title("Indian Flag")
flag = turtle.Turtle()

# Setting properties

flag.penup()
flag.speed(1)
flag.goto(-180, 60)

# First Rectangle
flag.pendown()
flag.begin_fill()
flag.fillcolor("orange")
flag.left(90)
flag.forward(90)
flag.right(90)
flag.forward(400)
flag.right(90)
flag.forward(90)
flag.right(90)
flag.forward(400)
flag.end_fill()

# Second Rectangle
flag.begin_fill()
flag.fillcolor("white")
flag.left(90)
flag.forward(90)
flag.left(90)
flag.forward(400)
flag.left(90)
flag.forward(90)
flag.left(90)
flag.forward(400)
flag.left(90)
flag.forward(90)
flag.end_fill()

# Third Rectangle
flag.begin_fill()
flag.fillcolor("green")
flag.forward(90)
flag.left(90)
flag.forward(400)
flag.left(90)
flag.forward(90)
flag.left(90)
flag.forward(400)
flag.end_fill()

# Ashoka Chakra
flag.penup()
flag.goto(28, 58)
flag.color("#000080")
flag.pendown()
flag.circle(45)
flag.end_fill()
# Creating the lines
for i in range(24):
	flag.penup()
	flag.goto(29, 16)
	flag.left(15)
	flag.pendown()
	flag.forward(45)

turtle.done()
