from decimal import Decimal
dc_1 = Decimal(1.000000001)
dc_2 = Decimal(1.000000000)
print(f"{1 / (dc_1 - dc_2)}")

fl_1 = float(1.000000001)
fl_2 = float(1.000000000)
print(f"{1 / (fl_1 - fl_2)}")

print(f"{float((1 / (dc_1 - dc_2))) - (1 / (fl_1 - fl_2))}")