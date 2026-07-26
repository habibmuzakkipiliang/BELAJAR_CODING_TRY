print ("\n Kalkulator dasar \n")

def tambah (x, y):
    return x + y


def kurang (x, y):
    return x - y


def kali (x, y):
    return x * y


def bagi (x, y):
    return x / y


def pangkat (x, y):
    return x ** y


hasil_a = tambah (10, 10)
hasil_b = kurang (10, 5)
hasil_c = kali (10, 10)
hasil_d = bagi (10, 5)
hasil_e = pangkat (10, 10)


hitung = f"""
- Tambah  = {hasil_a}
- Kurang  = {hasil_b}
- Kali    = {hasil_c}
- Bagi    = {hasil_d}
- Pangkat = {hasil_e}
"""

print (hitung)


print ("\n --- batas --- \n")




print ("\n Tipe Data Pemrograman \n")

teks = "Hujan"
angka = 12
desimal = 2.12
cek = True
char = 'a'
kosong = None


tipe = f"""
- Teks    : {teks}
- Angka   : {angka}
- Desimal : {desimal}
- Cek     : {cek}
- Char    : {char}
- Kosong  : {kosong}
"""


print (tipe)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan dasar \n")

def run (a):
    
    if a >= 5:
        print (f"Besar, angka a = {a}")
        
    else:
        print (f"Kecil, angka a = {a}")
        
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


print ("\n --- batas -- \n")




print ("\n Fungsi dengan Percabangan Lanjutan \n")

def run (e):
     
     if e >= 8:
          print (f"Besar, angka e = {e}")
          
     elif e >= 5:
          print (f"Tengah, angka e = {e}")
          
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




print ("\n Fungsi dengan Percabangan Skor \n")

def skor (f):
     
     if f >= 95:
          print (f"A, skor = {f}")
          
     elif f >= 90:
          print (f"B, skor = {f}")
          
     elif f >= 80:
          print (f"C, skor = {f}")
          
     elif f >= 70:
          print (f"D, skor = {f}")
     
     elif f >= 60:
          print (f"E, skor = {f}")
          
     elif f >= 50:
          print (f"F, skor = {f}")
          
     else:
          print (f"Jelek amat, skor = {f}")
          
skor (100)
skor (90)
skor (80)
skor (70)
skor (60)
skor (50)
skor (40)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Nested \n")

def run (w):
     
     cek = True
     
     if w >= 5:
          if cek:
               print (f"Besar, angka w = {w}")
               
     else:
          print (f"Kecil, angka w = {w}")
          
          
run (10)
run (8)
run (7)
run (5)
run (4)
run (3)
run (2)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Switch Case dengan Int \n")

def rust (l):
     
     match (l):
          
          case 1:
               print ("Angka 1")
               
          case 2:
               print ("Angka 2")
               
          case 3:
               print ("Angka 3")
               
          case 4:
               print ("Angka 4")
               
          case 5:
               print ("Angka 5")
               
          case _:
               print ("Angka lain")
               
rust (1)
rust (2)
rust (3)
rust (4)
rust (5)
rust (6)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Swich Case dengan String \n")

def warna (e):
     
     match (e):
          
          case "Merah":
               print ("Warna Merah")
               
          case "Kuning":
               print ("Warna Kuning")
               
          case "Hijau":
               print ("Warna Hijau")
               
          case _:
               print ("Warna lain")
               
warna ("Merah")
warna ("Kuning")
warna ("Hijau")
warna ("Hitam")


print ("\n --- batas --- \n")




print ("\n Fungsi + Percabangan Dasar + Mencari angka terkecil \n")

def kecil (c, d):
     
     if c <= d:
          return c 
     
     else:
          return d
     
hasil_1 = kecil (10, 5)
hasil_2 = kecil (5, 10)
hasil_3 = kecil (23, 5)
hasil_4 = kecil (7, 10)


print (hasil_1)
print (hasil_2)
print (hasil_3)
print (hasil_4)


print ("\n --- batas --- \n")




print ("\n Fungsi + Percabangan Dasar + Mencari angka terbesar \n")

def besar (l, m):
     
     if l >= m:
          return l
     
     else:
          return m
     
hasil_der = besar (20, 5)
hasil_ver = besar (90, 3)
hasil_wer = besar (34, 9)
hasil_rer = besar (2, 12)


print (hasil_der)
print (hasil_ver)
print (hasil_wer)
print (hasil_rer)


print ("\n --- batas --- \n")




print ("\n Fungsi + Percabangan Dasar + Mencari Angka Besar \n")

for a in range (15):
     if a == 10:
          continue
     print (a)
     
     
print ("\n --- batas --- \n")




print ("\n For + If lanjutan 2 \n")

for i in range (15):
     if i == 10:
          break
     print (i)
     
     
print ("\n --- batas --- \n")




print ("\n Array + For + If Lanjutan \n")

daf = ["Rans", "Fans", "Fons", "Kesh", "Best"]

for i in daf:
     if i == "Fons":
          continue
     print (i)
     
     
print ("\n --- batas --- \n")




print ("\n Array + For + If Lanjutan \n")

der = ["Plan", "Run", "Compiler", "Rust", "Int", "Float"]

for k in der:
     if k == "Compiler":
          break
     print (i)
     
     
print ("\n --- batas --- \n")




print ("\n Struktur Data \n")

data = {
     "teks" : "halo dunia",
     "angka" : 12,
     "desimal" : 3.14,
     "cek" : True,
     "kosong" : None,
}

print ("Teks :", data ["teks"])

print ("Angka :", data ["angka"])

print ("Desimal :", data ["desimal"])

print ("Cek :", data ["cek"])

print ("Kosong :", data ["kosong"])