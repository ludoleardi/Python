import math

class Subnetting(): 
    def __init__(self,ip_stringa):
        self.ip_notazione_dec = ip_stringa
        self.ip_notazione_bin = None
        self.ip_Broadcast = None
        self.ip_Rete = None

    def subnetMask(self, sub, num):
        tmp = round(math.log(num, 2), 0)
        self.subnet_base = sub + tmp
        self.subnet_base = int(self.subnet_base)
        return self.subnet_base

    
    
def dec2bin(ip):
    l = ip.split('.')
    l_bin = [str(bin(int(n)))[2:] for n in l]
    return '.'.join(['0' * (8 - len(num)) + num for num in l_bin])
    
def main():
    ip_Utente = input("Indirizzo IP: ")
    indirizzoIP = Subnetting(ip_Utente)
    indirizzoIP_bin = dec2bin(ip_Utente)
    print(indirizzoIP_bin)
    sottoreti = int(input("Inserire il numero di sottoreti: "))
    while True:
        subnet_mask = input("Inserire subnetmask: \n")
        if(int(subnet_mask[1:])>0 and int(subnet_mask[1:]) <=32):
            subnet_mask = int(subnet_mask[1:])
            break
    print(indirizzoIP.subnetMask(subnet_mask, sottoreti))
    
                
if __name__ == "__main__":
    main()