def get_valid_int(prompt):
    while True:
        user_number = input(prompt)
        if user_number.isdigit():
            number = int(user_number)
            if number > 0:
                return number
            print("Ошибка! Шаг сдвига должно быть больше 0.")
        else:
            print("Ошибка! Введите целое число.")
eng_lower = "abcdefghijklmnopqrstuvwxyz"
eng_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rus_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

direction = input("Что мы делаем? (ш = шифруем, д = дешифруем): ").lower().strip()

shift = get_valid_int("Введите шаг сдвига (число): ")

text = input("Введите ваш текст: ")

def enscrypt_char(char, shift, direction):
    if direction == "д":
        current_shift = -shift
    else:
        current_shift = shift
    if char in eng_lower:
        return eng_lower[(eng_lower.find(char) + current_shift) % 26]
    elif char in eng_upper:
        return eng_upper[(eng_upper.find(char) + current_shift) % 26]
    
    elif char in rus_lower:
        return rus_lower[(rus_lower.find(char) + current_shift) % 32]
    elif char in rus_upper:
        return rus_upper[(rus_upper.find(char) + current_shift) % 32]
    else:
        return char
    
result_text = ''
for symbol in text:
    result_text += enscrypt_char(symbol, shift,direction)
if direction == "д":
    print(f"\nРасшифрованный текст: {result_text}")
else:
    print(f"\nЗашифрованный текст: {result_text}")