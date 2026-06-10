print ("\n Bikin Hello World \n")

print ("Hello World")


print ("\n --- Batas --- \n")




print ("\n Profil Habib Muzakki \n")


nama = "Habib Muzakki"
marga = "Piliang"
kelas = "12 Agama (Keagamaan)"
absen = "15"
sekolah = "MAN 2 KOTA SERANG"
coding = "HTML, CSS, JavaScript dan Python"
lomba = "Finalis OSN-K Informatika tahun 2025"
tinggi = "170 cm"
berat = "60 kg"


profil = f"""
- Nama         : {nama}
- Marga        : {marga}
- Kelas        : {kelas}
- Absen        : {absen}
- Sekolah      : {sekolah}
- Coding       : {coding}
- Lomba        : {lomba}
- Tinggi badan : {tinggi}
- Berat badan  : {berat}

"""


print (profil)


print ("\n --- Batas --- \n")




print ("\n Variabel dan Sintaks dasar \n")


nama = "John Doe"

print (nama)


kelas = "12 Agama"

print (kelas)


# Komentar 


# Komen 1


# Komen 2


print ("\n --- Batas --- \n")




print ("\n Tipe data pemrograman \n")


teks = "Halo Dunia"
angka = 12
desimal = 23.12
cek = True
kosong = None
huruf = 'A'
array = [
    
    "1. Bukittinggi",
    "2. Padang",
    "3. Padang Panjang",
    "4. Batusangkar",
    "5. Solok",
    "6. Payakumbuh",
    "7. Sijunjung",
    "8. Sitiung",
    "9. Timpeh",
    "10. Silaut",
    
    ]
    
    
print ("Teks =", teks)
print ("Angka =", angka)
print ("Desimal =", desimal)
print ("Cek =", cek)
print ("Kosong =", kosong)
print ("Huruf =", huruf)
print ("Array :")


for a in array:
    print (a)
    
    
print ("\n --- Batas --- \n")




print ("\n Tuple \n")


daf = (
    
    "1. Bukittinggi",
    "2. Padang",
    "3. Padang Panjang",
    "4. Batusangkar",
    "5. Solok",
    "6. Payakumbuh",
    "7. Sijunjung",
    "8. Sitiung",
    "9. Timpeh",
    "10. Silaut",
    
    
    )
    
    
for e in daf:
    print (e)
    
    
print ("\n --- Batas --- \n")




print ("\n Set \n")


der = {
    "1. Bukittinggi",
    "2. Padang",
    "3. Padang Panjang",
    "4. Batusangkar",
    "5. Solok",
    "6. Payakumbuh",
    "7. Sijunjung",
    "8. Sitiung",
    "9. Timpeh",
    "10. Silaut", 
}


for j in der:
    print (j)
    
    
print ("\n --- Batas --- \n")




print ("\n Dictionary \n")


data = {
    "nama" : "Johan",
    "asal" : "Serang",
    "usia" : "25 tahun",
    "kerja" : "Software Engineer",
}


print ("Nama :", data ["nama"])

print ("Asal :", data ["asal"])

print ("Usia :", data ["usia"])

print ("Kerja :", data ["kerja"])


print ("\n --- Batas --- \n")




print ("\n Operasi Dasar \n")


x = 50
y = 5


print ("Tambah =", x + y)
print ("Kurang =", x - y)
print ("Kali =", x * y)
print ("Pangkat =", x ** y)
print ("Modulus =", x % y)


print ("\n --- Batas --- \n")




print ("\n Operasi Perbandingan \n")


print ("Hasil =", x > y)
print ("Hasil =", x < y)
print ("Hasil =", x <= y)
print ("Hasil =", x >= y)
print ("Hasil =", x == y)
print ("Hasil =", x != y)


print ("\n --- Batas --- \n")




print ("\n Operator Logika \n")


print ("Hasil =", x > y and x < y)
print ("Hasil =", x < y or x > y)
print ("Hasil =", not x)
print ("Hasil =", not y)


print ("\n --- Batas --- \n")




print ("\n Switch Case \n")


nilai = 9

match (nilai):
    
    case 1:
        print ("1")
        
    case 2:
        print ("2")
        
    case 3:
        print ("3")
        
    case 4:
        print ("4")
        
    case 5:
        print ("5")
        
    case 6:
        print ("6")
        
    case 7:
        print ("7")
        
    case 8:
        print ("8")
        
    case 9:
        print ("9")
        
    case 10:
        print ("10")
        
    case _:
        print ("Semula")
        
        
print ("\n --- Batas --- \n")




print ("\n Percabangan Dasar \n")


a = 9

if a > 5:
    print (f"Besar, nilai = {a}")
    
else:
    print (f"Kecil, nilai = {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan dasar 1 \n")


h = 3

if h > 5:
    print (f"Besar, h = {h}")
    
else:
    print (f"Kecil, h = {h}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan dasar 1 \n")


k = 3

if k > 5:
    print (f"Besar, k = {k}")
    
else:
    print (f"Kecil, k = {k}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan \n")


s = 9

if s > 5:
    print (f"Besar, s = {s}")
    
elif s < 5:
    print (f"Kecil, s = {s}")
    
else:
    print (f"Sama saja, s = {s}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan lanjutan 1 \n")


d = 3

if d > 5:
    print (f"Besar, d = {d}")
    
elif d < 5:
    print (f"Kecil, d = {d}")
    
else:
    print (f"Sama saja, d = {d}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 1 \n")


x = 9
cek = True

if cek:
    if x > 5:
        print (f"Besar, x = {x}")
        
    elif x < 5:
        print (f"Kecil, x = {x}")
        
else:
    print (f"Sama saja, x = {x}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 2 \n")


y = 3
cek = True

if cek:
    if y > 5:
        print (f"Besar, y = {y}")
        
    else:
        print (f"Kecil, y = {y}")
        
else:
    print (f"Sama saja, y = {y}")


print ("\n --- Batas --- \n")