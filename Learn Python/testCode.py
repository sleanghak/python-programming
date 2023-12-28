from turtle import*
from math import log10

up()
goto(-100,160)
down()

write('1-1/2+13-14+1/5-...+1/n=ln(2)')

up()
goto(-160,0)
down()
write('0')

up()
goto(155,0)
write('1')

up()
# goto(log(2)*75,-10)
down()
write('ln(2)')

c='blue','red'
def tr(n):
    up()
    goto(-150,0)
    down()
    left(90)

    for i in range(1,n):
        color(c[(i+1)%2])
        circle(-150/i,((-1)**(i+1))*180)
    hideturtle
tr(20)




# import turtle
# from turtle import*

# #screen for output
# screen = turtle.Screen()

# # Defining a turtle Instance
# t = turtle.Turtle()
# speed(0)

# # initially penup()
# t.penup()
# t.goto(-400, 250)
# t.pendown()

# # Orange Rectangle
# #white rectangle
# t.color("orange")
# t.begin_fill()
# t.forward(800)
# t.right(90)
# t.forward(167)
# t.right(90)
# t.forward(800)
# t.end_fill()
# t.left(90)
# t.forward(167)

# # Green Rectangle
# t.color("green")
# t.begin_fill()
# t.forward(167)
# t.left(90)
# t.forward(800)
# t.left(90)
# t.forward(167)
# t.end_fill()

# # Big Blue Circle
# t.penup()
# t.goto(70, 0)
# t.pendown()
# t.color("navy")
# t.begin_fill()
# t.circle(70)
# t.end_fill()

# # Big White Circle
# t.penup()
# t.goto(60, 0)
# t.pendown()
# t.color("white")
# t.begin_fill()
# t.circle(60)
# t.end_fill()

# # Mini Blue Circles
# t.penup()
# t.goto(-57, -8)
# t.pendown()
# t.color("navy")
# for i in range(24):
# 	t.begin_fill()
# 	t.circle(3)
# 	t.end_fill()
# 	t.penup()
# 	t.forward(15)
# 	t.right(15)
# 	t.pendown()
	
# # Small Blue Circle
# t.penup()
# t.goto(20, 0)
# t.pendown()
# t.begin_fill()
# t.circle(20)
# t.end_fill()
# # Spokes

# t.penup()
# t.goto(0, 0)
# t.pendown()
# t.pensize(2)
# for i in range(24):
# 	t.forward(60)
# 	t.backward(60)
# 	t.left(15)
	
# #to hold the
# #output window
# turtle.done()



