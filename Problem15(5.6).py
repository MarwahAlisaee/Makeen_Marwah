import math

def volume(h, r):
    V = (1/3) * math.pi * r**2 * h
    return round(V, 2)

result = volume(7, 4)
print(result)

result1 = volume(10, 5)
print(result1)

