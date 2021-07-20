# Найдите три ключа с самыми высокими значениями 
# в словаре my_dict = {'a': 400, 'b': 58700, 'c': -560,'d': 'one', 'e': 20000, 'f': 2000, 'd': 400}

my_dict = {'a': 400, 'b': 58700, 'c': -560, 'd': 'one', 'e': 20000, 'f': 2000, 'd': 400}

keys = [key for key, value in my_dict.items() if value in sorted([value for value in my_dict.values()])[-3:]]
print(keys)
