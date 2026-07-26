print ("Hello World")


nama = "Habib Muzakki"
print (nama)


print ("\n --- batas --- \n")



print ("\n variabel dasar \n")


nama = "Habib Muzakki"
print (nama)


angka = 12
print (angka)


desimal = 3.13
print (desimal)


print ("\n --- batas ---\n")




print ("\n F String \n")

nama = "Habib Muzakki"
asal = "Kota Serang, Banten"
jurusan = "D4 Vokasi Teknik Informatika"
kuliah = "Universitas Harkat Negeri Tegal"

profil = f"""
- Nama    : {nama}
- Asal    : {asal}
- Jurusan : {jurusan}
- Kuliah  : {kuliah} 
"""

print (profil)


print ("\n --- batas ---\n")




print ("\n Opearasi dasar \n")

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




hasil_1 = tambah (10, 10)
hasil_2 = kurang (10, 5)
hasil_3 = kali (10, 10)
hasil_4 = bagi (10, 5)
hasil_5 = pangkat (10, 3)


hitung = f"""
- Hasil tambah  = {hasil_1}
- Hasil kurang  = {hasil_2}
- Hasil kali    = {hasil_3}
- Hasil bagi    = {hasil_4}
- Hasil pangkat = {hasil_5}
"""

print (hitung)


print ("\n --- batas ---\n")



print ("\n Operasi Perbandingan \n")

x = 10
y = 5

banding = f"""
- Hasil = {x > y}
- Hasil = {x < y}
- Hasil = {x >= y}
- Hasil = {x <= y}
- Hasil = {x == y}
- Hasil = {x != y}
"""

print (banding)


print ("\n --- batas ---\n")




print ("\n Operasi Logika \n")

logic = f"""
- Hasil = {x > y and x < y}
- Hasil = {x < y or x > y}
- Hasil = {not (x > y)}
- Hasil = {not (x < y)}
"""

print (logic)


print ("\n --- batas ---\n")




print ("\n Fungsi dengan Percabangan Dasar \n")


def gun (a):

    if a >= 5:
        print (f"Besar, angka a = {a}")

    else:
        print (f"Kecil, angka a = {a}")


gun (10)
gun (8)
gun (3)
gun (2)
gun (1)


print ("\n --- batas --- \n")



print ("\n Fungsi dengan percabangan lanjutan \n")

def tun (l):

    if l >= 8:
        print (f"Besar, angka l = {l}")

    elif l >= 5:
        print (f"Tengah, angka l = {l}")

    else:
        print (f"Kecil, angka l = {l}")


tun (10)
tun (9)
tun (7)
tun (6)
tun (5)
tun (3)
tun (2)



print ("\n --- batas --- \n")





print ("\n Struktur data Dic \n")

data = {
    "nama" : "Habib Muzakki",
    "asal" : "Kota Serang",
    "usia" : 19,
    "cek" : True,
}

print ("Nama :", data ["nama"])
print ("Asal :", data ["asal"])
print ("Usia :", data ["usia"])
print ("Cek :", data ["usia"])


print ("\n --- batas --- \n")





print ("\n Array dasar \n")


daftar = ["For", "While", "Do While", "OOP", "Jangan"]


for a in daftar:
    print (a)



print ("\n --- batas --- \n")




print ("\n For break \n")


for i in daftar:
    if i == "Do While":
        break
    print (i)



print ("\n --- batas --- \n")





print ("\n OOP dasar \n")

class Mobil:

    def __init__(self, nama, warna, lari):
        self.nama = nama
        self.warna = warna
        self.lari = lari

    
    def aksi (self):
        print (f"- Mobil {self.nama} dengan berwarna {self.warna} dengan kecepatan {self.lari} km / jam")


hasil_k = Mobil ("Toyota", "Hitam", 10)
hasil_r = Mobil ("Avanza", "Hitam", 100)
hasil_u = Mobil ("Xenia", "Hitam", 89)


hasil_r.aksi ()
hasil_u.aksi ()
hasil_k.aksi ()


print ("\n --- batas --- \n")





print ("\n OOP dasar 1 \n")

class HP:

    def __init__(self, nama_1, warna, spek):
        self.nama_1 = nama_1
        self.warna = warna
        self.spek = spek


    def aksiM (self):
        print (f"- HP merek {self.nama_1} dengan berwarna {self.warna}, dan dengan spek {self.spek}")


hasil_e = HP ("Tecno", "Hitam", "Tinggi")
hasil_w = HP ("Infinix", "Hitam", "Sedang")
hasil_r = HP ("Itel", "Hitam", "Rendah")


hasil_e.aksiM ()
hasil_w.aksiM ()
hasil_r.aksiM ()


print ("\n --- batas --- \n")




