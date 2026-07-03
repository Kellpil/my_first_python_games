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
# print(pascal(n))