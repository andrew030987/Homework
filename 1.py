# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые больше 8, но не более чем в 5 раз.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

result = [num for num in a if num > 8 and num <= 40]

print(result)
