# Profil Habib Muzakki

nama = "Habib Muzakki"
asal = "Kota Serang"
gen = "Z Core (Inti)"
alumni_sekolah = "MAN 2 KOTA SERANG (Kelas atau Jurusan Agama) lulusan tahun 2026"
alumni_angkatan = "34 ASCENDRIA (lulusan 2026) MAN 2 KOTA SERANG"
coding = "HTML, CSS, JavaScript dan Python"
status = "Aspiring (Beginner) Full Stack Dev dan Bug Hunter"
jurusan = "D4 Vokasi Teknik Informatika (lebih suka Tech (Praktisi), bukan Math (Akademisi Teoritis))"
kampus = "Universitas Harkat Negeri Tegal"
lomba = "Finalis OSN-K Informatika tahun 2025"
fans = "JKT48 (Wota)"
game = "Minecraft Offline Android dan Warplane WW2  (World War 2) Dogfight Offline Android"
ig = "@habib_muzakki_piliang"
github = "https://github.com/habibmuzakkipiliang"
linkedin = "https://www.linkedin.com/in/habib-muzakki-piliang-15978b315/"


profil = f"""
- Nama lengkap    : {nama}
- Asal daerah     : {asal}
- Gen             : {gen}
- Alumni sekolah  : {alumni_sekolah}
- Alumni angkatan : {alumni_angkatan}
- Coding          : {coding}
- Status          : {status}
- Jurusan         : {jurusan}
- Kampus          : {kampus}
- Lomba           : {lomba}
- Fans            : {fans}
- Game            : {game}
- Instagram       : {ig}
- Github          : {github}
- LinkedIn        : {linkedin}
"""

print (profil)


print ("\n --- batas --- \n")



# Dokumentasi Jadwal Free Bootcamp Pemrograman Python

judul = "Free Class Pemrograman Python"
tipe = "Bootcamp atau Kursus IT Coding"
bootcamp = "Special Skill Indonesia"
tanggal = "26 Juli - 1 Agustus 2026"
waktu = " Fleksibel"
tempat = "E-Learning dan WhatsApp Grup"
tutor = "Febriyanti Paramudita S.T (Data Science di Bank Rakyat Indonesia)"
materi = [
     "Mindset Programmer dan Algoritma",
     "Fundamental Python",
     "Struktur data dan Percabangan",
     "Perulangan dan Pattern Thinking",
     "Function dan Clean Code",
     "Utilizing AI (AI Agent Tools : Claude dan Antigravity)",
     "Final Project",
]

bootcamp_kursus = f"""
- Judul bootcamp   : {judul}
- Tipe bootcamp    : {bootcamp}
- Tanggal bootcamp : {tanggal} 
- Waktu bootcamp   : {waktu}
- Tempat           : {tempat}
- Tutor            : {tutor}
- Materi           :
"""

print (bootcamp_kursus)

for a in materi:
     print (a)


print ("\n --- batas --- \n")




# MINI TASK 4: Teknik Perulangan dan Pattern Thinking

# Studi Kasus: Kasir Toko Buku Sederhana

# 1. Struktur data (List)

daftar_buku = ["Novel", "Komik", "Pelajaran"]




# 2, For Iterasi dasar (Tampilkan daftar buku)

print ("\n --- Daftar jenis kategori buku --- \n")

for buku in daftar_buku:
     print (buku)


print ("\n --- batas --- \n")





# 3. Percabangan Lanjutan untuk menentukan harga

pilihan = int (input ("Masukkan pilihan buku 1 - 3 :"))
jumlah = int (input ("Masukkan jumlah buku kamu :"))

if pilihan == 1:
     harga = 50000
     buku_pilih = daftar_buku [0]

elif pilihan == 2:
     harga = 30000
     buku_pilih = daftar_buku [1]


elif pilihan == 3:
     harga = 40000
     buku_pilih = daftar_buku [2]

else:
     harga = 0
     buku_pilih = "Gak ada"
     print ("Gak ada dalam daftar")




# Hitung dan tampilkan hasilnya 

if harga > 0:
     total = harga * jumlah 
     print ("\n ---- Detail Pembelian ---- \n")
     print (f"Buku yang dipilih = {buku_pilih}")
     print (f"Total harga nya = {total}")


print ("\n --- batas --- \n")




# Variasi Tambahan Looping dasar dan Looping Lanjutan

# For Dasar

for i in range (1, 11):
     print (f"Urutan ke {i}")

print ("\n --- batas --- \n")



# For dasar 2

for k in range (1, 11):
     print (F"Urutan ke - {k}")


print ("\n --- batas --- \n")



# For dasar 4

for t in range (11):
     print (f"urutan ke - {t}")


