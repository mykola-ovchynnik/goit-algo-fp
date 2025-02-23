import math
import turtle


def setup_turtle():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    t = turtle.Turtle()
    t.hideturtle()
    t.left(90)
    t.penup()
    t.backward(200)
    t.pendown()
    t.speed(0)
    return t


def pythagoras_tree(t, level, branch_len: int | float = 100):
    if level == 0:
        return

    t.forward(branch_len)

    t.left(45)
    pythagoras_tree(t, level - 1, branch_len / math.sqrt(2))

    t.right(90)
    pythagoras_tree(t, level - 1, branch_len / math.sqrt(2))

    t.left(45)
    t.backward(branch_len)


def main():
    level = int(input("Enter the recursion level: "))
    t = setup_turtle()
    pythagoras_tree(t, level, 100)
    turtle.done()


if __name__ == "__main__":
    main()
