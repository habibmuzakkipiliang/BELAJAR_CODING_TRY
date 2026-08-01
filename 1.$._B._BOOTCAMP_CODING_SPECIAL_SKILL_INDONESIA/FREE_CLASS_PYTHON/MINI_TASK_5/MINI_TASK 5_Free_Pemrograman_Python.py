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




# MINI TASK 5: Struktur Modular (Function dan Clean Code)
# Studi Kasus: Kasir Toko Buku Sederhana


# 1. Fungsi untuk tampilkan daftar buku

def tampilkan_menu ():

     print ("\n --- daftar buku --- \n")
     print ("1. Buku Novel     = Rp 50000")
     print ("2. Buku Komik     = Rp 30000")
     print ("3. Buku Pelajaran = Rp 40000")



# 2. Fungsi untuk menghitung total harga pembelian

def hitung_harga (pilihan, jumlah):

     if pilihan == 1:
          nama_buku = "Buku Novel"
          harga = 50000

     elif pilihan == 2:
          nama_buku = "Buku Komik"
          harga = 30000

     elif pilihan == 3:
          nama_buku = "Buku Pelajaran"
          harga = 40000

     else:
          nama_buku = "tidak ada"
          harga = 0

     total_bayar = harga * jumlah

     return nama_buku, total_bayar


# 3. Fungsi utama untuk menjalankan program

def jalankan_kasir ():

     # Tampilkan menu

     tampilkan_menu ()
     print ()



     # input dari pembeli

     pilihan = int (input ("Pilih nomor buku (1 - 3) : "))
     jumlah = int (input ("Jumlah buku : "))



     # hitung pakai fungsi 

     nama_buku, total_bayar = hitung_harga (pilihan, jumlah)


     # Tampilkan detail hasil transaksi

     if total_bayar > 0:
          print ("--- DETAIL PEMBELIAN ---")
          print (f"Buku yang dipilih : {nama_buku}")
          print (f"Total yang dibayar : Rp {total_bayar}")

     else:
        print ("Pilihan buku tidak valid!")


# Jalankan program utama
jalankan_kasir()

print ("\n --- batas --- \n")




# Variasi Function (Fungsi) Python dan Error Handling (Raise Exception) dan Dasar OOP (Object Oriented Programming) Python

# Fungsi dengan dasar

def dasar ():
     print (f"Halo Dunia yang Indah")

dasar ()


# Fungsi dengan dasar

def dan ():
     print ("Hello World")
     print ("Hello San")
     print ("Hello Fon")
     print ("Hello Final Oke")

dan ()

print ("\n --- batas --- \n")



# Fungsi dasar 4

def run ():
     print ("Hello Minecraft")

run ()
run ()
run ()
run ()
run ()


print ("\n --- batas --- \n")




# Fungsi dengan parameter 1, studi kasus perkenalan nama dan asalnya

def dasar_1 (sapa):
     print (f"Halo saya {sapa} dari Jakarta Timur")

dasar_1 ("Rayyan")
dasar_1 ("Fayyan")
dasar_1 ("Royyan")
dasar_1 ("Dankud")
dasar_1 ("Arroyan")
dasar_1 ("Ferz")


print ("\n --- batas --- \n")


# Fungsi dengan parameter 2, studi kasus perkenalan nama, asal, dan kuliah nya

def dasar_3 (nama, asal, kuliah):
     print (f"Halo nama saya {nama} dari daerah {asal}, dan sedang kuliah di {kuliah}")

dasar_3 ("Hayyan", "Jakarta", "UI")
dasar_3 ("Rayyan", "Jakarta", "ITB")
dasar_3 ("Fayyan", "Bandung", "Telkom Bandung")
dasar_3 ("Royyan", "Jatim", "ITS")


print ("\n --- batas --- \n")



# Fungsi dengan parameter 3, studi kasus perkenalan nama, asal, dan keahliannya

def dasar_4 (nama, asal, ahli):
     print (f"Nama saya {nama} dari daerah {asal} dan keahlian {ahli}")

dasar_4 ("Hayyan", "Jakarta Timur", "Coding")
dasar_4 ("Rayyan", "Jakarta Utara", "Desain Web")
dasar_4 ("Foyyan", "Jakarta Barat", "Desain Poster Digital")
dasar_4 ("Huyyan", "Jakarta Timur", "Desain Grafis")
dasar_4 ("Foi", "Jakarta Pusat", "AI Engineer")


print ("\n --- batas --- \n")



# Fungsi dengan parameter 4, studi kasus daftar Game Lain-lain

