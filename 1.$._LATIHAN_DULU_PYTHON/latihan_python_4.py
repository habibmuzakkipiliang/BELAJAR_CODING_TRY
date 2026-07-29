print ("Hello world")


print ("\n --- batas --- \n")


print ("\n Tipe data pemrograman \n")

teks = "Habib Muzakki"
angka = 12
desimal = 1.12
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



print ("\n Variabel dasar \n")

nama_1 = "Habib Muzakki"
print (nama_1)


angka_1 = 12
print (angka_1)


desimal_1 = 31.2
print (desimal_1)


print ("\n --- batas --- \n")




print ("\n Profil Habib Muzakki \n")

nama = "Habib Muzakki"
akrab = "Habib"
asal = "Kota Serang, Banten"
jurusan = "D4 Vokasi Teknik Informatika"
kuliah = "Universitas Harkat Negeri Tegal"
coding = "HTML, CSS, JavaScript dan Python"
lomba = "Finalis OSN-K Informatika 2025"

profil = f"""
- Nama lengkap   : {nama}
- Nama panggilan : {akrab}
- Asal daerah    : {asal}
- Jurusan        : {jurusan}
- Kuliah         : {kuliah}
"""

print (profil)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan dasar \n")

def run (e):

    if e >= 5:
        print (f"Angka e = {e}")

    else:
        print (f"Kecil, angka e = {e}")

run (10)
run (8)
run (5)
run (3)
run (2)
run (1)


print ("\n --- batas --- \n")




print ("\n Error Handling \n")

try:
    a = 10 / 0
    print (a)

except ZeroDivisionError:
    print ("Gagal")

else:
    print ("Berhasil")

finally:
    print ("Selesai")


print ("\n --- batas --- \n")




print ("\n Error Handling + percabangan dasar \n")

def untuk (k):

    try:
        if k < 0:
            raise ("Minus")
        
        if k >= 5:
            print (f"Besar, angka k = {k}")

        else:
            print (f"Kecil, angka k = {k}")

    except:
        print (f"Hasilnya minus, angka k = {k}")

untuk (-99)
untuk (-10)
untuk (-19)
untuk (-12)
untuk (10)
untuk (6)
untuk (3)
untuk (2)
untuk (1)


print ("\n --- batas --- \n")




print ("\n Daftar Buah-buahan \n")

daf = ["Melon", "Apel", "Buah Naga", "Semangka", "Mangga", "Pepaya"]

for i in daf:
    if i == "Buah Naga":
        continue
    print (i)


print ("\n --- batas --- \n")



print ("\n Daftar nama ikan \n")

ikan = ["Mas", "Bawal", "Piranha", "Layang", "Tuna", "Ikan Arwana", "Ikan Cupang"]

for j in ikan:
    if j == "Tuna":
        continue
    print (j)


print ("\n --- batas --- \n")



print ("\n OOP dasar \n")

class Kucing:

    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def out (self):
        print (f"- Kucing {self.nama} yang berwarna {self.warna} dan bersuara miaw miaw lucu")

hasil_1 = Kucing ("Rayyan", "Hitam")
hasil_2 = Kucing ("Fayyan", "Putih")


hasil_1.out ()
hasil_2.out ()


print ("\n --- batas --- \n")




print ("\n Struktur data sederhana \n")

data = {
    "nama" : "John Hans",
    "asal" : "Amerika Serikat",
    "usia" : 25,
    "coding" : "HTML, CSS, JavaScript dan Python",
}

print ("Nama :", data ["nama"])
print ("Asal :", data ["asal"])
print ("Usia :", data ["usia"])
print ("Coding :", data ["coding"])


print ("\n --- batas --- \n")