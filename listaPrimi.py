def isPrimoBis(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
        
    return True

n = 100
list = [i for i in range(2, n) if isPrimoBis(i)] ##list comprehension con filtro
print(list)