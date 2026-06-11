# Latihan Coding Python


print ("\n Latihan Coding Python \n")


print ("Hello World")


print ("\n --- Batas --- \n")




print ("\n Sintaks dasar \n")


nama = "Jansen Rust"
umur = "25 tahun"
tinggi = "170 cm"
coding = "HTML, CSS, JavaScript dan Python"
warga = "Amerika Serikat"
asal = "Silicon Valley"


print ("Nama :", nama)
print ("Umur :", umur)
print ("Tinggi :", tinggi)
print ("Coding :", coding)
print ("Warga :", warga)
print ("Asal :", asal)


print ("\n --- Batas --- \n")




print ("\n Sintaks dasar 2 \n")


nama = "Habib Muzakki"
marga = "Piliang"
kelas = "12 Agama"
absen = 15
coding = "HTML, CSS, JavaScript dan Python"
sekolah = "MAN 2 KOTA SERANG"
tinggi = "170 cm"


print ("Nama :", nama)
print ("Marga :", marga)
print ("Kelas :", kelas)
print ("Absen :", absen)
print ("Coding :", coding)
print ("Sekolah :", sekolah)
print ("Tinggi badan :", tinggi)


print ("\n --- Batas --- \n")




print ("\n Tipe data dasar \n")


teks = "Tes aja"
angka = 34
desimal = 34.2
cek_1 = True
cek_2 = False
kosong = None


print ("Teks =", teks)
print ("Angka =", angka)
print ("Desimal =", desimal)
print ("Cek 1 =", cek_1)
print ("Cek 2 =", cek_2)
print ("Kosong =", kosong)


print ("\n --- Batas --- \n")




print ("\n Operator Dasar \n")


x = 25
y = 5


print ("Tambah =", x + y)
print ("Kurang =", x - y)
print ("Kali =", x * y)
print ("Bagi =", x / y)
print ("Pangkat =", x ** y)
print ("Modulus =", x % y)


print ("\n --- Batas --- \n")




print ("\n Operator Perbandingan \n")


print ("Hasil =", x > y)
print ("Hasil =", x < y)
print ("Hasil =", x >= y)
print ("Hasil =", x <= y)
print ("Hasil =", x == y)
print ("Hasil =", x != y)


print ("\n --- Batas --- \n")




print ("\n Operator Logika \n")


print ("Hasil =", x > y and x < y)
print ("Hasil =", x < y or x > y)
print ("Hasil =", not x)
print ("Hasil =", not y)


print ("\n --- Batas --- \n")




print ("\n Switch Case \n")


nilai = 95

match (nilai):
    
    case 95:
        print ("A")
        
    case 90:
        print ("B")
        
    case 80:
        print ("C")
        
    case 75:
        print ("D")
        
    case 70:
        print ("E")
        
    case 60:
        print ("F")
        
    case _:
        print ("Sama saja")
        
        
print ("\n --- Batas --- \n")




print ("\n Switch Case 2 \n")


kondisi = 2

match (kondisi):
    
    case 1:
        print ("Iya")
        
    case 2:
        print ("Tidak")
        
    case 3:
        print ("Kadang-kadang")
        
    case _:
        print ("Bukan dong")
        
        
print ("\n --- Batas --- \n")




print ("\n Percabangan Dasar \n")


a = 9

if a >= 5:
    print (f"Besar, nilai = {a}")
    
else:
    print (f"Kecil, nilai = {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan \n")


b = 3

if b >= 5:
    print (f"Besar, nilai = {b}")
    
elif b <= 5:
    print (f"Kecil, nilai = {b}")
    
else:
    print (f"Sama sekali, nilai {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Skor Sederhana \n")


c = 5 

if c >= 9:
    print (f"A, nilai = {c}")
    
elif c >= 8:
    print (f"B, nilai = {c}")
    
elif c >= 7:
    print (f"C, nilai = {c}")
    
elif c >= 6:
    print (f"D, nilai = {c}")
    
elif c >= 5:
    print (f"E, nilai = {c}")
    
elif c >= 4:
    print (f"F, nilai = {c}")
    
else:
    print (f"Sama saja, nilai = {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nilai Rapor Sederhana \n")


nilai = 95

if nilai >= 95:
    print (f"A, nilai = {nilai}")
    
elif nilai >= 90:
    print (f"B, nilai = {nilai}")
    
elif nilai >= 80:
    print (f"C, nilai = {nilai}")
    
