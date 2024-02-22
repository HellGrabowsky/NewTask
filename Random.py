import random

def is_valid(guess):
    try:
        guess = int(guess)
        return 1 <= guess <= 100
    except ValueError:
        return False

def number_guessing_game():
    attempts = 0
    random_number = random.randint(1, 100)
    
    print('Добро пожаловать в числовую угадайку!')
    
    while True:
        user_input = input('Введите число от 1 до 100: ')
        
        if not is_valid(user_input):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        
        attempts += 1
        user_number = int(user_input)
        
        if user_number < random_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif user_number > random_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print(f'Вы угадали, поздравляем! Количество попыток: {attempts}')
            break
            
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

number_guessing_game()
