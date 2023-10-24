with open('receipt.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        dish_amount = int(file.readline())
        print(dish_amount)

# with open('receipt.txt', encoding='utf-8') as file:
#     cookbook = {}
#     for line in file:
#         dish = line.strip()
#         dish_amount = int(file.readline())
#         dish_list = []
#         for _ in range(dish_amount):
#             structure = file.readline().strip()
#             ingredient, count, unit_measure = structure.split(' | ')
#             dish_list.append(
#                 {'ingredient_name': ingredient,
#                  'quantity': count,
#                  'measure': unit_measure}
#             )
#         cookbook[dish] = dish_list
#         file.readline()
# print(cookbook)
