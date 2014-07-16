

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

# def anotherFactorial(r):
#     print ("starting to calculate factorial of " + str(r))
#     if r==1: result = 1
#     else: result = r * anotherFactorial(r-1)
#     print ("Calculated " + str(r) + "!=" + str(result))
#     return result

# # x = factorial(3)
# # print ("3! = " + str(x))

# y = anotherFactorial(3)
# print ("3! = " + str(y))

# def input_int(n):
#     min_value = 1
#     max_malue = 100
#     if x.isdigit():
#         print "It's a number"

def fibofibo(n):
  if n == 0: return 0
  if n == 1: return 1
  return fibo(n - 1) + fibo(n - 2)

import time

def compare_functions(f, g, arg):
  i = 0
  t1 = 0
  t2 = 0
  while i < 10:
    last_time = time.clock()
    f(arg)
    t1 += time.clock() - last_time
    last_time = time.clock()
    g(arg)
    t2 += time.clock() - last_time
    i += 1
  print(t2 / t1)

# допустим fibo1 и fibo2 - это две функции
# вычисляющие значения чисел Фибоначчи,
# но разными методами
compare_functions(fibo, fibo, 50)
# после этого вызова на экран будет выведено
# во сколько раз вторая функция работает быстрее
# или медленнее первой
