# Задание 2.1. Напишите функцию input_int(a, b),
# которая будет работать так же как функция input() без параметров,
# но только она будет проверять, что введённая пользователем строка
# действительно является числом в интервале [a;b],
# и если это не так, то будет просить пользователя повторить попытку ввода.
# http://heller.ru/course/

def input_int(min_value, max_value):
    print ("Enter number between "+ str(min_value)+" and "+str(max_value)+":")
    x = input()

    while not x.isdigit() or int(x) > max_value or int(x) < min_value:
        print ("Please try again. Enter number between "+ str(min_value)+" and "+str(max_value)+":")
        x = input()

    x = int(x)
    return x

y = input_int(5,30)
print ("Great! You've entered: " +str(y))
