class IPAddress():
    def __init__(self, ip_stringa):
        self.ip_dec = ip_stringa
        self.ip_bin = self.dec2bin(self.ip_dec)

    def dec2bin(self, ip_dec):
        binary = ""
        for elemento in ip_dec:
            binary = binary + str(bin(elemento))
        return binary

    def toList(self):
        lista_str = self.ip_dec.split(".")
        return [int(gruppo) for gruppo in lista_str]

def main():
    indirizzoIP = IPAddress("192.168.0.123")
    print(indirizzoIP.ip_dec)
    print(indirizzoIP.toList())
    print(indirizzoIP.ip_bin)

if __name__ == "__main__":
    main()