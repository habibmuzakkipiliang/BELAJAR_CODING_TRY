# Hello World

print ("Hello World")


print ("\n --- batas --- \n")




# variabel dasar

contoh = "Hello World dong"
print (contoh)


contoh_1 = 12
print (contoh_1)


contoh_2 = 12.12
print (contoh_2)


print ("\n --- batas --- \n")




# Tipe data pemrograman 

teks = "Hello World dong guys"
angka = 12
desimal = 12.12
cek = True
kosong = None

tipe = f"""
- Teks    : {teks}
- Angka   : {angka}
- Desimal : {desimal}
- Cek     : {cek}
- Kosong  : {kosong}
"""

print (tipe)


print ("\n --- batas --- \n")



# Cek jenis tipe data pemrograman

tipek = f"""
- Teks    : {type (teks)}
- Angka   : {type (angka)}
- Desimal : {type (desimal)}
- Cek     : {type (cek)}
- Kosong  : {type (kosong)}
"""

print (tipek)


print ("\n --- batas --- \n")



# Fungsi dengan kalkulator dasar

def tambah (x, y):
     return x + y


def kurang (x, y):
     return x - y


def kali (x, y):
     return x * y


def bagi (x, y):
     return x / y


def modulus (x, y):
     return x % y


print ("Hasil tambah =", tambah (10, 9))
print ("Hasil kurang =", kurang (10, 5))
print ("Hasil kali =", kali (10, 3))
print ("Hasil bagi =", bagi (10, 5))
print ("Hasil modulus =", modulus (10, 5))


print ("\n --- batas --- \n")




# fungsi dengan operator perbandingan

def banding_1 (x, y):
     return x > y


def banding_2 (x, y):
     return x < y


def banding_3 (x, y):
     return x == y


def banding_4 (x, y):
     return x != y


print ("Hasil banding =", banding_1 (10, 4))
print ("Hasil banding =", banding_2 (10, 9))
print ("Hasil banding =", banding_3 (40, 5))
print ("Hasil banding =", banding_4 (40, 33))


print ("\n --- batas --- \n")



# fungsi dengan percabangan dasar

def tes (f):

     if f >= 5:
          print (f"angka besar f, angka f = {f}")

     else:
          print (f"angka f kecil, angka f = {f}")


tes (10)
tes (9)
tes (8)
tes (7)
tes (6)
tes (5)
tes (4)
tes (3)
tes (2)
tes (1)

print ("\n --- batas --- \n")



# Fungsi dengan percabangan nested

def run (e):

     cek = True

     if e >= 5:
          if cek:
               print (f"angka e besar, angka = {e}")

          else:
               print (f"angka e kecil, angka e = {e}")

     else:
          print (f"angka kecil, angka e = {e}")

run (10)
run (9)
run (8)
run (5)
run (3)
run (3)
run (1)


print ("\n --- batas --- \n")




# For dasar

for r in range (11):
     print (f"urutan ke - {r}")


print ("\n --- batas --- \n")




# for dasar 2

for k in range (11):
     print (f"urutan ke {k}")

print ("\n --- batas --- \n")



# For dasar 4

for o in range (1, 12):
     print (f"urutan ke - {o}")


print ("\n --- batas --- \n")




# For dasar 5

for j in range (11):
     print (f"urutan ke - {j}")


print ("\n --- batas --- \n")



# While dasar

a = 1

while a < 11:
     print (f"urutan ke - {a}")
     a = a + 1


print ("\n --- batas --- \n")




# While dasar 3

b = 11

while b > 0:
     print (f"urutan ke - {b}")
     b = b - 1


print ("\n --- batas --- \n")




# While dasar

a = 1

while a < 15:
     print ("Halo Dunia")
     a = a + 1


print ("\n -- batas -- \n")