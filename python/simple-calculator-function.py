def tambah (angka1,angka2):
          return angka1 + angka2

def kurang (angka1, angka2):
           return angka1 - angka2 
angka1 = float(input("Angka Pertama:"))
angka2 = float(input("Angka Kedua:"))

hasil_tambah = tambah(angka1,angka2)
print (f"{angka1}  + {angka2} = {hasil_tambah}")

hasil_kurang = kurang(angka1,angka2)
print (f"{angka1}  - {angka2} = {hasil_kurang}")

def kali (angka1, angka2):
           return angka1 * angka2 

hasil_kali = kali(angka1,angka2)
print (f"{angka1} * {angka2} = {hasil_kali}")

def bagi (angka1, angka2):
           return angka1 / angka2 

hasil_bagi = bagi(angka1,angka2)
print (f"{angka1} /{angka2} = {hasil_bagi}")