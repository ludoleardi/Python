class Robot():
    def __init__(self, n, m, t):
        self.nome = n
        self.massa = m
        self.tipologia=t

    def stampa_nome(self):
        print(self.nome)

    def pericoloso(self):
        if self.massa >=100:
            print("pericoloso")
        else:
            print("non pericoloso")
    


def main():
    robot = Robot("jack", 90, "u")
    robot.stampa_nome()
    robot.pericoloso()

if __name__ == "__main__":
    main()


