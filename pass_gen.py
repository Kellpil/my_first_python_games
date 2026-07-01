import random
def get_valid_int(prompt):
    while True:
        user_number = input(prompt)
        if user_number.isdigit():
            number = int(user_number)
            if number > 0:
                return number
            print("Ошибка! число должно быть больше 0.")
        else:
            print("Ошибка! Вами введенный символ - не целое число. Попробуйте еще раз!")
    
len_pwds = get_valid_int("Сколько паролей хотите создать? ")
len_pwd = get_valid_int("Какой длины хотите создать пароль? ")

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

digt = input('Включать ли цифры? "0123456789" (д = да, н = нет): ').lower.strip
up = input('Включать ли прописные буквы? "ABCDEFGHIJKLMNOPQRSTUVWXYZ?" (д = да, н = нет): ').lower.strip
low = input('Включать ли строчные буквы* "abcdefghijklmnopqrstuvwxyz?" (д = да, н = нет): ').lower.strip
puk = input('Включать ли символы() "!#$%&*+-=?@^_?" (д = да, н = нет): ').lower.strip
delt = input('Исключать ли неоднозначные символы? "il1Lo0O" (д = да, н = нет): ').lower.strip

pool = ""
if digt == "д":
    pool += digits
if up == "д":
    pool += uppercase_letters
if low == "д":
    pool += lowercase_letters
if puk == "д":
    pool += punctuation

if delt == "д":
    for bad_char in "il1Lo0O":
        pool = pool.replace(bad_char, "")

if not pool:
    print("Ошибка! Вы не выбрали ни одного типа символов. Мешок пуст,пароль создать нельзя.")
print("\nВаши сгенерированные пароли:")
for _ in range(len_pwds):
    password = ""
    for _ in range(len_pwd):
        password += random.choice(pool)
    print(password)