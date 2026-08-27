# Hello World

print ("Hello World")


print ("\n --- Batas --- \n")



# variabel dasar

a = "Halo Habib"
print (a)


b = 12
print (b)


c = 12.12
print (c)


d = True
print (d)


e = None
print (e)


print ("\n --- batas --- \n")



# Tipe data pemrograman

teks = "Halo"
angka = 12
desimal = 12.12
cek = True
kosong = None

data = f"""
- Teks = {teks}
- Angka = {angka}
- Desimal = {desimal}
- Cek = {cek}
- Kosong = {kosong}
"""

print (data)


print ("\n --- batas --- \n")




# Fungsi dasar dengan operator dasar

def tambah (x, y):
     return x + y


def kurang (x, y):
     return x - y


def kali (x, y):
     return x * y


def pangkat (x, y):
     return x ** y


def modulus (x, y):
     return x % y


print ("Hasil tambah =", tambah (10, 8))
print ("Hasil kurang =", kurang (10, 2))
print ("Hasil kali =", kali (10, 3))
print ("Hasil pangkat =", pangkat (10, 3))
print ("Hasil modulus =", modulus (90, 1))


print ("\n --- batas --- \n")



# Fungsi dengan angka terbesar

def fungsi (x, y):

     if x < y:
          return x 

     else:
          return y

print ("Hasil besar =", fungsi (10, 8))
print ("Hasil besar =", fungsi (80, 9))
print ("Hasil besar =", fungsi (34, 8))
print ("Hasil besar =", fungsi (34, 12))
print ("Hasil besar =", fungsi (34, 1))
print ("Hasil besar =", fungsi (12, 2))
print ("Hasil besar =", fungsi (12, 1))
print ("Hasil besar =", fungsi (34, 12))
print ("Hasil besar =", fungsi (22, 3))
print ("Hasil besar =", fungsi (12, 5))


print ("\n --- batas --- \n")



# Fungsi dengan angka terkecil

def kecil (x, y):

     if x < y:
          return x

     else:
          return y

print ("Hasil kecil =", kecil (10, 1))
print ("Hasil kecil =", kecil (23, 2))
print ("Hasil kecil =", kecil (23, 4))
print ("Hasil kecil =", kecil (26, 8))
print ("Hasil kecil =", kecil (23, 4))
print ("Hasil kecil =", kecil (23, 2))
print ("Hasil kecil =", kecil (34, 6))


print ("\n --- batas --- \n")




# Percabangan dasar

a = 7

if a >= 5:
     print (f"Besar, angka a = {a}")

else:
     print (f"kecil, angka a = {a}")


print ("\n --- batas --- \n")




# Percabangan lanjutan

b = 9

if b >= 8:
     print (f"Besar, angka b = {b}")

elif b >= 5:
     print (f"tengah, angka b = {b}")

else:
     print (f"kecil, angka b = {b}")


print ("\n --- batas --- \n")




# Percabangan nested

fer = 9
cek = True

if fer >= 9:
     if cek:
          print (f"Besar, angka f = {fer}")

     elif fer >= 5:
          print (f"kecil, angka f = {fer}")

else:
     print (f"kecil, angka f = {fer}")


print ("\n --- batas --- \n")




# Percabangan nested 1

hun = 8
cek = True

if hun >= 8:
     if cek:
          print (f"besar, angka hun = {hun}")

     else:
          print (f"kecil, angka hun = {hun}")

else:
     print (f"kecil, angka hun = {hun}")


print ("\n --- batas --- \n")




# Percabangan nested kom

usia = 12
cek = True

if usia >= 10 and usia <= 50:
     if cek:
          print (f"usia kamu sudah cukup, usia = {usia}")

     elif usia > 50:
          print (f"usia kamu sudah tua, usia = {usia}")

else:
     print (f"usia kamu masih kecil, usia = {usia}")


print ("\n --- batas --- \n")



# Percabangan nested er

hun = 23
cek = True

if hun >= 34 and hun <= 50:
     if cek:
          print (f"sudah oke, hun = {hun}")

     else:
          print (f"sudah lebih dari oke, hun = {hun}")

