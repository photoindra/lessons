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
# print (myDic)
# print ("End of part A\n")

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

# print (myListB)
# print ("End of part B\n")

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

# print (myListC)
# print ("End of part C\n")

# get_name(phone) -------------

# getting name from dictionary
def get_name_from_dic(phone):
    phoneBook = readingToDic()
    if phone in phoneBook:
        name = phoneBook[phone]
        return name

def get_name_from_list_b(phone):
    """getting name from unorded list using simple if"""
    phoneBook = readingToList()
    n = 0
    while n != len(phoneBook):
        if phoneBook[n][0] == phone:
            name = phoneBook[n][1]
            return name
            break
        n += 1
# Another way from github can be something like:
# Without dict, a generator would give you:
# next((item[1] for item in l if item[0] == search), None)
# next returns the second argument (None) if the generator is empty

def get_name_from_list_c(phone):
    """getting name from sorted list using bisect"""
    from bisect import bisect_left
    phoneBook = readingToSortedList()

    tempListOfPhones = [tup[0] for tup in phoneBook]
    name = phoneBook[bisect_left(tempListOfPhones, phone)][1]
    return name

def get_name_from_list_d(phone):
    """getting name from sorted list using half-list"""
    phoneBook = readingToSortedList()

    center = phoneBook[len(phoneBook)//2]
    phoneBookLow = phoneBook[0:int(len(phoneBook)//2)]
    phoneBookHi = phoneBook[int(len(phoneBook)//2):]

    while phone != center[0]:
      halfBookSize = len(phoneBook)//2
      center = phoneBook[halfBookSize]
      phoneBookLow = phoneBook[0:int(halfBookSize)]
      phoneBookHi = phoneBook[int(halfBookSize):]
      if phone > center[0]: phoneBook = phoneBookHi
      if phone < center[0]: phoneBook = phoneBookLow
    return center[1]


searchNumber = 6911219
print ("Getting name from dictionary:")
print ("Phone number belongs to " + str(get_name_from_dic(searchNumber).capitalize()) + "\n")

print("Getting name from unorded list using simple if:")
print ("Phone number belongs to " + str(get_name_from_list_b(searchNumber).capitalize()) + "\n")

print ("Getting name from sorted list using bisect:")
print ("Phone number belongs to " + str(get_name_from_list_c(searchNumber).capitalize()) + "\n")

print ("Getting name from sorted list using half-list:")
print ("Phone number belongs to " + str(get_name_from_list_d(searchNumber).capitalize()) + "\n")

import time

def compare_functions(test01, test02, test03, test04, arg):
  i = 0
  t1 = 0
  t2 = 0
  t3 = 0
  t4 = 0
  while i < 10:
    last_time = time.clock()
    test01(arg)
    t1 += time.clock() - last_time
    last_time = time.clock()
    test02(arg)
    t2 += time.clock() - last_time
    last_time = time.clock()
    test03(arg)
    t3 += time.clock() - last_time
    last_time = time.clock()
    test04(arg)
    t4 += time.clock() - last_time
    i += 1
  print ("Getting name from dictionary:")
  print(t1)
  print("Getting name from unorded list using simple if:")
  print(t2)
  print ("Getting name from sorted list using bisect:")
  print(t3)
  print ("Getting name from sorted list using half-list:")
  print(t4)
  # print(t2 / t1)
  # print(t3 / t1)
  # print(t3 / t2)
  # print (t1)
  # print (t2)

compare_functions(get_name_from_dic, get_name_from_list_b, get_name_from_list_c, get_name_from_list_d, searchNumber)

