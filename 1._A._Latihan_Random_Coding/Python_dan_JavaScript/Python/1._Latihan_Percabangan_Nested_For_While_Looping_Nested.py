print ("\n Profil Habib Muzakki Piliang \n")


nama = "Habib Muzakki"
panggil = "Habib"
marga = "Piliang"
suku = "Minangkabau"
coding = "HTML, CSS, JavaScript dan Python"
lomba = "Finalis OSN-K Informatika tahun 2025"
alumni = "MAN 2 KOTA SERANG (tahun 2026)"
kelas = "12 Agama (tahun 2026)"
tinggi = "170 cm"
berat = "60 kg"
darah = "B"
fans = "JKT48"
oshi = "Michie, Gracie, Fritzy, Anindya, Christy, Freya, Fiony JKT48"


profil = f"""

- Nama lengkap   : {nama}
- Nama panggilan : {panggil}
- Marga          : {marga}
- Suku           : {suku}
- Coding         : {coding}
- Lomba          : {lomba}
- Alumni         : {alumni}
- Kelas          : {kelas}
- Tinggi badan   : {tinggi}
- Berat badan    : {berat}
- Golongan darah : {darah}
- Fans           : {fans}
- Oshi JKT48     : {oshi}

"""


print (profil)


print ("\n --- Batas --- \n")




print ("\n Tipe data pemrograman \n")


teks = "Halo Guys"
angka = 23
desimal = 45.2
cek = True
kosong = None
huruf = 'A'


ner = f"""

- Teks    = {teks}
- Angka   = {angka}
- Desimal = {desimal}
- Cek     = {cek}
- Kosong  = {kosong}
- Huruf   = {huruf}

"""

print (ner)


print ("\n --- Batas --- \n")




print ("\n Operator Dasar \n")


x = 10
y = 5


print ("Tambah =", x + y)
print ("Kurang =", x - y)
print ("Kali =", x * y)
print ("Pangkat =", x ** y)
print ("Bagi =", x / y)
print ("Modulus =", x % y)


print ("\n --- Batas --- \n")




print ("\n Operator Perbandingan \n")


print ("Hasil =", x > y)
print ("Hasil =", x < y)
print ("Hasil =", x == y)
print ("Hasil =", x != y)
print ("Hasil =", x >= y)
print ("Hasil =", x <= y)


print ("\n --- Batas --- \n")




print ("\n Operator Logika \n")


print ("Hasil =", x > y and x < y)
print ("Hasil =", x < y or x > y)
print ("Hasil =", not x)
print ("Hasil =", not y)


print ("\n --- Batas --- \n")




print ("\n List \n")


far = [
    
    "1. Perang Dunia 1",
    "2. Perang Dunia 2",
    "3. Front Timur WW2",
    "4. Front Barat WW2",
    "5. Front Timur WW1",
    "6. Front Barat WW1",
    
    
    ]
    
    
for a in far:
    print (a)


print ("\n --- Batas --- \n")




print ("\n Tuple \n")


der = (
    
    "1. Perang Dunia 1",
    "2. Perang Dunia 2",
    "3. Front Timur WW2",
    "4. Front Barat WW2",
    "5. Front Timur WW1",
    "6. Front Barat WW1",
    
    
    )
    
    
for b in der:
    print (b)
    
    
print ("\n --- Batas --- \n")




print ("\n Set \n")


fer = {
    "1. Perang Dunia 1",
    "2. Perang Dunia 2",
    "3. Front Timur WW2",
    "4. Front Barat WW2",
    "5. Front Timur WW1",
    "6. Front Barat WW1",
}


for c in fer:
    print (c)
    
    
print ("\n --- Batas --- \n")




print ("\n Dictionary \n")


profil = {
    "nama" : "John Sam",
    "asal" : "Amerika Serikat",
    "kerja" : "Software Engineer",
    "usia" : "25 tahun",
    "coding" : "HTML, CSS, JavaScript dan Python",
}


print ("Nama :", profil ["nama"])

print ("Asal :", profil ["asal"])

print ("Kerja :", profil ["kerja"])

print ("Usia :", profil ["usia"])

print ("Coding :", profil ["coding"])


print ("\n --- Batas --- \n")




print ("\n Switch Case \n")


hari = "Senin"

match (hari):
    
    case "Senin":
        print ("Senin")
        
    case "Selasa":
        print ("Selasa")
        
    case "Rabu":
        print ("Rabu")
        
    case "Kamis":
        print ("Kamis")
        
    case "Jumat":
        print ("Jumat")
        
    case _:
        print ("Libur")
        
        
print ("\n --- Batas --- \n")




print ("\n Switch Case 1 \n")


kondisi = 2 

match (kondisi):
    
    case 1:
        print ("Aman")
        
    case 2:
        print ("Baik")
        
    case 3:
        print ("Senang")
        
    case 4:
        print ("Bahagia")
        
    case 5:
        print ("Oke")
        
    case _:
        print ("Biasa aja")
        
        
print ("\n --- Batas --- \n")




print ("\n Percabangan dasar \n")


a = 9

if a > 5:
    print (f"Besar, a = {a}")
    
else:
    print (f"Kecil, a = {a}")


print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan \n")


k = 3

if k > 5:
    print (f"Besar, k = {k}")
    
elif k < 5:
    print (f"Kecil, k = {k}")

else:
    print (f"Sama saja, k = {k}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Ledder \n")

s = 7

if s >= 9:
    print (f"A, skor = {s}")
    
