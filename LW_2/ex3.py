birth_date = int("05.06.2008".replace('.', ''))
bin_birt_date = bin(birth_date)
hex_birth_date = hex(birth_date)

bit_length_in_birth_date = birth_date.bit_length()

print("birth_date = ", birth_date)
print("bin_birth_date = ", bin_birt_date)
print("hex_birth_date = ", hex_birth_date)
print(f"bit length = {bit_length_in_birth_date}\nbyte = {bit_length_in_birth_date * 8}" )