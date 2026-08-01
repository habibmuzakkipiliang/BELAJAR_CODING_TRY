# Bonus tambahan (spesial) untuk nambah materi baru + nambah skor poinnya

# Fungsi dasar 

def dasar ():
     print ("Hello Dunia Indonesia")

dasar ()


print ("\n --- batas --- \n")



# Fungsi dasar 2 

def run ():
     print ("Hello Miner")
     print ("Hello Happy Ghast")
     print ("Hello Ghast")
     print ("Hello Steve")

run ()


print ("\n --- batas --- \n")




# Fungsi dengan parameter

def nama (sapa):
     print (f"Halo saya {sapa}, dari kota Jakarta Pusat")

nama ("Hayyan")
nama ("Rayyan")
nama ("Yunan")
nama ("Rafis")
nama ("Travis")


print ("\n --- batas --- \n")



# Fungsi dengan parameter 2

def halo (sapa, asal):
     print (f"- Halo nama saya {sapa}, dari {asal} dan asli orang Indonesia")

halo ("Fayyan", "Jakarta Timur")
halo ("Rayyan", "Jakarta Utara")
halo ("Just", "Jakarta Pusat")
halo ("Ivan", "Jakarta Barat")
halo ("Next", "Jakarta Selatan")

print ("\n --- batas --- \n")



# Fungsi dengan return

def halo (sapa):
     return f"Halo saya {sapa} dari Jakarta Utara"

print (halo ("Hayyan"))
print (halo ("Max"))
print (halo ("Stevan"))
print (halo ("Jundy"))
print (halo ("Jun"))


print ("\n --- batas --- \n")



# Fungsi dengan return 2 

def hello (sapa, asal): 
     return f"- Halo saya {sapa} dari {asal} dan asli orang Indonesia"

print (hello ("Rayyan", "Jakarta Utara"))
print (hello ("Hayyan", "Jakarta Selatan"))
print (hello ("Fayyan", "Jakarta Pusat"))
print (hello ("Royman", "Jakarta Barat"))
print (hello ("Frilsen", "Jakarta Pusat"))


print ("\n --- batas --- \n")




# Fungsi return dengan mencari Angka Terbesar

def angka_terbesar (dk, ml):

     if dk > ml:
          return dk

     else:
          return ml

print ("Angka Besar =", angka_terbesar (10, 8))
print ("Angka Besar =", angka_terbesar (9, 10))
print ("Angka Besar =", angka_terbesar (3, 15))
print ("Angka Besar =", angka_terbesar (4, 30))
print ("Angka Besar =", angka_terbesar (9, 34))
print ("Angka Besar =", angka_terbesar (89, 8))
print ("Angka Besar =", angka_terbesar (90, 3))


print ("\n --- batas --- \n")




# Fungsi return dengan mencari angka terkecil

def angka_terkecil (ka, kl):

     if ka < kl:
          return ka

     else:
          return kl

print ("Angka Kecil = ", angka_terkecil (9, 10))
print ("Angka Kecil =", angka_terkecil (3, 23))
print ("Angka Kecil =", angka_terkecil (90, 7))
print ("Angka Kecil =", angka_terkecil (8, 34))
print ("Angka Kecil =", angka_terkecil (4, 23))
print ("Angka Kecil =", angka_terkecil (5, 13))
print ("Angka Kecil =", angka_terkecil (89, 2))


print ("\n --- batas --- \n")




# Fungsi dengan rumus bangun datar 

def persegi (s):
     return s * s

def persegi_panjang (p, l):
     return p * l

def segitiga (a, t):
     return a * t / 2

def layang_layang (d1, d2):
     return d1 * d2 / 2

def lingkaran (phi, r):
     return phi * r * r


print ("Luas persegi =", persegi (10))
print ("Luas persegi panjang = ", persegi_panjang (10, 5))
print ("Luas segitiga =", segitiga (10, 10))
print ("Luas layang-layang = ", layang_layang (10, 30))
print ("Luas lingkaran =", lingkaran (3.14, 10))


print ("\n --- batas --- \n")



# Fungsi dengan Operator dasar

def tambah (x, y):
     return x + y

def kurang (x, y):
     return x - y

def kali (x, y):
     return x * y

def pangkat (x, y):
     return x ** y

def bagi (x, y):
     return x / y

def modulus (x, y):
     return x % y


print ("Tambah =", tambah (10, 10))
print ("Kurang =", kurang (10, 5))
print ("Kali =", kali (10, 10))
print ("Pangkat =", pangkat (10, 3))
print ("Bagi =", bagi (10, 5))
print ("Modulus =", modulus (10, 9))

print ("\n --- batas --- \n")




# Match Case 1 

def lop (g):

     match (g):

          case 1:
               print ("Angka 1")

          case 2:
               print ("Angka 2")

          case 3:
               print ("Angka 3")

          case 4:
               print ("Angka 4")


          case _:
               print ("Angka lain")

lop (1)
lop (2)
lop (3)
lop (4)
lop (5)


print ("\n --- batas --- \n")




# Match Case 2 : Warna rambu lalu lintas kota besar

def warna (df):

     match (df):

          case "Merah":
               print ("Merah")

          case "Kuning":
               print ("Warna kuning")

          case "Hijau":
               print ("Warna hijau")

          case _:
               print ("Warna lain")

warna ("Merah")
warna ("Kuning")
warna ("Hijau")
warna ("Hitam")


print ("\n --- batas --- \n")




# Fungsi dengan percabangan dasar

def coba_1 (k):

     if k >= 5:
          print (f"angka besar, angka k = {k}")

     else:
          print (f"angka kecil, angka k = {k}")

