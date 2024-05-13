tambah = lambda  angka1,angka2: angka1 + angka2
kurang = lambda  angka1,angka2: angka1 - angka2
bagi = lambda  angka1,angka2: angka1 / angka2
kali= lambda  angka1,angka2: angka1 * angka2

angka1 = float(input ("input angka pertama: "))
angka2 = float(input ("input angka kedua: "))

hasil_tambah = tambah(angka1,angka2)
print (f'{angka1}+{angka2}= {hasil_tambah}')

hasil_kurang = kurang(angka1,angka2)
print (f'{angka1}-{angka2}= {hasil_kurang}')

hasil_kali= kali(angka1,angka2)
print (f'{angka1}*{angka2}= {hasil_kali}')

hasil_bagi = bagi(angka1,angka2)
print (f'{angka1}/{angka2}= {hasil_bagi}')