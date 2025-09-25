a = 13505250816894811427 # ключ
b = 80740728437266373009 # секретний ключ
c = 51397231703758601707 # модуль

text = 'run'

seq_bytes = text.encode("utf-8")
print('seq_bytes =', seq_bytes.hex(' '))

m = int.from_bytes(seq_bytes, byteorder="big")
print('message =', hex(m))

s = (m**a) % c
print('ciphertext =', hex(s), s)

p = (s**b) % c
print('p =', hex(p))

p = p.to_bytes((p.bit_length() + 7) // 8, byteorder="big")

plaintext = p.decode("utf-8")
print('plaintext =', plaintext)