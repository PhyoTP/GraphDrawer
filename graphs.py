import turtle

print("Numbers must be less than ten")
# mode=input("Equation (e) or coordinates (c)?")

# x positive coordinates
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

# x negative coordinates
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


# y positive coordinates
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

# y negative coordinates
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

print("Done with graph")


# drawing of points
xpoints=[]
ypoints=[]
first_point = True
ptr = turtle.Turtle()
while True:
    pointx = float(input("Enter point x"))*30
    xpoints.append(pointx)
    pointy = float(input("Enter point y"))*30
    ypoints.append(pointy)
    if first_point:
        ptr.penup()
    ptr.goto(pointx,pointy)
    if first_point:
        ptr.pendown()
        first_point = False
    cont = input("Type 's' to stop")
    if cont == 's':
        turtle.done()
        break
