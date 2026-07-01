import random
word_list = [
    "питон", "программист", "компьютер", "интернет", "функция", 
    "переменная", "разработчик", "матрица", "инженер", "сервер",
    "алгоритм", "кодинг", "ноутбук", "монитор", "клавиатура",
    "автоматизация", "база", "логика", "интерфейс", "терминал",
    "фриланс", "заработок", "проект", "ошибка", "индекс",
    "скрипт", "модуль", "библиотека", "структура", "процессор"
]
def get_word(words):
    random_word = random.choice(words)
    return random_word.upper()
def play():
    secret_word = get_word(word_list)
    world_complection = ['_'] * len(secret_word)
    lives = 6
    guessed_litters = []
    while lives > 0 and '_' in world_complection:
        print("\nЗагаданное слово:", *world_complection)
        print(f"Осталось жизней: {lives}")
        guess = input("Введи букву: ").upper().strip()
        if not guess.isalpha() or len(guess) != 1:
            print("Ошибка! Введи строго одну букву.")
            continue
        if guess in guessed_litters:
            print("Ты уже вводил эту букву! Попробуй другую.")
            continue
        guessed_litters.append(guess)
        if guess in secret_word:
            print(f"Отлично! Буква '{guess}' есть в слове.")
            for index in range(len(secret_word)):
                if secret_word[index] == guess:
                    world_complection[index] = guess
        else:
            print(f"Упс, буквы '{guess}' нет в слове.")
            lives -= 1
    if '_' not in world_complection:
        print(f"\nПОЗДРАВЛЯЮ! Ты угадал слово: {secret_word} 🎉")
        print("Ты спас человека от виселицы!")
    else: 
        print(f"\nИГРА ОКОНЧЕНА. Жизни закончились. 💀")
        print(f"Компьютор загадал слово: {secret_word}")
again = 'д'

while again.lower() == 'д':
    play()
    again = input('Играем еще раз? (д = да, н = нет):')
