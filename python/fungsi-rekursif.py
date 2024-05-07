def countdown (number):
    print(number)
    if number == 0:
          return 
    else:
          countdown(number-1)
          
countdown(10)

print(50*"=")
print('Faktorial')

def factorial(number):
   if number <= 1:
    return 1
   else:
      result = number * factorial(number-1)
      return result

lima = factorial(5)
print(lima)

enam = factorial(6)
print(enam)