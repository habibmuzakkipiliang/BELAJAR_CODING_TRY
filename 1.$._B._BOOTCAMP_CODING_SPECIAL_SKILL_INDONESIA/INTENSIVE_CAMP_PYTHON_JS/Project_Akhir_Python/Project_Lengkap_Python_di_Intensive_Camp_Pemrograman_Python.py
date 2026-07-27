# Project Lengkap Python di Intensive Camp Pemrograman Python

print ("\n Project Lengkap Python di Intensive Camp Pemrograman Python \n")

print ("Hello World")



nama = "Habib Muzakki"
akrab = "Habib"
asal = "Kota Serang, Banten"
alumni = "Alumni MAN 2 KOTA SERANG (Kemenag) tahun 2023 - 2026"
kelas = "Alumni Kelas Jurusan Agama tahun 2023 - 2026"
angkatan = 34
linkedin = "Habib Muzakki Piliang"
instagram = "@habib_muzakki_piliang"
github = "https://github.com/habibmuzakkipiliang"



profil = f"""
- Dibuat Oleh :

- Nama lengkap   : {nama}
- Nama panggilan : {akrab}
- Asal           : {asal}
- Alumni         : {alumni}
- Kelas          : {kelas}
- Angkatan       : {angkatan}
- LinkedIn       : {linkedin}
- Instagram      : {instagram}
- Github         : {github}
"""

print (profil)


print ("\n --- Batas --- \n")




print ("\n Input dan Output Formulir data \n")

nama_lengkap = input ("Siapa Nama lengkap Kamu ? ")
nama_panggilan = input ("Apa nama panggilan kamu ? ")
asal = input ("Darimana asal kamu ? ")
tempat = input ("Dimana tempat tinggal kamu ? ")
kerja = input ("Kerja apa kamu sekarang ? ")
tinggi = int (input ("Berapa tinggi badan kamu ? "))
berat = int (input ("Berapa berat badan kamu ? "))
usia = int (input ("Berapa usia kamu sekarang ? "))
hobi = input ("Hobi kamu apa sekarang ? ")
passion = input ("Passion kamu apa sekarang ? ")
desimal = float (input ("Ketik angka desimal terserah ? "))



form = f"""
- Nama lengkap   : {nama_lengkap}
- Nama panggilan : {nama_panggilan}
- Asal           : {asal}
- Tempat tinggal : {tempat}
- Pekerjaan      : {kerja}
- Tinggi badan   : {tinggi}
- Berat badan    : {berat}
- Usia           : {usia}
- Hobi           : {hobi}
- Passion        : {passion}
- Desimal        : {desimal}
"""

print (form)


print ("\n --- Batas --- \n")




print ("\n Tipe Data Pemrograman dasar \n")

teks = "Halo Teks"
angka = 12
desimal = 3.14
cek_1 = True
cek_2 = False
char = 'A'
kosong = None


tipe = f"""
- Teks    : {teks}
- Angka   : {angka}
- Desimal : {desimal}
- Cek 1   : {cek_1}
- Cek 2   : {cek_2}
- Char    : {char}
- Kosong  : {kosong}
"""

print (tipe)


print ("\n --- Batas --- \n")




print ("\n Free Class Pemrograman Python \n")

kursus = "Special Skill Indonesia (2026) Online"
tipe = "Bootcamp atau Kursus IT Coding"
platform = "Zoom Meeting dan Google Colab"
tutor = "Febriyanti Paramudita S.T (Data Science di Bank Rakyat Indonesia)"
tanggal = "24 Mei 2026"
waktu = "19.00 - 21.00 WIB"

     
data = f"""
- Kursus   : {kursus}
- Tipe     : {tipe}
- Platform : {platform}
- Tutor    : {tutor}
- Tanggal  : {tanggal}
- Waktu    : {waktu}
"""

print (data)


print ("\n --- Batas --- \n")




print ("\n Intensive Camp Pemrograman Python \n")

