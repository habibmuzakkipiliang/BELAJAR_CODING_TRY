# Latihan Python Tes 1 


print ("\n Latihan Python Tes 1 \n")


print ("\n Pertama dulu \n")


print ("Hello World")


print ("\n --- Batas --- \n")




print ("\n Sintaks dasar \n")


teks = "Halo Indonesia"
print ("Teks :", teks)


angka = 34
print ("Angka :", angka)


desimal = 12.13
print ("Desimal :", desimal)


huruf = 'A'
print ("Huruf :", huruf)



print ("\n --- Batas --- \n")




print ("\n Tipe data dasar \n")


teks = "Halo Tes"
angka = 23 
desimal = 34.23
cek = True
cek_1 = False
huruf = 'B'


print ("Teks :", teks)
print ("Angka :", angka)
print ("Desimal :", desimal)
print ("Cek :", cek)
print ("Cek 1 :", cek_1)
print ("Huruf :", huruf)


print ("\n --- Batas --- \n")



print ("\n Array \n")


kos = [
    
    "1. Nangka",
    "2. Buah Naga",
    "3. Apel",
    "4. Salak",
    "5. Anggur"
    
    ]
    
    
for a in kos:
    print (a)
    
    
print ("\n --- Batas --- \n")




print ("\n Dictionary \n")  
    
    
objek = {
    "kursi" : "Rp 55.000",
    "meja" : "Rp 50.000",
    "gelas" : "Rp 5.000",
    "piring" : "Rp 10.000",
}


print ("Kursi :", objek ["kursi"])

print ("Meja :", objek ["meja"])

print ("Gelas :", objek ["gelas"])

print ("Piring :", objek ["piring"])


print ("\n --- Batas ---")




nama = "Habib Muzakki"
kelas = "12 Agama"
absen = "15"
sekolah = "MAN 2 KOTA SERANG"
coding = "HTML, CSS, JavaScript dan Python"
lomba = "Finalis OSN-K Informatika tahun 2025"
tinggi = "170 cm"
berat = "60 kg"


profil = f""" 

----- Profil Saya ------

- Nama         : {nama}
- Kelas        : {kelas}
- Absen        : {absen}
- Sekolah      : {sekolah}
- coding       : {coding}
- Lomba        : {lomba}
- Tinggi badan : {tinggi}
- Berat badan  : {berat}

""" 


print (profil)


print ("\n --- Batas ---")




print ("\n Operator dasar \n")


x = 10
y = 5

print ("Tambah =", x + y)
print ("Kurang =", x - y)
print ("Kali =", x * y)
print ("Pangkat =", x ** y)
print ("Bagi =", x / y)
print ("Modulus =", x % y)


print ("\n --- Batas --- \n")




print ("\n Operator Perbandingan \n")


print ("Hasil =", x > y)
print ("Hasil =", x < y)
print ("Hasil =", x >= y)
print ("Hasil =", x <= y)
print ("Hasil =", x == y)
print ("Hasil =", x != y)


print ("\n --- Batas --- \n")




print ("\n Operator Logika \n ")


print ("Hasil =", x > y and x < y)
print ("Hasil =", x < y or x > y)
print ("Hasil =", not x)
print ("Hasil =", not y)


print ("\n --- Batas --- \n")




print ("\n Switch Case 1 \n")


a = 5

match (a):
    
    case 1:
        print ("Senin")
        
    case 2:
        print ("Selasa")
    
    case 3:
        print ("Rabu")
        
    case 4:
        print ("Kamis")
        
    case 5:
        print ("Jumat")
        
    case 6:
        print ("Sabtu")
        
    case 7:
        print ("Minggu")
        
    case _:
        print ("Biasa")
        
        
print ("\n --- Batas --- \n")




print ("\n Switch Case 2 \n")


b = 3

match (b):
    
    case 1:
        print ("Iya")
        
    case 2:
        print ("Tidak")
        
    case 3:
        print ("Kadang-kadang")
        
    case 4:
        print ("Salah")
        
    case _:
        print ("Biasa")
        
        
print ("\n --- Batas --- \n")




print ("\n Percabangan Dasar \n")


a = 8

if a > 5:
    print (f"Besar, nilai = {a}")
    
else:
    print (f"Kecil, nilai = {a}")


