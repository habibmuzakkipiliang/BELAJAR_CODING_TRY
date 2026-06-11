# Latihan Demo Python

print ("\n Bikin Hello World \n")


print ("Hello World")


print ("\n --- Batas --- \n")




print ("\n Variabel dasar \n")


nama = "Habib Muzakki"
print (nama)


angka = 23
print (angka)


desimal = 23.1
print (desimal)


char = 'A'
print (char)


cek = True
print (cek)


kosong = None
print (kosong)


print ("\n --- Batas --- \n")




print ("\n Habib Muzakki Piliang \n")


nama = "Habib Muzakki"
panggil = "Habib"
marga = "Piliang"
asal = "Kota Bukittinggi"
tinggal = "Kota Serang"
suku = "Minangkabau"
coding = "HTML, CSS, JavaScript dan Python"
lomba = "Finalis OSN-K Informatika tahun 2025"
alumni = "MAN 2 KOTA SERANG (tahun 2026)"
kelas = "12 Agama (tahun 2026)"
tinggi = "170 cm"
berat = "60 kg"
darah = "B"
fans = "JKT48"
oshi = "Michie, Gracie, Fritzy, Lily, Anindya, Christy, Freya JKT48"


profil = f"""

- Nama lengkap    : {nama}
- Nama panggilan  : {panggil}
- Marga           : {marga}
- Asal daerah     : {asal}
- Tempat tinggal  : {tinggal}
- Suku            : {suku}
- Coding          : {coding}
- Lomba           : {lomba}
- Alumni          : {alumni}
- Kelas           : {kelas}
- Tinggi badan    : {tinggi}
- Berat badan     : {berat}
- Golongan darah  : {darah}
- Fans            : {fans}
- Oshi JKT48      : {oshi}

"""

print (profil)


print ("\n --- Batas --- \n")




print ("\n Tipe data pemrograman \n")


teks = "Halo Dunia"
angka = 22
desimal = 23.22
cek = True
char = 'A'
kosong = None


tipe = f"""

- Teks    = {teks}
- Angka   = {angka}
- Desimal = {desimal}
- Cek     = {cek}
- Char    = {char}
- Kosong  = {kosong}


"""


print (tipe)


print ("\n --- Batas --- \n")




print ("\n Operator dasar \n")


x = 10 
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




print ("\n Array \n")


perang = [
    
    "1. Front Timur WW1",
    "2. Front Barar WW1",
    "3. Front Timur WW2",
    "4. Front Barat WW2",
    "5. Front Afrika WW2",
    "6. Perang Pasifik WW2",
    "7. Perang Dunia 2",
    "8. Perang Dunia 1",
    
    ]
    
    
for a in perang:
    print (a)


print ("\n --- Batas --- \n")




print ("\n Set \n")


perang_man = {
    
    "1. Front Timur WW1",
    "2. Front Barar WW1",
    "3. Front Timur WW2",
    "4. Front Barat WW2",
    "5. Front Afrika WW2",
    "6. Perang Pasifik WW2",
    "7. Perang Dunia 2",
    "8. Perang Dunia 1",
    
}

for b in perang_man:
    print (b)
    
    
print ("\n --- Batas --- \n")




print ("\n Tuple \n")


perang_dun = (
    
    "1. Front Timur WW1",
    "2. Front Barar WW1",
    "3. Front Timur WW2",
    "4. Front Barat WW2",
    "5. Front Afrika WW2",
    "6. Perang Pasifik WW2",
    "7. Perang Dunia 2",
    "8. Perang Dunia 1",
    
    )
    
    
for c in perang_dun:
    print (c)


print ("\n --- Batas --- \n")




print ("\n Dictionary \n")


biodata = {
    "nama" : "Harold Paul von Hindenburg",
    "asal" : "Jerman",
    "kerja" : "Programmer",
    "usia" : "25 tahun",
    "tinggi" : "175 cm",
    "berat" : "60 kg",
    "coding" : "HTML, CSS, JavaScript, Python, C++, Rust dan Go",
    "fans" : "AKB48, JKT48, K-Pop",
    "oshi" : "Michie JKT48, Lily JKT48, Fritzy JKT48, Yui Oguri AKB48",
}

print ("Nama :", biodata ["nama"])

print ("Asal :", biodata ["asal"])

print ("Kerja :", biodata ["kerja"])

print ("Tinggi badan :", biodata ["tinggi"])

print ("Berat badan :", biodata ["berat"])

