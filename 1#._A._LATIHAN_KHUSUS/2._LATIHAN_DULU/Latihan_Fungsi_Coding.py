# Fungsi dasar 

def dasar ():
     print ("Hello World")

dasar ()


print ("\n --- batas --- \n")



# Fungsi dasar 2

def run ():
     print ("Hello World")
     print ("Hello Dankut")
     print ("Hello Hayyan")
     print ("Hello Fas")

run ()


print ("\n --- batas --- \n")



# Fungsi dengan parameter

def vun (nama):
     print (f"Halo nama saya {nama}, dari Kota Serang")

vun ("Hayyan")
vun ("Rayyan")
vun ("Jun")
vun ("Jundy")
vun ("Burundy")
vun ("Kop")


print ("\n --- batas --- \n")



# Fungsi dengan parameter

def fun (j):
     print (f"Halo nama saya {j}, dari Jakarta Timur")

fun ("Vest")
fun ("Yonda")
fun ("Honda")
fun ("Vonda")
fun ("Jue")


print ("\n --- batas --- \n")




# Fungsi dengan return

def kem (nama):
     return f"Halo saya {nama} dari jakarta pusat"

print (kem ("Habib"))
print (kem ("Roy"))
print (kem ("Yun"))
print (kem ("Kopral"))
print (kem ("Jun"))
print (kem ("Nuk"))


print ("\n --- batas --- \n")



# Fungsi dengan return

def run (kop):
     return f"Halo dunia {kop} dari dunia lain"

print (run ("Hyn"))
print (run ("Lop"))
print (run ("Jun"))
print (run ("Hun"))


print ("\n --- batas --- \n")



# Rumus bangun datar 

def persegi (s):
     return s * s

def persegi_panjang (p, l):
     return p * l

print ("Luas persegi =", persegi (10))
print ("Luas persegi panjang =", persegi_panjang (10, 5))


print ("\n --- batas --- \n")




# Rumus dasar

def tambah (x, y):
     return x + y


def kurang (x, y):
     return x - y


print ("Tambah =", tambah (10, 10))
print ("Kurang =", kurang (10, 5))


print ("\n --- batas --- \n")



# Switch Case 1

def dosk (j):

     match (j):

          case 1:
               print ("Angka 1")

          case 2:
               print ("Angka 2")

          case 3:
               print ("Angka 4")

          case _:
               print ("Angka lain")

dosk (1)
dosk (2)
dosk (3)
dosk (4)


print ("\n --- batas --- \n")




# Fungsi dalam percabangan dasar

def kopi (e):

     if e >= 5:
          print (f"Besar, angka e = {e}")

     else:
          print (f"kecil, angka e = {e}")

kopi (10)
kopi (9)
kopi (8)
kopi (5)
kopi (3)
kopi (2)
kopi (1)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan lanjutan

def erun (c):

     if c >= 8:
          print (f"Besar, angka c = {c}")

     elif c >= 5:
          print (f"Tengah, angka c = {c}")

     else:
          print (f"Kecil, angka c = {c}")

erun (10)
erun (9)
erun (8)
erun (7)
erun (6)
erun (5)
erun (4)
erun (3)
erun (2)
erun (1)


print ("\n --- batas --- \n")





# Fungsi dengan percabangan nilai rapor 

def skor (x):

     if x >= 95:
          print (f"A, nilai = {x}")

     elif x >= 90:
          print (f"B, nilai = {x}")

     elif x >= 80:
          print (f"C, nilai = {x}")

     elif x >= 70:
          print (f"D, nilai = {x}")

     elif x >= 60:
          print (f"E, nilai = {x}")

     elif x >= 50:
          print (f"F, nilai = {x}")

     else:
          print (f"Jelek amat, nilai = {x}")

skor (100)
skor (90)
skor (80)
skor (70)
skor (60)
skor (50)
skor (40)
skor (30)
skor (20)
skor (10)


print ("\n --- batas --- \n")




# Fungsi dengan percabangan nested 1

def ruj (f):

     cek = True

     if f >= 5:
          if cek:
               print (f"Besar, angka f = {f}")

          else:
               print (f"Tengah, angka f = {f}")

     else:
          print (f"Kecil, angka f = {f}")

ruj (10)
ruj (9)
ruj (8)
ruj (7)
ruj (6)
ruj (5)
ruj (4)
ruj (3)
ruj (2)
ruj (1)


print ("\n --- batas --- \n")




# Fungsi dengan percabangan nested 2

