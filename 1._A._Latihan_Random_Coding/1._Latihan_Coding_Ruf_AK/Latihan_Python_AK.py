# Latihan Python AK

print ("Hello World")


print ("\n --- Batas --- \n")




print ("\n Variabel Dasar dan Tipe data pemrograman \n")

nama = "Habib Muzakki"
panggil = "Habib"
oshi = "Michie dan Gracie JKT48"
angka = 12
desimal = 23.12
cek = True
cek_1 = False
kosong = None
daftar = [
    
    "1. Stuka",
    "2. Hellcat",
    "3. Mustang",
    "4. Corsair",
    "5. ME 262",
    "6. Ilyushin",
    "7. Tupolev",
    
    ]
    
 
print ("\n --- Batas --- \n") 
   
    
    


detail = f"""
- Nama    : {nama}
- Panggil : {panggil}
- Oshi    : {oshi}
- Angka   : {angka}
- Desimal : {desimal}
- Cek     : {cek}
- Cek 1   : {cek_1}
- Kosong  : {kosong}
- Daftar  : 
"""

print (detail)



# Tambah Elemen

daftar.append ("8. T34")
daftar.append ("9. T55")
daftar.append ("10. Stuart")
daftar.append ("11. Sherman")
daftar.append ("12. Hurricane")
daftar.append ("13. Spitfire")
daftar.append ("14. WW2")
daftar.append ("15. WW1")
daftar.append ("16. Teater Pasifik WW2")



# Hapus Elemen

daftar.remove ("14. WW2")
daftar.remove ("15. WW1")
daftar.remove ("16. Teater Pasifik WW2")



for a in daftar:
    print (a)
    
    
print ("\n --- Batas --- \n")




print ("\n Dictionary \n")

bio = {
    "tinggi" : 170,
    "berat" : 60,
    "cek" : True,
    "kosong" : None,
    "teks" : "Halo Michie dan Gracie JKT48",
    "desimal" : 23.23,
} 

print ("Tinggi :", bio ["tinggi"])
print ("Berat :", bio ["berat"])
print ("Cek :", bio ["cek"])
print ("Kosong :", bio ["kosong"])
print ("Teks :", bio ["teks"])
print ("Desimal :", bio ["desimal"])


print ("\n --- Batas --- \n")




print ("\n Profil Habib Muzakki \n")

nama = "Habib Muzakki"
panggil = "Habib"
asal = "Padang"
tinggal = "Kota Serang"
usia = "19 tahun"
tinggi = "170 cm"
berat = "60 kg"
angka = 100
desimal = 12.12
cek_3 = True


profil = f"""
- Nama lengkap   : {nama}
- Nama panggilan : {panggil}
- Asal           : {asal}
- Tempat tinggal : {tinggal}
- Tinggi badan   : {tinggi}
- Berat badan    : {berat}
- Angka          : {angka}
- Desimal        : {desimal}
- Cek 3          : {cek_3}
"""


print (profil)


print ("\n --- Batas --- \n")




print ("\n Fungsi return dengan kalkulator dasar \n")

def tambah (a, b):
    return a + b
    
    
def kurang (x, y):
    return x - y
    
    
def kali (s, d):
    return s * d
    
    
def bagi (r, t):
    return r / t
    
    
def pangkat (t, r):
    return t ** r
    
    
def modulus (j, q):
    return j % q



hasil_1 = tambah (10, 10)
hasil_2 = kurang (15, 5)
hasil_3 = kali (10, 10)
hasil_4 = bagi (20, 5)
hasil_5 = pangkat (20, 2)
hasil_6 = modulus (10, 5)



print ("Tambah =" ,hasil_1)
print ("Kurang =" ,hasil_2)
print ("Kali =" ,hasil_3)
print ("Bagi =" ,hasil_4)
print ("Pangkat =" ,hasil_5)
print ("Modulus =" ,hasil_6)


print ("\n --- Batas --- \n")




print ("\n Operator Perbandingan dan logika \n")

x = 10
y = 6

banding = f"""
Hasil : {x > y}
Hasil : {x < y}
Hasil : {x >= y}
Hasil : {x <= y}
Hasil : {x == y}
Hasil : {x != y}


----------------


Hasil : {x > y and x < y}
Hasil : {x < y or x > y}
Hasil : {not x > y}
Hasil : {not x < y}
Hasil : {not x}
Hasil : {not y}
"""


print (banding)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan percabangan dasar \n")