kursus = "Special Skill Indonesia (2026) Online"
tipe = "Bootcamp atau Kursus IT Coding"
platform = "Zoom Meeting dan Google Colab"
tutor = "Febriyanti Paramudita S.T (Data Science di Bank Rakyat Indonesia)"
tanggal = "29 - 31 Mei 2026"
waktu = "19.00 - 21.00 WIB"
materi = [
     "1. Hello World",
     "2. Variabel, Sintaks, Komen dasar",
     "3. Operasi dasar (Aritmatika, Perbandingan dan Logika)",
     "4. F String",
     "5. Input dan Output data",
     "6. Percabangan dan Nested If (Match Case, If, Elif, Else)",
     "7. Perulangan dan Nested Loop (For dan While)",
     "8. Struktur data (List, Tuple, Set dan Dictionary)",
     "9. Fungsi (Dasar, Parameter dan Return)",
]


data = f"""
- Kursus   : {kursus}
- Tipe     : {tipe}
- Platform : {platform}
- Tutor    : {tutor}
- Tanggal  : {tanggal}
- Waktu    : {waktu}
- Materi   :
"""

print (data)

for a in materi:
     print (a)


print ("\n --- Batas --- \n")




print ("\n Variabel dasar \n")

nama = "Halo Dunia"
print (nama)

print ("\n --- Batas --- \n")



angka = 19
print (angka)

print ("\n --- Batas --- \n")



desimal = 20.12
print (desimal)

print ("\n --- Batas --- \n")




print ("\n Kalkulator Operasi Arimatika dalam Fungsi pakai Return \n")

def tambah (a, b):
     return a + b

def kurang (x, y):
     return x - y

def kali (e, r):
     return e * r

def bagi (w, k):
     return w / k

def pangkat (l, p):
     return l ** p

def modulus (k, m):
     return k % m


hasil_1 = tambah (10, 10)
hasil_2 = kurang (10, 9)
hasil_3 = kali (10, 10)
hasil_4 = bagi (10, 2)
hasil_5 = pangkat (10, 3)
hasil_6 = modulus (10, 5)


print (hasil_1)
print (hasil_2)
print (hasil_3)
print (hasil_4)
print (hasil_5)
print (hasil_6)


print ("\n --- Batas --- \n")





print ("\n Operasi Perbandingan dan Logika \n")

o = 10
u = 5

hasil = f"""
Operasi Perbandingan

- Hasil = {o > u}
- Hasil = {o < u}
- Hasil = {o >= u}
- Hasil = {o <= u}
- Hasil = {o == u}
- Hasil = {o != u}

-------------------------------

Operasi Logika

- Hasil = {o > u and o < u}
- Hasil = {o < u or o > u}
- Hasil = {not (o < u)}
- Hasil = {not (o > u)}
- Hasil = {not o}
- Hasil = {not u}
"""

print (hasil)


print ("\n --- Batas --- \n")




print ("\n Match Case dengan Fungsi \n")

def jun (a):
     
     match (a):
          
          case 1:
               print ("Oke")
               
          case 2:
               print ("Setengah Oke")
               
          case _:
               print ("Biasa aja")
               
jun (1)
jun (2)
jun (3)


print ("\n --- Batas --- \n")




print ("\n Match Case 1 dengan Fungsi \n")

def warna (k):
     
     match (k):
          
          case "Merah":
               print ("Warna Merah")
               
          case "Biru":
               print ("Warna Biru")
               
          case "Kuning":
               print ("Warna Kuning")
               
          case "Ungu":
               print ("Warna Ungu")
               
          case "Hijau":
               print ("Warna Hijau")
               
          case "Nila":
               print ("Warna Nila")
               
          case _:
               print ("Warna lain")

warna ("Nila")
warna ("Merah")
warna ("Biru")
warna ("Kuning")
warna ("Hijau")
warna ("Aqua")
warna ("Aquamarine")


print ("\n --- Batas --- \n")




print ("\n Percabangan dasar dengan Fungsi \n")

def fk (a):
     
     if a > 5:
          print (f"Besar, angka a = {a}")
          
     else:
          print (f"Kecil, angka a = {a}")
          
fk (10)
fk (3)
fk (1)
fk (2)
fk (4)
fk (7)
fk (4)


print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan dengan Fungsi \n")

def hj (b):
     
     if b > 5:
          print (f"Besar, angka b = {b}")
          
     elif b < 5:
          print (f"Kecil, angka b = {b}")
          
     else:
          print (f"Sama saja, angka b = {b}")
          
