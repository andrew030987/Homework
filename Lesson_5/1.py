# 1. Написать функцию date, принимающую 3 аргумента — день, месяц и год.
# Вернуть True, если такая дата есть в нашем календаре, и False иначе

def calendar(day, month, year):
    leap = False
    if year % 400 == 0 and year % 100 != 0 or year % 4 == 0:
        leap = True

    long_months = {(1, 3, 5, 7, 8, 10, 12): [i for i in range(1, 32)]}
    short_months = {(4, 6, 9, 11): [i for i in range(1, 31)]}

    if any((all((month == 2, leap, day in [i for i in range(1, 30)])), all(
            (month == 2, not leap, day in [i for i in range(1, 29)])),
            all((month in list(long_months.keys())[0], day in list(long_months.values())[0])), all(
            (month in list(short_months.keys())[0], day in list(short_months.values())[0])))):
        return True
    else:
        raise Exception('There is no such date in calendar')
