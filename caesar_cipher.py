def caesar_cipher(text, key, decrypt=False):
    
    result = []
    shift = -key if decrypt else key  # Для дешифрования смещение делается отрицательным

    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            if 'А' <= char <= 'Я' or 'а' <= char <= 'я':  # Русский алфавит
                base = ord('А') if char.isupper() else ord('а')
                alphabet_size = 33  # Количество букв в русском алфавите
            elif 'A' <= char <= 'Z' or 'a' <= char <= 'z':  # Латинский алфавит
                base = ord('A') if char.isupper() else ord('a')
                alphabet_size = 26  # Количество букв в латинском алфавите
            else:
                result.append(char)  # Оставляем символ без изменений
                continue

            # Применяем формулу шифра Цезаря
            result.append(chr((ord(char) - base + shift) % alphabet_size + base))
        else:
            result.append(char)  # Не буквы оставляем без изменений

    return ''.join(result)


def caesar_bruteforce(ciphertext, language='ru'):

    possible_texts = []
    alphabet_size = 33 if language == 'ru' else 26  # Размер алфавита зависит от языка

    for key in range(1, alphabet_size):  # Перебираем все возможные ключи
        decrypted_text = caesar_cipher(ciphertext, key, decrypt=True)
        possible_texts.append((key, decrypted_text))
    return possible_texts


# Шифрование
encrypted_text = caesar_cipher("Привет, Мир!", 3)
print("Encrypted:", encrypted_text)

# Дешифрование
decrypted_text = caesar_cipher(encrypted_text, 3, decrypt=True)
print("Decrypted:", decrypted_text)

# Восстановление текста без знания ключа
for key, text in caesar_bruteforce(encrypted_text, language='ru'):
    print(f"Key {key}: {text}")