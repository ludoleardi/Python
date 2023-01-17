import turtle

WIDTH = 4
HEIGHT = 100
SEP = 1

class Barcode():
    def __init__(self, stringa):
        self.listaAscii = [] #lista per salvare codice ascii caratteri
        self.codiceBin = [] 
        for carattere in stringa: #scorro la stringa e converto ogni valore in ascii, lo salvo solo se <= 255
            if(ord(carattere) <= 255):
                self.listaAscii.append(ord(carattere))
        
        #print(self.listaAscii)

        for elemento in self.listaAscii: #scorro i codici ascii dei caratteri e li converto in binario, salvando sempre 8 bit
            temp= bin(elemento)[2:]
            temp = "0"*(8-len(temp))+temp
            for c in temp: #scorro i caratteri della stringa binaria e li salvo in una lista convertendoli in interi
                self.codiceBin.append(int(c))
            print(self.codiceBin)

    def disegnaCodice(self):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.penup() #setto la posizione di partenza della penna e la ruoto verso l'alto
        pen.goto(-300,0)
        pen.pendown
        pen.left(90)
        
        for bit in self.codiceBin: #scorro tutti i bit nella lista
            print(bit) #stampo il bit per debug
            pen.pensize(WIDTH)
            if(bit == 0): #setto il colore della penna in base al valore del bit
                pen.pencolor("white")
            else:
                pen.pencolor("black")
            pen.forward(HEIGHT) #disegno la linea

            pen.pencolor("white") #setto la penna a bianco e disegno la linea separatrice
            pen.pensize(SEP)
            pen.right(90)
            pen.penup()
            pen.forward((WIDTH/2) + 1)
            pen.right(90)
            pen.pendown()
            pen.forward(HEIGHT)
            pen.left(90)
            pen.penup()
            pen.forward((WIDTH/2) + 1)
            pen.left(90) #rioriento la penna
            pen.pendown()

def main():
    screen = turtle.Screen()

    codiceBarre = Barcode("test1234")
    codiceBarre.disegnaCodice()
    turtle.done()

if __name__ == "__main__":
    main()