print ("Hello World")


print ("\n --- Batas --- \n")


teks = "Halo dunia"
print (teks)


angka = 12
print (angka)


desimal = 3.14
print (desimal)


print ("\n --- Batas --- \n")



print ("\n Tipe Data Pemrograman \n")

nama = "Habib"
angka = 12
desimal = 3.14
cek = True
char = 'A'
kosong = None

detail = f"""
- Nama     : {nama}
- Angka    : {angka}
- Desimal  : {desimal}
- Boolean  : {cek}
- Char     : {char}   
- Kosong   : {kosong}
"""

print (detail)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan kalkulator \n") 

def tambah (a, b):
     return a + b


def kurang (x, y):
     return x - y


def kali (w, e):
     return w * e


def bagi (z, v):
     return z / v


def pangkat (j, l):
     return j ** l


def modulus (y, g):
     return y % g


hasil_1 = tambah (10, 5)
hasil_2 = kurang (10, 5)
hasil_3 = kali (10, 5)
hasil_4 = bagi (10, 5)
hasil_5 = pangkat (10, 5)
hasil_6 = modulus (10, 5)

print (f"""
- Hasil tambah : {hasil_1}
- Hasil kurang : {hasil_2}
- Hasil kali   : {hasil_3}
- Hasil bagi   : {hasil_4}
- Hasil pangkat: {hasil_5}
- Hasil modulus: {hasil_6}
""")


print ("\n --- Batas --- \n")




print ("\n Operator Perbandingan \n")

x = 10
y = 5

detail = f"""
- Hasil  : {x == y}
- Hasil  : {x > y}
- Hasil  : {x < y}
- Hasil  : {x <= y}
- Hasil  : {x >= y}
- Hasil  : {x != y}
"""

print (detail)


print ("\n --- Batas --- \n")




print ("\n Operator Logika \n")

detail = f"""
- Hasil  : {x and y}
- Hasil  : {x or y}
- Hasil  : {not x}
"""

print (detail)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan rumus bangun datar \n")


print ("\n Luas Persegi \n")

def persegi (s):
     return s * s

hasil_k = persegi (5)
print ("Luas persegi =", hasil_k)


print ("\n --- Batas --- \n")



print ("\n Luas Persegi Panjang \n")

def persegi_panjang (p, l):
     return p * l

hasil_e = persegi_panjang (5, 10)
print ("Luas persegi panjang =", hasil_e)




print ("\n --- Batas --- \n")


print ("\n Luas Segitiga \n")

def segitiga (a, t):
     return a * t / 2

hasil_b = segitiga (5, 10)
print ("Luas segitiga =", hasil_b)


print ("\n --- Batas --- \n")



print ("\n Luas lingkaran \n")

def lingkaran (phi, r):
     return phi * r * 2

hasil_l = lingkaran (3.14, 5)
print ("Luas lingkaran =", hasil_l)


print ("\n --- Batas --- \n")




print ("\n Luas Layang-Layang \n")

def layang_layang (d1, d2):
     return d1 * d2 / 2

hasil_t = layang_layang (5, 10)
print ("Luas layang-layang =", hasil_t)


print ("\n --- Batas --- \n")




print ("\n Luas jajar genjang \n")

def jajar_genjang (a, t):
     return a * t

hasil_f = jajar_genjang(5, 10)
print ("Luas jajar genjang =", hasil_f)


print ("\n --- Batas --- \n")



print ("\n Switch Case 1 \n")

def hei (k):
     
     match (k):
          
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
               print ("Angka tidak ditemukan")

hei (1)
hei (2)
hei (3)
hei (5)
hei (6)


print ("\n --- Batas --- \n")




print ("\n Switch Case 2 \n")

def hai (h):
     
     match (h):
          
          case "A":
               print ("Huruf A")
               
          case "B":
               print ("Huruf B")
               
          case "C":
               print ("Huruf C")
               
          case "D":
               print ("Huruf D")
               
          case "E":
               print ("Huruf E")
               
          case _:
               print ("Huruf tidak ditemukan")

hai ("A")
hai ("B")
hai ("C")
hai ("D")
hai ("E")
hai ("F")


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan percabangan dasar \n")

