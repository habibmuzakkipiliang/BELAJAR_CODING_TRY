print ("\n Bikin Impor Random dan Time Python \n")


import time
import random


print ("\n Bikin Hello World \n")

print ("\n --- batas --- \n")




print ("\n Variabel dasar \n")

nama = "Habib Muzakki"
akrab = "Habib"
asal = "Kota Serang, Banten"
kuliah = "Universitas Harkat Negeri Tegal"
jurusan = "D4 Vokasi Teknik Informatika"
tinggi = "170 cm"
alumni = "MAN 2 KOTA SERANG (KELAS AGAMA)"


profil = f"""
- Nama           : {nama}
- Nama panggilan : {akrab}
- Asal           : {asal}
- Kuliah         : {kuliah}
- Jurusan        : {jurusan}
- Tinggi badan   : {tinggi}
- Alumni         : {alumni}
"""


time.sleep (1)


print (profil)


print ("\n --- batas --- \n")




print ("\n Percabangan Dasar + Impor \n")

jun = random.randint (2, 10)

if jun >= 8:
     print (f"Besar, angka jun = {jun}")
     
else:
     print (f"Kecil, angka jun = {jun}")
     
     
print ("\n --- batas --- \n")




print ("\n Percabangan Lanjutan + Impor \n")

u = random.randint (1, 15)

if u >= 8:
     print (f"Besar, angka u = {u}")
     
elif u >= 5:
     print (f"Tengah, angka u = {u}")
     
else:
     print (f"Kecil, angka u = {u}")
     
     
print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Lanjutan + Impor")

def dasar (hun):
     
     time.sleep (1)
     
     if hun >= 8:
          print (f"Besar, angka hun = {hun}")
          
     elif hun >= 5:
          print (f"Tengah, angka hun = {hun}")
          
     else:
          print (f"Kecil, angka hun = {hun}")
          
dasar (10)
dasar (7)
dasar (6)
dasar (5)
dasar (3)
          
          
print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Dasar \n")

def tur (kar):
     
     time.sleep (1)
     
     if kar >= 5:
          print (f"Besar, angka kar = {kar}")
          
     else:
          print (f"Kecil, angka kar = {kar}")
          
tur (10)
tur (7)
tur (3)
tur (2)
tur (9)
tur (4)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Kalkulator dasar \n")

def tambah (x, y): 
     return x + y


def kurang (e, r):
     return e - r


def kali (t, y):
     return t * y   


def pangkat (q, w):
     return q ** w


def bagi (u, i):
     return u / i 


def modulus (r, b):
     return r % b


hasil_1 = tambah (10, 10)
hasil_2 = kurang (10, 5)
hasil_3 = kali (10, 10)
hasil_4 = pangkat (10, 3)
hasil_5 = bagi (10, 2)
hasil_6 = modulus (10, 9)


time.sleep (1)


hitung = f"""
- Hasil tambah  = {hasil_1}
- Hasil kurang  = {hasil_2}
- Hasil kali    = {hasil_3}
- Hasil pangkat = {hasil_4}
- Hasil bagi    = {hasil_5}
- Hasil modulus = {hasil_6}
"""


time.sleep (1)


print (hitung)


print ("\n --- Batas --- \n")




print ("\n Operator Perbandingan \n")

x = 15
y = 10

detail = f"""
- Hasil  = {x > y}
- Hasil  = {x < y}
- Hasil  = {x >= y}
- Hasil  = {x <= y}
- Hasil  = {x == y}
- Hasil  = {x != y}
"""

time.sleep (1)

print (detail)


print ("\n --- batas --- \n")