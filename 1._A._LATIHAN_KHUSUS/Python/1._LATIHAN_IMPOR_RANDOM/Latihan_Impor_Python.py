import time
import random

print ("\n Bikin Hello World \n")

print ("\n --- batas --- \n")



print ("\n Variabel dasar \n")

nama = "Habib Muzakki"
akrab = "Habib"
asal = "Kota Serang, Banten"
kuliah = "Universitas Harkat Negeri Tegal"
jurusan = "D4 Vokasi Teknik Informatika"
tinggi = "170 cm"
alumni = "MAN 2 KOTA SERANG (KELAS AGAMA)"

profil = f"""
- Nama           : {nama}
- Nama panggilan : {akrab}
- Asal           : {asal}
- Kuliah         : {kuliah}
- Jurusan        : {jurusan}
- Tinggi badan   : {tinggi}
- Alumni         : {alumni}
"""

print (profil)


print ("\n --- batas --- \n")




print ("\n Percabangan Dasar + Impor \n")

jun = random.randint (2, 10)

if jun >= 8:
     print (f"Besar, angka jun = {jun}")
     
else:
     print (f"Kecil, angka jun = {jun}")
     
     
print ("\n --- batas --- \n")



print ("\n Fungsi dengan Percabangan Lanjutan + Impor")

def dasar (hun):
     hun = random.randint (1, 20)
     time.sleep (1)
     
     if hun >= 8:
          print (f"Besar, angka hun = {hun}")
          
     elif hun >= 5:
          print (f"Tengah, angka hun = {hun}")
          
     else:
          print (f"Kecil, angka hun = {hun}")
          
dasar (10)
dasar (7)
dasar (6)
dasar (5)
dasar (3)
          
          
print ("\n --- batas --- \n")