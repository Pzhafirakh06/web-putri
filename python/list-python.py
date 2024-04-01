numbers = [1,2,3,4,5]
print(numbers)
print(type(numbers))
print(len(numbers))  # jumlah  element list

names = ["Sintia","Salma","Ruby"]
print(names)
print(type(names))
print(len(names))  

print(50*"=")
print("List Manipulation")

animals =["Panda","Cat","Lion",]
print(animals)
# menambah item list
animals.append("owl")
print(animals)

# mengubah item
animals[1]="Mouse"
print(animals)

# menghapus item list
animals.remove("Lion")
print(animals)

# clear all item
animals.clear()
print(animals)

# list contructor
country = list (("Indonesia", "Singapure","Brunei","Sulawesi"))
print(country)
print(type(country))