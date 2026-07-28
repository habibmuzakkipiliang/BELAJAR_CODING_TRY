print ("\n Bikin Program Python \n")

print ("Hello World")


print ("\n --- batas --- \n")



print ("\n Tipe data pemrograman \n")

teks = "Habib Muzakki"
angka = 12
desimal = 12.13
cek = True
kosong = None


tipe = f"""
- Teks    : {teks}
- Angka   : {angka}
- Desimal : {desimal} 
- Cek     : {cek}
- Kosong  : {kosong}
"""

print (tipe)

print ("\n --- batas --- \n")




print ("\n Profil Habib Muzakki \n")

nama = "Habib Muzakki"
akrab = "Habib"
asal = "Kota Serang, Banten"
coding = "HTML, CSS, JavaScript dan Python"
kuliah = "Universitas Harkat Negeri Tegal"
prodi = "D4 Vokasi Informatika"
lomba = "Finalis OSN-K Informatika 2025"


profil = f"""
- Nama lengkap   : {nama}
- Nama panggilan : {akrab}
- Asal           : {asal}
- Coding         : {coding}
- Kuliah         : {kuliah}
- Prodi          : {prodi}
- Lomba          : {lomba}
"""

print (profil)


print ("\n --- batas --- \n")



print ("\n Array 1 \n")

daf = ["Halo", "Tes", "Fast", "Green", "Job"]

for a in daf:
     print (a)


print ("\n --- batas --- \n")




print ("\n Array 2 \n")

hun = ["Fan", "Ran", "Creeper", "Skeleton", "Wither", "XP"]

for b in hun:
     print (b)



print ("\n --- batas --- \n")




print ("\n Array 3 \n")

fun = ["Wither", "Hostile Mob", "Mob", "Monster", "Golem", "Dead Golem", "Main kart"]


for j in fun:
     print (j)


print ("\n --- batas --- \n")



print ("\n Dictionary \n")

data = {
     "wahana" : "Bianglala",
     "tipe" : "Roda",
     "status" : "Oke",
     "tinggi" : 20,
}

print ("Wahana :", data ["wahana"])
print ("Tipe :", data ["tipe"])
print ("Status :", data ["status"])
print ("Tinggi :", data ["tinggi"])


print ("\n --- batas --- \n")



print ("\n Fungsi dengan Percabangan Dasar \n")

def dasar (j):

     if j >= 5:
          print (f"Besar, angka j = {j}")

     else:
          print (f"Kecil, angka j = {j}")

dasar (10)
dasar (9)
dasar (8)
dasar (7)
dasar (6)
dasar (5)
dasar (4)
dasar (3)
dasar (2)
dasar (1)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Lanjutan \n")

def run (i):

     if i >= 8:
          print (f"Besar, angka i = {i}")

     elif i >= 5:
          print (f"Tengah, angka i = {i}")

     else:
          print (f"Kecil, angka i = {i}")

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



print ("\n Fungsi dengan percabangan nested 1 \n")

def funt (k):

     if k >= 8:
          if cek == True:
               print (f"Besar, angka k = {k}")

     elif k >= 5:
          print (f"Kecil, angka k = {k}")

funt (10)
funt (9)
funt (8)
funt (7)
funt (6)
funt (5)
funt (4)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan nested dengan simbol \n")

def tunt (v):

     if v >= 8 and v >= 10:
          if cek == True:
               print (f"Besar, angka v = {v}")

     elif v >= 5 or v >= 9:
          print (f"Kecil, angka v = {v}")

tunt (10)
tunt (9)
tunt (8)
tunt (7)
tunt (6)
tunt (5)
tunt (4)
tunt (3)


print ("\n --- batas --- \n")



print ("\n OOP Dasar \n")

class Entity:

     def __init__(self, nama, versi):
          self.nama = nama
          self.versi = versi

     def aksi (self):
          print (f"- {self.nama} dari versi {self.versi}")

hasil_1 = Entity ("Entity 303", "1.7")
hasil_2 = Entity ("Herobrine", "1.14")
hasil_3 = Entity ("Null", "1.24")


hasil_1.aksi ()
hasil_2.aksi ()
hasil_3.aksi ()


print ("\n --- batas --- \n")




print ("\n --- batas --- \n")



print ("\n OOP Dasar \n")

class Mobil:

     def __init__(self, nama, warna, lari):
          self.nama = nama
          self.warna = warna
          self.lari = lari

     def aksi (self):
          print (f"- Mobil {self.nama} yang berwarna {self.warna} dengan kecepatan {self.lari}")


hasil_1 = Mobil ("Rush", "Hitam", 20)
hasil_2 = Mobil ("Terios", "Hitam", 20)


hasil_1.aksi ()
hasil_2.aksi ()


print ("\n --- batas --- \n")