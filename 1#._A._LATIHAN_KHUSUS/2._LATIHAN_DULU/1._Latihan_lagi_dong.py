# Bikin Latihan Python dulu

print ("Hello World")


print ("\n --- batas --- \n")




# Variabel dasar 

a = "Habib Muzakki"
print (a)

b = 12
print (b)


c = 3.13
print (c)


d = True
print (d)


print ("\n --- batas --- \n")



# Tipe data pemrograman 

teks = "Halo Dunia"
angka = 12
desimal = 1.12
cek = True
kosong = None

tipe = f"""
- Teks   : {teks}
- Angka  : {angka}
- Desimal : {desimal}
- Cek     : {cek}
- Kosong : {kosong}
"""

print (tipe)


print ("\n --- batas --- \n")




# Switch Case 

def er (a):

     match (a):

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

er (1)
er (2)
er (3)
er (4)


print ("\n --- batas --- \n")




# Switch Case 2

def erur (i):

     match (i):

          case "Merah":
               print ("Warna merah")

          case "Kuning":
               print ("Warna kuning")

          case "Hijau":
               print ("Warna hijau")

          case _:
               print ("Warna lain")

erur ("Merah")
erur ("Kuning")
erur ("Hijau")
erur ("Hitam")


print ("\n --- batas --- \n")




# Fungsi dengan Percabangan Dasar 

def dasar (a):

     if a >= 5:
          print (f"Besar, angka a = {a}")

     else:
          print (f"Kecil, angka a = {a}")

dasar (10)
dasar (9)
dasar (8)
dasar (7)
dasar (6)
dasar (5)
dasar (4)
dasar (3)
dasar (2)
dasar (1)


print ("\n --- batas --- \n")



# Fungsi dengan Percabangan Lanjutan 

def rt (b):

     if b >= 8:
          print (f"Besar, angka b = {b}")

     elif b >= 5:
          print (f"Tengah, angka b = {a}")

     else:
          print (f"Kecil, angka b = {b}")

rt (10)
rt (9)
rt (8)
rt (7)
rt (6)
rt (5)
rt (4)
rt (3)
rt (2)
rt (1)

print ("\n --- batas --- \n")



# Fungsi dengan Percabangan Nested

def nes (r):

     cek = True

     if r >= 5:
          if cek:
               print (f"Besar, angka r = {r}")

     else:
          print (f"Kecil, angka a = {a}")

nes (10)
nes (9)
nes (8)
nes (7)
nes (6)
nes (5)
nes (4)
nes (3)
nes (2)
nes (1)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan nilai rapor 

def skor (e):

     if e >= 95:
          print (f"A, nilai = {a}")

     elif e >= 90:
          print (f"B, nilai = {b}")

     elif e >= 80:
          print (f"C, nilai = {e}")

     elif e >= 70:
          print (f"D, nilai = {e}")

     elif e >= 60:
          print (f"E, nilai = {e}")

     elif e >= 50:
          print (f"F, nilai = {e}")

     else:
          print (f"Jelek amat, nilai = {e}")

skor (10)
skor (9)
skor (8)
skor (7)
skor (6)
skor (5)
skor (4)
skor (3)
skor (2)
skor (1)


print ("\n --- batas --- \n")




# Usia Produktif manusia 

def usia (d):

     if d >= 15 and d <= 40:
          print (f"Usia sudah produktif, usia = {d}")

     elif d > 40:
          print (f"Sudah tua usiannya, usia = {d}")

     else:
          print (f"Masih kecil usiannya, usia = {d}")


usia (60)
usia (50)
usia (40)
usia (30)
usia (20)
usia (15)
usia (10)
usia (5)


print ("\n --- batas --- \n")




# Usia masuk JKT48 

def oshi (d):

     if d >= 15 and d <= 19:
          print (f"Boleh daftar jkt48, usia = {d}")

     elif d > 19:
          print (f"Sudah lebih dari cukup, usia = {d}")

     else:
          print (f"Masih kecil usiannya, usia = {d}")

oshi (20)
oshi (19)
oshi (18)
oshi (17)
oshi (16)
oshi (15)
oshi (14)
oshi (13)
oshi (12)
oshi (11)


print ("\n --- batas --- \n")




# Usia kerja manusia

def kerja (w):

     if w >= 23 and w <= 40:
          print (f"Boleh kerja, usia = {w}")

     elif w > 40:
          print (f"Sudah pensiun, usia = {w}")

     else:
          print (f"Masih kecil usiannya, usia = {w}")

kerja (60)
kerja (50)
kerja (40)
kerja (30)
kerja (20)
kerja (10)
kerja (5)


print ("\n --- batas --- \n")



# For dasar 

for i in range (1, 11):
     print (f"urutan ke - {i}")


print ("\n --- batas --- \n")




# For dasar 2 

for b in range (11):
     print (f"Urutan ke - {b}")


print ("\n --- batas --- \n")


# While dasar 

a = 1

while a < 11:
     print (f"Urutan ke - {a}")
     a = a + 1


print ("\n --- batas --- \n")




# While dasar 2

b = 11

while b > 0:
     print (f"Urutan ke - {b}")
     b = b - 1


print ("\n --- batas --- \n")



# For nested

for x in range (1, 11):
     for y in range (1, 11):
          print (f"Luar : {x} dan Dalam : {y}")


print ("\n --- batas --- \n")



# Struktur data 

data = [
     "Rusia",
     "Ukraina",
     "Turki",
     "Uzbekistan",
     "Inggris",
     "Amerika"
]

for a in data:
     print (a)


print ("\n --- batas --- \n")



# For break 1 

for i in range (1, 11):
     if i == 5:
          continue
     print (i)

print ("\n --- batas --- \n")



# For break 1

for i in range (1, 20):
     if i == 10:
          break
     print (i)


print ("\n --- batas --- \n")





print ("\n break for \n")

far = ["Run", "Un", "Fir", "Uk"]

for a in far:
     if a == "Far":
          continue
     print (a)


print ("\n --- batas --- \n")



# For continue 3

op = ["Oke", "Good", "Job", "Fair", "Not"]

for r in op:
     if r == "Job":
          break
     print (r)


print ("\n --- batas --- \n")




# Dictionary 

data = {
     "nama" : "Habib Muzakki",
     "usia" : 18,
     "cek" : True,
}

print ("Nama :", data ["nama"])
print ("Usia :", data ["usia"])
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




# Bikin Error Handling + Percabangan dasar 

def eror (k):

     try:
          if k < 0:
               raise ("Gagal")

          if k >= 5:
               print (f"Besar, angka k = {k}")

          else:
               print (f"Kecil, angka k = {k}")

     except:
          print (f"Angka minus, angka k = {k}")

eror (10)
eror (9)
eror (3)
eror (5)
eror (7)
eror (7)
eror (9)
eror (-4)
eror (-23)
eror (-90)
eror (-00)


print ("\n --- batas --- \n")




# Error Handling + Percabangan Lanjutan 

def run (e):

     try:

          if e < 0:
               raise ("Gagal")

          if e >= 8:
               print (f"Angka besar, angka e = {e}")

          elif e >= 5:
               print (f"Tengah, angka e = {e}")

          else:
               print (f"Kecil, angka e = {e}")

     except:
          print (f"Angka minus, angka e = {e}")

run (-10)
run (-9)
run (-6)
run (-3)
run (-2)
run (-1)
run (10)
run (-8)
run (6)
run (5)
run (3)
run (4)
run (2)
run (1)


print ("\n --- batas --- \n")