elif nilai >= 70:
    print (f"D, nilai = {nilai}")
    
elif nilai >= 60:
    print (f"E, nilai = {nilai}")
    
elif nilai >= 50:
    print (f"F, nilai = {nilai}")
    
else:
    print (f"Sama saja, nilai = {nilai}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar \n")


for a in range (11):
    print (f"Urutan ke - {a}")
    
    
print ("\n --- Batas --- \n")




for b in range (11):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- Batas --- \n")




for c in range (11):
    print (f"Urutan ke - {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar \n")


a = 5

while a < 16:
    print (f"Urutan ke - {a}")
    a = a + 1
    
    
print ("\n --- Batas --- \n")




b = 10 

while b < 21:
    print (f"Urutan ke - {b}")
    b = b + 1
    
    
print ("\n --- Batas --- \n")




c = 6 

while c < 16:
    print (f"Urutan ke - {c}")
    c = c + 1
    
    
print ("\n --- Batas --- \n")




print ("\n Array \n")


data = [
    
    "1. Nangka",
    "2. Melon",
    "3. Semangka",
    "4. Buah Naga",
    "5. Pepaya",
    "6. Buah Anggur",
    
    ]
    
    
for a in data:
    print (a)
    
    
print ("\n --- Batas --- \n")




print ("\n Array 2 \n")


daftar = [
    
    "1. Rendang",
    "2. Nasi Padang",
    "3. Nasi Kapau",
    "4. Ayam Gulai",
    "5. Rendang Daging",
    "6. Sala lauak",
    
    ]
    
    
for b in daftar:
    print (b)
    
    
print ("\n --- Batas --- \n")




print ("\n Set \n")

data = {
    
    "1. Rusia",
    "2. Ukraina",
    "3. Belarus",
    "4. Belgia",
    "5. Belanda",
    "6. Estonia",
    "7. Lithuania",
    
}


print (data)


print ("\n --- Batas --- \n")




print ("\n Tuple \n")


data = (
    
    "1. Rusia",
    "2. Ukraina",
    "3. Belarus",
    "4. Belgia",
    "5. Belanda",
    "6. Estonia",
    "7. Lithuania",
    
    )
    
    
print (data)


print ("\n --- Batas --- \n")




print ("\n Dictionary \n")


profil = {
    
    "nama" : "Jansen Rust",
    "umur" : "25 tahun",
    "tinggi" : "170 cm",
    "coding" : "HTML, CSS, JavaScript, dan Python",
    "warga" : "Amerika Serikat",
    "asal" : "Silicon Valley",
    
}


print ("Nama :", profil ["nama"])

print ("Umur :", profil ["umur"])

print ("Tinggi :", profil ["tinggi"])

print ("Coding :", profil ["coding"])

print ("Asal :", profil ["asal"])


print ("\n --- Batas --- \n")




print ("\n Dictionary 2 \n")


profil = {
    
    "nama" : "Habib Muzakki",
    "marga" : "Piliang",
    "kelas" : "12 Agama",
    "absen" : 15,
    "coding" : "HTML, CSS, JavaScript, Python",
    "sekolah" : "MAN 2 KOTA SERANG",
    "tinggi" : "170 cm",
    
}


print ("Nama :", profil ["nama"])

print ("Marga :", profil ["marga"])

print ("Kelas :", profil ["kelas"])

print ("Absen :", profil ["absen"])

print ("Coding :", profil ["coding"])

print ("Sekolah :", profil ["sekolah"])

print ("Tinggi badan :", profil ["tinggi"])


print ("\n --- Batas --- \n")




print ("\n Fungsi dasar \n")


def dasar ():
    print ("Hello World")
    
dasar ()


print ("\n --- Batas --- \n")




print ("\n Fungsi dasar 1 \n")


def das ():
    print ("Hello Jansen")
    print ("Hello Van")
    print ("Hello Verb")
    print ("Hello Janson")
    
das ()


print ("\n --- Batas --- \n")




print ("\n Fungsi dasar 1 \n")


def hut ():
    print ("Hello Jan")
    
hut ()
hut ()
hut ()
hut ()


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Parameter 1 \n")


def ren (nama):
    print ("Halo " + nama + " dari Glodok, Jakbak")
    
ren ("Anton Djin Yan")
ren ("Reyvon Djan")
ren ("Ren Hard")
ren ("Ben Anderson")
ren ("Dart Bento Djin Zhan")


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan parameter 2 \n")