def lets_game (nama, pembuat, publisher, asal, rilis):

     print (f"Game {nama}, dengan pembuat oleh {pembuat}, dipublish oleh {publisher}, berasal dari negara {asal} dan dirilis tahun {rilis}")

lets_game ("Minecraft", "Notch", "Perusahaan Mojang", "Swedia", 2009)
lets_game ("Mobile Legend", " Justin Yuan bersama Xu Zhenhua", "Moonton", "China", 2016)
lets_game ("Free Fire", "111 Dots Studio", "Garena", "China", 2017)
lets_game ("PUBG", "Chang-han Ki", "Bluehole / PUBG Corporation", "China", 2017)
lets_game ("Warplane WW2 Dogfight", "Home Net Games", "Home Net Games",  "Polandia", 2018)
lets_game ("Warplanes WW1 Sky Aces", "Home Net Games", "Home Net Games", "Polandia", 2019)
lets_game ("Warplanes: Task Force", "Home Net Games", "Home Net Games", "Polandia", 2026)


print ("\n --- batas --- \n")




# Fungsi dengan parameter, studi kasus tentang daftar oshi JKT48 punya saya (Habib Muzakki)

def oshi_jkt48 (nama, asal, generasi, debut):
     print (f"- {nama} JKT48, dari daerah {asal}, dari {generasi}, dan debut tahun {debut}")

oshi_jkt48 ("Gracie", "Tangerang", "Gen 11", 2024)
oshi_jkt48 ("Michie", "Palembang", "Gen 11", 2024)
oshi_jkt48 ("Lily", "Amerika Serikat", "Gen 11", 2025)
oshi_jkt48 ("Aralie", "Jakarta", "Gen 12", 2026)
oshi_jkt48 ("Fritzy", "Jakarta", "Gen 12", 2025)
oshi_jkt48 ("Lana", "Bekasi", "Gen 12", 2025)
oshi_jkt48 ("Anindya", "Depok", "Gen 11", 2025)
oshi_jkt48 ("Christy", "Jakarta", "Gen 7", 2019)
oshi_jkt48 ("Celine Eks", "Malaysia", "Gen 4", 2016)
oshi_jkt48 ("Freya (Kapten)", "Tangerang", "Gen 7", 2020)


print ("\n --- batas --- \n")



# Fungsi dengan return, 

def halo (nama):
     return f"Halo {nama}, selamat datang di dunia pemrograman Python"

print (halo ("Habib Muzakki"))
print (halo ("Rayyan"))
print (halo ("Fayyan"))
print (halo ("Royyan"))
print (halo ("Dankud"))
print (halo ("Arroyan"))
print (halo ("Ferz"))
print (halo ("Ron"))


print ("\n --- batas --- \n")





# Fungsi dengan return, studi kasus tentang Operasi Aritmatika Dasar

x = int (input ("Masukkan angka x : "))
y = int (input ("Masukkan angka y : "))

def tambah (x, y):
     return x + y

def kurang (x, y):
     return x - y

def kali (x, y):
     return x * y

def pangkat (x, y):
     return x ** y

def bagi_bulat (x, y):
     return x // y

def bagi (x, y):
     return x / y

def modulus (x, y):
     return x % y


print ("Hasil penjumlahan =", tambah (x, y))
print ("Hasil pengurangan =", kurang (x, y))
print ("Hasil perkalian =", kali (x, y))
print ("Hasil pangkat  =", pangkat (x, y))
print ("Hasil pembagian bulat =", bagi_bulat (x, y))
print ("Hasil pembagian =", bagi (x, y))
print ("Hasil modulus =", modulus (x, y))


print ("\n --- batas --- \n")



# Fungsi dengan return, studi kasus tentang Operasi Perbandingan

def banding_1 (x, y):
     return x > y

def banding_2 (x, y):
     return x < y

def banding_3 (x, y):
     return x >= y

def banding_4 (x, y):
     return x <= y

def banding_5 (x, y):
     return x == y

def banding_6 (x, y):
     return x != y

print ("Hasil perbandingan =", banding_1 (x, y))
print ("Hasil perbandingan =", banding_2 (x, y))
print ("Hasil perbandingan =", banding_3 (x, y))
print ("Hasil perbandingan =", banding_4 (x, y))
print ("Hasil perbandingan =", banding_5 (x, y))
print ("Hasil perbandingan =", banding_6 (x, y))


print ("\n --- batas --- \n")




# Fungsi dengan return, studi kasus tentang Operasi logika

def logika_1 (x, y):
     return x and y

def logika_2 (x, y):
     return x or y

def logika_3 (x, y):
     return not x

def logika_4 (x, y):
     return not y

