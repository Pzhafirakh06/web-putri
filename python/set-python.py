'''
SET 
-> diawali dengan curly bracket {}
-> tidak berurutan
-> tidak dapat diubah
-> tidak bisa duplicate
'''
numbers = {0,1,2,3,4,5,6,7,8,9,7}
print(numbers)

country ={"India", "Taiwan", "Indonesia","Malaisya","Brunei"}
print(country)

#country[0] ="Singapura"  # errors karena set tidak bisa diubah

#print(country[0]) # Error : karena tidak  bisa diakses dengan index

for  i in country:
   print (i)
   
   print('=====SET MANIPULATION=====')
   names ={'Andy', "Benny", "Jhon", "Neni"}
   print(names)
   
   names.add('Tony')
   print(names)
   
   names.discard('Andy')
   print(names)
   
   names.discard('Fatih')
   print(names)
   
   names.remove('Benny')
   print(names)
   
   #names.remove('Fatih') # errors : item not found 
   #print(names)
   
   friends ={"Rendy", "Dzakwan", "Rana",}
   names.update(friends)
   print(names)
   
   friends_list ={"Fadhlan", "Khaira", "IIs",}
   names.update(friends_list)
   print(names)
   
   cars_model = set (("Honda","Volvo","Hyundai","4x4"))
   print(cars_model)