def tur (g):

     cek = True

     if g >= 8:
          if cek:
               print (f"Besar, angka g = {g}")

          elif g >= 5:
               print (f"Tengah, angka g = {g}")

     else:
          print (f"Kecil, angka g = {g}")

tur (10)
tur (9)
tur (8)
tur (7)
tur (6)
tur (5)
tur (4)
tur (3)
tur (2)
tur (1)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan usia produktif manusia

def usia (i):

     if i >= 15 and i <= 40:
          print (f"Usia yang sudah produktif, usia = {i}")

     elif i > 40:
          print (f"Sudah tua, usia = {i}")

     else:
          print (f"usia yang masih kecil, usia = {i}")

usia (70)
usia (60)
usia (50)
usia (40)
usia (30)
usia (20)
usia (10)          


print ("\n --- batas --- \n")



# Fungsi untuk usia kerja manusia

def kerja (j):

     if j >= 24 and j <= 45:
          print (f"Boleh kerja, usia = {j}")

     elif j > 45:
          print (f"Sudah lanjut usia, usia = {j}")

     else:
          print (f"Masih kecil usiannya, usia = {j}")

kerja (70)
kerja (60)
kerja (50)
kerja (40)
kerja (30)
kerja (20)
kerja (10)
kerja (5)


print ("\n --- batas --- \n")




# For dasar 

for a in range (1, 11):
     print (f"Urutan ke - {a}")


print ("\n --- batas --- \n")




# For dasar 2 

for b in range (11):
     print (f"Urutan ke - {b}")


print ("\n --- batas --- \n")




# For dasar 3

for u in range (45, 70):
     print (f"Urutan ke - {u}")


print ("\n --- batas --- \n")





# While dasar 1

a = 1

while a < 11:
     print (f"Urutan ke - {a}")
     a = a + 1


print ("\n --- batas --- \n")





# While dasar 4

b = 10

while b > 0:
     print (f"Urutan ke - {b}")
     b = b - 1


print ("\n --- batas --- \n")




# Struktur data List

daf = ["Halo Dunia", "Halo Indonesia", "Halo Kuliah", "Halo Harkat"]

for h in daf:
     print (h)


print ("\n --- batas --- \n")



# Struktur data Tuple 

der = ("Halo", "Tes", "Submit", "Hun", "Staf")

for k in der:
     print (k)


print ("\n --- batas --- \n")



# Struktur data Set

fer = {"Halo", "Tes", "Submit", "Hun", "Staf"}

for n in fer:
     print (n)


print ("\n --- batas --- \n")




# Dictionary 

data = {
     "nama" : "Habib Muzakki",
     "usia" : 18,
     "asal" : "Kota Serang",
     "cek" : True,
}

print ("Nama :", data ["nama"])
print ("Usia :", data ["usia"])
print ("Asal :", data ["asal"])
print ("Cek :", data ["cek"])


print ("\n --- batas --- \n")



# Error Handling

try:
     a = 10 / 0
     print (a)

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Berhasil")

finally:
     print ("Selesai")


print ("\n --- batas --- \n")




# Error Handling 

try:
     b = 10 + 10
     print (b)

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Berhasil")

finally:
     print ("Selesai")


print ("\n --- batas --- \n")




# Raise Error Handling

def eror (k):

     try:

          if k < 0:
               raise ("Angka minus")

          if k >= 5:
               print (f"Besar, angka k = {k}")

          else:
               print (f"Kecil, angka k = {k}")

     except:
          print (f"Angka minus, angka k = {k}")

eror (-10)
eror (-5)
eror (-6)
eror (-3) 
eror (-9)
eror (-13)
eror (10)
eror (9)
eror (8)
eror (7)
eror (5)
eror (4)


print ("\n --- batas --- \n")




# OOP dasar

class Kucing:

     def __init__(self, nama, warna):
          self.nama = nama
          self.warna = warna

     def aksi (self):
          print (f"- Kucing {self.nama} dengan berwarna {self.warna}")

hasil_1 = Kucing ("Hayyan", "Hitam")
hasil_2 = Kucing ("Rayyan", "Putih")


hasil_1.aksi ()
hasil_2.aksi ()


print ("\n --- batas --- \n")




# OOP Mobil

class Mobil:

     def __init__(self, nama, warna):
          self.nama = nama
          self.warna = warna

     def aksi (self):
          print (f"- Mobil {self.nama} dengan berwarna {self.warna} dengan kecepatan 100 km / h")

hasil_3 = Mobil ("Toyota", "Hitam")
hasil_4 = Mobil ("Terios", "Putih")


hasil_3.aksi ()
hasil_4.aksi ()


print ("\n --- batas --- \n")