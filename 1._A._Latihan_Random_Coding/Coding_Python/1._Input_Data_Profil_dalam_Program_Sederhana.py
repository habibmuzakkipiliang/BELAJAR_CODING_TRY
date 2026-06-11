# Input Data Profil dalam Program Sederhana di Python


print ("\n Input Data Profil dalam Program Sederhana  di Python \n")


nama = input ("Masukkan nama : ")
kelas = input ("Masukkan kelas : ")
absen = int (input ("Masukkan nomor absen : "))
sekolah = input ("Masukkan sekolah : ")
tinggi = input ("Masukkan tinggi badan : ")
berat =  input ("Masukkan berat badan : ")
coding = input ("Masukkan coding kamu : ")
lomba = input ("Masukkan lomba yang pernah kamu ikuti : ")
darah = input ("Masukkan golongan darah kamu : ")
hobi = input ("Masukkan hobi kamu : ")


detail = f"""

- Nama           : {nama}
- Kelas          : {kelas}
- Nomor Absen    : {absen}
- Sekolah        : {sekolah}
- Tinggi Badan   : {tinggi}
- Berat Badan    : {berat}
- Coding         : {coding}
- Lomba          : {lomba}
- Golongan darah : {darah}
- Hobi           : {hobi}


"""

print (detail)


print ("\n --- Batas --- \n")




x = int (input ("Masukkan angka x : "))
y = int (input ("Masukkan angka y : "))


print ("\n Operasi Dasar \n")


print ("Tambah =", x + y)
print ("Kurang =", x - y)
print ("Kali =", x * y)
print ("Bagi =", x / y)
print ("Pangkat =", x ** y)
print ("Modulus =", x % y)


print ("\n --- Batas --- \n")




print ("\n Operasi Perbandingan \n")

print ("Hasil =", x > y)
print ("Hasil =", x < y)
print ("Hasil =", x == y)
print ("Hasil =", x != y)
print ("Hasil =", x >= y)
print ("Hasil =", x <= y)


print ("\n --- Batas --- \n")




print ("\n Operasi Logika \n")


print ("Hasil =", x > y and x < y)
print ("Hasil =", x > y or x < y)
print ("Hasil =", not x)
print ("Hasil =", not y)


print ("\n --- Batas --- \n")



print ("\n Switch Case 1 \n")


hari = input ("Masukkan hari : ")


match (hari):
    
    case "senin":
        print ("senin")
        
    case "selasa":
        print ("selasa")
        
    case "rabu":
        print ("rabu")
        
    case "kamis":
        print ("kamis")
        
    case "jumat":
        print ("jumat")
        
    case _:
        print ("libur")
        
        
print ("\n --- Batas --- \n")




print ("\n Switch Case 2 \n")


kondisi = int (input ("Masukkan kondisi dalam angka : "))


match (kondisi):
    
    case 1:
        print ("Iya")
        
    case 2:
        print ("Tidak")
    
    case 3:
        print ("Kadang-kadang")
        
    case 4:
        print ("Bukan")
        
    case _:
        print ("semula")
        
        
print ("\n --- Batas --- \n")




print ("\n Hasil Logika Sederhana \n")


hasil = int (input ("Masukkan logic 1 : "))


if hasil > 70:
    print (f"Lulus dong, skor = {hasil}")
    
elif hasil < 50:
    print (f"Belum dong, skor = {hasil}")
    
else:
    print (f"Jangan dulu, skor = {hasil}")
    
    
print ("\n --- Batas --- \n")




print ("\n Hasil Logika 1 \n")


logic = int (input ("Masukkan logic 2 :"))


if logic > 5:
    print (f"Oke dong, logic = {logic}")
    
else:
    print (f"Belum dong, logic = {logic}")
    
    
print ("\n --- Batas --- \n")




print ("\n Logika Rapor Sederhana \n")


rapor = int (input ("Masukkan nilai rapor : "))


if rapor >= 90:
    print (f"A, skor = {rapor}")
    
elif rapor >= 80:
    print (f"B, skor = {rapor}")
    
elif rapor >= 70:
    print (f"C, skor = {rapor}")
    
elif rapor >= 60:
    print (f"D, skor = {rapor}")
    
elif rapor >= 50:
    print (f"E, skor = {rapor}")
    
elif rapor >= 40:
    print (f"F, skor = {rapor}")
    
else:
    print (f"Jelek amat, skor = {rapor}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 1 \n")


tes = int (input ("Masukkan tes 1 :"))
cek = True


if cek:
    if tes > 5:
        print (f"Oke, tes = {tes}")
        
    else:
        print (f"Belum boleh dong, tes = {tes}")
        
