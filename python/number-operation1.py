number_int = 99999
print(number_int)
print(type(number_int))

number_int_negatif=-123
print(number_int_negatif)
print(type(number_int_negatif))

print("------------")

number_float=56.896
print(number_float)
print(type(number_float))

print("------------")

number_complex = 3 + 5j
print(number_complex)
print(type(number_complex))

print("------------")

number1=80
number2=4

add=number1+number2
print(f"{number1}{number2}={add}")
print("------------")


sub=number1-number2
print(f"{number1}{number2}={sub}")
print("------------")

multiply=number1*number2
print(f"{number1}{number2}={multiply}")
print("------------")

eks=number1**number2
print(f"{number1}^{number2}={eks}")
print("------------")

sisa_bagi = 10 % 3 
print(f"10 % 3={sisa_bagi}")
print("------------")


number = 10
number += 2 # number = number + 2
print(number)

number = 4
number += 2 # number = number -4
print(number)

number *= 3 # number= number-3
print(number)

print("simple Calculator")
print("========\n")
angka1= int(input("input The Fist Number:"))
angka2= int(input("input The Fist Number:"))

result_add = angka1 + angka2
print(f"{angka1}+{angka2}={result_add}")
print("------------")

result_add = angka1-angka2
print(f"{angka1}-{angka2}={result_add}")
print("------------")

result_add = angka1*angka2
print(f"{angka1}*{angka2}={result_add}")
print("------------")