def dasar (a):
     
     if a >= 5:
          print (f"Angka besar, angka a = {a}")
          
     else:
          print (f"Angka kecil, angka a = {a}")
          
dasar (10)
dasar (8)
dasar (7)
dasar (3)
dasar (5)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan percabangan dasar 1 \n")

def dun (b):
     
     if b >= 5:
          print (f"Angka b, b = {b}")
          
     else:
          print (f"Angka kecil, angka b = {b}")

dun (10)
dun (8)
dun (7)
dun (3)
dun (5)


print ("\n --- Batas --- \n")



print ("\n Fungsi dengan percabangan lanjutan \n")

def ran (c):
     
     if c >= 8:
          print (f"Angka besar, c = {c}")
          
     elif c >= 5:
          print (f"Angka setengah, c = {c}")
          
     else:
          print (f"Angka kecil, c = {c}")
              
ran (10)
ran (9)
ran (8)
ran (4)
ran (3)
ran (2)


print ("\n --- Batas --- \n")



print ("\n Fungsi dengan percabangan lanjutan \n")

def daf (c):
     
     if c >= 8:
          print (f"Besar, angka c = {c}")
          
     elif c >= 5:
          print (f"Setengah, angka c = {c}")
          
     else:
          print (f"Keci, angka c = {c}")
          
daf (1)
daf (4)
daf (2)
daf (6)
daf (9)
daf (3)


print ("\n --- Batas --- \n")



print ("\n Fungsi dengan percabangan nilai rapor \n")

def rapor (r):
     
     if r >= 90:
          print (f"A, nilai kamu = {r}")
          
     elif r >= 80:
          print (f"B, nilai kamu = {r}")
          
     elif r >= 70:
          print (f"C, nilai kamu = {r}")
          
     elif r >= 60:
          print (f"D, nilai kamu = {r}")
          
     elif r >= 50:
          print (f"E, nilai kamu = {r}")
          
     else:
          print (f"Jelek banget, nilai kamu = {r}")
          
rapor (100)
rapor (90)
rapor (80)
rapor (70)
rapor (60)
rapor (50)
rapor (40)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan nested 1 \n")

def dask (k):
     
     if k >= 9:
          if cek == True:
               print (f"Besar, angka k = {k}")
               
          elif k >= 5:
               print (f"Kecil, angka k = {k}")
     
     else:
          print (f"Lebih kecil, angka k = {k}")
          
dask (10)
dask (8)
dask (9)
dask (7)
dask (5)
dask (3)


print ("\n --- batas --- \n")



print ("\n Fungsi dengan percabangan Nested 2 \n")

def runk (l):
     
     if l >= 9:
          if cek == True:
               print (f"Besar, angka l = {l}")
               
          else:
               print (f"Kecil, angka l = {l}")
               
     else:
          print (f"Lebih kecil, angka l = {l}")
          
runk (10)
runk (9)
runk (8)
runk (5)
runk (3)
runk (2)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan nested majemuk \n")

def hun (uang, usia):
     
     if usia >= 19 and uang >= 10000:
          if cek == True:
               print (f"Usia dan uang kamu oke, uang = {uang} dan usia = {usia}")
               
          elif usia >= 19 or uang < 5000:
               print (f"Usia kamu mencukupi tapi uang gak cukup, uang = {uang} dan usia = {usia}")
               
          else:
               print (f"Usia dan uang kamu belum cukup, uang = {uang} dan usia = {usia}")
               
     else:
          print (f"Lain kali kamu ikut, uang = {uang} dan usia = {usia}")
          
hun (20, 100000)
hun (19, 50000)
hun (12, 10000)
hun (25, 500000)


print ("\n --- batas --- \n")




print ("\n For dasar \n")

for a in range (15):
     print (f"Urutan ke - {a}")
     
print ("\n --- Batas --- \n")



print ("\n For dasar 1 \n")

for b in range (1, 11):
     print (f"Urutan ke - {b}")
     
     
print ("\n --- batas --- \n")



print ("\n For dasar 3 \n")

for c in range (5, 16):
     print (f"Urutan ke - {c}")
     
     
print ("\n --- batas --- \n")