def dasar (a):
    
    if a >= 5:
        print (f"Besar, angka a = {a}")
        
    else:
        print (f"Kecil, angka a = {a}")
        
dasar (10)
dasar (3)
dasar (7)
dasar (5)
dasar (8)


print ("\n --- Batas --- \n")





print ("\n Fungsi dengan Percabangan dasar 2 \n")

def er (b):
    
    if b >= 5:
        print (f"Besar, angka b = {b}")
        
    else:
        print (f"Kecil, angka b = {b}")
        
er (10)
er (7)
er (5)
er (3)
er (6)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Lanjutan \n")

def rt (c):
    
    if c >= 8:
        print (f"Besar, angka c = {c}")
        
    elif c >= 5:
        print (f"Setengah, angka c = {c}")
        
    else:
        print (f"Kecil, angka c = {c}")
        
rt (10)
rt (9)
rt (5)
rt (1)
rt (3)
rt (7)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Lanjutan 2 \n")

def tr (d):
    
    if d >= 8:
        print (f"Besar, angka d = {d}")
        
    elif d >= 5:
        print (f"Kecil, angka d = {d}")
        
    else:
        print (f"Sama saja, angka d = {d}")
        
tr (10)
tr (4)
tr (8)
tr (5)
tr (3)
tr (11)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Tangga Ladder, Nilai Rapor Sekolah \n")

def rapor (n):
    
    if n >= 95:
        print (f"A, nilai = {n}")
        
    elif n >= 90:
        print (f"B, nilai = {n}")
        
    elif n >= 80:
        print (f"C, nilai = {n}")
        
    elif n >= 70:
        print (f"D, nilai = {n}")
        
    elif n >= 60:
        print (f"E, nilai = {n}")
        
    elif n >= 50:
        print (f"F, nilai = {n}")
        
    else:
        print (f"Jelek amat dah, nilai = {n}")

rapor (100)
rapor (95)        
rapor (90)
rapor (80)
rapor (70)
rapor (60)
rapor (50)
rapor (40)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Nested 1 \n")

def lo (f):
    
    cek = True
    
    if f >= 5:
        if cek:
            print (f"Besar, angka f = {f}")
            
    else:
        print (f"Kecil, angka f = {f}")
        
lo (10)
lo (8)
lo (5)
lo (7)
lo (4)
lo (3)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Nested 2 \n")

def der (g):
    
    cek = True
    
    if g >= 5:
        if cek:
            print (f"Besar, angka g = {g}")
            
    else:
        print (f"Kecil, angka g = {g}")
        
der (10)
der (8)
der (4)
der (9)
der (3)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Nested Majemuk Kompleks, Usia dan Uang \n")

def iop (usia, uang):
    
    cek = True
    
    if usia >= 18 and uang >= 5000:
        if cek:
            print (f"Uang kamu mencukupi {uang} dan usia kamu {usia} oke")
            
    else:
        print (f"Belum cukup sama sekali uang {uang} dan usianya {usia} juga")
        
        
lop (19, 6000)
lop (20, 10000)
lop (15, 3000)
lop (18, 5000)
lop (19, 7000)
lop (17, 6000)


print ("\n --- Batas --- \n")




print ("\n For dasar \n")

for a in range (11):
    print (f"Urutan ke - {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar 1 \n")

for b in range (1, 11):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar 3 \n")

for c in range (5, 21):
    print (f"Urutan ke - {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar, hitung maju \n")

a = 1

while a < 11:
    print (f"Urutan ke - {a}")
    a = a + 1
    
    
print ("\n --- Batas --- \n")




print ("\n While Dasar, Hitung Mundur \n")

b = 20

while b > 0:
    print (f"Urutan ke - {b}")
    b = b - 1
    
    
print ("\n --- Batas --- \n")




print ("\n For Nested 1 \n")


for a in range (4):
    for b in range (4):
        print (f"Luar : {a} dan Dalam : {b}")
        
        
print ("\n --- Batas --- \n")




print ("\n For Nested 2 \n")

for x in range (4):
    for y in range (4):
        print (f"Luar : {x} dan Dalam : {y}")
        
        
print ("\n --- Batas --- \n")




print ("\n For Nested 4 \n")

for k in range (4):
    for f in range (4):
        for j in range (4):
            print (f"Kiri : {k}, Tengah : {f}, Kanan : {j}")
            
            
print ("\n --- Batas --- \n")
