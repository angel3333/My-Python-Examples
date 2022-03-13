#Functional Programming Example
from functools import reduce

# Capitalize all of the currencies and print the list using map() function
my_currency = ['usd', 'eur', 'bgn', 'gbp', 'aud', 'cad', 'chf']


def capitalize(string):
    return string.upper()


print(list(map(capitalize, my_currency)))


# Filter the scores that pass over 50% using filter() function
scores = [73, 20, 65, 19, 76, 100, 88, 33, 49, 51, 99]


def is_smart_student(score):
    return score > 50


print(list(filter(is_smart_student, scores)))


# Zip the 2 lists into a list of tuples and sort the numbers from lowest to highest using zip() function
my_strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
my_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))


# Combine all of the numbers that are in a list on this file using reduce() function (my_numbers and scores)
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))