print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan \n")


b = 3 


if b > 5:
    print (f"Besar, nilai = {b}")
    
elif b < 5:
    print (f"Kecil, nilai = {b}")
    
else:
    print (f"Semula, nilai = {b}")


print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan 1 \n")


c = 9

if c > 5:
    print (f"Besar, nilai = {c}")
    
elif c < 5:
    print (f"Kecil, nilai = {c}")
    
else:
    print (f"Semula, nilai = {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nilai Rapor \n")


skor = 90

if skor >= 100:
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
    print (f"Semula, skor = {skor}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 1 \n")


e = 8
cek = True

if cek:
    if e > 5:
        print (f"Besar, nilai = {e}")
        
    elif e < 5:
        print (f"Kecil, nilai = {e}")
        
else:
    print (f"Semula, nilai = {e}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 2 \n")


j = 3
cek = True


if cek:
    if j > 5:
        print (f"Besar, nilai = {j}")
        
    else:
        print (f"Kecil, nilai = {j}")
        
else:
    print (f"Semula, nilai = {j}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested, Join Member JKT48 tahun 2026 terbaru \n")


usia = 15
cek = True

if cek:
    if usia >= 13 and usia <= 18:
        print (f"Boleh join JKT48, usia = {usia}")
        
    elif usia > 18:
        print (f"Sudah lebih dari cukup untik gabung JKT48, usia = {usia}")
        
    else:
        print (f"Masih dibawah umur, usia = {usia}")
        
else:
    print (f"Join saat sudah cukup umur, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested, usia produktif manusia di tahun 2026 terbaru \n")


usia = 15
cek = True

if cek:
    if usia >= 15 and usia <= 64:
        print (f"Usia yang produktif, usia =  {usia}")
        
    elif usia > 64:
        print (f"Sudah tua, usia = {usia}")
        
    else:
        print (f"Belum mencapai usia produktif, usia = {usia}")
        
else:
    print (f"Masih belum cukup usia, usia = {usia}")


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




c = 16

while c < 21:
    print (f"Urutan ke - {c}")
    c = c + 1
    
    
print ("\n --- Batas --- \n")




print ("\n For Nested \n")


for a in range (3):
    for b in range (3):
        for c in range (3):
            print (f"Urutan ke - {a}, urutan ke - {b} dan urutan ke - {c}")
            
            
print ("\n --- Batas --- \n")




for d in range (4):
    for e in range (4):
        for s in range (4):
            print (f"Urutan ke - {d}, Urutan ke - {e}, Urutan ke - {s}")
            
            
print ("\n --- Batas --- \n")




for x in range (5):
    for y in range (5):
        for z in range (5):
            print (f"Urutan ke - {x}, Urutan ke - {y}, Urutan ke - {z}")
            
            
print ("\n --- Batas --- \n")




print ("\n Fungsi dasar \n")


def dasar ():
    print ("Hello World")
    
dasar ()


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan parameter 1 \n")


def dat (nama):
    print (f"Halo {nama} dari Jakarta")
    
dat ("Hayyan")
dat ("Naren")
dat ("Sar")
dat ("Nares")
dat ("Rust")


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan parameter 2 \n")


def ero (nama):
    print (f"Halo semuanya, saya {nama} dari Jakarta Utara")
    
ero ("Rafel")
ero ("Rafa")
ero ("Rael")
ero ("Nael")


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan return \n")


def tambah (a, b):
    return a + b
    
hasil = tambah (20, 20)
print ("Tambah =", hasil)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Return 1 \n")


def aro (nama):
    print (f"Halo saya {nama} dari Kota Serang")
    
hasil = aro ("Habib")
print (hasil)


print ("\n --- Batas --- \n")




print ("\n Error Handling 1 \n")


try:
    a = 10 / 0
    print (a)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("Bagus")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")





print ("\n Error Handling 2 \n")


try:
    b = 20 / 0
    print (b)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("Bagus")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 3 \n")


try:
    c = 10 + 10
    print (c)
    
except SyntaxError as c:
    print ("Gagal")
    
else:
    print ("Bagus")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 4 \n")


try:
    d = 30 + 30
    print (d)
    
except SyntaxError:
    print ("Gagal")
    
else:
    print ("Bagus")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")
