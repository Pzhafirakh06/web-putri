def even_number(numbers):
   even_list= []
   for num in numbers:
        if num % 2 == 0:
          even_list.append(num)

   print(even_list)


even_number(range(1,100))

print("===FILTER===")
numbers = range(1,101)

def is_even(number):
      return number % 2 == 0

even_numbers = filter(is_even,numbers)

print(list(even_numbers))    