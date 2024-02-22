def caesar_cipher(text, shift):
    encrypted_text = ""
    alphabet_size = 32  # Размер русского алфавита
    for char in text:
        if char.isalpha():  # Проверка, является ли символ буквой
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('я'):
                    shifted -= alphabet_size
            elif char.isupper():
                if shifted > ord('Я'):
                    shifted -= alphabet_size
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

text = "Блажен, кто верует, тепло ему на свете!"
shift = 11
encrypted_text = caesar_cipher(text, shift)
print("Зашифрованный текст:", encrypted_text)