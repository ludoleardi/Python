import random
import time

n = 1000000
l = [random.uniform(0.,1.) for _ in range(n)]

start_time = time.time()
max = l[0]
for element in l:
    if element > max:
        max = element

end_time = time.time()
print(f"Il valore massimo è {max}")
print(f"Durata dell'algoritmo: {end_time - start_time} s")