import turtle
import vetva


def main():
    t = turtle.Turtle()

    t.left(90)
    t.pencolor('brown')
    vetva.vetva(t,5)

    turtle.exitonclick()

if __name__ == '__main__':
    main()
    print("ahoj ludia")