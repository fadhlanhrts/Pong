import turtle

win = turtle.Screen()
win.title("Ini Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Paddle kiri
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#paddle kanan
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)

bola.dx = 1
bola.dy = -1


#Fungsi menggerakkan paddle

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
win.listen()
win.onkey(paddle_a_up, "w")
win.onkey(paddle_a_down, "s")
win.onkey(paddle_b_up, "Up")
win.onkey(paddle_b_down, "Down")


#Loop

while True:
    win.update()

    #Gerakin bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #batas layar
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
    
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1

     if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
    
    #Paddle & bola
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor()< paddle_b.ycor() + 40 and bola.ycor() > paddle_b.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1
