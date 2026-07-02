# Задача 1: Математический принт
# a, b = int(input()), int(input())
# print(a + b, a - b, a * b, a / b, a // b, a % b, (a ** 10 + b ** 10) ** 0.5, sep="\n")

# Задача 2: Вычисление ИМТ
# Weight = float(input())
# Height = float(input())
# IMT = Weight / (Height * Height)
# if IMT < 18.5:
#     print("Недостаточная масса")
# elif IMT > 25:
#     print("Избыточная масса")
# else:
#     print("Оптимальная масса")


# Задача 3: Стоимость строки
# text = len(input())
# print(f"{(text * 60) // 100} р. {(text * 60) % 100} коп.")

# Задача 4: Различные элементы
# print(len(set(input().split())))

# Задача 6: Произведение двух чисел
# n = int(input())
# numbers = []
# for _ in range(n):
#     numbers.append(int(input()))
# target = int(input())
# found = False
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] * numbers[j] == target:
#             found = True
#             break
# if found:
#     print("ДА")
# else:
#     print("НЕТ")

# Задача 7: Кремниевая долина (Антон)
# n = int(input())
# for i in range(1, n + 1):
#     text = input()
#     reference = "anton"
#     pointer = 0
#     for char in text:
#         if char == reference[pointer]:
#             pointer += 1
#             if pointer == 5:
#                 break
#     if pointer == 5:
#         print(i, end=" ")