coba_1 (10)
coba_1 (9)
coba_1 (8)
coba_1 (7)
coba_1 (6)
coba_1 (5)
coba_1 (4)
coba_1 (3)
coba_1 (2)
coba_1 (1)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan lanjutan

def coba_2 (f):

     if f >= 8:
          print (f"Angka besar, angka f = {f}")

     elif f >= 5:
          print (f"Angka tengah, angka f = {f}")

     else:
          print (f"Angka kecil, angka f = {f}")

coba_2 (10)
coba_2 (9)
coba_2 (8)
coba_2 (7)
coba_2 (6)
coba_2 (5)
coba_2 (4)
coba_2 (3)
coba_2 (2)
coba_2 (1)


print ("\n --- batas --- \n")


# Fungsi dengan percabangan nested 

def coba_3 (k):

     cek = True

     if k >= 5:
          if cek:
               print (f"Angka Besar, angka k = {k}")

          else:
               print (f"Angka Tengah, angka k = {k}")

     else:
          print (f"Angka Kecil, angka k = {k}")

coba_3 (10)
coba_3 (9)
coba_3 (8)
coba_3 (7)
coba_3 (6)
coba_3 (5)
coba_3 (4)
coba_3 (3)
coba_3 (2)
coba_3 (1)


print ("\n --- batas --- \n")




# For Dasar 

for v in range (1, 11):
     print (f"Urutan ke - {v}")


print ("\n --- batas --- \n")




# While dasar (Hitung Maju)

a = 1

while a < 11:
     print (f"Urutan ke - {a}")
     a = a + 1


print ("\n --- batas --- \n")




# While dasar (Hitung mundur)

b = 10

while b > 0:
     print (f"Urutan ke - {b}")
     b = b - 1


print ("\n --- batas --- \n")




# For Nested 

for x in range (4):
     for y in range (4):
          print (f"Urutan ke - {x} dan Urutan ke - {y}")


print ("\n --- batas --- \n")



# List (Array) + For Continue Control   

buah_buahan = ["Apel", "Pepaya", "Mangga", "Anggur", "Nanas", "Buah Naga","Buah Merah Papua", "Pisang", "Jambu Biji", "Jambu Air"]

for k in buah_buahan:
     if k == "Anggur":
          continue
     print (k)


print ("\n --- batas --- \n")




# List (Array) + For Break Control

for k in buah_buahan:
     if k == "Anggur":
          break
     print (k)


print ("\n --- batas --- \n")



# List dan manipulasi List (OSHI, WOTA DAN FANS JKT48)

oshi_jkt48 = ["Gracie JKT48", "Michie JKT48", "Lily JKT48", "Aralie JKT48", "Fritzy JKT48"]

oshi_jkt48.append ("Lana JKT48")
oshi_jkt48.append ("Anindya JKT48")
oshi_jkt48.append ("Christy JKT48")
oshi_jkt48.append ("Celine Eks JKT48")
oshi_jkt48.append ("Freya JKT48")
oshi_jkt48.append ("Olla JKT48")
oshi_jkt48.append ("Jessi JKT48")
oshi_jkt48.append ("Fiony JKT48")
oshi_jkt48.append ("Marsha JKT48")
oshi_jkt48.append ("Muthe JKT48")
oshi_jkt48.append ("Eli JKT48")

for h in oshi_jkt48:
     print (h)


print ("\n --- batas --- \n")


# Tuple 

lore = ("Gracie JKT48", "Michie JKT48", "Lily JKT48", "Aralie JKT48", "Fritzy JKT48")

for k in lore:
     print (k)


print ("\n --- batas --- \n")




# Set 

jor = {"Gracie JKT48", "Michie JKT48", "Lily JKT48", "Aralie JKT48", "Fritzy JKT48"}

for j in jor:
     print (j)


print ("\n --- batas --- \n")




# Dictionary 

data = {
     "nama" : "Habib Muzakki",
     "asal" : "Kota Serang",
     "usia" : 19,
     "cek" : True,
     "coding" : "HTML, CSS, JavaScript dan Python"
}

for yin, yang in data.items():
     print (f"{yin} : {yang}")


print ("\n --- batas --- \n")




# Error Handling 

try:
     vor = 10 + 10
     print (vor)

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Oke")

finally:
     print ("Selesai")


print ("\n --- batas --- \n")




# Error Handling 2

try:
     fol = 10 / 0
     print (fol)

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Oke")

finally:
     print ("Selesai")


print ("\n --- batas --- \n")




# Raise Error Handling 

def eror (fg):

     try:
          if fg < 0:
               raise Exception ("Angka minus")

          if fg >= 8:
               print (f"Angka besar, angka fg = {fg}")

          elif fg >= 5:
               print (f"Angka tengah, angka fg = {fg}")

          else:
               print (f"Angka kecil, angka fg = {fg}")

     except:
          print (f"Angka minus, angka fg = {fg}")

eror (-10)
eror (-9)
eror (-8)
eror (10)
eror (9)
eror (8)
eror (7)
eror (6)
eror (5)
eror (4)
eror (3)
eror (2)
eror (1)


print ("\n --- batas --- \n")





# OOP dasar

class Kucing:

     def __init__(self, nama, warna):
          self.nama = nama
          self.warna = warna

     def aksi (self):
          print (f"- Kucing {self.nama} dengan berwarna {self.warna} dengan bersuara miaw miaw miaw")

hasil_1 = Kucing ("Reon", "Hitam")
hasil_2 = Kucing ("Feon", "Putih")


hasil_1.aksi ()
hasil_2.aksi ()


print ("\n --- batas --- \n")