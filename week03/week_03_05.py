# Задание 3.5.Для работы со всеми перечислимыми объектами Python предлагает функции map и filter. Прочитайте про эти функции и реализуйте сами собственные функции my_map и my_filter, которые работают точно так же как map и filter.

def foo(x):
  x *= 2
  return x

testList = list(range(1, 14))
print("Original list is:")
print(testList)

resultList = list(map(foo, testList))
print("Result of map function:")
print(resultList)

def my_map(workingFu, workingList):
  """recreating python map function"""
  resultList = []
  for i in range(len(workingList)):
    resultList.append(workingFu(workingList[i]))
  return resultList

print("Result of my_map function:")
print(my_map(foo, testList))



fastList = [6, 7, 8, 9, 8, 10, 12, 14, 16, 18, 20, 22, 24, 0 , 1, 4, 17, 34, 2]
print("Original list is:")
print(fastList)


def fooTrueFalse(x):
  """test function that returns true or false"""
  if x < 10:
    return True
  else:
    return False

resultList = list(filter(fooTrueFalse, fastList))
print("Result of filter function:")
print(resultList)

def my_filter(workingFu, workingList):
  """recreating python filter function"""
  resultList = []
  for i in range(len(workingList)):
    if workingFu(workingList[i]):
      resultList.append(workingList[i])
  return resultList

print("Result of my_filter function:")
print(my_filter(fooTrueFalse, fastList))

