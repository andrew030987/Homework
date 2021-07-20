# Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.


text = "text  Lorem ipsum dolor sit amet Lorem dolor lorem consectetur dolor dolor adipiscingadipiscing elit orem dolor ipsum lorem dolor "

words = text.lower().split()

# 1) Находим наиболее часто встречающееся слово:
# 1.1) Первый вариант, обычный:

words_count = 0
for word in words:
    if words.count(word) > words_count:
        most_frequent_word = word
        words_count = words.count(word)
print(most_frequent_word)

# 1.2) Второй вариант, решение в 1 строку:

e = list(dict(sorted({words.count(i): i for i in words}.items())).values())[-1]
print(e)

# 2) Находим самое длинное слово:
# 2.1) Первый вариант, обычный:


longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)

# 2.2) Второй вариант, решение в 1 строку:

f = words[list(dict(sorted({len(i): words.index(i) for i in words}.items())).values())[-1]]
print(f)
