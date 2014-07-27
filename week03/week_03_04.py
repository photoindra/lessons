# Прочитайте вашу телефонную книгу из файла:
# а) В словарь
# б) В список кортежей:
# [(1234567, "RandomName"), (0034625, "Olololo"), ...]
# в) В список кортежей, упорядоченных по номеру телефона (подсказка: используйте метод sort):
# [(0034625, "Olololo"), (1234567, "RandomName"), ...]

# Напишите функцию get_name(phone), которая по номеру телефона возвращает имя. Для упорядоченного списка придумайте эффективный метод поиска. Сравните скорость поиска в трёх случаях (придумайте сами методику, по которой можно сравнить скорость).

# week_03_04_part_a -------------

def readingToDic():

    dic = {}
    with open("phone_numbers.txt") as f:
        for line in f:
            line = line.strip ('\n')
            (phone, name) = line.split(" - ")
            dic[int(phone)] = name
    return dic

myDic = readingToDic()
print (myDic)
print ("End of part A\n")

# week_03_04_part_b -------------

def readingToList():
    myList = []
    with open("phone_numbers.txt") as f:
        for line in f:
            line = line.strip ('\n')
            (phone, name) = line.split(" - ")
            phone = int(phone)
            myTuple = (phone, name)
            myList.append(myTuple)
    return myList

myListB = readingToList()
print (myListB)

print ("End of part B\n")

# week_03_04_part_c -------------

def readingToSortedList():
    myList = []
    with open("phone_numbers.txt") as f:
        for line in f:
            line = line.strip ('\n')
            (phone, name) = line.split(" - ")
            phone = int(phone)
            myTuple = (phone, name)
            myList.append(myTuple)

    myListSorted = sorted(myList, key=lambda tup: tup[0])
    return myListSorted

myListC = readingToSortedList()
print (myListC)

print ("End of part C\n")

# get_name(phone) -------------

def get_name_01(phone):
    phoneBook = readingToDic()
    if phone in phoneBook:
        name = phoneBook[phone]
        print ("Phone number of " + str(phone) + " belongs to " + str(name.capitalize()))
    else:
        print ("There is no such number in telephone book.")


