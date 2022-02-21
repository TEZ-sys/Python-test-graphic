import turtle

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
drawing_area = turtle.Screen()
position = my_turtle.pos()
# -------------------------Start-position--------------------------
x = -450
y = 375

x1 = -450
y1 = 350

point_x = x
point_y = y

point_x1 = x1
point_y1 = y1

step = 0
row = 0
column = 0

# ------------------------Turtle-settings-------------------------
my_turtle.hideturtle()
my_turtle.width(1)
my_turtle.speed("fastest")

# ------------------------Turtle-work-till------------------------
while row < 8 and column < 8:
    # ------------------------Turtle-jump-go-to-1----------------------
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()

    my_turtle.left(45)
    my_turtle.forward(35)
    my_turtle.left(135)
    my_turtle.forward(70)
    my_turtle.left(135)
    my_turtle.forward(35)
    my_turtle.left(45)
    my_turtle.forward(22)

    x = x + 100

    # ------------------------Turtle-jump-go-to-1----------------------
    my_turtle.penup()
    my_turtle.goto(x1, y1)
    my_turtle.pendown()

    my_turtle.right(45)
    my_turtle.forward(35)
    my_turtle.right(135)
    my_turtle.forward(70)
    my_turtle.right(135)
    my_turtle.forward(35)
    my_turtle.right(45)
    my_turtle.forward(22)

    x1 = x1 + 100
    step = step + 1

    if step == 10:

        column = column + 1
        row = row + 1
        step = 0

        x = point_x
        y = point_y - 80

        point_x = x
        point_y = y

        x1 = point_x1
        y1 = point_y1 - 80

        point_x1 = x1
        point_y1 = y1



# ------------------------Turtle-Position----------------------
print(my_turtle.pos())
drawing_area.exitonclick()
