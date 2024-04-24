n = int (input("Enter range :"))
choise = input("Enter Even/odd :").lower()

if choise == "even":
   print("Even numbers in the range")
   for  i in range (n):
      if i % 2 ==0:
          print(i)
           
elif choise == "odd":
   print("odd numbers in the range")
   for  i in range (n):
      if i  % 2 ==1:
          print(i)