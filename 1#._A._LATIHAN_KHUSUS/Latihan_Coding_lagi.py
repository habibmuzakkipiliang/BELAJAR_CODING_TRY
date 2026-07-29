# Bikin awal dulu

print ("Hello World")

print ("\n --- batas --- \n")



# variabel dasa


a = "Halo dunia"
print (a)


print ("\n --- batas --- \n")



# tipe data pemrograman

teks = "Halo dunia"
angka = 12
desimal = 1.12
cek = True
kosong = None
char = 'A'

tipe = f"""
- Teks : {teks}
- Angka : {angka}
- Desimal : {desimal}
- Cek : {cek}
- Kosong : {kosong}
"""

print (tipe)


print ("\n --- batas --- \n")




# Cek tipe pemrograman

teks = "Halo dunia"
angka = 12
desimal = 1.12
cek = True
kosong = None

cek_tipe = f"""
- Teks : {type (teks)}
- Angka : {type (angka)}
- Desimal : {type (desimal)}
- Cek : {type (cek)}
- Kosong : {type (kosong)}
"""

print (cek_tipe)

print ("\n --- batas --- \n")



# Kalkulator dengan fungsi + input

x = int (input ("Masukkan angka x :"))
y = int (input ("Masukkan angka y :"))

def tambah (x, y):
     return x + y

def kurang (x, y):
     return x - y

def kali (x, y):
     return x * y

def pangkat (x, y):
     return x ** y

def bagi (x, y):
     return x / y

def modulus (x, y):
     return x % y


print ("Hasil tambah =", tambah (x, y))
print ("Hasil kurang =", kurang (x, y))
print ("Hasil kali =", kali (x, y))
print ("Hasil pangkat = ", pangkat (x, y))
print ("Hasil bagi =", bagi (x, y))
print ("Hasil modulus =", modulus (x, y))


print ("\n --- batas --- \n")



# noob 

ml = int (input ("Masukkan angka ml :"))
mp = int (input ("Masukkan angka mp :"))

total = ml * mp

print (f"Total jumlah = {total}")

print ("\n --- batas -- \n")




# Percabangan dasar

a = int (input ("Masukkan angka a = "))

if a >= 5:
     print (f"Besar, angka a = {a}")

else:
     print (f"kecil, angka a = {a}")


print ("\n --- batas --- \n")




# Fungsi dengan percabangan dasar

an = int (input ("Masukkan angka an :"))

def dasar (an):

     if an >= 5:
          print (f"besar, angka an = {an}")

     else:
          print (f"kecil, angka an = {an}")

dasar (an)
dasar (an)
dasar (an)
dasar (an)


print ("\n --- batas --- \n")