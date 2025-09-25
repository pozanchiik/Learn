from math import cos, sqrt

a = float(input("a = "))
b = float(input("b = "))
y = float(input("y = "))

print(f"c = {sqrt( a**2 + b**2 - 2*a*b * cos(y))}")

