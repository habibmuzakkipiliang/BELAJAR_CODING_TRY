print ("\n Bikin Hello World \n")

print ("Hello World")


print ("\n --- batas --- \n")



print ("\n Variabel dasar dalam bentuk Profil \n")

nama = "Habib Muzakki"
akrab = "Habib"
asal = "Kota Serang, Banten"
kuliah = "Universitas Harkat Negeri Tegal"
jurusan = "Sekolah Vokasi D4 Teknik Informatika"
tinggi = "170 cm"
lomba = "Finalis OSN-K Informatika"
coding = "HTML, CSS, JavaScript dan Python"
wota = "JKT48"


profil = f"""
- Nama         : {nama}
- Panggil      : {akrab}
- Asal         : {asal}
- Kuliah       : {kuliah}
- Jurusan      : {jurusan}
- Tinggi badan : {tinggi}
- Lomba        : {lomba}
- Coding       : {coding}
- Wota         : {wota}
"""

print (profil)


print ("\n --- batas --- \n")




print ("\n Tipe data pemrograman \n")

print ("\n Fungsi dengan Operator dasar \n")

def tambah (x, y):
     return x + y


def kurang (w, e):
     return w - e


def kali (r, t):
     return r * t


def bagi (k, l):
     return k / l


def pangkat (e, r):
     return e ** r


def modulus (k, m):
     return k % m


hasil_1 = tambah (10, 10)
hasil_2 = kurang (10, 5)
hasil_3 = kali (10, 10)
hasil_4 = bagi (10, 5)
hasil_5 = pangkat (10, 3)
hasil_6 = modulus (10, 5)


hitung = f"""
- Hasil Tambah   : {hasil_1}
- Hasil Kurang   : {hasil_2}
- Hasil kali     : {hasil_3}
- Hasil bagi     : {hasil_4}
- Hasil pangkat  : {hasil_5}
- Hasil Modulus  : {hasil_6}
"""

print (hitung)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Switch Case 1\n")

def tan (b):
     
     match (b):
          
          case 1:
               print ("Angka 1")
               
          case 2:
               print ("Angka 2")
               
          case 3:
               print ("Angka 3")
               
          case 4:
               print ("Angka 4")
               
          case 5:
               print ("Angka 5")
               
          case _:
               print ("Kembali ke angka 0") 
               
tan (1)
tan (2)
tan (3)
tan (4)
tan (5)
tan (6)


print ("\n --- batas --- \n")



print ("\n Fungsi dengan Switch Case 2 \n")

def hun (c):
     
     match (c):
          
          case "Merah":
               print ("Warna Merah")
               
          case "Kuning":
               print ("Warna Kuning")
               
          case "Hijau":
               print ("Warna Hijau")
               
          case _:
               print ("Warna lain")
               
hun ("Merah")
hun ("Kuning")
hun ("Hijau")
hun ("Hitam")


print ("\n --- batas --- \n")




print ("\n Fungsi Percabangan Dasar \n")

def fungsi (a):
     
     if a >= 5:
          print (f"Besar, angka a = {a}")
          
     else:
          print (f"Kecil, angka a = {a}")
          
fungsi (10)
fungsi (8)
fungsi (6)
fungsi (5)
fungsi (3)
fungsi (2)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan nilai rapor \n")

def rapor (e):
     
     if e >= 90:
          print (f"A, nilai = {e}")
          
     elif e >= 80:
          print (f"B, nilai = {e}")
          
     elif e >= 70:
          print (f"C, nilai = {e}")
          
     elif e >= 60:
          print (f"D, nilai = {e}")
          
     elif e >= 50:
          print (f"E, nilai = {e}")
          
     else:
          print (f"Jelek amat, nilai = {e}")
          
rapor (100)
rapor (95)
rapor (90)
rapor (80)
rapor (70)
rapor (60)
rapor (50)
rapor (40)


print ("\n ---- batas ---- \n")