hj (10)
hj (3)
hj (5)
hj (8)
hj (4)
hj (2)
hj (1)
hj (3)
hj (6)


print ("\n --- Batas --- \n")




print ("\n Percabangan Ladder dengan Fungsi, nilai rapor \n")

def nilai (y):
    
    if y >= 95:
        print (f"A, nilai = {y}")
        
    elif y >= 90:
        print (f"B, nilai = {y}")
        
    elif y >= 80:
        print (f"C, nilai = {y}")
        
    elif y >= 70:
        print (f"D, nilai = {y}")
        
    elif y >= 60:
        print (f"E, nilai = {y}")
        
    elif y >= 50:
        print (f"F, nilai = {y}")
        
    else:
        print (f"Jelek banget, nilai = {y}")
        
        
nilai (100)
nilai (95)
nilai (90)
nilai (80)
nilai (70)
nilai (60)
nilai (50)


print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 1 dengan Fungsi \n")

def run (usia):
     
     cek = True
     
     if usia >= 17:
          if cek:
               print (f"Usia kamu oke kok, usia = {usia}")
               
          elif usia <= 17:
               print (f"Usia kamu belum oke kok, usia = {usia}")
               
     else:
          print (f"Kembali ke bocil, usia = {usia}")
          
run (20)
run (13)
run (16)
run (17)
run (18)
run (20)


print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 2 dengan Fungsi \n")

def yun (f):
     
     cek = True
     
     if f >= 18:
          if cek:
               print (f"Usia kamu udah oke kok, usia = {f}")
               
          else:
               print (f"Usia kamu belum kok, usia = {f}")
               
     else:
          print (f"Usia kamu masih bocil, usia = {f}")
          
yun (20)
yun (15)
yun (18)
yun (13)
yun (10)


print ("\n --- Batas --- \n")




print ("\n Percabangan Majemuk Kompleks dengan Fungsi, persyaratan nonton bioskop film Pengantin Setan Indonesia 2026 \n")

def fg (usia, uang):
     
     cek = True
     
     if usia >= 18 and uang >= 50000:
          if cek:
               print (f"Boleh nonton film horor yaitu Pengantin Setan, uang = {uang} dan usia {usia}")
               
          elif usia <= 18 and uang <= 50000:
               print (f"Jangan nontoh dibawah umur dan uang kecil untuk nonton film horor Pengantin Setan, uang = {uang} dan usia = {usia}")
               
          else:
               print (f"Uang dan umur anda kurang, uang = {uang} dan usia = {usia}") 
          
     else:
          print (f"Gak ada uang dan umur masih kurang, uang = {uang} dan usia = {usia}")
   
fg (19, 90000)
fg (20, 100000)
fg (18, 450000)
fg (25, 60000)
fg (10, 6000)
fg (12, 10000)       

          
print ("\n --- Batas --- \n")




print ("\n For Perulangan dasar \n")

for a in range (1, 11):
     print (f"Urutan ke - {a}")
     
     
print ("\n --- Batas --- \n")




print ("\n For Perulangan dasar 2 \n")

for b in range (20):
     print (f"Urutan ke - {b}")
     
     
print ("\n --- Batas --- \n")




print ("\n For Perulangan dasar 3 \n")


for c in range (30):
    print (f"Urutan ke - {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n While Perulangan Hitung Maju \n")

a = 1

while a < 15:
     print (f"Urutan = {a}")
     a = a + 1
     
     
print ("\n --- Batas --- \n")




print ("\n While Perulangan Hitung Mundur \n")

b = 15

while b > 0:
     print (f"Urutan ke - {b}")
     b = b - 1
     
     
print ("\n --- Batas --- \n")




print ("\n For Nested 1 \n")

for a in range (6):
     for b in range (6):
          print (f"Luar : {a} dan Dalam : {b}")
          
          
print ("\n --- Batas --- \n")




print ("\n For Nested 2 \n")

for x in range (6):
     for y in range (6):
          print (f"Luar : {x} dan Dalam : {y}")
          
          
print ("\n --- Batas --- \n")




print ("\n List dan Methods \n")

buah = [
     "Melon",
     "Semangka",
     "Apel",
     "Salak",
]

