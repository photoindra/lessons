# Задание 2.2
# Напишите функцию maximum_prime(n), которая принимает на вход какое-то натуральное число, а возвращает в качестве результата его наибольший простой множитель:
# maximum_prime(70) == 7
# maximum_prime(50) == 5
# maximum_prime(4294967297) = 6700417
# http://heller.ru/course/viewtopic.php?f=7&t=24

def maximum_prime(n):
    mlt = n - 1
    result = n
    while (result != 1 and mlt != 1):
        if (result%mlt != 0):
            mlt -= 1
        else:
            result = mlt
            mlt -= 1
            continue
        continue
    return result

x = maximum_prime(70)
print ("Biggest prime is: " +str(x))
