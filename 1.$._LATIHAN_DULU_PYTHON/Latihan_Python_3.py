print ("Hello World")


print ("\n --- batas --- \n")





print ("\n variabel dasar \n")

teks_1 = "Halo dunia"
print (teks_1)


angka_1 = 12
print (angka_1)


print ("\n --- batas --- \n")





print ("\n F String \n")

nama = "Habib Muzakki"
asal = "Kota Serang, Banten"
jurusan = "D4 Vokasi Teknik Informatika"
kuliah = "Universitas Harkat Negeri Tegal"
coding = "HTML, CSS, JavaScript dan Python"
lomba = "Finalis OSN-K Informatika 2025"
alumni = "MAN 2 KOTA SERANG (Kelas Agama)"
bidang = "Web Developer dan Python"


profil = f"""
- Nama lengkap = {nama}
- Asal daerah  = {asal}
- Jurusan      = {jurusan}
- Lomba        = {lomba}
- Alumni       = {alumni}
- Bidang       = {bidang}
"""

print (profil)


print ("\n --- batas --- \n")





print ("\n Operator dasar \n")

def tambah (x, y):
    return x + y


def kurang (x, y):
    return x - y


def kali (x, y):
    return x * y


def pangkat (x, y):
    return x ** y


hasil_a = tambah (10, 10)
hasil_b = kurang (15, 10)
hasil_c = kali (10, 10)
hasil_d = pangkat (10, 3)


hitung = f"""
- Tambah  = {hasil_a}
- Kurang  = {hasil_b}
- Kali    = {hasil_c}
- Pangkat = {hasil_d}
"""

print (hitung)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Dasar \n")

def un (a):

    if a >= 5:
        print (f"Besar, angka a = {a}")

    else:
        print (f"Kecil, angka a = {a}")

un (10)
un (6)
un (7)
un (5)
un (3)
un (4)
un (1)
un (2)


print ("\n --- batas --- \n")





print ("\n Fungsi dengan Percabangan Lanjutan \n")

def tun (b):

    if b >= 8:
        print (f"Besar, angka b = {b}")

    elif b >= 5 :
        print (f"Tengah, angka a = {b}")

    else:
        print (f"Kecil, angka a = {b}")

tun (10)
tun (9)
tun (8)
tun (7)
tun (5)
tun (4)
tun (3)
tun (2)


print ("\n --- batas --- \n")




print ("\n Error Handling \n")

try:
    a = 10 / 0
    print (a)

except ZeroDivisionError:
    print ("gagal")

else:
    print ("Berhasil")

finally:
    print ("Selesai")


print ("\n --- batas --- \n")



print ("\n Error Handling \n")

try:
    b = 10 + 10
    print (b)

except:
    print ("Gagal")

else:
    print ("Berhasil")

finally:
    print ("Selesai")



print ("\n Raise Error Handling \n")

def dun (k):

    try:

        if k < 0:
            raise ("Gagal")
        
        if k >= 8:
            print (f"Besar, angka k = {k}")

        elif k >= 5:
            print (f"Tengah, angka k = {k}")

        else:
            print (f"Kecil, angka k = {k}")

    except:
        print (f"Angka minus, angka k = {k}")

dun (-10)
dun (-8)
dun (-4)
dun (10)
dun (9)
dun (7)
dun (5)
dun (4)
dun (2)
dun (1)


print ("\n --- batas --- \n")




print ("\n For dasar \n")

for a in range (11):
    print (f"Urutan ke - {a}")


print ("\n --- batas --- \n")



for b in range (1, 11):
    print (f"Urutan ke - {b}")


print ("\n --- batas --- \n")



for c in range (5, 11):
    print (f"Urutan ke - {c}")


print ("\n --- batas --- \n")




print ("\n While dasar \n")

a = 1

while a < 11:
    print (f"Urutan ke - {a}")
    a = a + 1


print ("\n --- batas --- \n")




print ("\n While dasar 2 \n")

b = 10

while b > 0:
    print (f"Urutan ke - {b}")
    b = b - 1


print ("\n --- batas --- \n")



print ("\n For Nested \n")

for a in range (1, 5):
    for b in range (1, 5):
        print (f"Luar : {a} dan Dalam : {b}")


print ("\n --- batas --- \n")




print ("\n For Nested 3 \n")

for x in range (1, 4):
    for y in range (1, 4):
        for z in range (1, 4):
            print (f"x : {x}, y : {y}, z : {z}")


print ("\n --- batas --- \n")