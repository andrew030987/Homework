# Определить, сколько в числе четных цифр, а сколько нечетных. Число вводится с клавиатуры.


number = input('Please enter a number: ')

even = 0
odd = 0
try:
    for i in number:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'Number of odd digits: {odd}, Number of even digits: {even}')
except ValueError:
    print('Only integers are accepted on input')
