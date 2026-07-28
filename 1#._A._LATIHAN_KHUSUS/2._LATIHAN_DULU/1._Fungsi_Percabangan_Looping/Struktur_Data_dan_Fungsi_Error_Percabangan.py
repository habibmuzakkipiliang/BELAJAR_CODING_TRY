print ("\n Fungsi dengan Percabangan Dasar \n")

def runin (j):

     if j >= 5:
          print (f"Besar, angka j = {j}")

     else:
          print (f"Kecil, angka j = {j}")

runin (10)
runin (9)
runin (8)
runin (7)
runin (6)
runin (5)
runin (4)
runin (3)
runin (2)
runin (1)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Lanjutan \n")

def rut (d):

     if d >= 8:
          print (f"Besar, angka d = {d}")

     elif d >= 5:
          print (f"Tengah, angka d = {d}")

     else:
          print (f"Kecil, angka d = {d}")

rut (10)
rut (9)
rut (8)
rut (7)
rut (6)
rut (5)
rut (4)
rut (3)
rut (2)
rut (1)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Nilai Rapor \n")

def rapor (s):

     if s >= 90:
          print (f"A, nilai = {s}")

     elif s >= 80:
          print (f"B, nilai = {s}")

     elif s >= 70:
          print (f"C, nilai = {s}")

     elif s >= 60:
          print (f"D, nilai = {s}")
     
     elif s >= 50:
          print (f"E, nilai = {s}")

     else:
          print (f"Jelek amat, nilai = {s}")

rapor (100)
rapor (90)
rapor (80)
rapor (70)
rapor (60)
rapor (50)
rapor (30)

print ("\n --- batas --- \n")




print ("\n Nested 1 \n")

def rer (e):

     cek = True

     if e >= 5:
          if cek:
               print (f"Besar, angka e = {e}")

     else:
          print (f"Kecil, angka e = {e}")

rer (10)
rer (9)
rer (8)
rer (7)
rer (6)
rer (5)
rer (4)
rer (3)
rer (2)
rer (1)


print ("\n --- batas --- \n")



print ("\n Usia produktif Manusia \n")

def usia (w):

     if w >= 15 and w <= 45:
          print (f"Masuk usia produktif, usia = {w}")

     elif w > 45:
          print (f"Sudah tua, usia = {w}")

     else:
          print (f"Masih dibawah umur, umur = {w}")

usia (60)
usia (50)
usia (45)
usia (40)
usia (35)
usia (30)
usia (20)
usia (15)
usia (10)
usia (9)
usia (5)


print ("\n --- batas --- \n")




print ("\n Usia kerja manusia \n")

def kerja (n):

     if n >= 23 and n <= 40:
          print (f"Boleh kerja, usia = {n}")

     elif n > 40:
          print (f"Sudah tua, usia = {n}")

     else:
          print (f"Masih kecil usiannya, usia = {n}")

kerja (70)
kerja (60)
kerja (50)
kerja (40)
kerja (30)
kerja (20)
kerja (10)


print ("\n --- batas --- \n")




print ("\n Usia masuk JKT48 tahun 2026 \n")

def oshi (h):

     if h >= 13 and h <= 18:
          print (f"Boleh daftar jkt48, usia = {h}")

     elif h > 18:
          print (f"Sudah lebih dari cukup, usia = {h}")

     else:
          print (f"Masih dibawah umur, usia = {h}")

oshi (25)
oshi (24)
oshi (20)
oshi (18)
oshi (17)
oshi (15)
oshi (14)
oshi (13)
oshi (10)
oshi (9)


print ("\n --- batas --- \n")




print ("\n Array 1 \n")

rt = [1, 2, 3, 4, 5, 6, 7, 9]

rt.append (10)
rt.append (11)
rt.append (12)
rt.append (13)
rt.append (14)
rt.append (15)

for j in rt:
     print (j)


print ("\n --- batas --- \n")




print ("\n Array 2 \n")

dr = ["Run", "Ran", "Rust", "Var"]

dr.append ("Gun")
dr.append ("Bun")
dr.append ("Jun")
dr.append ("Ber")

for i in dr:
     print (i)


print ("\n --- batas --- \n")




print ("\n Array 3 \n")

gr = ["Eron", "Aron", "Ron", "Teron"]

gr.append ("Erons")
gr.append ("Bem")
gr.append ("Fer")
gr.append ("Gur")
gr.append ("Run")

for w in gr:
     print (w)


print ("\n --- batas --- \n")




print ("\n Dictionary \n")

data = {
     "nama" : "Habib Muzakki",
     "asal" : "Kota Serang",
     "jurusan" : "D4 Vokasi",
     "kuliah" : "Informatika",
}

print ("Nama :", data ["nama"])
print ("Asal :", data ["asal"])
print ("Jurusan :", data ["jurusan"])
print ("Kuliah :", data ["kuliah"])


print ("\n --- batas --- \n")




print ("\n Dictionary 1 \n")

profil = {
     "harga" : "Rp 1000",
     "item" : "5",
     "total" : "10",
     "rata" : "90",
}

print ("Harga :", profil ["harga"])
print ("Item :", profil ["item"])
print ("Total :", profil ["total"])
print ("Rata-rata :", profil ["rata"])


print ("\n --- batas --- \n")




print ("\n Dictionary 2 \n")

hun = {
     "nama" : "Johan",
     "usia" : 18,
     "tinggi" : "170 cm",
     "berat" : "60 kg",
}

print ("Nama :", hun ["nama"])
print ("Usia :", hun ["usia"])
print ("Tinggi :", hun ["tinggi"])
print ("Berat :", hun ["berat"])



print ("\n --- batas --- \n")




print ("\n Error Handling \n")

try:
     a = 10 / 0
     print (a)

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Selesai")

finally:
     print ("Selesai")


print ("\n --- batas --- \n")



print ("\n Error Handling \n")

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



print ("\n Fungsi dengan Angka terbesar \n")

def besar (n, m):

     if n > m:
          return n 
     
     else:
          return m
     
print (besar (10, 5))
print (besar (10, 3))
print (besar (4, 40))
print (besar (10, 2))


print ("\n --- batas --- \n")