def logika_5 (x, y):
     return not (x, y)

def logika_6 (x, y):
     return not (x, y)


print ("Hasil logika =", logika_1 (x, y))
print ("Hasil logika =", logika_2 (x, y))
print ("Hasil logika =", logika_3 (x, y))
print ("Hasil logika =", logika_4 (x, y))
print ("Hasil logika =", logika_5 (x, y))   
print ("Hasil logika =", logika_6 (x, y))


print ("\n --- batas --- \n")





# Fungsi dengan return, studi kasus tentang Operasi Rumus Luas bangun datar

def persegi (s):
     return s * s

def persegi_panjang (p, l):
     return p * l

def segitiga (a, t):
     return a * t / 2

def lingkaran (r):
     return 3.14 * r * r

def layang_layang (d1, d2):
     return d1 * d2 / 2

def belah_ketupat (d1, d2):
     return d1 * d2 / 2

def trapesium (a, b, t):
     return (a + b) * t / 2

print ("Luas persegi =", persegi (5))
print ("Luas persegi panjang =", persegi_panjang (5, 10))
print ("Luas segitiga =", segitiga (5, 10))
print ("Luas lingkaran =", lingkaran (5))
print ("Luas layang-layang =", layang_layang (5, 10))
print ("Luas belah ketupat =", belah_ketupat (5, 10))
print ("Luas trapesium =", trapesium (5, 10, 7))


print ("\n --- batas --- \n")




# Fungsi dengan return, mencari angka terbesar

def angka_terbesar (a, b):

     if a > b:
          return a
     else:
          return b

print ("Angka terbesar =", angka_terbesar (10, 20))
print ("Angka terbesar =", angka_terbesar (30, 20))
print ("Angka terbesar =", angka_terbesar (15, 15))
print ("Angka terbesar =", angka_terbesar (100, 50))
print ("Angka terbesar =", angka_terbesar (5, 10))
print ("Angka terbesar =", angka_terbesar (25, 30))
print ("Angka terbesar =", angka_terbesar (40, 20))
print ("Angka terbesar =", angka_terbesar (60, 80))
print ("Angka terbesar =", angka_terbesar (90, 70))

print ("\n --- batas --- \n")




# Fungsi dengan return, studi kasus tentang mencari angka terkecil

def angka_terkecil (a, b):

     if a < b:
          return a
     else:
          return b

print ("Angka terkecil =", angka_terkecil (10, 20))
print ("Angka terkecil =", angka_terkecil (30, 20))
print ("Angka terkecil =", angka_terkecil (15, 15))
print ("Angka terkecil =", angka_terkecil (100, 50))
print ("Angka terkecil =", angka_terkecil (5, 10))
print ("Angka terkecil =", angka_terkecil (25, 30))
print ("Angka terkecil =", angka_terkecil (40, 20))
print ("Angka terkecil =", angka_terkecil (60, 80))
print ("Angka terkecil =", angka_terkecil (90, 70))
print ("Angka terkecil =", angka_terkecil (5, 90))


print ("\n --- batas --- \n")




# Fungsi dengan parameter, percabangan dasar

def percabangan (x):

     if x > 0:
          print ("Angka positif")
     elif x < 0:
          print ("Angka negatif")
     else:
          print ("Angka nol")

percabangan (10)
percabangan (-5)
percabangan (0)
percabangan (100)
percabangan (-50)


print ("\n --- batas --- \n")




# Fungsi dengan percabangan lanjutan 

def percabangan_lanjutan (x):

     if x % 2 == 0:
          print ("Angka genap")
     else:
          print ("Angka ganjil")

percabangan_lanjutan (10)
percabangan_lanjutan (5)
percabangan_lanjutan (0)
percabangan_lanjutan (100)
percabangan_lanjutan (51)
percabangan_lanjutan (99)
percabangan_lanjutan (88)
percabangan_lanjutan (77)


print ("\n --- batas --- \n")





# Error Handling 

try:
     a = 10 / 0

except ZeroDivisionError:
     print ("Gagal membagi dengan nol, silakan masukkan angka yang valid.")

else:
     print ("berhasil membagi, hasilnya adalah", a)

finally:
     print ("Program selesai dijalankan.")


print ("\n --- batas --- \n")




# Error Handling 2

try:
     b = 10 + 10

except TypeError:
     print ("Terjadi kesalahan tipe data, silakan periksa input Anda.")

else:
     print ("Berhasil melakukan operasi penjumlahan, hasilnya adalah", b)

finally:
     print ("Program selesai dijalankan.")


print ("\n --- batas --- \n")




# Raise Exception Error Handling

