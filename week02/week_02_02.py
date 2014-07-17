# Задание 2.2
# Напишите функцию maximum_prime(n), которая принимает на вход какое-то натуральное число, а возвращает в качестве результата его наибольший простой множитель:
# maximum_prime(70) == 7
# maximum_prime(50) == 5
# maximum_prime(4294967297) = 6700417
# http://heller.ru/course/viewtopic.php?f=7&t=24

def maximum_prime(n):
    x = n-1
    for x in range(2,n-1):
        if (n%x == 0):
            result = x
        else:
            x= x-1



    return result

x = maximum_prime(50)
print ("Biggest prime: " +str(x))
