# Задание 3.1. Если x - строка, то используя x.isdigit() вы можете проверить содержит ли x только цифры. Напишите функцию is_number(x), которая будет проверять, является ли записанная в x строка произвольным числом:
# is_number("-234.12") == True
# is_number("asdf") == False
# http://heller.ru/course/viewtopic.php?f=7&t=30


def is_number(x):
    """Finding out if the input is a number"""

    print (x)
    #checking how many dots are in string
    amountOfDots = 0
    for n in x:
        if n == ".":
            amountOfDots +=1
        if amountOfDots > 1:
            return False

    if x[0]=="-": #validating if "-"" is only on the first position
        x = x[1:]
        print (x)

    char_set = set(x)
    print (char_set)
    char_set.discard(".")
    print (char_set)

    for elem in char_set:
        if not elem.isdigit():
            return False

    return True

print (is_number("-235.46"))
print (is_number("asdf"))
print (is_number("-23.12"))
print (is_number("-23.1.2"))
print (is_number("23.1.2"))
print (is_number("234.12"))
print (is_number("a23a"))
