import turtle

def poligono(posx, posy, nLati, curs, colore):
    curs.color("black")
    curs.begin_fill()
    curs.penup()
    curs.setposition(posx,posy)
    curs.pendown()
    lato = 360/nLati
    angolo = 360/nLati
    for _ in range(0, nLati):
        curs.right(angolo)
        curs.forward(lato)

def main():
    finestra = turtle.Screen()
    tartaruga = turtle.Turtle()
    

if __name__ == "__main__":
    main()