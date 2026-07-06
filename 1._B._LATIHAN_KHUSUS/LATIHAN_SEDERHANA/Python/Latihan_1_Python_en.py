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





print ("\n Fungsi dengan percabangan Lanjutan \n")

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