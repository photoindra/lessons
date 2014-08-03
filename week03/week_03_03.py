# coding: utf-8

# Задание 3.3. Пусть номер телефона - это просто семизначное число, а имя - это случайная строка символов английского алфавита, имеющая какую-то случайную длину от 4 до 10 символов. Сгенерируйте случайную "телефонную книгу", состоящую из 100000 телефонов и запишите её в файл (убедитесь, что у вас действительно 100000 разных телефонов). Придумайте сами в каком формате должны храниться данные в этом файле.

def generatePhones(n):
    """Create dictionary
    Define how many "words" will be inside
    while length of dictionary less that size generate new telephone number
    IF number IS NOT in the dictionary yet
    generate name and add it with number to dictionary"""

    import random
    import string

    phoneBook = {}
    bookSize = n

    with open('phone_numbers.txt', 'w') as f:
                f.write("")

    while len(phoneBook) < bookSize:

        phoneNumber = random.randint(1000000, 9999999)

        if phoneNumber not in phoneBook:
            personName = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(4,10)))
            phoneBook[phoneNumber] = personName

            myFile = str(phoneNumber) + str(' - ') + str(personName) + str("\n")
            with open('phone_numbers.txt', 'a') as f:
                f.write(myFile)

    return phoneBook

numOfPhones = 100000
listOfPhones = generatePhones(numOfPhones)
# print (listOfPhones)