print ("Coding :", biodata ["coding"])

print ("Fans :", biodata ["fans"])

print ("Oshi :", biodata ["oshi"])


print ("\n --- Batas --- \n")




print ("\n Switch Case \n")


kondisi = 3

match (kondisi):
    
    case 1:
        print ("1")
        
    case 2:
        print ("2")
        
    case 3:
        print ("3")
        
    case 4:
        print ("4")
        
    case 5:
        print ("5")
        
    case _:
        print ("Semula")


print ("\n --- Batas --- \n")




print ("\n Switch Case 1\n")


hari = "Jumat"

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




print ("\n Percabangan Dasar \n")


a = 9

if a > 5:
    print (f"Besar, a = {a}")
    
else:
    print (f"Kecil, a = {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Dasar 2 \n")


b = 3 

if b > 5:
    print (f"Besar, b = {b}")
    
else:
    print (f"Kecil, b = {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan 1 \n")


c = 9

if c > 5:
    print (f"Besar, c = {c}")
    
elif c < 5:
    print (f"Kecil, c = {c}")
    
else:
    print (f"Sama saja, c = {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan 2 \n")


d = 3

if d > 5:
    print (f"Besar, d = {d}")
    
elif d < 5:
    print (f"Kecil, d = {d}")
    
else:
    print (f"Sama saja, d = {d}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Ledder \n")


rapor = 90

if rapor >= 95:
    print (f"A, nilai = {rapor}")
    
elif rapor >= 90:
    print (f"B, nilai = {rapor}")
    
elif rapor >= 80:
    print (f"C, nilai = {rapor}")
    
elif rapor >= 70:
    print (f"D, nilai = {rapor}")
    
elif rapor >= 60:
    print (f"E, nilai = {rapor}")
    
elif rapor >= 50:
    print (f"F, nilai = {rapor}")
    
else:
    print (f"Jelek banget, nilai = {rapor}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 1 \n")


g = 10
cek = True

if cek:
    if g > 5:
        print (f"Besar, g = {g}")
        
    elif g < 5:
        print (f"Kecil, g = {g}")
        
else:
    print (f"Sama saja, g = {g}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 2 \n")


e = 3
cek = True

if cek:
    if e > 5:
        print (f"Besar, e = {e}")
    
    else:
        print (f"Kecil, e = {e}")
        
else:
    print (f"Sama saja, e = {e}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested , usia produktif \n")


usia = 19
cek = True

if cek:
    if usia >= 15 and usia <= 64:
        print (f"Masuk usia produktif, usia = {usia}")
        
    elif usia > 64:
        print (f"Sudah tua usianya, usia = {usia}")
        
    else:
        print (f"Belum masuk usia produktif, usia = {usia}")
        
else:
    print (f"Masih balita, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested, usia join JKT48 \n")


usia = 19
cek = True

if cek:
    if usia >= 13 and usia <= 18:
        print (f"Sudah boleh join JKT48, usia = {usia}")
        
    elif usia > 18:
        print (f"Sudah lebih dari cukup, usia = {usia}")
        
    else:
        print (f"Belum boleh masuk JKT48, usia = {usia}")
        
else:
    print (f"Di lain waktu daftarnya, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested, tinggi badan standar Cowok \n")


tinggi = 170
cek = True

if cek:
    if tinggi >= 163 and tinggi <= 168:
        print (f"Standar tinggi cowok, tinggi = {tinggi}")
        
    elif tinggi > 168:
        print (f"Ideal tinggi cowok, tinggi = {tinggi}")
        
    else:
        print (f"Masih pendek, tinggi = {tinggi}")
        
else:
    print (f"Belum tinggi, tinggi = {tinggi}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested, berat badan standar cowok \n")


berat = 60
cek = True

if cek:
    if berat >= 55 and berat <= 65:
        print (f"Berat badan ideal, berat = {berat}")
        
    elif berat > 65:
        print (f"Obesitas, berat = {berat}")
        
    else:
        print (f"Kurus, berat = {berat}")
        
else:
    print (f"Perlu asupan yang memadai dan bergizi, berat = {berat}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar \n")


for a in range (10):
    print (f"Urutan ke - {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar 1 \n")


for b in range (2, 20):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar 2 \n")


for c in range (15, 30):
    print (f"Urutan ke - {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar 3 \n")


for d in range (10, 30):
    print (f"Urutan ke - {d}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar 5 \n")


