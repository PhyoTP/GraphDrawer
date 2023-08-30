import turtle

xp=turtle.Turtle()
xpos=30
while xpos <= 300:
    xp.goto(xpos,0)
    xp.penup()
    xp.goto(xpos,10)
    xp.pendown()
    xp.goto(xpos,-10)
    xp.penup()
    xp.goto(xpos,0)
    xp.pendown()
    xpos+=30
xp.goto(xpos,0)

xn=turtle.Turtle()
xn.left(180)
xneg=-30
while xneg >= -300:
    xn.goto(xneg,0)
    xn.penup()
    xn.goto(xneg,10)
    xn.pendown()
    xn.goto(xneg,-10)
    xn.penup()
    xn.goto(xneg,0)
    xn.pendown()
    xneg-=30
xn.goto(xneg,0)



yp=turtle.Turtle()
yp.left(90)
ypos=30
while ypos <= 300:
    yp.goto(0,ypos)
    yp.penup()
    yp.goto(10,ypos)
    yp.pendown()
    yp.goto(-10,ypos)
    yp.penup()
    yp.goto(0,ypos)
    yp.pendown()
    ypos+=30
yp.goto(0,ypos)

yn=turtle.Turtle()
yn.right(90)
yneg=-30
while yneg >= -300:
    yn.goto(0,yneg)
    yn.penup()
    yn.goto(10,yneg)
    yn.pendown()
    yn.goto(-10,yneg)
    yn.penup()
    yn.goto(0,yneg)
    yn.pendown()
    yneg-=30
yn.goto(0,yneg)

turtle.done()
