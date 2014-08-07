# Задание 1. В восьмеричной системе счисления используется восемь цифр от 0 до 7. Напишите функцию, принимающую на вход строку в восьмеричной системе счисления, и выдающую в качестве результата число (в обычном Питоновском смысле).

testNumberIn10 = 1010

def converter(x):
  """returning number in 10th base, 16th, 8th and 2nd"""
  return "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(x)

print("Our test number:")
print(converter(testNumberIn10))


def converterTo8(x):
  """returning number in base of 8"""
  return "{0:o}".format(x)
print("Our test number in base of 8:")
print(converterTo8(testNumberIn10))


# simple way:
def eightToTenA(x):
  """receiving number with base 8 and returning decimal"""
  result = int(x, 8)
  return result

print("Using int(x, base) way:")
print(eightToTenA(converterTo8(testNumberIn10)))


# hard way:
def eightToTenB(x):
  """receiving number with base 8 and returning decimal"""
  x = str(x)
  result = 0
  degree = 8
  position = len(x)-1
  for i in x:
    result += int(i)*(degree**position)
    position -= 1
  return result

print("Using sum of degrees:")
print(eightToTenB(converterTo8(testNumberIn10)))


