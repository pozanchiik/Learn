pv = float(input("pv = "))
_int = float(input("int = "))
yrs = float(input("yrs = "))

print(f"fv = {pv * (1 + _int/100) ** yrs}")