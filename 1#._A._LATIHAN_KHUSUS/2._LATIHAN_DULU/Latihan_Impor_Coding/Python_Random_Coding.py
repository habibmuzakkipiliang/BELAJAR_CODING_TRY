print ("\n Bikin Impor Random dan Time \n")

import time
import random

a = 10

random.randint (1, 10)

if a >= 5:
     print (f"Besar, angka a = {a}")

else:
     print (f"Kecil, angka a = {a}")


print ("\n --- batas --- \n")




print ("\n Percabangan Lanjutan 1 \n")

b = 15

random.randint (10, 20)

if b >= 20:
     print (f"Besar, angka b = {b}")

else:
     print (f"Kecil, angka b = {b}")


print ("\n --- batas --- \n")



print ("\n Percabangan Lanjutan 1 \n")

r = 14

random.randint (10, 20)

if r >= 20:
     print (f"Besar, angka r = {r}")

elif r >= 14:
     print (f"2, Angka r = {r}")

elif r >= 10:
     print (f"C, angka e = {r}")

else:
     print (f"Kecil, angka r = {r}")


print ("\n --- batas --- \n")



print ("\n Fungsi dengan Percabangan Dasar \n")

def sar (l):

     time.sleep (1)

     if l >= 5:
          print (f"Besar, angka l = {l}")

     else:
          print (f"Kecil, angka l = {l}")

sar (10)
sar (9)
sar (8)
sar (7)
sar (6)
sar (5)
sar (4)
sar (3)
sar (2)
sar (1)


print ("\n --- batas --- \n")



print ("\n percabangan nilai Rapor \n")

def nilai (w):

     time.sleep (1)

     if w >= 95:
          print (f"A, nilai = {w}")

     elif w >= 90:
          print (f"B, nilai = {w}")

     elif w >= 80:
          print (f"C, nilai = {w}")

     elif w >= 70:
          print (f"D, nilai = {w}")

     elif w >= 60:
          print (f"E, nilai = {w}")

     else:
          print (f"Kecil, nilai = {w}")

nilai (100)
nilai (90)
nilai (80)
nilai (70)
nilai (60)
nilai (50)
nilai (40)
nilai (30)
nilai (20)
nilai (10)


print ("\n --- batas --- \n")



print ("\n Usia masuk kerja \n")

def kerja (f):

     time.sleep (1)

     if f >= 21 and f <= 40:
          print (f"Sudah boleh kerja, usia = {f}")

     elif f > 40:
          print (f"Sudah tua, usia = {f}")

     else:
          print (f"Masih kecil usiannya, usia = {f}")

kerja (70)
kerja (60)
kerja (50)
kerja (40)
kerja (30)
kerja (20)
kerja (10)
kerja (5)


print ("\n --- batas --- \n")


print ("\n Fungsi dengan usia masuk JKT48 \n")

def run (k):

     if k >= 13 and k <= 19:
          print (f"Sudah boleh masuk JKT48, usia = {k}")

     elif k > 19:
          print (f"Sudah lebih dari cukup, usia = {k}")

     else:
          print (f"Masih kecil usiannya, usia = {k}")

run (20)
run (16)
run (15)
run (14)
run (13)
run (10)
run (5)
run (4)


print ("\n --- batas --- \n")




print ("\n Usia Produktif Manusia \n")

def usia (w):

     time.sleep (1)

     if w >= 15 and w <= 40:
          print (f"Usia produktif, usia = {w}")

     elif w > 40:
          print (f"Sudah tua, usia = {w}")

     else:
          print (f"Masih kecil usiannya, usia = {w}")

usia (70)
usia (60)
usia (50)
usia (40)
usia (30)
usia (20)
usia (10)
usia (5)


print ("\n --- batas --- \n")


print ("\n Fungsi dasar \n")

def dasar ():
     print ("Hello World")

dasar ()


print ("\n --- batas --- \n")



print ("\n Fungsi dengan parameter \n")

def run (sapa):
     time.sleep (1)
     print (f"Halo aku {sapa}, dari Jakarta Utara")

run ("Zaki")
run ("Abyan")
run ("Rayyan")
run ("Hayyan")

print ("\n --- batas --- \n")



print ("\n Fungsi dengan Return \n")

def rt (sapa):
     time.sleep (1)
     return f"Halo saya {sapa} dari Jakarta Timur"

print (rt ("Hayyan"))
print (rt ("Fayyan"))
print (rt ("Rayyan 1"))
print (rt ("TUyyan"))
print (rt ("Ror"))


print ("\n --- batas --- \n")



print ("\n Oshi JKT48 \n")

def oshi (sapa):
     time.sleep (1)
     print (f"{sapa} JKT48")

oshi ("Gracie")
oshi ("Michie")
oshi ("Lily")
oshi ("Aralie")
oshi ("Fritzy")
oshi ("Lana")

print ("\n --- batas --- \n")



print ("\n OOP dasar \n")

class Kucing:
     time.sleep (1)

     def __init__(self, nama, warna):
          self.nama = nama
          self.warna = warna

     def aksi (self):
          print (f"- Kucing {self.nama} dengan warna {self.warna} dengan suara miaw")

hasil_1 = Kucing ("Hayyan", "Hitam")
hasil_2 = Kucing ("Fayyan", "Putih")


hasil_1.aksi ()
hasil_2.aksi ()


print ("\n --- batas --- \n")



print ("\n OOP dasar \n")

class Mobil:

     time.sleep (1)

     def __init__(self, nama, lari):
          self.nama = nama
          self.lari = lari

     def aksi (self):
          print (f"- Mobil {self.nama} dengan warna hitam dan kecepatannya {self.lari}")

hasil_3 = Mobil ("Rust", 12)
hasil_4 = Mobil ("Terios", 99)

hasil_3.aksi ()
hasil_4.aksi ()


print ("\n --- batas --- \n")