else:
    print (f"Jangan dulu dong, tes = {tes}")
    
    
print ("\n --- Batas --- \n")




print ("\n Pendaftaran join JKT48 \n")


usia = int (input ("Masukkan usia kamu untuk Join JKT48 : "))
cek = True


if cek:
    if usia >= 13 and usia <= 19:
        print (f"Boleh join JKT48, usia = {usia}")
        
    elif usia > 19:
        print (f"Sudah lebih dari cukup untuk join JKT48, usia = {usia}")
        
    else:
        print (f"Belum boleh ikut join JKT48, usia = {usia}")
        
else:
    print (f"Gak lolos join JKT48, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n Usia Produktif manusia \n")


usia = int (input ("Masukkan usia kamu : "))
cek = True

if cek:
    if usia >= 15 and usia <= 64:
        print (f"Usia produktif manusia, usia = {usia}")
        
    elif usia > 64:
        print (f"Sudah tua, usia = {usia}")
        
    else:
        print (f"Belum masuk usia produktif, usia = {usia}")
        
else:
    print (f"Masih kecil usianya, usia = {usia}")


print ("\n --- Batas --- \n")




print ("\n For dasar \n")


for a in range (11):
    print (f"Urutan ke - {a}")
    
    
print ("\n --- Batas --- \n")




for b in range (11):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- Batas --- \n")




for c in range (11):
    print (f"Urutan ke - {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar \n")


a = 5

while a < 11:
    print (f"Urutan ke - {a}")
    a = a + 1
    
    
print ("\n --- Batas --- \n")




b = 10 

while b < 16:
    print (f"Urutan ke - {b}")
    b = b + 1
    
    
print ("\n --- Batas --- \n")




c = 15

while c < 21:
    print (f"Urutan ke - {c}")
    c = c + 1
    
    
print ("\n --- Batas --- \n")




print ("\n For Nested \n")


for a in range (11):
    for b in range (11):
        for c in range (11):
            print (f"Urutan ke - {a}, urutan ke - {b}, urutan ke - {c}")
            
            
print ("\n --- Batas --- \n")




for x in range (11):
    for y in range (11):
        for z in range (11):
            print (f"Urutan ke - {x}, urutan ke - {y}, urutan ke - {z}")
            
            
print ("\n --- Batas --- \n")




print ("\n Array 1 \n")


bahasa = [
    
    
    "1. Python",
    "2. JavaScript",
    "3. TypeScript",
    "4. HTML",
    "5. CSS",
    "6. Dart (Flutter)",
    
    ]
    
    
for a in bahasa:
    print (a)
    
    
print ("\n --- Batas --- \n")




print ("\n Array 2 \n")


ormas = [
    
    "1. Muhammadiyah",
    "2. Persis",
    "3. MUI",
    
    ]
    
    
for b in ormas:
    print (b)
    
    
print ("\n --- Batas --- \n")




print ("\n Dictionary 1 \n")


tes = {
    
    "cilok" : "Rp 1.000",
    "siomay" : "Rp 2.000",
    "batagor" : "Rp 2.000",
    "ayam_tusuk" : "Rp 3.000",
    "bakso" : "Rp 5.000",
    "telur_gulung" : "Rp 1.00",
} 


print ("Cilok :", tes ["cilok"])

print ("Siomay :", tes ["siomay"])

print ("Batagor :", tes ["batagor"])

print ("Ayam Tusuk :", tes ["ayam_tusuk"])

print ("Bakso :", tes ["bakso"])

print ("Telur gulung :", tes ["telur_gulung"])


print ("\n --- Batas --- \n")




print ("\n Fungsi dasar \n")


def dasar ():
    print ("Hello World")
    
dasar ()


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Parameter \n")


def das (nama):
    print (f"Halo aku {nama}, dari kota serang")
    
das ("Hayyan")
das ("Dani")
das ("Rayyan")
das ("Ivan")
das ("Rani")
das ("Ivaner")
das ("Yon")


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Return \n")


def tambah (x, y):
    return x + y
    
hasil = tambah (10, 10)
print ("Tambah =", hasil)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan return 1 \n")


def der (nama):
    return f"Halo saya {nama}, dari Jakarta"
    
hasil = der ("Ivan")
print (hasil)


print ("\n --- Batas --- \n")




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
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 1 \n")

try:
    b = 20 / 0
    print (b)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("Berhasil")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 2 \n")


try:
    c = 10 + 10
    print (c)
    
except SyntaxError:
    print ("Gagal")
    
else:
    print ("Berhasil")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 3 \n ")


try:
    d = 20 + 20
    print (d)
    
except SyntaxError:
    print ("Gagal")
    
else:
    print ("Berhasil")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")
