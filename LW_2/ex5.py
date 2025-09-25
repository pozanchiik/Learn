from secrets import token_bytes

sur_name = 'Baranovskyi'

seq_bytes = sur_name.encode("utf-8")
print('seq_bytes =', seq_bytes.hex(' '))

seq_size = len(seq_bytes)
print('Довжина повідомлення в байтах =', seq_size)

key = token_bytes(nbytes=seq_size)
key = int.from_bytes(key, byteorder='big')

m = int.from_bytes(seq_bytes, byteorder="big")
print('message =', hex(m))


c = m ^ key
print('ciphertext =', hex(c))

p = c ^ key
print('p =', hex(p))

p = p.to_bytes(seq_size, byteorder="big")
plaintext = p.decode("utf-8")
print('plaintext =', plaintext)