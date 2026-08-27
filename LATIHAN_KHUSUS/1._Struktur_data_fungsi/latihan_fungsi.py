# Fungsi dasar

def dasar ():
     print ("Hello World")

dasar ()


print ("\n --- batas --- \n")




# Fungsi dasar 2

def run ():
     print ("Hello Duniaku")
     print ("Hello Fun")
     print ("Hello Ser")
     print ("Hello Gun")

run ()


print ("\n --- batas --- \n")




# Fungsi dengan parameter

def nama (sapa):
     print (f"Halo saya {sapa} dari Jakarta Timur")

nama ("Hayyan")
nama ("Fayyan")
nama ("Arroyan")
nama ("Fai")
nama ("Fahai")
nama ("Royan")
nama ("Fayyun")


print ("\n --- batas --- \n")



# Fungsi dengan return

def nama (sapa):
     return f"Halo saya {sapa} dari Jakarta Timur"

print (nama ("Hayyan"))
print (nama ("Jund"))
print (nama ("Gru"))
print (nama ("Numberg"))
print (nama ("Fers"))
print (nama ("Hun"))


print ("\n --- batas --- \n")



# Fungsi dengan return

def run (nama):
     return f"Halo saya {nama} dari Jakarta Timur"

run ("Ron")
run ("Ran")
run ("Van")
run ("Var")
run ("Jun")
run ("Lop")


print ("\n --- batas --- \n")





# Fungsi dengan return

def run (nama):
     return f"Halo {nama} dari Kota Tegal"

print (run ("Habib"))
print (run ("Hayyan"))
print (run ("Run"))
print (run ("Vase"))
print (run ("Halim"))
print (run ("Kom"))


print ("\n --- batas --- \n")



# Fungsi dengan luas bangun datar

def persegi (s):
     return s * s

def persegi_panjang (p, l):
     return p * l

def segitiga (a, t):
     return a * t / 2

def belah_ketupat (d1, d2):
     return d1 * d2 / 2

def layang_layang (d1, d2):
     return d1 * d2 / 2


print ("Luas persegi =", persegi (10))
print ("Luas persegi panjang =", persegi_panjang (10, 4))
print ("Luas segitiga = ", segitiga (10, 9))
print ("Luas belah ketupat =", belah_ketupat (10, 9))
print ("Luas layang - layang", layang_layang (34, 12))


print ("\n --- batas --- \n")



# Fungsi dengan operator dasar

x = 10
y = 5

def tambah (x, y):
     return x + y

def kurang (x, y):
     return x - y

def kali (x, y):
     return x * y

def pangkat (x, y):
     return x ** y

def bagi (x, y):
     return x / y


print (tambah (x, y))
print (kurang (x, y))
print (kali (x, y))
print (pangkat (x, y))
print (bagi (x, y))


print ("\n --- batas --- \n")




# Fungsi dengan percabangan else

def fun (k):

     if k > 0:
          print (f"Angka positif, angka k = {k}")

     elif k < 0:
          print (f"Angka negatif, angka k = {k}")

     else:
          print (f"Angka nol, angka k = {k}")

fun (0)
fun (10)
fun (9)
fun (8)
fun (7)
fun (6)
fun (5)
fun (4)


print ("\n --- batas --- \n")




# Fungsi dengan usia produktifm manusia

def fer (k):

     if k >= 15 and k <= 40:
          print (f"usia yang produktif, usia = {k}")

     elif k > 40:
          print (f"usia yang sudah tua, usia = {k}")

     else:
          print (f"masih muda, usia = {k}")

fer (70)
fer (60)
fer (50)
fer (40)
fer (30)
fer (20)
fer (10)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan nested kompleks

def kop (f):

     cek = True

     if f >= 15 and f <= 40:
          if cek:
               print (f"usia yang sudah produktif, usia = {f}")

          else:
               print (f"usia yang sudah tua, usia = {f}")

     else:
          print (f"usia yang masih kecil, usia = {f}")

kop (10)
kop (9)
kop (8)
kop (7)
kop (6)
kop (5)
kop (4)

