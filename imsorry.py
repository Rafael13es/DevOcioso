import turtle

t = turtle.Turtle()

t.color('white')
t.left(180)
t.forward(100)
#Create the I
t.color('black')
t.forward(100)
t.right(180)
t.forward(50)
t.left(90)
t.forward(125)
t.left(90)
t.forward(50)
t.right(180)
t.forward(100)

#Create M
t.color('white')
t.forward(25)
t.right(90)
t.forward(125)
t.color('black')
t.left(180)
t.forward(125)
t.right(150)
t.forward(100)
t.left(120)
t.forward(100)
t.right(150)
t.forward(125)

#Create S
t.color('white')
t.left(90)
t.forward(150)
t.left(90)
t.forward(125)
t.left(90)
t.color('black')
t.forward(30)
t.circle(31.25,180)
t.forward(15)
t.circle(-31.25,180)
t.forward(30)
t.right(180)
t.forward(35)

#Create O
t.color('white')
t.forward(100)
t.color('black')
t.circle(62.5, 360)
t.forward(5)

#Create R
t.color('white')
t.forward(70)
