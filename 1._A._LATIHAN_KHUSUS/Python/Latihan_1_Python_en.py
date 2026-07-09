print ("\n Bikin Hello World \n")

print ("Hello World")


print ("\n --- Batas --- \n")




print ("\n Variabel \n")

nama = "habib"
print (nama)


angka = 19
print (angka)


desimal = 19.12
print (desimal)


cek = True
print (cek)


print ("\n --- batas --- \n")




print ("\n F String \n")

nama = "Habib Muzakki"
marga = "piliang"
asal = "Kota Serang"
jurusan = "D4 Teknik Informatika"
universitas = "Harkat Negeri"
fakultas = "Sekolah Vokasi"

details = f"""
- Nama        :  {nama}
- Marga       :  {marga}
- Asal        :  {asal}
- Jurusan     :  {jurusan}
- Universitas :  {universitas}
- Fakultas    :  {fakultas}


"""

print (details)


print ("\n --- batas --- \n")




print ("\n Operator dasar \n")

def tambah (x, y):
     return x + y


def kurang (a, b):
     return a - b


def kali (r, t):
     return r * t


def pangkat (y, u):
     return y ** u


hasil_a = tambah (10, 10)
hasil_b = kurang (30, 5)
hasil_c = kali (40, 5)
hasil_d = pangkat (20, 2)


hunnies = f"""
- Hasil tambah  = {hasil_a}
- Hasil kurang  = {hasil_b}
- Hasil kali    = {hasil_c}
- Hasil pangkat = {hasil_d}
"""

print (hunnies)


print ("\n --- batas --- \n")





print ("\n Operator perbandingan \n")

x = 10
y = 9

banding = f"""
- Hasil = {x > y}
- Hasil = {x < y}
- Hasil = {x >= y}
- Hasil = {x <= y}
- Hasil = {x == y}
- Hasil = {x != y}
"""

print (banding)


print ("\n --- Batas --- \n")




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

def switch (h):
     
     match (h):
          case 1:
               print ("Nilai baik")
               
          case 2:
               print ("Nilai agak baik")
               
          case 3:
               print ("Nilai sedang")
               
          case 4:
               print ("Nilai gak sedang")
               
          case _:
               print ("Nilai buruk")
               
switch (1)
switch (2)
switch (3)
switch (4)
switch (5)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan percabangan Nilai Rapor \n")

def nilai (a):
     
     if a >= 90:
          print (f"A, nilai = {a}")
          
     elif a >= 80:
          print (f"B, nilai = {a}")
          
     elif a >= 70:
          print (f"C, nilai = {a}")
          
     elif a >= 60:
          print (f"D, nilai = {a}")
          
     elif a >= 50:
          print (f"E, nilai = {a}")
          
     else:
          print (f"Nilai jelek")
          
nilai (100)
nilai (90)
nilai (80)
nilai (70)
nilai (60)
nilai (50)
nilai (40)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan dasar \n")

def daf (c):
     
     if c >= 8:
          print (f"Besar, angka c = {c}")
          
     else:
          print (f"Kecil, angka c = {c}")
          
daf (10)
daf (5)
daf (8)
daf (3)
daf (8)
daf (5)


print ("\n --- batas --- \n")




print ("\n Percabangan Lanjutan \n")

def fun (k):
     
     if k >= 8:
          print (f"Besar, angka k = {k}")
          
     elif k >= 5:
          print (f"Tengah, angka k = {k}")
          
     else:
          print (f"Kecil, angka k = {k}")
     
fun (10)
fun (6)
fun (7)
fun (6)
fun (5)
fun (3)
fun (2)
fun (1)


print ("\n --- batas --- \n")




print ("\n Percabangan Lanjutan 2 \n")

def run (d):
     
     if d >= 8:
          print (f"Besar, angka d = {d}")
          
     elif d >= 5:
          print (f"Tengah, angka d = {d}")
          
     else:
          print (f"Kecil, angka d = {d}")
          
run (10)
run (6)
run (5)
run (4)
run (2)


print ("\n --- batas --- \n")




print ("\n Percabangan Nested 1 \n")

def nest (r):
     
     if r >= 8:
          if cek == True:
               print (f"Besar, angka r = {r}")
               
          elif r >= 5:
               print (f"Tengah, angka r = {r}")
               
     else:
          print (f"Kecil, angka r = {r}")
          
nest (10)
nest (8)
nest (7)
nest (6)
nest (5)


print ("\n --- batas --- \n")




print ("\n For dasar \n")

for a in range (16):
     print (f"Angka a = {a}")
     

print ("\n --- batas --- \n")




print ("\n For dasar 2 \n")

for b in range (10, 21):
     print (f"Angka b = {b}")
     
     
print ("\n --- batas --- \n")




print ("\n For dasar 3 \n")

for c in range (5, 21):
     print (f"Urutan ke - {c}")
     
     
print ("\n --- batas --- \n")




print ("\n While dasar 1 \n")

a = 1

while a < 16:
     print (f"Angka a = {a}")
     a = a + 1
     

print ("\n --- batas --- \n")




print ("\n While dasar 2 \n")

b = 10

while b > 0:
     print (f"Urutan ke - {b}")
     b = b - 1
     
     
print ("\n --- batas --- \n")




print ("\n While True \n")

while True:
     print ("Hello World")
     break


print ("\n --- batas --- \n")




print ("\n While True 1 + Percabangan Dasar \n")

a = 3

while True:
     
     if a >= 8:
          print (f"Angka a = {a}, besar")
          break
     
     else:
          print (f"Angka a = {a}, kecil")
          break
     
print ("\n --- batas --- \n")




print ("\n While True 2  + Percabangan Lanjutan \n")

i = 10

while True:
     
     if i >= 9:
          print (f"Angka i = {i}")
          break
     
     elif i >= 5:
          print (f"Angka i = {i}")
          break
     
     else:
          print (f"Angka i = {i}")
          break
     

print ("\n --- batas --- \n")




print ("\n While True + Error Handling \n")

while True:
     
     try:
          
          a = 10
          
          if a >= 8:
               print (f"angka besar, a = {a}")
               break
               
          elif a >= 5:
               print (f"Angka Tengah, a = {a}")
               break
               
          else:
               print (f"Angka Kecil, a = {a}")
               break
          
     except:
          print ("Terjadi Error")
          
          
print ("\n --- batas --- \n")




print ("\n For Nested \n")

for i in range (1, 6):
     for e in range (1, 6):
          print (f"Urutan ke - {i}, Urutan ke - {e}")
          
          
print ("\n --- batas --- \n")




print ("\n For Nested 1 \n")

for t in range (1, 6):
     for j in range (1, 6):
          print (f"Urutan ke - {t}, urutan ke - {j}")
          
          
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