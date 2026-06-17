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




print ("\n Array \n")

array = [
    
    "1. Michie",
    "2. Fritzy",
    "3. Anindya",
    "4. Christy",
    "5. Freya",
    
    ]
    

for a in array:
    print (a)
    

print ("\n --- Batas --- \n")




print ("\n Tuple \n")


tup = (
    
    "1. Michie",
    "2. Fritzy",
    "3. Anindya",
    "4. Christy",
    "5. Freya",
    
    )
    
    
for b in tup:
    print (b)
    
 
print ("\n --- Batas --- \n")




print ("\n Set \n")   


sef = {
    "1. Michie",
    "2. Fritzy",
    "3. Anindya",
    "4. Christy",
    "5. Freya",
}


for c in sef:
    print (c)
    
    
print ("\n --- Batas --- \n")




print ("\n Dictionary \n")


data = {
    "nama" : "John Doe",
    "kelas" : "Menengah",
    "asal" : "Amerika Serikat",
    "coding" : "HTML, CSS, JavaScript dan Python"
}


print ("Nama :", data ["nama"])

print ("Kelas :", data ["nama"])

print ("Asal :", data ["asal"])

print ("Coding :", data ["coding"])


print ("\n --- Batas --- \n")




print ("\n Switch Case \n")


hari = "Senin"

match (hari):
    
    case "Senin":
        print ("Senin")
        
    case "Selasa":
        print ("Selesa")
        
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
        print ("Yes")
        
    case 2:
        print ("Tidak")
        
    case 3:
        print ("Kadang-kadang")
        
    case _:
        print ("Semula")
        
        
print ("\n --- Batas --- \n")




print ("\n Percabangan Dasar \n")

a = 9

if a > 5:
    print (f"Besar, a = {a}")
    
else:
    print (f"Kecil, a = {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan \n")


b = 8

if b > 5:
    print (f"Besar, b = {b}")
    
elif b < 5:
    print (f"Kecil, b = {b}")
    
else:
    print (f"Sama saja, b = {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Ledder \n")


nilai = 100

if nilai >= 90:
    print (f"A, nilai = {nilai}")
    
elif nilai >= 80:
    print (f"B, nilai = {nilai}")
    
elif nilai >= 70:
    print (f"C, nilai = {nilai}")
    
elif nilai >= 60:
    print (f"D, nilai = {nilai}")
    
elif nilai >= 50:
    print (f"E, nilai = {nilai}")
    
elif nilai >= 40:
    print (f"F, nilai = {nilai}")
    
elif nilai >= 30:
    print (f"G, nilai = {nilai}")
    
else:
    print (f"Semula, nilai = {nilai}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 1 \n")


a = 9
cek = True

if cek:
    if a > 5:
        print (f"Besar, a = {a}")
        
    elif a < 5:
        print (f"Kecil, a = {a}")
        
else:
    print (f"Sama saja, a = {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 2 \n")


b = 4
cek = True

if cek:
    if b > 5:
        print (f"Besar, b = {b}")
        
    elif b < 5:
        print (f"Kecil, b = {b}")
        
else:
    print (f"Sama saja, b = {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 3 \n")


c = 10
cek = True

if cek:
    if c > 5:
        print (f"Besar, c = {c}")
        
    elif c < 5:
        print (f"Kecil, c = {c}")
        
else:
    print (f"Sama saja, c = {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 4 \n")


d = 3
cek = True

if cek:
    if d > 5:
        print (f"Besar, d = {d}")
        
    elif d < 5:
        print (f"Kecil, d = {d}")
        
else:
    print (f"Sama saja, d = {d}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 5 \n")


e = 10
cek = True

if cek:
    if e > 5:
        print (f"Besar, e = {e}")
        
    else:
        print (f"Kecil, e = {e}")
        
else:
    print (f"Sama saja, e = {e}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 6 \n")


f = 3
cek = True

if cek:
    if f > 5:
        print (f"Besar, f = {f}")
        
    else:
        print (f"Kecil, f = {f}")
        
else:
    print (f"Sama saja, f = {f}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 6 \n")


g = 10
cek = True

if cek:
    if g > 5:
        print (f"Besar, g = {g}")
        
    else:
        print (f"Kecil, g = {g}")
        
else:
    print (f"Sama saja, g = {g}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested, join ke JKT48 dan ikut audisi JKT48 \n")


usia = 19
cek = True

if cek:
    if usia >= 13 and usia <= 17:
        print (f"Bisa join JKT48 dan ikut audisi JKT48, usia = {usia}")
        
    elif usia > 17:
        print (f"Sudah lebih dari cukup, usia = {usia}")
        
    else:
        print (f"Masih dibawah umur, usia = {usia}")
        
else:
    print (f"Daftar di lain waktu, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested, usia produktif manusia \n")


usia = 19
cek = True

if cek:
    if usia >= 15 and usia <= 64:
        print (f"Sudah masuk usia produktif manusia, usia = {usia}")
        
    elif usia > 64:
        print (f"Sudah lanjut usia, usia = {usia}")
        
    else:
        print (f"Masih belum usia produktif, usia = {usia}")
        
else:
    print (f"Usianya masih kecil, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n For Dasar 1 \n")


for a in range (11):
    print (f"Urutan ke - {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n For Dasar 2 \n")


for b in range (11):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n For Dasar 3 \n")


for c in range (11):
    print (f"Urutan ke - {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n For Dasar 4 \n")


for d in range (11):
    print (f"Urutan ke - {d}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar 5 \n")


for e in range (11):
    print (f"Urutan ke - {e}")
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar 1 \n")


a = 5

while a < 16:
    print (f"Urutan ke - {a}")
    a = a + 1
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar 2 \n")


b = 10

while b < 20:
    print (f"Urutan ke - {b}")
    b = b + 1
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar 3 \n")


c = 20 

while c < 30:
    print (f"Urutan ke - {c}")
    c = c + 1
    
    
print ("\n --- Batas --- \n")





print ("\n While dasar 4 \n")


d = 10

while d < 25:
    print (f"Urutan ke - {d}")
    
    d = d + 1
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar 5 \n")


e = 10

while e < 25:
    print (f"Urutan ke - {e}")
    e = e + 1
    
    
print ("\n --- Batas --- \n")




print ("\n For Nested 1 \n")

for a in range (4):
    for b in range (4):
        for c in range (4):
            for d in range (4):
                for e in range (e):
                    print (f"Urutan ke - {a}, urutan ke - {b}, urutan ke - {c}, urutan ke - {d}, urutan ke - {e}")
                    
                    
print ("\n --- Batas --- \n")




print ("\n For Nested 2 \n")


for x in range (4):
    for y in range (4):
        for z in range (4):
            for t in range (4):
                for s in range (4):
                    print (f"Urutan ke - {x}, urutan ke - {y}, urutan ke - {z}, urutan ke - {t}, urutan ke - {s}")
                    
                    
print ("\n --- Batas --- \n")
