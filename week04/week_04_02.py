# Задание 2. Напишите программу, переводящую числа из шестнадцатеричной системы счисления в семиричную. Сами числа задаются строками.


def hexToBaseSeven(x):
  """Returns base 7 representation of a hex number"""
  number = int(x,16)
  res = ""
  while number:
    res += str(number%7)
    number //= 7
  return res[::-1]

testNumberIn16 = "5b94"
print("Base 7 representation of " + str(testNumberIn16) + " is:")
print(hexToBaseSeven(testNumberIn16))

