# Задание 2.1. Напишите функцию input_int(a, b), которая будет работать так же как функция input() без параметров, но только она будет проверять, что введённая пользователем строка действительно является числом в интервале [a;b], и если это не так, то будет просить пользователя повторить попытку ввода.

# Проверить, что введённая строка является числом можно так:
# x = input()
# if x.isdigit():
  # значит число

# def factorial(n):
#     i = 1
#     result = 1
#     while i < n:
#         result *= i
#         i += 1
#     return result


def input_int(a, b):
    min_value = a
    max_value = b
    print ("Enter number between "+ str(min_value)+" and "+str(max_value))
    x = input()
    while x.isdigit():
        print ("It's a number")
        x = int(x)
        print ("I converted it to int")
        return x
    else:
        print ("You need to enter a number")
        
    while x > max_value or x < min_value:
        print ("Please try again to enter number between "+ str(min_value)+"and"+str(max_value))
        x = input()
        continue
    else:
        print ("The number is correct")
    return x

y = input_int(1,100)

print ("printing last answer " +str(y))
