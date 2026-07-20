print ("\n Bikin Hello World \n")

print ("Hello World")


print ("\n --- batas --- \n")




print ("\n bikin variabel \n")

nama = "Habib Muzakki"
asal = "Kota Serang"
kuliah = "Universitas Harkat Negeri Tegal"
jurusan = "D4 Vokasi Teknik Informatika"
lomba = "Finalis OSN-K Informatika 2025"
tinggi = "170 cm"
berat = "60 kg"
alumni = "MAN 2 KOTA SERANG"
kelas = "Agama"


details = f"""
- Nama         : {nama}
- Asal         : {asal}
- Kuliah       : {kuliah}
- Jurusan      : {jurusan}
- Lomba        : {lomba}
- Tinggi badan : {tinggi}
- Berat badan  : {berat}
- Alumni       : {alumni}
- Alumni kelas : {kelas}
"""

print (details)


print ("\n --- batas --- \n")




print ("\n Kalkulator dasar dengan fungsi \n")

def tambah (x, y):
    return x + y
    
    
def kurang (d, m):
    return d - m
    
    
def kali (w, u):
    return w * u
    
    
def pangkat (h, j):
    return h ** j
    
    
def bagi (k, n):
    return k / n
    
    
def modulus (e, p):
    return e % p
    
    
hasil_a = tambah (10, 10)
hasil_b = kurang (10, 5)
hasil_c = kali (10, 10)
hasil_d = pangkat (10, 3)
hasil_e = bagi (10, 5)
hasil_f = modulus (10, 5)


hitung = f"""
- Hasil tambah  = {hasil_a}
- Hasil kurang  = {hasil_b}
- Hasil kali    = {hasil_c}
- Hasil pangkat = {hasil_d}
- Hasil bagi    = {hasil_e}
- Hasil modulus = {hasil_f}
"""


print (hitung)


print ("\n --- batas --- \n")




print ("\n Operator Perbandingan \n")

x = 10
y = 5

detail = f"""
- Hasil nya : {x > y}
- Hasil nya : {x < y}
- Hasil nya : {x >= y}
- Hasil nya : {x <= y}
- Hasil nya : {x == y}
- Hasil nya : {x != y}
"""

print (detail)


print ("\n --- batas --- \n")



print ("\n Operator Logika \n")

run = f"""
- Hasil nya = {x < y and x > y}
- Hasil nya = {x > y or x < y}
- Hasil nya = {not (x > y)}
- Hasil nya = {not (x < y)}
"""

print (run)


print ("\n --- batas ---")




print ("\n Luas Bangun datas \n")

def persegi_panjang (p, l):
     return p * l


def persegi (s):
     return s * s


def segitiga (a, t):
     return a * t / 2


def layang_layang (d1, d2):
     return d1 * d2 / 2


hasil_a = persegi_panjang (10, 5)
hasil_b = persegi (5)
hasil_c = segitiga (10, 5)
hasil_d = layang_layang (8, 5)


bangun_datar = f"""
- Persegi Panjang = {hasil_a}
- Persegi         = {hasil_b}
- Segitiga        = {hasil_c}
- Layang2         = {hasil_d}
"""

print (bangun_datar)


print ("\n --- batas --- \n")




print ("\n Switch Case 1 \n")

i = 3

match (i):
    
    case 1:
        print ("Angka 1")
        
    case 2:
        print ("Angka 2")
        
    case 3:
        print ("Angka 3")
        
    case 4:
        print ("Angka 4")
        
    case _:
        print ("Angka benar")
        


print ("\n --- batas --- \n")




print ("\n Switch Case dengan Fungsi \n")

def und (i):
    
    match (i):
        
        case 1:
            print ("Angka 1")
            
        case 2:
            print ("Angka 2")
            
        case 3:
            print ("Angka 3")
            
        case 4:
            print ("Angka 4")
            
        case _:
            print ("Angka benar")
            
und (1)
und (2)
und (3)
und (4)
und (5)


print ("\n --- batas --- \n")




print ("\n Percabangan dasar \n")

a = 10

if a >= 5:
    print (f"Besar, angka a = {a}")
    
else:
    print (f"Kecil, angka a = {a}")
    
    
print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan dasar \n")

def am (a):
    
    if a >= 5:
        print (f"Besar, angka a = {a}")
        
    else:
        print (f"Kecil, angka a = {a}")
        
am (10)
am (8)
am (7)
am (6)
am (5)
am (3)


print ("\n --- batas --- \n")




print ("\n Percabangan lanjutan \n")

k = 5

if k >= 8:
    print (f"Besar, angka k = {k}")
    
elif k >= 5:
    print (f"Tengah, angka k = {k}")
    
else:
    print (f"Kecil, angka k = {k}")


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan lanjutan \n")

def unj (k):
    
    if k >= 8:
        print (f"Besar, angka k = {k}")
        
    elif k >= 5:
        print (f"tengah, angka k = {k}")
        
    else:
        print (f"Kecil, angka k = {k}")
        
unj (10)
unj (9)
unj (8)
unj (7)
unj (5)
unj (4)
unj (3)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Nilai Rapor \n")

def nilai (h):
     
     if h >= 90:
          print (f"Nilai A, angka h = {h}")
          
     elif h >= 80:
          print (f"Nilai B, angka h = {h}")
          
     elif h >= 70:
          print (f"Nilai C, angka h = {h}")
          
     elif h >= 60:
          print (f"Nilai D, angka h = {h}")
          
     else:
          print (f"Nilai E, angka h = {h}")
          
nilai (100)
nilai (90)
nilai (80)
nilai (70)
nilai (60)
nilai (50)


