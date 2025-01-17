def vernam_cipher(text, key):
    
    if len(text) != len(key):  # Проверяем, что длины совпадают
        raise ValueError("Длина текста и ключа должна совпадать!")
    
    # Шифруем текст побитовым XOR
    encrypted = ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, key))
    return encrypted


def vernam_decrypt(ciphertext, key):

    return vernam_cipher(ciphertext, key)  # Процесс обратимый, используем ту же функцию


# Пример: Текст и ключ должны быть одинаковой длины
text = "Привет Мир!"
key = "Ключ!+Ключ!"

# Шифрование
encrypted_text = vernam_cipher(text, key)
print("Encrypted:", encrypted_text)

# Дешифрование
decrypted_text = vernam_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)