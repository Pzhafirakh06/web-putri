number1=16
number2= 7

#equals to
print (number1==number2)

# not equal to
print(number1!=number2)

# greater than
print ( number1 > number2)

#  less than
print (number1 < number2)

#greater than equal
print(number1>=number2)

# less than equal
print(number1<=number2)

print("="  *20)
print("Logical  Operator")

print(number1==16 and number1 <10) # true and false = false
print(number1==16 and number1 >10) # true and false = true

print(number1==16 or number1 <10) # true or false = True
print(number2==16 or number1 <10) # true or false = False

print (not number1> 10)

print("="  *20)
print("Identity Operator")

number1 = 14
number2 = 15
text="Hello World"

print(number1 is number2)
print(number1 is 14)

print(number1 is not number2)
print (number1 is not text)

print("="  *20)
print("Membership Operator")

letter1 = "a"
words= "Hello Words"
number = 5
numbers = [1,2,3,4,5]

print(letter1 in words)
print(letter1 not in words)

print(number in numbers)