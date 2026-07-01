import random
secret_number = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку")
def is_valid(n):
    return 100 >= n >= 1
attempts = 0
while True:
    guess_text = input("Введите число от 1 до 100:\n")
    if not guess_text.isdigit():
        print("А может все-таки введем целое число?")
        continue
    guess = int(guess_text)
    if not is_valid(guess):
        print("А может все-таки введем целое число от 1 до 100?")
        continue
    attempts += 1
    if guess < secret_number:
        print("Ваше число меньше заданного, попробуйте еще раз!")
    elif guess > secret_number:
        print("Ваше число больше заданного, попробуйте еще раз!")
    else:
        print("Вы угадали число УРА!!!")
        print(f"У вас ушло попыток: {attempts}")
        break
    