else:
     print (f"sudah lebih dari cukup, hun = {hun}")


print ("\n --- batas --- \n")



# For dasar

for a in range (1, 9):
     print (f"urutan ke - {a}")


print ("\n --- batas --- \n")


for n in range (1, 15):
     print (f"urutan ke - {n}")


print ("\n --- batas --- \n")


for j in range (1, 4):
     print (f"urutan ke - {j}")


print ("\n --- batas --- \n")



# While dasar

a = 1

while a < 11:
     print (f"urutan ke - {a}")
     a = a + 1


b = 1

while b < 15:
     print (f"urutan ke - {b}")
     b = b + 1


print ("\n --- batas --- \n")




num = 10

while num > 0:
     print (f"urutan ke - {num}")
     num = num - 1


print ("\n --- batas --- \n")




# Fungsi dasar

def dasar ():
     print ("Halo Dunia")

dasar ()


print ("\n --- batas --- \n")



# Fungsi dengan parameter

def fer (nama):
     print (f"Nama kamu {nama} dari jakarta utara")

fer ("Cefnot")
fer ("Hunk")
fer ("Yer")
fer ("Jun")
fer ("Han")
fer ("Kop")
fer ("Jun")
fer ("lop")
fer ("Kos")


print ("\n --- batas --- \n")




# Fungsi dengan return

def ala (nama):
     return f"Halo saya {nama} dari Kota Jakarta Pusat"

print (ala ("Hayyan"))
print (ala ("Jundy"))
print (ala ("Jun"))
print (ala ("Mon"))
print (ala ("Gunn"))


print ("\n --- batas --- \n")



# Fungsi dengan parameter 2

def ho (nama):
     print (f"Saya {nama} dari Jakarta timur")

ho ("Jun")
ho ("Hun")
ho ("Nu")
ho ("Gun")
ho ("Run")
ho ("Er")
ho ("Der")
ho ("Dfer")
ho ("Dfr")
ho ("Kom")


print ("\n --- batas --- \n")



# Struktur data Dict

nama = {
     "nama" : "Johan",
     "asal" : "Jakarta pusat",
     "nomor" : 12,
     "cek" : True,

}

print ("Nama :", nama ["nama"])
print ("Asal :", nama ["asal"])
print ("Nomor :", nama ["nomor"])
print ("Cek :", nama ["cek"])


print ("\n --- batas --- \n")




# Array 

er = [
     "Satu",
     "Dua",
     "Tiga",
     "Empat",
     "Lima",
     "Enam",
     "Tujuh",
     "Delapan",
]

for u in er:
     print (u)


print ("\n --- batas --- \n")




# Daftar barang random

fer = [
     "Botol",
     "Kursi",
     "Meja",
     "Koper",
     "Kating",
     "Jundy",
     "hun",
]

for j in fer:
     print (j)


print ("\n --- batas --- \n")



# For + Jun

der = [
     "Jun",
     "Kop",
     "Mon",
     "Hnun",
     "Kol",
     "Gun"
]

for j in der:
     print (j)


print ("\n --- batas --- \n")




# Fungsi dengan parameter 2 item

def fun (nama, asal, nomor):
     print (f"- Halo {nama}, dari {asal}, dan bernomor {nomor}")

fun ("Habib", "Jakarta Timur", 12)
fun ("Rayyan", "Jakarta utara", 10)
fun ("Gunn", "Jakarta Pusat", 23)
fun ("Hun", "Jakarta Selatan", 34)
fun ("Gan", "Jatim", 12)
fun ("Bun", "Jabar", 34)
fun ("Fun", "Fune", 23)


print ("\n --- batas --- \n")



# Fungsi dengan return lagi

def nu (nama):
     return f"Halo nama saya {nama} dari jakarta utara"

print (nu ("Habib"))
print (nu ("Jundy"))
print (nu ("Kopr"))
print (nu ("Mun"))
print (nu ("Gun"))
print (nu ("Jun")) 

print ("\n --- batas --- \n")