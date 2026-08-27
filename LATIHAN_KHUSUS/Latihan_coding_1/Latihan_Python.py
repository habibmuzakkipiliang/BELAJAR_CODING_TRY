# Tipe data pemrograman 

teks = "Halo Dunia Indah"
angka = 12
desimal = 2.12
cek = True
kosong = None

tipe = f"""
- Teks : {teks}
- Angka : {angka}
- Desimal : {desimal}
- Cek : {cek}
- Kosong : {kosong} 
"""

print (tipe)

print ("\n --- batas --- \n")



# Cek tipe data pemrograman

teks = "Halo Dunia Indah"
angka = 12
desimal = 2.12
cek = True
kosong = None

cek_tipe = f"""
- Teks = {type (teks)}
- Angka = {type (angka)}
- Desimal = {type (desimal)}
- Cek = {type (cek)}
- Kosong = {type (kosong)}
"""

print (cek_tipe)

print ("\n --- batas --- \n")




# Bikin latihan simpel lagi

r = int (input ("Masukkan angka r :"))
u = int (input ("Masukkan angka u :"))

hasil = r * u

print (f"Total = {hasil}")

print ("\n --- batas --- \n")



# Latihan pake fungsi 

x = int (input ("Masukkan angka x :"))
y = int (input ("Masukkan angka y :"))

def tambah (x, y):
     return x + y

def kurang (x, y):
     return x - y

def kali (x, y):
     return x * y

def pangkat (x, y):
     return x ** y


print ("Hasil tambah =", tambah (x, y))
print ("Hasil kurang =", kurang (x, y))
print ("Hasil kali =", kali (x, y))
print ("Hasil pangkat =", pangkat (x, y))


print ("\n --- batas --- \n")


# Bikin nama pake fungsi

nama_1 = input ("Masukkan nama kamu :")

def cek_nama (nama):

     if nama_1 == "Habib":
          print ("Nama kamu Habib")

     else:
          print ("Bukan Habib")

cek_nama (nama_1)
cek_nama (nama_1)
cek_nama (nama_1)
cek_nama (nama_1)


print ("\n --- batas --- \n")



# Fungsi dengan mencari angka terbesar

x = int (input ("Masukkan angka x :"))
y = int (input ("Masukkan angka y :"))

def angka_terbesar (x, y):

     if x > y:
          return x

     else:
          return y

print ("Angka terbesar =", angka_terbesar (x, y))
print ("Angka terbesar =", angka_terbesar (x, y))
print ("Angka terbesar =", angka_terbesar (x, y))
print ("Angka terbesar =", angka_terbesar (x, y))


print ("\n --- batas --- \n")




# Fungsi dengan percabangan dasar

a = int (input ("Masukkan angka a = "))

def dasar (a):

     if a >= 5:
          print (f"Besar, angka a = {a}")

     else:
          print (f"Kecil, angka a = {a}")

dasar (a)
dasar (a)
dasar (a)
dasar (a)
dasar (a)
dasar (a)
dasar (a)


print ("\n --- batas --- \n")




# Fungsi dengan percabangan lanjutan

b = int (input ("Masukkan angka b ="))

def percabangan_1 (b):

     if b >= 8:
          print (f"Besar, angka b = {b}")

     elif b >= 5:
          print (f"Tengah, angka b = {b}")

     else:
          print (f"Kecil, angka b = {b}")

percabangan_1 (b)
percabangan_1 (b)
percabangan_1 (b)
percabangan_1 (b)

print ("\n --- batas --- \n")



# Fungsi dengan percabangan nested

c = int (input ("Masukkan angka c = "))

def percabangan_2 (c):

     cek = True

     if c >= 5:
          if cek:
               print (f"besar, angka c = {c}")

          else:
               print (f"tengah, angka c = {c}")

     else:
          print (f"kecil, angka c = {c}")

percabangan_2 (c)
percabangan_2 (c)
percabangan_2 (c)
percabangan_2 (c)
percabangan_2 (c)


print ("\n --- batas --- \n")




# Fungsi dengan percabangan usia produktif manusia

f = int (input ("Masukkan angka f : "))

def fun (f):

     if f >= 15 and f <= 40:
          print (f"usia yang sudah produktif, usia = {f}")

     elif f > 40:
          print (f"sudah tua usiannya, usia = {f}")

     else:
          print (f"masih kecil usia nya, usia = {f}")

fun (f)
fun (f)
fun (f)
fun (f)
fun (f)
fun (f)


print ("\n --- batas --- \n")




# Fungsi dengan percabangan usia masuk JKT48

g = int (input ("Masukkan usia kamu ?"))

def oshi (g):

     if g >= 13 and g <= 19:
          print (f"boleh daftar jkt48, usia = {g}")

     elif g > 19:
          print (f"sudah tua, usia = {g}")

     else:
          print (f"masih kecil, usia = {g}")

oshi (g)
oshi (g)
oshi (g)
oshi (g)
oshi (g)
oshi (g)
oshi (g)


print ("\n --- batas --- \n")



# For dasar

for i in range (1, 11):
     print (f"urutan ke - {i}")


print ("\n --- batas --- \n")




# For dasar 2
for a in range (11):
     print (f"urutan ke - {a}")


print ("\n --- batas --- \n")



# For dasar 3

for h in range (1, 15):
     print (f"urutan ke - {h}")


print ("\n --- batas --- \n")




# For dasar 4

for t in range (15):
     print (f"urutan ke {t}")


print ("\n --- batas --- \n")



# For dasar

for h in range (16):
     print (f"urutan ke - {h}")


print ("\n --- batas --- \n")



# While dasar

a = 1

while a < 11:
     print (f"urutan ke - {a}")
     a = a + 1


print ("\n --- batas --- \n")




# While dasar 

b = 10

while b > 0:
     print (f"urutan ke - {b}")
     b = b - 1


print ("\n --- batas --- \n")




# While dasar

f = 15 

while f > 0:
     print (f"urutan ke - {f}")
     f = f - 1


print ("\n -- batas --- \n")




# For Nested 

for a in range (1, 11):
     for b in range (1, 11):
          print (f"luar : {a} dan dalam : {b}")

print ("\n --- batas --- \n")



# Array 1 

daf = ["Halo Dunia", "Halo World", "Halo Base", "Bon meal"]

for i in daf:
     print (i)


print ("\n --- batas --- \n")



# Array 2

fan = ["Halo Ao Bing", "Halo Ne Zha", "Halo Fanos", "Halo Tanos"]

for j in fan:
     print (j)


print ("\n --- batas --- \n")



# Array 3

vaj = ["Ros", "Ror", "Ben", "ben", "Kom", "Kor"]

for t in vaj:
     print (t)


print ("\n --- batas --- \n")




# Array 5

rtu = ["Halo Dun", "Halo OShu", "Roan", "Jao", "FOs"]


rtu.append ("Halo Fus")
rtu.append ("Halo 223")
rtu.append ("Halo funs")
rtu.append ("Halo der")

for k in rtu:
     print (k)


print ("\n --- batas --- \n")




# Dictionary

data = {
     "nama" : "Halo Dunia",
     "angka" : 12,
     "desimal" : 1.1,
     "cek" : True
}

for awal, akhir in data.items():
     print (f"{awal} : {akhir}")

