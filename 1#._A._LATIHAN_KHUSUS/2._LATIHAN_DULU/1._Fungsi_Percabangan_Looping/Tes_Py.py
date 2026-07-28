# Biasa Input Operasi dasar

a = int (input ("Masukkan angka  a = "))
b = int (input ("Masukkan angka  b = "))

hasil = a * b

print (f"Hasilnya = {hasil}")


print ("\n --- batas --- \n")



# Fungsi dengan operator dasar

x = int (input ("Masukkan angka x =  "))
y = int (input ("Masukkan angka y =  "))

def tambah (x, y):
     return x + y

def kurang (x, y):
     return x - y

def kali (x, y):
     return x * y

def pangkat (x, y):
     return x ** y

def bagi (x, y):
     return x // y


print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Pangkat =", pangkat (x, y))
print ("Bagi =", bagi (x, y))


print ("\n --- batas --- \n")



# Fungsi dengan Operator Perbandingan

r = int (input ("Masukkan angka r =  "))
u = int (input ("Masukkan angka u =  "))

def banding_1 (r, u):
     return r > u

def banding_2 (r, u):
     return r < u

def banding_3 (r, u):
     return r >= u

def banding_4 (r, u):
     return r <= u

def banding_5 (r, u):
     return r == u

def banding_6 (r, u):
     return r != u

print ("Banding 1 =", banding_1 (r, u))
print ("Banding 2 =", banding_2 (r, u))
print ("Banding 3 =", banding_3 (r, u))
print ("Banding 4 =", banding_4 (r, u))
print ("Banding 5 =", banding_5 (r, u))
print ("Banding 6 =", banding_6 (r, u))


print ("\n --- batas --- \n")




# Fungsi dengan Logic

f = int (input ("Masukkan angka f =  "))
d = int (input ("Masukkan angka d =  "))

def logic_1 (f, d):
     return f > d and f < d

def logic_2 (f, d):
     return f > d or f < d

def logic_3 (f, d):
     return (not (f < d))

def logic_4 (f, d):
     return (not (f > d))


print ("Logic 1 =", logic_1 (f, d))
print ("Logic 2 =", logic_2 (f, d))
print ("Logic 3 =", logic_3 (f, d))
print ("Logic 4 =", logic_4 (f, d))


print ("\n --- batas --- \n")



# Isi nama dengan Fungsi + Percabangan + Input

nama_kamu = input ("Masukkan nama kamu ? ")

def cek_nama (nama):

     if nama == "Habib":
          print ("Kamu Habib")

     else:
          print ("Bukan Habib")

cek_nama (nama_kamu)
cek_nama (nama_kamu)
cek_nama (nama_kamu)
cek_nama (nama_kamu)
cek_nama (nama_kamu)


print ("\n --- batas --- \n")