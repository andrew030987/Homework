# В списке чисел проверить, все ли элементы являются уникальными, т. е. каждое число встречается только один раз.

lst = [1, 3, 6, 87, 2, 987, 403, 56, 18, 1, 731, 11, 90]

if len(set(lst)) == len(lst):
    print('All elements from the list are unique')
else:
    print('There are repeating elements in the list')
