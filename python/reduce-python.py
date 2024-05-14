from functools import reduce

def addtion(number1, number2):
          return number1 + number2

number_list = range(1,11)

x = reduce(addtion, number_list)

print(x)