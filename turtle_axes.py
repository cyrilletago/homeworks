__author__ = 'cryrille'
import turtle


def axis():
        turtle.backward(400)
        turtle.left(90)
        turtle.forward(90)
        turtle.left(180)
        turtle.forward(180)
        turtle.left(180)
        turtle.forward(90)


def main():
    turtle.setup()
    turtle.color("blue")
    axis()
    turtle.done()

main()