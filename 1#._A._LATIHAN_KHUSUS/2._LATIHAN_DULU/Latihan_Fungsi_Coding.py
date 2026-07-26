# Fungsi dasar 

def dasar ():
     print ("Hello World")

dasar ()


print ("\n --- batas --- \n")



# Fungsi dasar 2

def run ():
     print ("Hello World")
     print ("Hello Dankut")
     print ("Hello Hayyan")
     print ("Hello Fas")

run ()


print ("\n --- batas --- \n")



# Fungsi dengan parameter

def vun (nama):
     print (f"Halo nama saya {nama}, dari Kota Serang")

vun ("Hayyan")
vun ("Rayyan")
vun ("Jun")
vun ("Jundy")
vun ("Burundy")
vun ("Kop")


print ("\n --- batas --- \n")



# Fungsi dengan parameter

def fun (j):
     print (f"Halo nama saya {j}, dari Jakarta Timur")

fun ("Vest")
fun ("Yonda")
fun ("Honda")
fun ("Vonda")
fun ("Jue")


print ("\n --- batas --- \n")




# Fungsi dengan return

def kem (nama):
     return f"Halo saya {nama} dari jakarta pusat"

print (kem ("Habib"))
print (kem ("Roy"))
print (kem ("Yun"))
print (kem ("Kopral"))
print (kem ("Jun"))
print (kem ("Nuk"))


print ("\n --- batas --- \n")



# Fungsi dengan return

def run (kop):
     return f"Halo dunia {kop} dari dunia lain"

print (run ("Hyn"))
print (run ("Lop"))
print (run ("Jun"))
print (run ("Hun"))


print ("\n --- batas --- \n")



# Fungsi dalam percabangan dasar

def kopi (e):

     if e >= 5:
          print (f"Besar, angka e = {e}")

     else:
          print (f"kecil, angka e = {e}")

kopi (10)
kopi (9)
kopi (8)
kopi (5)
kopi (3)
kopi (2)
kopi (1)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan lanjutan

def erun (c):

     if c >= 8:
          print (f"Besar, angka c = {c}")

     elif c >= 5:
          print (f"Tengah, angka c = {c}")

     else:
          print (f"Kecil, angka c = {c}")

erun (10)
erun (9)
erun (8)
erun (7)
erun (6)
erun (5)
erun (4)
erun (3)
erun (2)
erun (1)


print ("\n --- batas --- \n")





# Fungsi dengan percabangan nilai rapor 

def skor (x):

     if x >= 95:
          print (f"A, nilai = {x}")

     elif x >= 90:
          print (f"B, nilai = {x}")

     elif x >= 80:
          print (f"C, nilai = {x}")

     elif x >= 70:
          print (f"D, nilai = {x}")

     elif x >= 60:
          print (f"E, nilai = {x}")

     elif x >= 50:
          print (f"F, nilai = {x}")

     else:
          print (f"Jelek amat, nilai = {x}")

skor (100)
skor (90)
skor (80)
skor (70)
skor (60)
skor (50)
skor (40)
skor (30)
skor (20)
skor (10)


print ("\n --- batas --- \n")




# Fungsi dengan percabangan nested 1

def ruj (f):

     cek = True

     if f >= 5:
          if cek:
               print (f"Besar, angka f = {f}")

          else:
               print (f"Tengah, angka f = {f}")

     else:
          print (f"Kecil, angka f = {f}")

ruj (10)
ruj (9)
ruj (8)
ruj (7)
ruj (6)
ruj (5)
ruj (4)
ruj (3)
ruj (2)
ruj (1)


print ("\n --- batas --- \n")