def rf (nama):
    print (f"Halo nama {nama}, dari Jakarta Timur dan Jatinegara")
    
rf ("E")
rf ("A")
rf ("R")
rf ("S")
rf ("V") 


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Parameter 3 spesial oshi member JKT48 \n") 


def oshi (nama):
    print (f"Halo {nama} cantik")
    
oshi ("Michie JKT48")
oshi ("Frizy JKT48")
oshi ("Anindya JKT48")
oshi ("Christy JKT48")
oshi ("Freya JKT48")
oshi ("Olla JKT48")
oshi ("Jessi JKT48")
oshi ("Fiony JKT48")
oshi ("Muthe JKT48")
oshi ("Marsha JKT48")
oshi ("Eli JKT48")
oshi ("Mikaela JKT48")


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan return \n")


def tambah (a, b):
    return a + b
    
hasil = tambah (10, 10)
print ("Tambah =", hasil)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan return 1 \n")


def der (nama):
    return "Halo " + nama + " Asal dari Jakarta"
    
hasil = der ("Johan")
print ("Hasil =", hasil)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan return 2 \n")


def dar (nama):
    return f"Halo semuanya, saya {nama}, dari Indonesia"
    
hasil = dar ("Hayyan")
print ("Hasil =", hasil)


print ("\n --- Batas --- \n")




print ("\n Error Handling \n")


try:
    hasil = 10 / 0
    print (hasil)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("100% Mantap")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 2 \n")


try:
    hasil = 30 / 0
    print (hasil)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("100% Mantap")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling \n")


try:
    hasil = 10 + 10 
    print ("Hasil =", hasil)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("100% Mantap")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 3 \n")


try:
    hasil = 20 + 20 
    print ("Hasil =", hasil)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("100% Mantap")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested  1 \n")

a = 9
cek = True

if cek:
    if a >= 5:
        print (f"Besar, nilai = {a}")
        
    elif a <= 5:
        print (f"Kecil, nilai = {a}")
        
else:
    print (f"Sama saja, nilai = {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 2 \n")


b = 3
cek = True

if cek:
    if b >= 5:
        print (f"Besar, nilai = {b}")
        
    else:
        print (f"Kecil, nilai = {b}")
        
else:
    print (f"Sama saja, nilai = {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested, Daftar masuk JKT48 \n")


usia = 19
cek = True

if cek:
    if usia >= 13 and usia <= 17:
        print (f"Sudah matang masuk JKT48, usia = {usia}")
        
    elif usia > 17:
        print (f"Sudah matang masuk JKT48, usia = {usia}")
        
    else:
        print (f"Belum boleh ya, {usia}")
        
else:
    print (f"Jangan dulu ya, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested , usia produktif manusia \n")


umur = 25
cek = True

if cek:
    if umur >= 15 and umur <= 64:
        print (f"Masuk usia produktif, umur = {umur}")
        
    elif umur > 64:
        print (f"Masuk lanjut usia, umur = {umur}")
        
    else:
        print (f"Bukan usia produktif, umur = {umur}")
        
else:
    print (f"Masih kecil usianya, umur = {umur}")
    
    
print ("\n --- Batas --- \n")




print ("\n For Nested \n")


for a in range (4):
    for b in range (4):
        print (f"Urutan ke - {a} dan Urutan ke - {b}")
        
        
print ("\n --- Batas --- \n")




print ("\n For Nested 1 \n")


for k in range (4):
    for j in range (4):
        print (f"Urutan ke - {k} dan Urutan ke - {j}")
        
        
print ("\n --- Batas --- \n")




print ("\n For Nested 2 \n")


for w in range (5):
    for s in range (5):
        print (f"Urutan ke - {w} dan Urutan ke - {s}")
        
        
print ("\n --- Batas --- \n")




print ("\n For Nested 3 \n")


for x in range (4):
    for y in range (4):
        for z in range (4):
            print (f"Urutan ke - {x}, Urutan ke - {y}, dan Urutan ke - {z}")
            
            
print ("\n --- Batas --- \n")




print ("\n For Nested 4 \n")


for j in range (5):
    for d in range (5):
        for f in range (5):
            print (f"Urutan ke - {j}, Urutan ke - {d} dan Urutan ke - {f}")
            
            
print ("\n --- Batas --- \n")
