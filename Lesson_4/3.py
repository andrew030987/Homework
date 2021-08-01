# Дана строка, содержащая натуральные числа и слова.
# Необходимо сформировать список из чисел, содержащихся в этой строке.
# Например, задана строка "abc83 cde7 1 b 24". На выходе мы должны получить список [83, 7, 1, 24].


"""
Making a list of example strings to test our function in different ways
"""
strings = ["abc83 cde7 1 b 24",
           "abc83cde71b24",
           "1a22 bc 83 c123d 123e7 1 b 24",
           "ab3c83 cde7 g 3 g 3341 b 2fsf sf4",
           "12344ggg33g3 {}-=  334 sdf d 4f 3f3f3 12d l"]


def numbers_separator(string):
    result_string = ''
    for char in string:
        if char.isalpha():
            result_string += ' '
        else:
            result_string += char
    result_string = result_string.split(' ')
    result_list = [item for item in result_string if item.isnumeric()]
    return result_list


"""
Printing our results
"""
for i in strings:
    print(numbers_separator(i))
