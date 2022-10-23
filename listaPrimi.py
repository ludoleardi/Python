def isPrimoBis(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
        
    return True

list = []

for i in range(1, 101):
    if isPrimoBis(i):
        list.append(i)

print(list)