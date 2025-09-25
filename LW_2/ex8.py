from math import sin,cos, log
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))


result = round((x + 2) ** 3 + (y + x) ** 0.2 - log(( 2 + abs(sin(x + y) / cos( x + z))),3),1)


print(f"Варіант: 1\nПрізвище: Барановський\nІм'я: Маским\n"
      f"Формула: round((x + 2) ** 3 + (y + x) ** 0.2 - log(( 2 + abs(sin(x + y) / cos( x + z))),3),1)\n"
      f"Вхідні данні: x = {x},  y = {y},  z = {z}\n"
      f"Результат: {result}")