for e in range (20, 30):
    print (f",Urutan ke - {e}")
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar 1 \n")


a = 10

while a < 20:
    print (f"Urutan ke - {a}")
    a = a + 1
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar 2 \n")


b = 5

while b < 30:
    print (f"Urutan ke - {b}")
    b = b + 1
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar 3 \n")


c = 15

while c < 30:
    print (f"Urutan ke - {c}")
    c = c + 1
    
    
print ("\n --- Batas --- \n")




print ("\n For Nested 1 \n")


for a in range (6):
    for b in range (6):
        print (f"Bagian luar a : {a}, Bagian dalam b : {b}")
        
        
print ("\n --- Batas --- \n")




print ("\n For Nested 2 \n")


for x in range (6):
    for y in range (6):
        print (f"Bagian luar x : {x}, Bagian dalam y : {y}")
        
        
print ("\n --- Batas --- \n")




print ("\n For Nested 3 \n")


for d in range (6):
    for e in range (6):
        print (f"Bagian luar d : {d}, Bagian dalam e : {e}")
        
        
print ("\n --- Batas --- \n")




print ("\n Iterasi For Continue \n")


for w in range (20):
    if w == 10:
        continue
    print (f"Urutan ke - {w}")
    
    
print ("\n --- Batas --- \n")




print ("\n Iterasi For Break \n")


for h in range (20):
    if h == 15:
        break
    print (f"Urutan ke - {h}")
    
    
print ("\n --- Batas --- \n")




print ("\n Array Iterasi For Continue \n")


tank = [
    
    "1. Tiger I",
    "2. Panther I",
    "3. Panther IV",
    "4. Panther III",
    "5. M4 Sherman",
    "6. M3 Stuart",
    "7. Leopard I",
    "8. Leopard II",
    "9. T34",
    "10. T55",
    
    ]
    
    
for e in tank:
    if e == "M4 Sherman":
        continue
    print (e)
    

print ("\n --- Batas --- \n")




print ("\n Array Iterasi For Break \n")


number = [
    
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    
    ]


for k in number:
    if k == 5:
        break
    print (k)
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 1 \n")


try:
    hasil = 10 / 0
    print (hasil)
    
except ZeroDivisionError:
    print ("Gagal")

else:
    print ("Mantap")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 2 \n")


try:
    hasil = 20 / k
    print (hasil)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("Mantap")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 3 \n")

try:
    hasil = 20 + 20
    print (hasil)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("Mantap")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Fungsi dasar 1\n")


def dasar ():
    print ("Hello World")
    
dasar ()


print ("\n --- Batas --- \n")




print ("\n Fungsi dasar 2 \n")


def eron ():
    print ("Hello Dun")
    print ("Hello Def")
    print ("Hello JKT48")
    print ("Hello Michie JKT48")
    print ("Hello Gracie JKT48")
    print ("Hello Fritzy JKT48")
    print ("Hello Lily JKT48")
    
eron ()


print ("\n --- Batas --- \n")




print ("\n Fungsi dasar dengan parameter \n")


def far (nama):
    print (f"Saya {nama}, dari Jakarta")
    
far ("Hayyan")
far ("Fayyan")
far ("Rayyan")
far ("Rust")
far ("Rush")


print ("\n --- Batas --- \n")




print ("\n Fungsi dasar dengan Return 1 \n")


def tambah (a, b):
    return a + b
    
hasil = tambah (10, 10)
print ("Tambah =", hasil)


print ("\n --- Batas --- \n")




print ("\n Fungsi dasar dengan return 2 \n")


def fin (nama):
    return f"Halo {nama}, dari Jakarta Barat"
    
hasil = fin ("Habib")
print (hasil)


print ("\n --- Batas --- \n")




print ("\n Fungsi Error Handling \n")

def cek_angka (a):
    try:
        if a < 0:
            raise ("Angka minus")
            print (f"Angka salah, angka = {a}")
            
        else:
            print (f"Angka benar, angka = {a}")
            
    except:
        print (f"Gak boleh minus, angka = {a}")
        
        
cek_angka (-10)


print ("\n --- Batas --- \n")




print ("\n Fungsi Error Handling \n")


def dasar (b):
    try:
        if b < 0:
            raise ("Minus")
            print (f"Angka salah, angka = {b}")
            
        else:
            print (f"Angka benar, angka = {b}")
            
    except:
        print (f"Gak boleh minus, angka = {b}")
        
dasar (10)


print ("\n --- Batas --- \n")
