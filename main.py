import turtle

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
drawing_area = turtle.Screen()
position = my_turtle.pos()

# ------------------------Turtle-settings-------------------------
my_turtle.hideturtle()
my_turtle.width(1)
my_turtle.speed(10)
# ------------------------Turtle-jump-go-to-1----------------------
my_turtle.penup()
my_turtle.goto(0, 100)
my_turtle.pendown()

# ------------------------Turtle-work-till------------------------
#my_turtle.left(45)
#my_turtle.forward(50)
#my_turtle.left(135)
#my_turtle.forward(120)
#my_turtle.left(135)
#my_turtle.forward(50)
#my_turtle.left(45)
#my_turtle.forward(50)

# ------------------------Turtle-jump-go-to-2----------------------

print(my_turtle.pos())

drawing_area.exitonclick()