def eror_raise (x):

     try:

          if x < 0:
               raise ValueError ("Angka tidak boleh negatif, silakan masukkan angka positif.")

          if x >= 10:
               print (f"Angka {x} diterima, program berjalan normal.")

          else:
               print (f"Angka {x} diterima, program berjalan normal.")


     except ValueError as e:
          print ("Terjadi kesalahan:", e)


eror_raise (-5)
eror_raise (5)
eror_raise (10)
eror_raise (15)
eror_raise (0)
eror_raise (-10)
eror_raise (20)

print ("\n --- batas --- \n")




# Raise Exception Error Handling 2

def eror_raise_2 (y):

     try:
          if y < 0:
               raise ValueError ("Angka tidak boleh negatif, silakan masukkan angka positif.")

          if y >= 100:
               print (f"Angka {y} diterima, program berjalan normal.")

          elif y < 100:
               print (f"Angka {y} diterima, program berjalan normal.")

          else:
               print (f"Angka {y} diterima, program berjalan normal.")

     except ValueError as y:
          print ("Terjadi kesalahan:", y)


eror_raise_2 (-50)
eror_raise_2 (50)
eror_raise_2 (100)
eror_raise_2 (150)
eror_raise_2 (0)
eror_raise_2 (-100)
eror_raise_2 (200)
eror_raise_2 (75)
eror_raise_2 (25)
eror_raise_2 (125)


print ("\n --- batas --- \n")




# OOP Dasar, Studi Kasus : tentang Kucing

class Kucing:

     def __init__(self, nama, warna, asal, lari):
          self.nama = nama
          self.warna = warna
          self.asal = asal
          self.lari = lari

     def aksi (self):
          print (f"Kucing {self.nama} berwarna {self.warna} berasal dari {self.asal} dan bisa berlari {self.lari} km/jam")

hasil_kucing = Kucing ("Mimi", "Putih", "Jakarta", 20)
hasil_kucing_1 = Kucing ("Momo", "Hitam", "Bandung", 15)
hasil_kucing_2 = Kucing ("Mumu", "Coklat", "Surabaya", 10)
hasil_kucing_3 = Kucing ("Mimi", "Abu-abu", "Medan", 25)

hasil_kucing.aksi ()
hasil_kucing_1.aksi ()
hasil_kucing_2.aksi ()
hasil_kucing_3.aksi ()


print ("\n --- batas --- \n")




# OOP Dasar 2, studi kasus tentang Anjing

class Anjing:

     def __init__(self, nama, warna, asal, lari):
           self.nama = nama
           self.warna = warna
           self.asal = asal
           self.lari = lari

     def akson (self):
          print (f"Anjing {self.nama} berwarna {self.warna} berasal dari {self.asal} dan bisa berlari {self.lari} km/jam")

hasil_anjing = Anjing ("Bobby", "Coklat", "Jakarta", 30)
hasil_anjing_1 = Anjing ("Bubu", "Hitam", "Bandung", 25)
hasil_anjing_2 = Anjing ("Bibi", "Putih", "Surabaya", 20)
hasil_anjing_3 = Anjing ("Bobo", "Abu-abu", "Medan", 35)
hasil_anjing_4 = Anjing ("Bibi", "Coklat Muda", "Makassar", 40)


hasil_anjing.akson ()
hasil_anjing_1.akson ()
hasil_anjing_2.akson ()
hasil_anjing_3.akson ()
hasil_anjing_4.akson ()


print ("\n --- batas --- \n")




# OOP dasar 3, studi kasus tentang mobil

class Mobil:

     def __init__(self, merk, warna, tahun, kecepatan):
          self.merk = merk
          self.warna = warna
          self.tahun = tahun
          self.kecepatan = kecepatan

     def akselerasi (self):
          print (f"Mobil {self.merk} berwarna {self.warna} keluaran tahun {self.tahun} bisa melaju dengan kecepatan {self.kecepatan} km/jam")

hasil_mobil   = Mobil ("Toyota", "Hitam", 2020, 180)
hasil_mobil_1 = Mobil ("Honda", "Putih", 2021, 200)
hasil_mobil_2 = Mobil ("Mitsubishi", "Merah", 2022, 220)
hasil_mobil_3 = Mobil ("Suzuki", "Biru", 2023, 240)
hasil_mobil_4 = Mobil ("Daihatsu", "Abu-abu", 2024, 260)


hasil_mobil.akselerasi ()
hasil_mobil_1.akselerasi ()
hasil_mobil_2.akselerasi ()
hasil_mobil_3.akselerasi ()
hasil_mobil_4.akselerasi ()


print ("\n --- batas --- \n")