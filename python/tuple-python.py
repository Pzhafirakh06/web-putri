numbers = (1,2,3,4,5)
print (numbers)
print(type(numbers))
print(len(numbers))  # jumlah item tuple

names = ["Sintia","Salma","Ruby"]
print(names)
print(type(names))
print(len(names))  

# access  tuple
# akses numbers index ke 2
print(numbers[2])
print(numbers[4])

# akses names index ke 3
print(names[2])

print(50 *"=")
print("Tuple Manipulation")
fruits =("Durian","Apple","Orange")
#fruits[1] ="Watermelon"  # Error : Tuple tidak boleh diubah

# cara memanipulasi tuple konversikan ke dalam list
fruits_list = list(fruits)
print(fruits_list)
print(type(fruits_list))
fruits_list[1]="Apple"

# jika list of tuple sudah di manipulasi konvert kembali mendai tuple

fruits = tuple(fruits_list)
print(fruits)