print ("\n --- batas --- \n")




print ("\n Percabangan Nested 1 \n")

h = 5
cek = True

if h >= 8:
    if cek == True:
        print (f"Besar, angka h = {h}")
        
    elif h >= 5:
        print (f"Tengah, angka h = {h}")
        
else:
    print (f"Kecil, angka h = {h}")
    
    
print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan nested 2 \n")

def fun (h):
    
    cek = True
    
    if h >= 8:
        if cek == True:
            print (f"Besar, angka h = {h}")
            
        elif h >= 5:
            print (f"Tengah, angka h = {h}")
            
    else:
        print (f"Kecil, angka h = {h}")
        
fun (10)
fun (8)
fun (7)
fun (6)
fun (5)
fun (5)
fun (5)
fun (3)


print ("\n --- batas --- \n")




print ("\n For Dasar \n")

for a in range (16):
    print (f"Urutan - {a}")
    

print ("\n --- batas --- \n")





print ("\n For dasar 1 \n")

for b in range (1, 11):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- batas --- \n")




print ("\n For dasar 2 \n")

for c in range (5, 16):
    print (f"Urutan ke - {c}")
    
    
print ("\n --- batas --- \n")




print ("\n While dasar \n")

a = 1

while a < 11:
    print (f"Urutan ke - {a}")
    a = a + 1


print ("\n --- batas --- \n")




print ("\n While dasar \n")

b = 10

while b > 0:
    print (f"Urutan ke - {b}")
    b = b - 1
    
    
print ("\n --- batas --- \n")



print ("\n While True dasar \n")

while True:
     print ("Ini adalah perulangan while True")
     break


print ("\n --- batas --- \n")



print ("\n While True + Percabangan dasar \n")

a = 10

while True:
     if a >= 8:
          print (f"Angka a = {a}, besar")
          break
     
     else:
          print (f"Angka a = {a}, kecil")
          break
     
print ("\n --- batas --- \n")



print ("\n While True + Percabangan Lanjutan \n")

b = 3

while True:
     
     if b >= 8:
          print (f"Angka b = {b}, besar")
          break
          
     elif b >= 5:
          print (f"Angka b = {b}, tengah")
          break
          
     else:
          print (f"Angka b = {b}, kecil")
          break
     
     
print ("\n --- batas --- \n")



print ("\n While True + Percabangan Validasi Data \n")

a = "Berhenti"

while True:
     
     if a == "Jalan":
          print (f"Boleh dong, a = {a}")
          break
     
     elif a == "Berhenti":
          print (f"Jangan dong, a = {a}")
          break
     
     else:
          print (f"Data tidak valid, a = {a}")
          break
     
print ("\n --- batas --- \n")



print ("\n While True + Error Handling \n")

while True:
     
     try:
          a = 10
          print (f"Angka a = {a}")
          break
     
     except:
          print ("Terjadi error")
          break
     
     finally:
          print ("Terima kasih")
          
print ("\n --- batas --- \n")



print ("\n While True + Percabangan Dasar + Error Handling \n")

while True:
     
     try:

          a = 10
          
          if a >= 9:
               print (f"Angka a = {a}, besar")
               break
          
          elif a >= 5:
               print (f"Angka a = {a}, tengah")
               break
          
          else:
               print (f"Angka a = {a}, kecil")
               break
          
     except:
          print ("Terjadi Error")
          
          
print ("\n --- batas --- \n")




print ("\n For Nested \n")

for n in range (1, 6):
     for m in range (1, 6):
          print (f"Urutan n = {n}, urutan ke - {k}")
          
print ("\n --- batas --- \n")



print ("\n For Nested 1 \n")

for u in range (1, 6):
     for w in range (1, 6):
          print (f"Urutan ke - {u}, urutan ke - {w}")
          
          
print ("\n --- batas --- \n")



print ("\n Array \n")

dan = [
     
     "Golden Sword",
     "Iron Sword",
     "Wood Sword",
     "Diamond Sword",
     "Stone Sword",
     "Nethereit Sword",
     "Fire of Sword",
     
]

for a in dan:
     print (a)
     

print ("\n --- batas --- \n")




print ("\n Tuple \n")

fer = (
     "Golden Sword",
     "Iron Sword",
     "Wood Sword",
     "Diamond Sword",
     "Stone Sword",
     "Nethereit Sword",
     "Fire of Sword",
)

for t in fer:
     print (t)
     
     
print ("\n --- batas --- \n")




print ("\n Set \n")

dal = {
     
     "Golden Sword",
     "Iron Sword",
     "Wood Sword",
     "Diamond Sword",
     "Stone Sword",
     "Nethereit Sword",
     "Fire of Sword",
     
}

for b in dal:
     print (b)
     
print ("\n --- batas --- \n")




print ("\n Dictionary \n")

data = {
     "nama" : "Habib Muzakki",
     "asal" : "Kota Serang",
     "nomor" : 12,
     "desimal" : 1.21,
     "cek" : True,
}

print ("Nama :", data ["nama"])

print ("Asal :", data ["asal"])

print ("Nomor :", data ["nomor"])

print ("Desimal :", data ["desimal"])

print ("Cek :", data ["cek"])


print ("\n --- batas --- \n")




print ("\n Error Handling \n")

try:
     a = 10
     print (a)
     
except:
     print ("Gagal")
     
finally:
     print ("Selesai")
     
     
print ("\n --- batas --- \n")




print ("\n Error Handling 1 \n")

try:
     h = 4
     print (h)
     
except:
     print ("Gagal")
     
else:
     print ("Oke")
     
finally:
     print ("Selesai")
     
     
print ("\n --- batas --- \n")