elif s >= 8:
    print (f"B, skor = {s}")
    
elif s >= 7:
    print (f"C, skor = {s}")
    
elif s >= 6:
    print (f"D, skor = {s}")
    
elif s >= 5:
    print (f"E, skor = {s}")
    
else:
    print (f"Jelek, skor = {s}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 1 \n")


f = 9
cek = True


if cek:
    if f > 5:
        print (f"Besar, f = {f}")
        
    elif f < 5:
        print (f"Kecil, f = {f}")
        
else:
    print (f"Sama saja, f = {f}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 2 \n")


d = 3
cek = True

if cek:
    if d > 5:
        print (f"Besar, d = {d}")
        
    else:
        print (f"Kecil, d = {d}")
        
else:
    print (f"Sama saja, d = {d}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested, usia produktif 1 \n")


usia = 19
cek = True

if cek:
    if usia >= 15 and usia <= 64:
        print (f"Sudah masuk usia produktif, usia = {usia}")
        
    elif usia > 64:
        print (f"Sudah lanjut usia, usia = {usia}")
        
    else:
        print (f"Belum masuk usia produktif, usia = {usia}")
        
else:
    print (f"Masih kecil usianya, usia = {usia}")
    
    
print ("\n --- Batas --- \n")
    
    
    
    
print ("\n Percabangan Nested, usia produktif manusia 2 \n")


usia = 13
cek = True

if cek:
    if usia >= 15 and usia <= 64:
        print (f"Sudah masuk usia produktif, usia = {usia}")
        
    elif usia > 64:
        print (f"Sudah lanjut usia, usia = {usia}")
        
    else:
        print (f"Belum masuk usia produktif, usia = {usia}")
        
else:
    print (f"Masih kecil usianya, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested, masuk dan join jadi member JKT48 (1) \n")


usia = 19
cek = True

if cek:
    if usia >= 13 and usia <= 17:
        print (f"Boleh daftar JKT48, usia = {usia}")
        
    elif usia > 17:
        print (f"Sudah lebih dari cukup, usia = {usia}")
        
    else:
        print (f"Belum cukup umur untuk daftar, usia = {usia}")
        
else:
    print (f"Di lain waktu daftarnya, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested, Percabangan Nested, masuk dan join jadi member JKT48 (2) \n")


usia = 10
cek = True

if cek:
    if usia >= 13 and usia <= 17:
        print (f"Boleh daftar JKT48, usia = {usia}")
        
    elif usia > 17:
        print (f"udah lebih dari cukup, usia = {usia}")
        
    else:
        print (f"Sudah lebih dari cukup, usia = {usia}")
        
else:
    print (f"Belum cukup umur untuk daftar, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar \n")


for a in range (11):
    print (f"Urutan ke - {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar 2 \n")


for b in range (21):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar 3 \n")


for c in range (26):
    print (f"Urutan ke - {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar 1 \n")


a = 5

while a < 21:
    print (f"Urutan ke - {a}")
    a = a + 1
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar 2 \n")


b = 15 

while b < 31:
    print (f"Urutan ke - {b}")
    b = b + 1
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar 3 \n")


c = 10

while c < 21:
    print (f"Urutan ke - {c}")
    c = c + 1
    
    
print ("\n --- Batas --- \n")




print ("\n For Nested 1 \n")


for a in range (5):
    for b in range (5):
        for c in range (5):
            print (f"Urutan ke - {a}, urutan ke - {b}, urutan ke - {c}")
            
            
print ("\n --- Batas --- \n")




print ("\n For Nested 2 \n")


for x in range (6):
    for y in range (6):
        for z in range (6):
            print (f"Urutan ke - {x}, urutan ke - {y}, urutan ke - {z}")
            
            
print ("\n --- Batas --- \n")




print ("\n For Nested 3 \n")


for t in range (7):
    for j in range (7):
        for h in range (7):
            print (f"Urutan ke - {t}, urutan ke - {j}, urutan ke - {h}")
            
            
print ("\n --- Batas --- \n")




print ("\n Fungsi dasar \n")


def dasar ():
    print ("Hello Tes")


dasar ()


print ("\n --- Batas --- \n")




print ("\n Fungsi dasar 1 \n")

 
def nos ():
    print ("Hello Tes 1")
    print ("Hello Jan")
    print ("Hello Jer")
    print ("Ser Don")


nos ()


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Parameter \n")


def der (nama):
    print (f"Halo saya {nama} dari Karawang")

der ("Hanif")
der ("Hayyan")
der ("Roy")
der ("For")
der ("Fer")
der ("Iyan")


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan parameter 1 \n")


def fer (nama):
    print (f"Halo aku {nama} dari Jakarta")

fer ("Johan")
fer ("Royan")
fer ("Notch")
fer ("Arthur")
fer ("Mobile")
fer ("Nuron")
fer ("Ring")


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Return \n")


def tambah (x, y):
    return x + y

hasil = tambah (10, 8)
print ("Tambah =", hasil)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Return 1 \n")


def ron (nama):
    return f"Halo saya {nama} dari Jakarta Pusat"

hasil = ron ("Habib")
print (hasil)


print ("\n --- Batas --- \n")




print ("\n Error Handling 1 \n")


try:
    hasil = 10 / 0
    print (hasil)
    
except ZeroDivisionError:
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
    
except ZeroDivisionError:
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
    
except ZeroDivisionError:
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
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("Oke")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")
