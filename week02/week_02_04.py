
# Задание 2.4. Напишите функцию fibo так, чтобы она вычислялась эффективно, то есть без рекурсии.
#Числа фибоначи:
#0,1,1,2,3,5,8,13,21,34,55

def fibo(n):
    a = 0
    b = 1
    i = 2 #2 because first and secont are 0 and 1
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    while (i != n):
        result =  a + b
        i += 1
        a = b
        b = result
    return result
n = 11
print (str(n) + "th fibonacci number is: "+ str(fibo(n)))
