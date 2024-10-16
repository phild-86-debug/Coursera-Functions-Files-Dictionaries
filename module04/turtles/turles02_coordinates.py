import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
alex = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
alex.shape('turtle')
tur_list = [t, alex]
while isInScreen(wn,tur_list[0]):
    if not isInScreen(wn, tur_list[0]):
        break
    coin = random.randrange(0, 2)
    if coin == 0:
        tur_list[coin].left(90)
    else:
        tur_list[coin].right(90)
    t_select = random.randrange(0, 2)

    tur_list[t_select].forward(50)

wn.exitonclick()
