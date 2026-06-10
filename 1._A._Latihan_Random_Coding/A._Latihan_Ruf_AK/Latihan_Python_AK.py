# Latihan Python AK

print ("Hello World")


print ("\n --- Batas --- \n")




print ("\n Variabel Dasar dan Tipe data pemrograman \n")

nama = "Habib Muzakki"
panggil = "Habib"
oshi = "Michie dan Gracie JKT48"
angka = 12
desimal = 23.12
cek = True
cek_1 = False
kosong = None
daftar = [
    
    "1. Stuka",
    "2. Hellcat",
    "3. Mustang",
    "4. Corsair",
    "5. ME 262",
    "6. Ilyushin",
    "7. Tupolev",
    
    ]
    
 
print ("\n --- Batas --- \n") 
   
    
    


detail = f"""
- Nama    : {nama}
- Panggil : {panggil}
- Oshi    : {oshi}
- Angka   : {angka}
- Desimal : {desimal}
- Cek     : {cek}
- Cek 1   : {cek_1}
- Kosong  : {kosong}
- Daftar  : 
"""

print (detail)



# Tambah Elemen

daftar.append ("8. T34")
daftar.append ("9. T55")
daftar.append ("10. Stuart")
daftar.append ("11. Sherman")
daftar.append ("12. WW2")
daftar.append ("13. WW1")
daftar.append ("14. Teater Pasifik WW2")



# Hapus Elemen

daftar.remove ("12. WW2")
daftar.remove ("13. WW1")
daftar.remove ("14. Teater Pasifik WW2")



for a in daftar:
    print (a)
    
    
print ("\n --- Batas --- \n")




print ("\n Dictionary \n")

bio = {
    "tinggi" : 170,
    "berat" : 60,
    "cek" : True,
    "kosong" : None,
    "teks" : "Halo Michie dan Gracie JKT48",
    "desimal" : 23.23,
} 

print ("Tinggi :", bio ["tinggi"])
print ("Berat :", bio ["berat"])
print ("Cek :", bio ["cek"])
print ("Kosong :", bio ["kosong"])
print ("Teks :", bio ["teks"])
print ("Desimal :", bio ["desimal"])


print ("\n --- Batas --- \n")




print ("\n Profil Habib Muzakki \n")

nama = "Habib Muzakki"
panggil = "Habib"
asal = "Padang"
tinggal = "Kota Serang"
usia = "19 tahun"
tinggi = "170 cm"
berat = "60 kg"
angka = 100
desimal = 12.12
cek_3 = True


profil = f"""
- Nama lengkap   : {nama}
- Nama panggilan : {panggil}
- Asal           : {asal}
- Tempat tinggal : {tinggal}
- Tinggi badan   : {tinggi}
- Berat badan    : {berat}
- Angka          : {angka}
- Desimal        : {desimal}
- Cek 3          : {cek_3}
"""


print (profil)


print ("\n --- Batas --- \n")




print ("\n Fungsi return dengan kalkulator dasar \n")

def tambah (a, b):
    return a + b
    
    
def kurang (x, y):
    return x - y
    
    
def kali (s, d):
    return s * d
    
    
def bagi (r, t):
    return r / t
    
    
def pangkat (t, r):
    return t ** r
    
    
def modulus (j, q):
    return j % q



hasil_1 = tambah (10, 10)
hasil_2 = kurang (15, 5)
hasil_3 = kali (10, 10)
hasil_4 = bagi (20, 5)
hasil_5 = pangkat (20, 2)
hasil_6 = modulus (10, 5)



print ("Tambah =" ,hasil_1)
print ("Kurang =" ,hasil_2)
print ("Kali =" ,hasil_3)
print ("Bagi =" ,hasil_4)
print ("Pangkat =" ,hasil_5)
print ("Modulus =" ,hasil_6)