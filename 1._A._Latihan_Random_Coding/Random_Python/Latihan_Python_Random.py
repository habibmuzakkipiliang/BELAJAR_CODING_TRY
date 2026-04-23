# Latihan kode Python 


print ("\n Latihan kode Python \n")


print ("Hello World")




print ("\n Variabel dan Tipe data pemrograman \n")


angka = 34
teks = "Teks aja"
desimal = 34.23
char = 'A'
daftar = [
    
    "1. F4F Wildcat",
    "2. SBD Dauntless",
    "3. F4U Corsair",
    "4. F6F Hellcat",
    "5. P-51 Mustang",
    "6. P-38 Lightning",
    "7. SB2C Helldiver",
    "8. B-29 Superfortress",
    "9. B-17 Flying Fortress",
    "10. A-20 Havoc",
    "11. B-25 Mitchell",
    "12. PBY Catalina",
    
    ]
    
    
detail = f"""
- Angka   : {angka}
- Teks    : {teks}
- Desimal : {desimal}
- Char    : {char}
- Daftar  : 

"""


print (detail)
    
    
for a in daftar:
    print (a)
    
    
print ("\n --- Batas --- \n")




print ("\n Profil Habib Muzakki \n")


nama = "Habib Muzakki"
panggil = "Habib"
marga = "Piliang"
kelas = "12 Agama (Keagamaan)"
absen = 15
asal  = "Banten"
kota = "Serang"
sekolah = "MAN 2 KOTA SERANG"
darah = "B"
coding = "HTML, CSS, JavaScript"
lomba = "Finalis OSN-K Informatika tahun 2025"
usia = "19 tahun"
suku = "Minangkabau"
tinggi = "172 cm"
berat = "60 kg"


detail = f""" 

- Nama lengkap   : {nama}
- Nama panggilan : {panggil}
- Marga          : {marga}
- Kelas          : {kelas}
- Absen          : {absen}
- Asal           : {asal}
- Kota           : {kota}
- Sekolah        : {sekolah}
- Golongan darah : {darah}
- Coding         : {coding}
- Lomba          : {lomba}
- Usia           : {usia}
- Suku           : {suku}
- Tinggi badan   : {tinggi}
- Berat badan    : {berat}


"""


print (detail)


print ("\n --- Batas --- \n")




print ("\n Operator Dasar \n")


x = 20
y = 5

print ("Tambah =", x + y)
print ("Kurang =", x - y)
print ("Kali =", x * y)
print ("Bagi =", x / y)
print ("Pangkat =", x ** y)
print ("Modulus =", x % y)


print ("\n --- Batas --- \n"




print ("\n Operator Perbandingan \n")


print ("Hasil =", x > y)
print ("Hasil =", x < y)
print ("Hasil =", x >= y)
print ("Hasil =", x <= y)
print ("Hasil =", x == y)
print ("Hasil =", x != y)


print ("\n --- Batas --- \n")




print ("\n Operator Logika \n")


print ("Hasil =", x > y and x < y)
print ("Hasil =", x < y or x > y)
print ("Hasil =", not x)
print ("Hasil =", not y)


print ("\n --- Batas --- \n")




print ("\n Logika 1 \n")


a = 9

if a > 5:
    print (f"Besar, a = {a}")
    
else:
    print (f"Kecil, a = {a}")
    
    
    
print ("\n --- Batas --- \n")




print ("\n Logika 2 \n")


b = 3

if b > 5:
    print (f"Besar, b = {b}")
    
elif b < 5:
    print (f"Kecil, b = {b}")
    
else:
    print (f"Sama saja, b = {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n Logika Ladder \n")


skor = 90

if skor >= 95:
    print (f"A, skor = {skor}")
    
elif skor >= 90:
    print (f"B, skor = {skor}")
    
elif skor >= 80:
    print (f"C, skor = {skor}")
    
elif skor >= 70:
    print (f"D, skor = {skor}")
    
elif skor >= 60:
    print (f"E, skor = {skor}")
    
elif skor >= 50:
    print (f"F, skor = {skor}")
    
else:
    print (f"Jelek, skor = {skor}")
    
    
print ("\n --- Batas --- \n")




print ("\n Logika Nested 1 \n")


f = 9
cek = True


if cek:
    if f > 5:
        print (f"Besar, f = {f}")
        
    elif f < 5:
        print (f"Kecil, f = {f}")
        
else:
    print (f"Sama saja, f = {f}")
    
    
print ("\n --- Batas --- \n")




print ("\n Logika Nested 2 \n")


k = 4
cek = True

if cek:
    if k > 5:
        print (f"Besar, k = {k}")
        
    else:
        print (f"Kecil, k = {k}")
        
else:
    print (f"Sama saja, k = {k}")
    
    
print ("\n --- Batas --- \n")
