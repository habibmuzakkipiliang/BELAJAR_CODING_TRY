print ("Hello World")


print ("\n --- batas --- \n")



nama = "Habib Muzakki"
print (nama)


print ("\n --- batas --- \n")


print ("\n Tipe data pemrograman \n")

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
- Kosong  : {kosong}
"""

print (tipe)


print ("\n --- batas --- \n")



print ("\n Profil Habib Muzakki \n")

nama_lengkap = "Habib Muzakki"
nama_panggilan = "Habib"
asal_daerah = "Kota Serang"
jurusan = "D4 Vokasi Teknik Informatika"
kampus = "Universitas Harkat Negeri Tegal"
coding = "HTML, CSS, JavaScript dan Python"


profil = f"""
- Nama lengkap   : {nama_lengkap}
- Nama panggilan : {nama_panggilan}
- Asal daerah    : {asal_daerah}
- Jurusan        : {jurusan}
- Kampus         : {kampus}
- Coding         : {coding}
"""

print (profil)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Switch Case 1 \n")

def dor (f):

     match (f):

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

dor (1)
dor (2)
dor (3)
dor (4)
dor (5)
dor (6)


print ("\n --- batas --- \n")



def dar (e):

     if e >= 5:
          print (f"Besar, angka e = {e}")

     else:
          print (f"Kecil, angka e = {e}")

dar (10)
dar (8)
dar (6)
dar (5)
dar (2)


print ("\n --- batas --- \n")



def run (b):

     if b >= 8:
          print (f"Besar, angka b = {b}")

     elif b >= 5:
          print (f"Tengah, angka b = {b}")

     else:
          print (f"Kecil, angka b = {b}")

run (10)
run (9)
run (8)
run (7)
run (6)
run (5)
run (4)
run (3)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Nilai Rapor \n")

def run (w):

     if w >= 90:
          print (f"A, nilai = {w}")

     elif w >= 80:
          print (f"B, nilai = {w}")

     elif w >= 70:
          print (f"C, nilai = {w}")

     elif w >= 60:
          print (f"D, nilai = {w}")

     else:
          print (f"Jelek banget, nilai = {w}")

run (10)
run (8)
run (7)
run (5)
run (4)
run (3)
run (2)
run (1)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Nested 1 \n")

def rut (r):

     cek = True

     if r >= 5:
          if cek:
               print (f"Besar, angka r = {r}")

     else:
          print (f"Kecil, angka r = {r}")

rut (10)
rut (8)
rut (5)
rut (4)
rut (3)
rut (2)
rut (1)


print ("\n --- batas --- \n")




print ("\n Error Handling \n")

try:
     a = 10 / 0

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Berhasil")

finally:
     print ("Selesai")


print ("\n --- batas --- \n")




print ("\n Error Handling \n")

try:
     h = 10 + 10
     print (h)

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Berhasil")

finally:
     print ("Selesai")


print ("\n --- batas --- \n")




print ("\n Error Handling + Percabangan 1 \n")

def ruk (e):

     try:

          if e < 0:
               raise ("Gagal")

          if e >= 5:
               print (f"Besar, angka e = {e}")

          else:
               print (f"Kecil, angka e = {e}")

     except:
          print (f"Angka minus, angka e = {e}")

ruk (10)
ruk (9)
ruk (8)
ruk (7)
ruk (5)
ruk (4)
ruk (3)
ruk (2)
ruk (1)


print ("\n --- batas --- \n")



print ("\n Usia Produktif manusia + Percabangan \n")

def usia (d):

     if d >= 15 and d <= 40:
          print (f"usia produktif manusia, usia = {d}")

     elif d > 40:
          print (f"Usia yang sudah tua, usia = {d}")

     else:
          print (f"Masih kecil usiannya, usia = {d}")

usia (10)
usia (90)
usia (40)
usia (30)
usia (20)
usia (15)
usia (1)
usia (4)
usia (8)