# Bonus Tambahan (Spesial) untuk nambah poin nilai 

# Hello World dulu dong

print ("Hello World")


print ("\n --- batas --- \n")



# variabel simpel

contoh = "Halo Dunia"
print (contoh)


contoh_1 = 12
print (contoh_1)


contoh_2 = 1.12
print (contoh_2)


print ("\n --- batas --- \n")



# Tipe data pemrograman dasar

teks = "Halo Dunia"
angka = 12
desimal = 3.12
cek = True
kosong = None

tipe = f"""
- Teks : {teks}
- Angka : {angka}
- Desimal : {desimal}
- Cek : {cek}
- Kosong : {kosong}
"""

cek_tipe = f"""
- Teks : {type (teks)}
- Angka : {type (angka)}
- Desimal : {type (desimal)}
- Cek : {type (cek)}
- Kosong : {type (kosong)}
"""

print (tipe)
print (cek_tipe)


print ("\n --- batas --- \n")




# Operasi Aritmatika dengan Fungsi return 

x = 10
y = 9

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

def bagi_bulat (x, y):
     return x // y

def modulus (x, y):
     return x % y


print ("Hasil tambah =", tambah (x, y))
print ("Hasil kurang =", kurang (x, y))
print ("Hasil Kali =", kali (x, y))
print ("Hasil pangkat =", pangkat (x, y))
print ("Hasil bagi =", bagi (x, y))
print ("Hasil bagi bulat =", bagi_bulat (x, y))
print ("Hasil modulus =", modulus (x, y))


print ("\n --- batas --- \n")




# Operator perbandingan dengan fungsi return

df = 9
fd = 3

def banding_1 (df, fd):
     return df > fd

def banding_2 (df, fd):
     return df < fd

def banding_3 (df, fd):
     return df >= fd

def banding_4 (df, fd):
     return df <= fd

def banding_5 (df, fd):
     return df == fd

def banding_6 (df, fd):
     return df != df

print ("Hasil banding 1 =", banding_1 (df, fd))
print ("Hasil banding 2 =", banding_2 (df, fd))
print ("Hasil banding 3 =", banding_3 (df, fd))
print ("Hasil banding 4 =", banding_4 (df, fd))
print ("Hasil banding 5 =", banding_5 (df, fd))
print ("Hasil banding 6 =", banding_6 (df, fd))


print ("\n --- batas --- \n")




# Operasi Logika dengan fungsi return

f = 9
g = 3

def logic_1 (f, g):
     return f > g and f < g

def logic_2 (f, g):
     return f < g or f > g

def logic_3 (f, g):
     return not (x > y)

def logic_4 (f, g):
     return not (x < y)


print ("Hasil logic 1 =", logic_1 (f, g))
print ("Hasil logic 2 =", logic_2 (f, g))
print ("Hasil logic 3 =", logic_3 (f, g))
print ("Hasil logic 4 =", logic_4 (f, g))


print ("\n --- batas --- \n")



# Fungsi return dengan luas bangun datar

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

print ("Luas Persegi =", persegi (10))
print ("Luas Persegi Panjang =", persegi_panjang (10, 8))
print ("Luas segitiga =", segitiga (90, 2))
print ("Luas Layang - layang =", layang_layang (10, 90))
print ("Luas lingkaran =", lingkaran (3.14, 80))


print ("\n --- batas --- \n")




# Fungsi return dengan mencari angka terbesar 

def angka_terbesar (df, jk):

     if df > jk:
          return df

     else:
          return jk

print ("Hasil besar =", angka_terbesar (10, 9))
print ("Hasil besar =", angka_terbesar (9, 23))
print ("Hasil besar =", angka_terbesar (4, 23))
print ("Hasil besar =", angka_terbesar (34, 23))
print ("Hasil besar =", angka_terbesar (78, 21))
print ("Hasil besar =", angka_terbesar (45, 22))
print ("Hasil besar =", angka_terbesar (34, 23))


print ("\n --- batas --- \n")




# Fungsi return dengan mencari angka terkecil

def angka_terkecil (gh, jl):

     if gh < jl:
          return gh

     else:
          return jl

print ("Hasil kecil =", angka_terkecil (2, 12))
print ("Hasil kecil =", angka_terkecil (4, 23))
print ("Hasil kecil =", angka_terkecil (45, 3))
print ("Hasil kecil =", angka_terkecil (4, 56))
print ("Hasil kecil =", angka_terkecil (5, 12))
print ("Hasil kecil =", angka_terkecil (6, 90))
print ("Hasil kecil =", angka_terkecil (90, 7))


