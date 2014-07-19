# Задание 2.3. По аналогии с тем, как я поступил с факториалом, сделайте вывод каждого шага вычисления функции fibo на экран, чтобы понять что реально тут происходит и почему функция работает медленно.

def fibo(n, step):
    print("Calculating with: " + str(n))

    if n == 0:
        print("n is: " + str(n))
        step += 1
        print ("and step is: " + str(step))
        return 0
    if n == 1:
        print("n is: " + str(n))
        step += 1
        print ("and step is: " + str(step))
        return 1
    step += 1
    print ("step is: " + str(step))
    return fibo(n - 1, step) + fibo(n - 2, step)

n = 5
step = 0
print (str(n) + "th fibonacci number is: "+ str(fibo(n, step)))
