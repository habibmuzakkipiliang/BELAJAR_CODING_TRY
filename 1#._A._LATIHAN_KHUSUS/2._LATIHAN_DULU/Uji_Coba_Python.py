print ("\n Bikin Hello World \n")

print ("\n --- batas --- \n")




print ("\n Sintaks, Variabel dan Komentar \n")

# Halo Komen
# Tes Kommen

a = "Habib Muzakki"
print (a)


b = 12
print (b)


print ("\n --- batas --- \n")





print ("\n Tipe data pemrograman \n")

teks = "Halo Dunia"
angka = 12
desimal = 12.12
cek = True
kosong = None

tipe = f"""
- Teks    : {teks}
- Desimal : {desimal}
- Cek     : {cek}
- Kosong  : {kosong}
"""

print (tipe)


print ("\n --- batas --- \n")





print ("\n F String \n")

nama = "Habib Muzakki"
akrab = "Habib"
asal = "Kota Serang"
alumni = "MAN 2 KOTA SERANG (Kelas Agama)"
coding = "HTML, CSS, JavaScript dan Python"
jurusan = "D4 Vokasi Teknik Informatika"
kuliah = "Harkat Negeri Tegal"

profil = f"""
- Nama lengkap   : {nama}
- Nama panggilan : {akrab}
- Asal daerah    : {asal}
- Alumni sekolah : {alumni}
- Coding         : {coding}
- Jurusan        : {jurusan}
- Kuliah         : {kuliah}
"""

print (profil)


print ("\n --- batas --- \n")




print ("\n Operator Dasar \n")

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


hasil_1 = tambah (10, 10)
hasil_2 = kurang (10, 5)
hasil_3 = kali (10, 5)
hasil_4 = pangkat (10, 2)
hasil_5 = bagi (10, 5)


hitung = f"""
- Tambah = {hasil_1}
- Kurang = {hasil_2}
- Kali   = {hasil_3}
- Pangkat = {hasil_4}
- Bagi = {hasil_5}
"""

print (hitung)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Switch Case dengan Int \n")

def run (r):

     match (r):

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

run (1)
run (2)
run (3)
run (4)
run (5)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Switch Case dengan String \n")

def ryu (m):

     match (m):

          case "Merah":
               print ("Warna merah")

          case "Kuning":
               print ("Warna kuning")

          case "Hijau":
               print ("Warna hijau")

          case _:
               print ("Warna lain")

ryu ("Merah")
ryu ("Kuning")
ryu ("Hijau")
ryu ("Warna lain")


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Dasar \n")

def fun (j):

     if j >= 5:
          print (f"Besar, angka j = {j}")

     else:
          print (f"Kecil, angka j = {j}")

fun (10)
fun (9)
fun (8)
fun (7)
fun (6)
fun (5)
fun (4)
fun (3)
fun (2)
fun (1)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan lanjutan \n")

def wer (n):

     if n >= 8:
          print (f"Besar, angka n = {n}")

     elif n >= 5:
          print (f"Tengah, angka n = {n}")

     else:
          print (f"Kecil, angka n = {n}")

wer (10)
wer (9)
wer (8)
wer (7)
wer (6)
wer (5)
wer (4)
wer (3)
wer (2)
wer (1)


print ("\n --- batas --- \n")



print ("\n Fungsi dengan Percabangan Nilai Rapor \n")

def nilai (j):

     if j >= 90:
          print (f"A, nilai = {j}")

     elif j >= 80:
          print (f"B, nilai = {j}")

     elif j >= 70:
          print (f"C, nilai = {j}")

     elif j >= 60:
          print (f"D, nilai = {j}")

     elif j >= 50:
          print (f"E, nilai = {j}")

     else:
          print (f"Jelek amat, nilai = {j}")

nilai (100)
nilai (90)
nilai (80)
nilai (70)
nilai (60)
nilai (50)
nilai (40)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan Nested simbol \n")

def run (k):

     if k >= 5 and k >= 7:
          if cek == True:
               print (f"Besar, angka k = {k}")

     elif k >= 9 or k >= 3:
          print (f"Kecil, angka k = {k}")

run (10)
run (9)
run (8)
run (7)
run (6)
run (5)
run (4)
run (3)
run (2)
run (1)


print ("\n --- batas --- \n")




print ("\n Error Handling \n")

try:
     a = 10 / 0
     print (a)

except ZeroDivisionError:
     print ("Gagal")

else:
     print ("Berhasil")

finally:
     print ("Selesai")