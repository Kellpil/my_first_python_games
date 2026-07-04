# Задача 1:
# flat_list = [num for sub_list in list1 for num in sub_list]
# print(sum(flat_list) / len(flat_list))

# Задача 2: Треугольник Паскаля 1 🌶️
# def pascal(n):
#     row = [1]
#     for _ in range(n):
#         next_row = [1]
#         for i in range(len(row) - 1):
#             next_row.append(row[i] + row[i + 1])
#         next_row.append(1)
#         row = next_row
#     return row
# n = int(input())
# for i in range(n):
#     print(*pascal(i))

# Задача 3: Разбиение на чанки 🌶️
# def chunked(text, num):
#     chars = []
#     char = []  
#     text_list = text.split()  
#     for i in range(len(text_list)):
#         if len(char) < num:
#             char.append(text_list[i])
#         else:
#             chars.append(char)
#             char = [text_list[i]]  
#     if char:
#         chars.append(char)
    
#     return chars

# text = input()
# num = int(input())
# print(chunked(text, num))

# Задача 4: Вывести матрицу 1
# n, m = int(input()), int(input())
# matrix = [[input() for _ in range(m)] for _ in range(n)]
# for row in matrix:
#     print(*row)

# Задача 5: Максимальный в области 1
# n = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(n)]
# print(max([matrix[i][j] for i in range(n) for j in range(i + 1)]))

# Задача 6: Суммы четвертей
# n = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(n)]
# total1, total2, total3, total4 = [], [], [], []

# for i in range(n):
#     for j in range(n): 
#         if j > i and j < n - i - 1:
#             total1.append(matrix[i][j])
#         elif j > i and j > n - i - 1:
#             total2.append(matrix[i][j])
#         elif j < i and j > n - i - 1:
#             total3.append(matrix[i][j])
#         elif j < i and j < n - i - 1:
#             total4.append(matrix[i][j])
# print(f"Верхняя четверть: {sum(total1)}")
# print(f"Правая четверть: {sum(total2)}")
# print(f"Нижняя четверть: {sum(total3)}")
# print(f"Левая четверть: {sum(total4)}")