print ("\n --- batas --- \n")




# While True dasar

a = 10

while True:
     print (f"While True Pertama {a}")
     break


print ("\n --- batas --- \n")



# While True 

b = 1

while True:
     print (f"Tes while true {b}")
     break


print ("\n --- batas --- \n")




# Error Handling

try:
     a = 10 + 10

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Berhasil")

finally:
     print ("Selesai")


print ("\n --- batas --- \n")





# Error Handing 2

try:
     h = 10 / 0
     print (h)

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Berhasil")

finally:
     print ("Selesai")


print ("\n --- batas --- \n")



# Fungsi dengan Error Handling Raise Exception + Percabangan Dasar

def eror (i):

     try:
          if i < 0:
               raise Exception ("Angka minus")

          if i >= 5:
               print (f"Angka i besar, angka i = {i}")

          else:
               print (f"Angka i kecil, angka i = {i}")

     except:
          print (f"Angka minus, angka i = {i}")
     
eror (-1)
eror (-4)
eror (-6)
eror (-90)
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




# Fungsi dengan Error Handling Raise Exception + Percabangan Lanjutan 

def lan_eror (p):

     try:
          if p < 0:
               raise Exception ("Angka minus")

          if p >= 8:
               print (f"Angka p besar, angka p = {p}")

          elif p >= 5:
               print (f"Angka p tengah, angka p = {p}")

          else:
               print (f"Angka p kecil, angka p = {p}")

     except:
          print (f"Angka minus, angka p = {p}")

lan_eror (-10)
lan_eror (-90)
lan_eror (-98)
lan_eror (-34)
lan_eror (-2)
lan_eror (10)
lan_eror (9)
lan_eror (8)
lan_eror (7)
lan_eror (6)
lan_eror (5)
lan_eror (4)
lan_eror (3)
lan_eror (2)
lan_eror (1)


print ("\n --- batas --- \n")




# Fungsi dengan Error Handling Raise Exception + Percabangan Nilai Rapor

def rapor (k):

     try:

          if  k < 0:
               raise Exception ("Angka minus")

          if k >= 95:
               print (f"A, nilai = {k}")

          elif k >= 90:
               print (f"B, nilai = {k}")

          elif k >= 80:
               print (f"C, nilai = {k}")

          elif k >= 70:
               print (f"D, nilai = {k}")

          elif k >= 60:
               print (f"E, nilai = {k}")

          elif k >= 50:
               print (f"F, nilai = {k}")

          else:
               print (f"Jelek amat, nilai = {k}")

     except:
          print (f"Angka minus, nilai = {k}")

rapor (-100)
rapor (-90)
rapor (-80)
rapor (-70)
rapor (-60)
rapor (100)
rapor (90)
rapor (80)
rapor (70)
rapor (60)
rapor (50)
rapor (40)


print ("\n --- batas --- \n")




# OOP dasar

class Kucing:

     def __init__(self, nama, warna, lari):
          self.nama = nama
          self.warna = warna
          self.lari = lari

     def aksi (self):
          print (f"- Kucing {self.nama} dengan warna {self.warna} dan dengan kecepatan {self.lari} km / jam")

hasil_1 = Kucing ("Rayyan", "Hitam", 10)
hasil_2 = Kucing ("Fayyan", "Putih", 15)
hasil_3 = Kucing ("Hoyyan", "Oren", 10)
hasil_4 = Kucing ("Jon", "Putih Hitam", 15)
hasil_5 = Kucing ("Joni", "Grey", 10)


hasil_1.aksi ()
hasil_2.aksi ()
hasil_3.aksi ()
hasil_4.aksi ()
hasil_5.aksi ()


print ("\n --- batas --- \n")




# OOP dasar Mobil

class Mobil:

     def __init__(self, nama, warna, lari):
          self.nama = nama
          self.warna = warna
          self.lari = lari

     def ans (self):
          print (f"- Mobil {self.nama} dengan warna {self.warna} dengan kecepatan {self.lari} km / jam")

mobil_1 = Mobil ("Rush", "Hitam", 90)
mobil_2 = Mobil ("Terios", "Putih", 100)
mobil_3 = Mobil ("Avanza", "Putih", 80)
mobil_4 = Mobil ("Xenia", "Putih", 90)


mobil_1.ans ()
mobil_2.ans ()
mobil_3.ans ()
mobil_4.ans ()


print ("\n --- batas --- \n")