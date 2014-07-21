# 1. Multiples of 3 and
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

n = 1000
result = 0
testNumber = n - 1
while (testNumber > 2):
    if not (n%testNumber and testNumber%3 and testNumber%5):
        result += testNumber
    testNumber -= 1
print ("Result is " + str(result))

#result is 233180
