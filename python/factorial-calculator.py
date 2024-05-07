def factorial(number):
   if number <= 1:
    return 1
   else:
      result = number * factorial(number-1)
      return result

number = int(input("Masukkan angka:"))
hasil = factorial(number)
print(f"Faktorial dari {number} = {hasil}")
