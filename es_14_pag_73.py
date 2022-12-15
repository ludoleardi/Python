class Quadrato():

    def __init__(self, l1, l2, l3, l4):
        self.lato1 = l1
        self.lato2 = l2
        self.lato3 = l3
        self.lato4 = l4

    def is_quadrato(self):
        p=self.lato1
        if (self.lato2 == p and self.lato3 == p and self.lato4 == p):
            return True

    def perimetro(self):
        return self.lato1*4

    def area(self):
        return self.lato1*self.lato1


def main():
    quadrato= Quadrato(3, 3, 3, 3)
    if (quadrato.is_quadrato()==True):
        per=quadrato.perimetro()
        area=quadrato.area()
        print (per, area)
    else:
        print ("non e un quadrato")


if __name__ == "__main__":
    main()        