import math

#tuple simili alle liste ma immutabili
punto = (1.5, 3.6)
print(f"La coordinata x del punto è {punto[0]}")
triangolo = [(1.5, 3.6), (-1.0, 0.0), (5.1, 4.3)]

area = 0.5 * abs(triangolo[0][0] * triangolo[1][1] + triangolo[0][1] * triangolo[2][0] + triangolo[1][0] * triangolo[2][1] - triangolo[2][0] * triangolo[1][1] - triangolo[2][1] * triangolo[0][0] - triangolo[1][0] * triangolo[0][1])
print(area)