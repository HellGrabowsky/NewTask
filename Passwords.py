import random

# Строковые константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
ambiguous_chars = 'il1Lo0O'

def generate_password(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    num_passwords = int(input("Введите количество паролей для генерации: "))
    password_length = int(input("Введите длину одного пароля: "))

    include_digits = input("Включать ли цифры (0123456789)? (да/нет): ").lower() == 'да'
    include_lowercase = input("Включать ли строчные буквы (abcdefghijklmnopqrstuvwxyz)? (да/нет): ").lower() == 'да'
    include_uppercase = input("Включать ли прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? (да/нет): ").lower() == 'да'
    include_punctuation = input("Включать ли символы (!#$%&*+-=?@^_)? (да/нет): ").lower() == 'да'
    exclude_ambiguous = input("Исключать ли неоднозначные символы (il1Lo0O)? (да/нет): ").lower() == 'да'

    chars = ''
    if include_digits:
        chars += digits
    if include_lowercase:
        chars += lowercase_letters
    if include_uppercase:
        chars += uppercase_letters
    if include_punctuation:
        chars += punctuation
    if exclude_ambiguous:
        chars = ''.join(char for char in chars if char not in ambiguous_chars)

    if not chars:
        print("Ошибка: Не выбраны символы для генерации пароля.")
        return

    print("Генерация паролей:")
    for _ in range(num_passwords):
        password = generate_password(password_length, chars)
        print(password)

if __name__ == "__main__":
    main()
