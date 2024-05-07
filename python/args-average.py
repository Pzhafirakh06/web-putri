def average(*numbers):
   jumlah = sum(numbers)
   total = len(numbers)
   avg = jumlah / total
   return avg

rata1 =  average(160,40,100)
print(f'Hasil Rata-rata={rata1}"')

rata2 =  average(90,80,87,67,70)
print(f'Hasil Rata-rata={rata2}"')