buah.append ("Buah Naga")
buah.append ("Buah Merah Papua")
buah.append ("Nangka") 
buah.append ("Nanas")
buah.append ("Mangga")
print (buah)


for a in buah:
     print (a)
     
     
print ("\n --- Batas --- \n")




print ("\n Set \n")

buah = {
     "Melon",
     "Semangka",
     "Apel",
     "Salak",
}

for b in buah:
     print (b)
     
     
print ("\n --- Batas --- \n")
     



print ("\n Tuple \n")

buah = (
     "Melon",
     "Semangka",
     "Apel",
     "Salak",
)

for c in buah:
     print (c)
     
     
print ("\n --- Batas --- \n")




print ("\n Dictionary \n")

data = {
     "nama" : "Johan",
     "kerja" : "IT Senior",
     "status" : "hidup",
     "asal" : "Amrik",
     "usia" : 20,
}

print ("Nama :", data ["nama"])
print ("Kerja :", data ["kerja"])
print ("Status :", data ["status"])
print ("Asal :", data ["asal"])
print ("Usia :", data ["usia"])


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan parameter \n")

def run (nama, asal):
     print (f"Halo nama saya {nama}, dari {asal}")
     
run ("Hans", "Jerman")
run ("Luther", "Jerman")
run ("James", "Inggris")
run ("Frank", "Amerika")
run ("Frederick", "Jerman")
run ("Otto", "Jerman")

print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Parameter 2 \n")

def wer (nama, asal, tinggi):
     print (f"Halo nama saya {nama}, dari {asal}, dan tinggi badan saya {tinggi}")
     
wer ("Chuck", "Amerika", 175)
wer ("Leonard", "Amerika", 180)
wer ("Jansen", "Belanda", 190)
wer ("Luger", "Jerman", 175)
wer ("Jon", "Italia", 170)


print ("\n --- Batas --- \n")




print ("\n Fungsi dasar \n")

def tun ():
     print ("Hello World")
     
tun ()


print ("\n --- Batas --- \n")




print ("\n Error Handling \n")

try:
     hasil = 10 / 0
     print (hasil)
     
except:
     print ("Gagal")
     
else:
     print ("Oke")
     
finally:
     print ("Selesai")
     
     
print ("\n --- Batas --- \n")




print ("\n Error Handling 2 \n")

try:
     hasil = 20 / 0
     print (hasil)
     
except:
     print ("Gagal")
     
else:
     print ("Oke")
     
finally:
     print ("Selesai")
     
     
print ("\n --- Batas --- \n")




print ("\n Error Handling 3 \n")

try:
     hasil = 10 + 10
     print (hasil)
     
except:
     print ("Gagal")
     
else:
     print ("Oke")
     
finally:
     print ("Selesai")
     
     
print ("\n --- Batas --- \n")




print ("\n Error Handling 4 \n")

try:
     hasil = 20 + 20
     print (hasil)
     
except:
     print ("Gagal")
     
else:
     print ("Oke")
     
finally:
     print ("Selesai")
     
     
print ("\n --- Batas --- \n")




print ("\n Fungsi Raise Error Handling 1 \n")

def er (a):
     
     try:
          if a < 0:
               raise ("Gagal")
          
          if a >= 5:
               print (f"Besar, angka a = {a}")
               
          elif a <= 5:
               print (f"Kecil, angka a = {a}")
               
          else:
               print (f"Sama saja, angka a = {a}")
               
     except:
          print (f"gak boleh minus, angka = {a}")
          
er (-10)
er (-2)
er (-6)
er (10)
er (3)
er (7)
er (5)

       
print ("\n --- Batas --- \n")




print ("\n Fungsi Raise Error Handling \n")

def rus (b):
     
     try:
          if b < 0:
               raise ("Gagal")
          
          if b >= 5:
               print (f"Besar, angka b = {b}")
               
          elif b <= 5:
               print (f"Kecil, angka b = {b}")
               
          else:
               print (f"Sama saja, angka b = {b}")
               
     except:
          print (f"Gak boleh minus, angka b = {b}")
          
rus (10)
rus (-2)
rus (-7)
rus (3)
rus (7)
rus (5)


print ("\n --- Batas --- \n")