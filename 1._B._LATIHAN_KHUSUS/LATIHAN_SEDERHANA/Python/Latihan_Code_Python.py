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