print ("\n Bikin Hello World \n")


print ("Hello World")


print ("\n --- batas --- \n")




print ("\n Variabel dasar \n")

teks = "nama"

print (teks)


angka = 19
print (angka)


print ("\n --- batas --- \n")




print ("\n F String \n")


nama = "Habib Muzakki"
asal = "Kota Serang, Banten"
lomba = "Finalis OSN-K Informatika 2025"
jurusan = "D4 Vokasi Teknik Informatika"
kuliah = "Harkat Negeri Tegal"
coding = "Html, css, javascript dan python"


profil = f"""
- Nama    : {nama}
- Asal    : {asal}
- Lomba   : {lomba}
- Jurusan : {jurusan}
- Kuliah  : {kuliah}
- Coding  : {coding}
"""

print (profil)


print ("\n --- batas --- \n")




print ("\n Tipe data pemrograman \n")

teks = "Halo Dunia"
angka = 12
desimal = 12.3
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




print ("\n Operator dasar \n")

def tambah (x, y):
    return x + y
    
    
def kurang (x, y):
    return x - y
    
    
def kali (x, y):
    return x * y
    
    
hasil_1 = tambah (10, 10)
hasil_2 = kurang (10, 5)
hasil_3 = kali (10, 10)


hitung = f"""
- Tambah = {hasil_1}
- Kurang = {hasil_2}
- Kali   = {hasil_3}
"""


print (hitung)


print ("\n --- batas --- \n")




print ("\n Operasi Perbandingan \n")

x = 10
y = 5

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




print ("\n Switch Case 1 \n")

def er (k):
    
    match (k):
        
        case 1:
            print ("Angka 1")
            
        case 2:
            print ("Angka 2")
            
        case 3:
            print ("Angka 3")
            
        case _:
            print ("Angka lain")
            
er (1)  
er (2)
er (3)
er (4)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Dasar \n")

def tun (r):
    
    if r >= 5:
        print (f"Besar, angka r = {r}")
        
    else:
        print (f"Kecil, angka r = {r}")
        
tun (10)
tun (7)
tun (5)
tun (4)
tun (3)
tun (2)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Lanjutan \n")

def jun (p):
    
    if p >= 8:
        print (f"Besar, angka p = {p}")
        
    elif p >= 5:
        print (f"Tengah, angka p = {p}")
        
    else:
        print (f"Kecil, angka p = {p}")
        
jun (10)
jun (9)
jun (8)
jun (6)
jun (5)
jun (4)
jun (3)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Nilai Rapor \n")

def rapor (k):
    
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
        print (f"Nilai jelek amat, nilai = {k}")
        
rapor (100)
rapor (90)
rapor (80)
rapor (70)
rapor (60)
rapor (50)
rapor (40)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Nested \n")

def ruk (h):
    
    cek = True
    
    if h >= 5:
        if cek:
            print (f"Besar, angka h = {h}")
            
    else:
        print (f"Kecil, angka h = {h}")
        
ruk (10)
ruk (9)
ruk (6)
ruk (4)
ruk (3)
ruk (5)


print ("\n --- batas --- \n")




print ("\n For dasar \n")

for i in range (11):
    print (f"Urutan ke - {i}")
    
    
print ("\n --- batas --- \n")




for h in range (1, 11):
    print (f"Urutan ke - {h}")
    
    
print ("\n --- batas --- \n")




print ("\n While dasar \n")

a = 1

while a < 11:
    print (f"Urutan ke - {a}")
    a += 1
    
    
print ("\n --- batas --- \n")




b = 10

while b > 0:
    print (f"Urutan ke - {b}")
    b -= 1
    
    
print ("\n --- batas --- \n")




print ("\n For Nested \n")

for a in range (1, 5):
    for b in range (1, 5):
        print (f"Luar : {a} dan Dalam : {b}")
        
        
print ("\n --- batas --- \n")




print ("\n For Nested 2 \n")

for x in range (1, 5):
    for y in range (1, 5):
        for z in range (1, 5):
            print (f"x : {x}, y : {y}, z : {z}")
            
            
print ("\n --- batas --- \n")




print ("\n List \n")

dar = ["Harold", "Word", "Yan", "Fan", "Ror", "Ver", "Run", "Lua"]

for i in dar:
    print (i)
    
    
print ("\n --- batas --- \n")




for i in dar:
    if i == "Fan":
        break
    print (i)
    
    
print ("\n --- batas --- \n")





print ("\n Dictionary \n")


data = {
    "nama" : "Don",
    "asal" : "Surabaya",
    "usia" : 19,
}

print ("Nama :", data ["nama"])

print ("Asal :", data ["asal"])

print ("Usia :", data ["usia"])


print ("\n --- batas --- \n")



print ("\n Fungsi dengan parameter \n")

def run (nama):
    print (f"Halo {nama}")
    
run ("Habib")


print ("\n --- batas --- \n")




print ("\n Fungsi dengan return \n")

def run (nama):
    return f"Halo {nama}"
    
hasil_e = run ("Yun")
print (hasil_e)


print ("\n --- batas --- \n")




print ("\n Error Handling \n")

try:
    a = 10 / 0
    print (a)
    
except:
    print ("Gagal")
    
finally:
    print ("Selesai")
    
    
print ("\n --- batas --- \n")




print ("\n Error Handling 2 \n")

try:
    h = 10 + 10
    print (h)
    
except:
    print ("Gagal")
    
finally:
    print ("Selesai")
    
    
print ("\n --- batas --- \n")



print ("\n Raise Eror \n")

def jun (h):
    
    try:
        
        if h < 0:
            raise ("Gagal")
        
        if h >= 5:
            print (f"Besar, angka h = {h}")
            
        else:
            print (f"Kecil, angka h = {h}")
            
    except:
        print (f"Gak boleh minus, angka h = {h}")

jun (-10) 
jun (-7)
jun (-9)
jun (10)
jun (8)
jun (7)
jun (2)
jun (3)


print ("\n --- batas --- \n")




print ("\n OOP dasar \n")


class Mobil:
    
    def __init__(self, nama, lari):
        self.nama = nama
        self.lari = lari
        
      
    def aksi (self):
        print (f"- Mobil {self.nama} yang warna Hitam dengan Kecepatan {self.lari} km / jam")
  
        
hasil_1 = Mobil ("Toyota", 90)
hasil_2 = Mobil ("Avanza", 80)


hasil_1.aksi ()
hasil_2.aksi ()


print ("\n --- batas --- \n")




print ("\n OOP dasar \n")

class Tes:
    
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
        
        
    def aksin (self):
        print (f"- Halo nama saya {self.nama} yang berasal dari {self.asal}")
 
        
hasil_h = Tes ("Dankut", "Serang")
hasil_f = Tes ("Hayyan", "Jakarta")


hasil_h.aksin ()
hasil_f.aksin ()


print ("\n --- batas --- \n")
