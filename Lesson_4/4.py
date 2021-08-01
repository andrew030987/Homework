# Написать функцию is_year_leap, принимающую 1 аргумент — год,
# и возвращающую True, если год високосный, и False иначе.


def is_year_leap(year):
    return year % 400 == 0 and year % 100 != 0 or year % 4 == 0


"""
Unittest to test our function
"""
import unittest


class TestIsYearLeap(unittest.TestCase):
    def test_positive(self):
        test_values = [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964,
                       1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028,
                       2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092,
                       2096]

        for test_value in test_values:
            self.assertTrue(is_year_leap(test_value), 'Error')

    def test_negative(self):
        test_values_neg = [1903, 1907, 1911, 1917, 1921, 1925, 1927, 1933, 1935, 1941, 1945, 1947, 1951, 1957, 1961,
                           1963, 1969, 1971, 1977, 1981, 1985, 1989, 1991, 1997, 2001, 2005, 2009, 2011, 2017, 2021,
                           2025, 2029, 2031, 2035, 2041, 2045, 2049, 2051, 2057, 2061, 2065, 2067, 2071, 2077, 2081,
                           2085, 2089, 2091, 2095]

        for test_value in test_values_neg:
            self.assertFalse(is_year_leap(test_value), "Error")


if __name__ == '__main__':
    unittest.main()
