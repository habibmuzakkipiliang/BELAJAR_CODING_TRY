print ("\n Bikin Hello World \n")


print ("Hello World")


print ("\n --- batas --- \n")




print ("\n Variabel dasar \n")

nama = "Habib"
print (nama)


angka = 12
print (angka)


desimal = 3.19
print (desimal)


print ("\n --- batas --- \n")




print ("\n Tipe data pemrograman \n")

teks = "Ini contoh aja"
angka = 12
desimal = 3.19
cek = True
kosong = None

tipe = f"""
- Teks    : {teks}
- Angka   : {angka}
- Desimal : {desimal}
- Cek     : {cek}
- Kosong  : {kosong}
"""


print (tipe)


print ("\n --- batas --- \n")




print ("\n Profil Habib Muzakki \n")

nama = "Habib Muzakki"
akrab = "Habib"
marga = "Piliang"
asal = "Kota Serang, Banten"
kuliah = "Universitas Harkat Negeri Tegal"
jurusan = "D4 Vokasi Teknik Informatika"
alumni = "MAN 2 KOTA SERANG (KELAS AGAMA) tahun 2026 ini"
coding = "HTML, CSS, JavaScript dan Python"
lomba = "Finalis OSN-K Informatika 2025"


profil = f"""
- Nama lengkap   : {nama}
- Nama panggilan : {akrab}
- Marga          : {marga}
- Asal           : {asal}
- Jurusan        : {jurusan}
- Alumni         : {alumni}
- Coding         : {coding}
- Lomba          : {lomba}
"""

print (profil)


print ("\n --- batas --- \n")




print ("\n Dictionary (Meme) \n")

data = {
    "nama" : "Erling Haaland",
    "asal" : "Norwegia",
    "kerja" : "Programmer",
    "coding" : "HTML, CSS, JavaScript dan Python"
}

print ("Nama :", data ["nama"])

print ("Asal :", data ["asal"])

print ("Kerja :", data ["kerja"])

print ("Coding :", data ["coding"])


print ("\n --- batas --- \n")




print ("\n List \n")

dar = [
    
    "1. Android 17",
    "2. Android 16",
    "3. Android 15",
    "4. Android 14",
    "5. Android 13",
    
    ]
    
    
for a in dar:
    print (a)
    
    
print ("\n --- batas --- \n")




print ("\n Tuple \n")

der = (
    
    "1. Android 17",
    "2. Android 16",
    "3. Android 15",
    "4. Android 14",
    "5. Android 13",
    
    )
    
for b in der:
    print (b)
    
    
print ("\n --- batas --- \n")




print ("\n Set \n")

wer = {
    "1. Android 17",
    "2. Android 16",
    "3. Android 15",
    "4. Android 14",
    "5. Android 13",
}
    
    
for c in wer:
    print (c)
    
    
print ("\n --- batas --- \n")




print ("\n Kalkulator dasar dalam Fungsi \n")


def tambah (x, y):
    return x + y
    
    
def kurang (e, r):
    return e - r
    
    
def kali (s, t):
    return s * t
    
    
def pangkat (s, d):
    return s ** d
    
    
def bagi (d, f):
    return d / f
    
    
def modulus (e, k):
    return e % k
    
    
hasil_1 = tambah (10, 10)
hasil_2 = kurang (10, 5)
hasil_3 = kali (10, 10)
hasil_4 = pangkat (10, 3)
hasil_5 = bagi (10, 5)
hasil_6 = modulus (10, 5)


hitung = f"""
- Tambah  = {hasil_1}
- Kurang  = {hasil_2}
- Kali    = {hasil_3}
- Pangkat = {hasil_4}
- Bagi    = {hasil_5}
- Modulus = {hasil_6}
"""

print (hitung)


print ("\n --- batas --- \n")




print ("\n Operator Perbandingan \n")

x = 15
y = 10

banding = f"""
- Hasil = {x > y}
- Hasil = {x < y}
- Hasil = {x >= y}
- Hasil = {x <= y}
- Hasil = {x == y}
- Hasil = {x != y}
"""


print (banding)


print ("\n --- batas --- \n")




print ("\n Operator Logika \n")

logic = f"""
- Hasil = {x > y and x < y}
- Hasil = {x < y or x > y}
- Hasil = {not (x > y)}
- Hasil = {not (x < y)}
"""

print (logic)


print ("\n --- batas --- \n")




print ("\n Fungsi + Switch Case dengan Int \n")

