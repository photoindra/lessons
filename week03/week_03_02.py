# coding: utf-8
# Задание 3.2. Найдите описание решета Эратосфена и реализуйте этот алгоритм. Вы должны написать функцию sieve(n), которая возвращает список всех простых чисел вплоть до n. (Если бы функцию maximum_prime из прошлой недели пришлось бы звать для целого набора чисел, то было бы куда эффективнее вначале получить список всех простых чисел используя решето Эратосфена, а затем уже искать делители среди известных простых чисел). Обратите внимание, что в Википедии приведена реализация на Питоне якобы решета Эратосфена. На самом деле приведённый там код - это не решето Эратосфена, а его подобие, которое работает на порядок хуже оригинального алгоритма. (Задание со звёздочкой - объясните чем хуже алгоритм из Википедии).

# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


def sieve(n):
    """Returning list of all prime numbers til n"""
    if n==2:
        return n
    myList = list(range(2, n+1))
    print (myList)

    p = 2
    listToRemove = []
    resultList = []

    while True:

        for y in range(p,n+1,p):
            print ("p is " + str(p))
            print ("y is " + str(y))
            if y != p:
                listToRemove.append(y)
            print ("listToRemove is " + str(listToRemove))
            resultList = [x for x in myList if x not in listToRemove]
            print ("resultList is "+ str(resultList))

        for z in resultList:
            if z > p:
                p = z
                print ("new p is " +str(z))
                break

        print ("For now last number in result list is: " + str(resultList[-1]))
        if p == resultList[-1]:
            return resultList

print (sieve(10))
