import time
import random


print ("\n Tipe data pemrograman \n")

teks = "Halo Dunia"
angka = 12
desimal = 1.12
cek = True
kosong = None

tipe = f"""
- Teks =  {teks}
- Angka = {angka}
- Desimal = {desimal}
- Cek     = {cek}
- Kosong  = {kosong}
"""

print (tipe)


print ("\n --- batas --- \n")




print ("\n Percabangan Dasar \n")

a = 10
random.randint (1, 10)

if a >= 5:
     print (f"Besar, angka a = {a}")

else:
     print (f"Kecil, angka a = {a}")


print ("\n --- batas --- \n")




print ("\n Percabangan Lanjutan \n")

b = 3
random.randint (1, 15)

if b >= 8:
     print (f"Besar, angka b = {b}")

elif b >= 5:
     print (f"Tengah, angka b = {b}")

else:
     print (f"Kecil, angka b = {b}")

print ("\n --- batas --- \n")




print ("\n percabangan nilai rapor \n")

nilai = 50

random.randint (1, 100)

if nilai >= 90:
     print (f"A, nilai = {nilai}")

elif nilai >= 80:
     print (f"B, nilai = {nilai}")

elif nilai >= 70:
     print (f"C, nilai = {nilai}")

elif nilai >= 60:
     print (f"D, nilai = {nilai}")

elif nilai >= 50:
     print (f"E, nilai = {nilai}")

else:
     print (f"Kecil banget, nilai = {nilai}")

print ("\n --- batas --- \n")



print ("\n Fungsi dengan Percabangan Dasar \n")

def run (e):

     time.sleep (1)

     if e >= 5:
          print (f"Besar, angka e = {e}")

     
     else:
          print (f"Kecil, angka e = {e}")

run (10)
run (8)
run (5)
run (4)
run (3)
run (2)
run (1)


print ("\n --- batas --- \n")



print ("\n Fungsi dengan Percabangan Lanjutan \n")

def rn (k):

     time.sleep (1)

     if k >= 8:
          print (f"Besar, angka k = {k}")

     elif k >= 5:
          print (f"Tengah, angka k = {k}")

     else:
          print (f"Kecil, angka k = {k}")

rn (10)
rn (8)
rn (6)
rn (7)
rn (5)
rn (4)
rn (3)
rn (2)
rn (1) 


print ("\n --- batas --- \n")




print ("\n Looping dasar \n")

for a in range (1, 11):
     time.sleep (1)
     print (f"Urutan ke - {a}")


print ("\n --- batas --- \n")



print ("\n For dasar 1 \n")

for i in range (11):
     time.sleep (1)
     print (f"Urutan ke - {i}")


print ("\n --- batas --- \n")




print ("\n While dasar \n")

a = 1

while a < 11:
     time.sleep (1)
     print (f"Urutan ke - {a}")
     a = a + 1


print ("\n --- batas --- \n")




print ("\n While dasar \n")

b = 11

while b > 0:
     time.sleep (1)
     print (f"Urutan ke - {b}")
     b = b - 1


print ("\n --- batas --- \n")


print ("\n For Nested 1 \n")

for x in range (1, 11):
     for y in range (1, 11):
          time.sleep (1)
          print (f"Luar : {x} dan Dalam : {y}")

print ("\n --- batas --- \n")



print ("\n Error Handling \n")

try:
     a = 10 / 0

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Berhasil")

finally:
     print ("Selesai")


print ("\n --- batas --- \n")



print ("\n Fungsi dengan Percabangan Lanjutan \n")

def un (k):

     time.sleep (1)

     if k >= 8:
          print (f"Besar, angka k = {k}")

     elif k >= 5:
          print (f"Tengah, angka k = {k}")

     else:
          print (f"Kecil, angka k = {k}")

un (10)
un (9)
un (8)
un (7)
un (6)
un (5)
un (4)
un (3)
un (2)
un (1)


print ("\n --- batas --- \n")



print ("\n Fungsi dengan usia produktif manusia \n")

def run (e):

     time.sleep (1)

     if e >= 15 and e <= 40:
          print (f"Masuk usia produktif, usia = {e}")

     elif e > 40:
          print (f"Sudah tua, usia = {e}")

     else:
          print (f"Masih kecil usiannya, usia = {e}")

run (60)
run (50)
run (40)
run (30)
run (20)
run (10)

print ("\n --- batas --- \n")



print ("\n OOP dasar \n")

class Kucing:

     time.sleep (1)

     def __init__(self, nama, warna):
          self.nama = nama
          self.warna = warna

     def aksi (self):
          print (f"- Kucing {self.nama} dengan warna {self.warna}")

hasil_1 = Kucing ("Rayyan", "Hitam")
hasil_2 = Kucing ("Fayyan", "Putih")

hasil_1.aksi ()
hasil_2.aksi ()


print ("\n --- batas --- \n")