def lan (f):
    
    match (f):
        
        case 1:
            print ("Angka 1")
            
        case 2:
            print ("Angka 2 ")
            
        case 3:
            print ("Angka 3")
            
        case 4:
            print ("Angka 4")
            
        case 5:
            print ("Angka 5")
        
        case _:
            print ("Angka lain")
            
lan (1)
lan (2)
lan (3)
lan (4)
lan (5)
lan (6)


print ("\n --- batas --- \n")




print ("\n Fungsi + Switch Case dengan String \n")

def stan (n):
    
    match (n):
        
        case "Merah":
            print ("Merah")
            
        case "Kuning":
            print ("Kuning")
            
        case "Hijau":
            print ("Hijau")
            
        case _:
            print ("Warna lain")
            
stan ("Merah")
stan ("Kuning")
stan ("Hijau")
stan ("Hitam")


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan dasar \n")

def kot (e):
    
    if e >= 5:
        print (f"Besar, angka e = {e}")
        
    else:
        print (f"Kecil, angka e = {e}")
        
kot (10)
kot (9)
kot (7)
kot (6)
kot (5)
kot (4)
kot (3)
kot (2)
kot (1)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Lanjutan \n")

def dej (u):
    
    if u >= 8:
        print (f"Besar, angka u = {u}")
        
    elif u >= 5:
        print (f"Tengah, angka u = {u}")
        
    else:
        print (f"Kecil, angka u = {u}")

dej (10)
dej (9)
dej (8)
dej (7)
dej (6)
dej (5)
dej (4)
dej (3)
dej (2)
dej (1)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan Nilai Rapor \n")

def skor (t):
    
    if t >= 95:
        print (f"A, nilai = {t}")
        
    elif t >= 90:
        print (f"B, nilai = {t}")
        
    elif t >= 80:
        print (f"C, nilai = {t}")
        
    elif t >= 70:
        print (f"D, nilai = {t}")
        
    elif t >= 60:
        print (f"E, nilai = {t}")
        
    elif t >= 50:
        print (f"F, nilai = {t}")
        
    else:
        print (f"Jelek banget, nilai = {t}")

skor (100)
skor (90)
skor (80)
skor (70)
skor (60)
skor (50)
skor (40)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Nested 1 \n")

def run (e):
    
    cek = True
    
    if e >= 5:
        if cek:
            print (f"Besar, angka e = {e}")
            
    else:
        print (f"Kecil, angka e = {e}")
        
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




print ("\n For dasar 1 \n")

for a in range (10):
    print (f"Urutan ke - {a}")
    
    
print ("\n --- batas --- \n")




print ("\n For dasar 2 \n")


for b in range (1, 11):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- batas --- \n")




print ("\n While dasar \n")

a = 1

while a < 11:
    print (f"Urutan ke - {a}")
    a = a + 1
    
    
print ("\n --- batas --- \n")




print ("\n While dasar 2 \n")

b = 10 

while b > 0:
    print (f"Urutan ke - {b}")
    b = b - 1
    
    
print ("\n --- batas --- \n")




print ("\n For Nested 1 \n")

for w in range (1, 3):
    for r in range (1, 3):
        print (f"Luar : {w} dan Dalam : {r}")
        
        
print ("\n --- batas --- \n")




print ("\n For Nested 2 \n")

for x in range (1, 3):
    for y in range (1, 3):
        for z in range (1, 3):
            print (f"x : {x}, y : {y}, z : {z}")
            
            
print ("\n --- batas --- \n")




print ("\n Error Handling 1 \n")

try:
    a = 10 / 0
    print (a)
    
except:
    print ("Gagal")
    
else:
    print ("Oke dong")

finally:
    print ("Selesai")
    
    
print ("\n --- batas --- \n")




print ("\n Error Handling 2 \n")

try:
    b = 10 + 10
    print (b)
    
except:
    print ("Gagal")
    
else:
    print ("Oke dong")
    
finally:
    print ("Selesai")
    
    
print ("\n --- batas --- \n")




print ("\n Fungsi dengan Error Handling Raise 1 \n")

def ron (e):
    
    try:
        if e < 0:
            raise ("Minus")
        
        if e >= 8:
            print (f"Besar, angka e = {e}")
            
        elif e >= 5:
            print (f"Tengah, angka e = {e}")
            
        else:
            print (f"Kecil, angka e = {e}")
            
    except:
        print (f"Gak boleh minus, angka e = {e}")
        
        
ron (-10)
ron (-11)
ron (-4)
ron (-3)
ron (10)
ron (8)
ron (5)
ron (2) 
ron (3)
ron (1)


print ("\n --- batas --- \n")
