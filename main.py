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
bola.velx = 3
bola.vely = 3

#PLACAR
placar = turtle.Turtle()
placar.penup()
placar.speed(0)
placar.shape('square')
placar.color('white')
placar.hideturtle()
placar.goto(0,300)
placar.a = 0
placar.b = 0
placar.write('JOGADOR 1: {}  JOGADOR 2: {}'.format(placar.a,placar.b), align='center', font=('Arial', 15, 'normal'))
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

def pontuacao():
    placar.clear()
    bola.velx *= -1
    placar.write('JOGADOR 1: {}  JOGADOR 2: {}'.format(placar.a, placar.b), align='center', font=('Arial', 15, 'normal'))
    bola.goto(0,0)

def move_bola():
    bola.setx(bola.xcor() + bola.velx)
    bola.sety(bola.ycor() + bola.vely)

    if bola.xcor() > 640:
        placar.a += 1
        pontuacao()
    elif bola.xcor() < -640:
        placar.b += 1
        pontuacao()

    if bola.ycor() > 350:
        bola.sety(350)
        bola.vely *= -1
    elif bola.ycor() < -350:
        bola.sety(-350)
        bola.vely *= -1


window.listen()
window.onkeypress(up,'w')
window.onkeypress(down,'s')

#ESTRUTURA DE REPETIÇÂO (MANTE A JANELA ABERTA(update))
loop = True

while loop:
    move_bola()
    window.update()