print ("\n --- batas --- \n")


# for dasar + nama saya

for nama in range (20):
     print ("Habib Muzakki itu cool dan oke")

print ("\n --- batas --- \n")




# For dasar + oshi JKT48

for oshi in range (20):
     print ("Gracie dan Michie JKT48 itu cantik")


print ("\n --- batas --- \n")




# For dasar + Coding Teks

for coding in range (1, 11):
     print ("HTML, CSS, JavaScript dan Python")


print ("\n --- batas --- \n")



# While dasar (Hitung mundur)

a = 30

while a > 1:
     print (f"Urutan ke - {a}")
     a = a - 1


print ("\n --- batas --- \n")




# While dasar (Hitung Maju)

b = 1

while b < 31:
     print (f"Urutan ke - {b}")
     b = b + 1


print ("\n --- batas --- \n")



# For nested 1 (sebanyak 2 kali)

for km in range (1, 3):
     for jk in range (1, 3):
          print (f"Luar : {km} dan Dalam : {jk}")


print ("\n --- batas --- \n")




# For Nested 2 (sebanyak 4 kali)

for x in range (1, 3):
     for y in range (1, 3):
          for z in range (1, 3):
               for j in range (1, 3):
                    print (f"x : {x}, y : {y}, z : {z}, j : {j}")


print ("\n --- batas --- \n")



# For Nested 3 (sebanyak 5 kali)

for jk in range (1, 3):
     for jf in range (1, 3):
          for fq in range (1, 3):
               for hg in range (1, 3):
                    for nm in range (1, 3):
                         print (f"JK : {jk}, JF : {jf}, FG : {fq}, HG : {hg}, NM : {nm}")


print ("\n --- batas --- \n")



# Nested For 4 (Sebanyak 4 kali)

for nf in range (1, 3):
     for hn in range (1, 3):
          for hj in range (1, 3):
               for df in range (1, 3):
                    print (f"nf : {nf}, hn : {hn}, hj : {hj}, df : {df}")

print ("\n --- batas --- \n")



# Break and Control Looping For

# For + Control continue

for i in range (1, 20):
     if i == 10:
          continue
     print (i)


print ("\n --- batas --- \n")



# For + Control Break

for j in range (1, 30):
     if j == 15:
          break
     print (j)


print ("\n --- batas --- \n")



# Oshi JKT48 Continue Looping For + List

oshi = ["Gracie JKT48", "Michie JKT48", "Lily JKT48", "Aralie JKT48", "Fritzy JKT48", "Lana JKT48"]

oshi.append ("Anindya JKT48 ")
oshi.append ("Christy JKT48")
oshi.append ("Celine Eks JKT48")
oshi.append ("Freya JKT48 (Kapten JKT48)")
oshi.append ("Olla JKT48")
oshi.append ("Jessi JKT48")
oshi.append ("Fiony JKT48")

for h in oshi:
     if h == "Aralie JKT48":
          continue
     print (h)


print ("\n --- batas --- \n")




# Buah-buahan Control Continue Looping For + List

buah = ["Buah Naga", "Buah Merah Papua", "Buah Salak", "Buah Apel", "Buah Nanas", "Buah Pepaya", "Buah Jambu Biji"]

buah.append ("Buah Zaitun")
buah.append ("Buah Kelapa")
buah.append ("Buah Kelapa Kopyor")
buah.append ("Buah Nangka")
buah.append ("Buah Matoa")
buah.append ("Buah Sawo")
buah.append ("Buah lengkeng")

for j in buah:
     if j == "Buah Jambu Biji":
          continue
     print (j)


print ("\n --- batas --- \n")




# Ikan-ikan lain Control break Looping For + List

ikan = ["Ikan Laut Halal", "Ikan Air Tawar Halal", "Ikan Sungai Halal", "Ikan Danau", "Ikan Patin", "Ikan Tenggiri", "Ikan Gabus", "Ikan Bawal", "Ikan Kembung", "Ikan Kakap", "Ikan Tuna", "Ikan Tongkol", "Ikan Sarden", "Ikan Lele", "Ikan Bilis", "Ikan Teri"]

ikan.append ("Ikan Hiu")
ikan.append ("Ikan Piranha")
ikan.append ("Ikan Hiu Harimau")
ikan.append ("Ikan Hiu Martil")
ikan.append ("Ikan Hiu Goblin")
ikan.append ("Ikan Hiu Berjumbai")
ikan.append ("Ikan Hiu Greenland")
ikan.append ("Ikan Hiu Hantu laut dalam")

for j in ikan:
     if j == "Ikan Kembung":
          break
     print (j)


print ("\n --- batas --- \n")




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