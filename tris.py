import turtle
import math

def creaCampo():
    c = turtle.Turtle()
    c.penup()
    c.speed(100)
    c.pensize(10)
    
    c.goto(-100, 300)
    c.right(90)
    c.pendown()
    c.forward(600)
    c.penup()
    c.goto(100, 300)
    c.pendown()
    c.forward(600)

    c.penup()
    c.goto(-300, 100)
    c.pendown()
    c.left(90)
    c.pendown()
    c.forward(600)
    c.penup()
    c.goto(-300, -100)
    c.pendown()
    c.forward(600)

def g1(x, y, t):
    t.penup()
    t.goto(x, y)
    t.pencolor("blue")
    t.pendown()
    t.circle(50)

def g2(x, y, t):
    t.penup()
    t.goto(x, y)
    t.pencolor("red")
    t.pendown()
    t.circle(50)

def simbolo(g, n, t, diz):

    t.pensize(10)
    if g == 1:
        g1(diz[n][0], diz[n][1], t)
    if g == 2:
        g2(diz[n][0], diz[n][1], t)
    


def main():
    diz_pos={1:(-200, 150), 2:(0, 150), 3:(200, 150),
    4:(-200, -50), 5:(0, -50), 6:(200, -50),
    7:(-200, -250), 8:(0, -250), 9:(200, -250)}
    cont=0
    gioc1 = []
    gioc2 = []
    pos = 0
    s = turtle.getscreen()
    t = turtle.Turtle()
    creaCampo()
    while cont < 9:
        if cont % 2 == 0:
            while pos in gioc1 or pos in gioc2 or pos < 1 or pos >9:
                pos = int(input("posizione desidedrata giocatore1: "))
            gioc1.append(pos)
            simbolo(1, pos, t, diz_pos)
            cont+=1
        else:
            while pos in gioc1 or pos in gioc2 or pos < 1 or pos >9:
                pos = int(input("posizione desidedrata giocatore2: "))
            gioc2.append(pos)
            simbolo(2, pos, t, diz_pos)
            cont+=1


if __name__ == "__main__":
    main()