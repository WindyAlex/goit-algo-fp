import turtle


def pythagoras_tree(t, length, level):
    if level == 0:
        return

    t.forward(length)

    t.left(45)
    pythagoras_tree(t, length * 0.7, level - 1)

    t.right(90)
    pythagoras_tree(t, length * 0.7, level - 1)

    t.left(45)
    t.backward(length)


def main():
    level = int(input("Recursion level: "))
    length = 150

    screen = turtle.Screen()

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.color("red")

    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    pythagoras_tree(t, length, level)

    t.hideturtle()
    screen.mainloop()


main()
