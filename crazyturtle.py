import turtle

t = turtle.Turtle()
t.shape('turtle')

step=5

def moveRight():
    t.setheading(0)
    t.forward(step)
    print(t.pos())

def moveLeft():
    t.setheading(180)
    t.forward(step)

def moveUp():
    t.setheading(90)
    t.forward(step)

def moveDown():
    t.setheading(270)
    t.forward(step)

screen = turtle.Screen()
screen.onkeypress(moveRight, "Right")
screen.onkeypress(moveLeft, "Left")
screen.onkeypress(moveUp, "Up")
screen.onkeypress(moveDown, "Down")
screen.listen()  

turtle.done()
