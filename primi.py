def isPrimo(x):
    cont = 0
    for i in range(2, int(x**0.5)+1):
        y = x % i
        if(y == 0):
            cont +=1

    if cont == 0:
        return True
    else:
        return False


def isPrimoBis(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
        
    return True