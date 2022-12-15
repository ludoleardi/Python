import turtle
finestra = turtle.Screen()
def leggiFile(bob):
    file=open("/Users/mac/Documents/Personale/Scuola/Visual_Studio/Python/comandi.csv", "r")
    lista_righe=file.readlines()
    file.close()
    lista_comandi=[]
    lista_num=[]
    for riga in lista_righe[:]:
        lista_c0= riga[:-1].split(',')
        lista_comandi.append(lista_c0[0])
        lista_num.append((int)(lista_c0[1]))
    
    for c, n in zip(lista_comandi, lista_num):
        if(c=="forward"):
            bob.forward(n)
        else: 
            if(c=="right"):
                bob.right(n)
            else:
                if(c=="left"):
                    bob.left(n)
    turtle.done()
    

def main():
    bob=turtle.Turtle()
    leggiFile(bob)

if __name__ =="__main__":
    main()