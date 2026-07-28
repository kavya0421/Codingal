import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Spiral")

pen = turtle.Turtle()
pen.speed("fastest")
pen.hideturtle()

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(120):
	pen.color(colors[i % len(colors)])
	pen.width(i // 20 + 1)
	pen.forward(i * 2)
	pen.right(61)

turtle.done()
