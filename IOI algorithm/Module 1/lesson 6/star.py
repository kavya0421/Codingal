import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Star Pattern")

pen = turtle.Turtle()
pen.speed("fastest")
pen.hideturtle()
pen.color("gold", "yellow")

pen.penup()
pen.goto(0, -120)
pen.setheading(90)
pen.pendown()

pen.begin_fill()
for _ in range(5):
	pen.forward(240)
	pen.right(144)
pen.end_fill()

turtle.done()
