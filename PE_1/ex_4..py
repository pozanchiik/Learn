a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discriminant = (b ** 2) - (4 * a * c)

if discriminant < 0:
    print("discriminant < 0")
elif discriminant == 0:
    x_1 = round((-b) / (2 * a))
    print(f'x_1 = x_2 = {x_1}')
elif discriminant > 0:
    x_1 = round((-b - discriminant) / (2 * a))
    x_2 = round((-b + discriminant) / (2 * a), 2)
    print(f'x_1 = {x_1}, x_2 = {x_2}')
else:
    print("error")