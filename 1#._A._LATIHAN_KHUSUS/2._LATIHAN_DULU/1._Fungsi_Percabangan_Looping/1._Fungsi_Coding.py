print ("\n Fungsi dasar \n")

def dasar ():
     print ("Hello World")

dasar ()


print ("\n --- batas --- \n")




print ("\n Fungsi dasar 1 \n")


def un ():
     print ("Hello Dunia")

un ()
un ()
un ()


print ("\n --- batas --- \n")




print ("\n Fungsi dengan parameter \n")

def nama (sapa):
     print (f"Halo saya {sapa}, asal dari Surabaya")

nama ("Hayyan")
nama ("Rayyan")
nama ("Fayyan")


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Parameter 2 \n")

def run (sapa):
     print (f"Halo saya {sapa}, dari Jakarta Utara")

run ("Roy")
run ("Alvin")
run ("Kevin")
run ("Royyan")


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Return \n")

def nama (sapa):
     return f"Halo Aku {sapa}, dari Indonesia"

print (nama ("Habib"))


print ("\n --- batas --- \n")




print ("\n Fungsi dengan return 1 \n")

def run (sapa):
     return f"Halo aku {sapa}, dari Indonesia"

print (run ("Nam"))
print (run ("VOn"))
print (run ("UTr"))


print ("\n --- batas --- \n")



print ("\n Fungsi dengan Angka Terbesar \n")

def besar (x, y):

     if x > y:
          return x
     
     else:
          return y

print (besar (10, 1))
print (besar (9, 10))
print (besar (30, 1))
print (besar (4, 23))
print (besar (12, 3))


print ("\n --- batas --- \n")



print ("\n Fungsi dengan Angka Terkecil \n")

def kecil (x, y):

     if x < y:
          return x 
     
     else:
          return y
     
print (kecil (10, 4))
print (kecil (2, 12))
print (kecil (45, 2))
print (kecil (90, 6))
print (kecil (33, 6))


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Operator dasar \n")

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


print ("Tambah =", tambah (10, 5))
print ("Kurang =", kurang (10, 5))
print ("Kali =", kali (10, 10))
print ("Bagi =", bagi (10, 2))
print ("Pangkat =", pangkat (10, 3))


print ("\n --- batas --- \n")




print ("\n Fungsi dengan rumus bangun datar \n")

def persegi (s):
     return s * s

def persegi_panjang (p, l):
     return p * l

def segitiga (a, t):
     return a * t / 2

print ("Luas persegi =", persegi (10))
print ("Luas persegi panjang =", persegi_panjang (10, 10))
print ("Luas segitiga =", segitiga (10, 10))


print ("\n --- batas --- \n")




print ("\n Fungsi dalam Angka Terbesar \n")

def besar (x, y):

     if x > y:
          return x
     
     else:
          return y
     
print (besar (10, 6))
print (besar (12, 8))
print (besar (9, 23))
print (besar (23, 1))


print ("\n --- batas --- \n")




print ("\n Fungsi dalam Percabangan Dasar \n")

def dasar (x):

     if x >= 5:
          print (f"Besar, angka x = {x}")
     
     else:
          print (f"Kecil, angka x = {x}")

dasar (10)
dasar (9)
dasar (8)
dasar (7)
dasar (5)
dasar (4)
dasar (2)
dasar (1)


print ("\n --- batas --- \n")




print ("\n Fungsi dalam Percabangan lanjutan \n")

def det (l):

     if l >= 8:
          print (f"Besar, angka l = {l}")

     elif l >= 5:
          print (f"Tengah, angka l = {l}")

     else:
          print (f"Kecil, angka l = {l}")

det (10)
det (9)
det (8)
det (7)
det (6)
det (5)
det (4)
det (3)
det (2)
det (1)

print ("\n --- batas --- \n")