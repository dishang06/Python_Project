import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("Mother's Day Celebration")
screen.bgcolor("pink")

# Create the turtle object
pen = turtle.Turtle()
pen.color("red")
pen.fillcolor("red")
pen.pensize(3)
pen.speed(1)

# Draw the heart shape
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

# Move the turtle to write the message
pen.up()
pen.goto(0, 150)
pen.down()
pen.color("white")
pen.write("Happy Mother's Day", align="center", font=("Arial", 16, "bold"))

# Hide the turtle
pen.hideturtle()

# Exit on click
turtle.exitonclick()