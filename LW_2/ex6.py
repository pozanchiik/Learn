# Рядок для шифрування
text = "Baranovskyi"

# Ключ для XOR
key = 301

# === Шифрування ===
encrypted = [ord(ch) ^ key for ch in text]
print("Зашифрований:", encrypted)

# === Розшифрування ===
decrypted = "".join(chr(num ^ key) for num in encrypted)
print("Розшифрований:", decrypted)
