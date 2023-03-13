import random

f = open("casuali.txt", "w")

l_Ali = [random.randint(1, 6) for _ in range(0, 10)]
l_Bob = [random.randint(1, 6) for _ in range(0, 10)]

for i in range(0, 10):
    f.write(f"{l_Ali[i]}, {l_Bob[i]}")