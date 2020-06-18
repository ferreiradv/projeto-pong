import os
import turtle


#JANELA DO JOGO
window = turtle.Screen()
window.setup(1280.720)
window.title('PONG')
window.bgcolor('black')

#PENUP REMOVE O TRAÇO
#PLAY1
player1 = turtle.Turtle()
player1.penup()
player1.speed(0)
player1.shape('square')
player1.shapesize(8,1)
player1.color('white')
player1.goto(-500,0)

#PLAY2
player2 = turtle.Turtle()
player2.penup()
player2.speed(0)
player2.shape('square')
player2.shapesize(8,1)
player2.color('white')
player2.goto(500,0)

#BOLA
bola = turtle.Turtle()
bola.penup()
bola.speed(0)
bola.shape('circle')
bola.shapesize(1,1)
bola.color('white')
bola.goto(0,0)
bola.vel = 2



def up():
    y = player1.ycor()
    y += 20
    player1.sety(y)

    if player1.ycor() >= 260:
        player1.sety(260)
    pass

def down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)

    if player1.ycor() <= -260:
        player1.sety(-260)

def move_bola():
    bola.setx(bola.xcor() + bola.vel)
    if bola.xcor() > 600:
        bola.vel *= -1
    elif bola.xcor() < -600:
        bola.vel *= -1


window.listen()
window.onkeypress(up,'w')
window.onkeypress(down,'s')

#ESTRUTURA DE REPETIÇÂO (MANTE A JANELA ABERTA(update))
loop = True

while loop:
    move_bola()
    window.update()