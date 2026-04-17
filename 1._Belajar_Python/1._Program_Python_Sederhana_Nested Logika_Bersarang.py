# Program Python Sederhana Nested Logika Bersarang 

print ("\n Program Python Sederhana Nested Logika Bersarang \n")


print ("\n Tipe data dasar \n")


string = "Halo Michie JKT48"
angka = 22
desimal = 33.64
cek = True
cek_1 = False
kosong = None


print ("String =", string)
print ("Angka =", angka)
print ("Desimal =", desimal)
print ("Cek =", cek)
print ("Cek 1 =", cek_1)
print ("Kosong =", kosong)


print ("\n --- Batas --- \n")




print ("\n Oshi (Member Favorit) saya \n")


array = [
    
    "1. Michie JKT48 (Utama)",
    "2. Fritzy JKT48 (Utama)",
    "3. Anindya JKT48 (Utama)",
    "4. Christy JKT48 (Utama)",
    "5. Freya JKT48",
    "6. Olla JKT48",
    "7. Jessi JKT48",
    "8. Fiony JKT48",
    "9. Muthe JKT48",
    "10. Marsha JKT48",
    "11. Eli JKT48",
    "12. Mikaela JKT48",
    "13. Yui Oguri (AKB48)",
    "14. Endo Rino (Rain Tree)",
    
    ]


for a in array:
    print (a)


print ("\n --- Batas --- \n")




print ("\n Objek (Dictionary) \n")


objek = {
    
    "nama" : "Johan Dick",
    "asal" : "Amerika Serikat",
    "job" : "Programmer dan Software Engineer",
    "coding" : "Python, JavaScript dan Dart (Flutter)",
    "tinggi_badan" : "175 cm",
}


print ("Nama :", objek ["nama"])

print ("Asal :", objek ["asal"])

print ("Kerja :", objek ["job"])

print ("Coding :", objek ["coding"])

print ("Tinggi badan :", objek ["tinggi_badan"])


print ("\n --- Batas --- \n")




print ("\n Switch Case \n")


kondisi = 8

match (kondisi):
    
    case 1:
        print ("Ada Energi")
        
    case 2:
        print ("Kenyang banget")
        
    case 3:
        print ("Kenyang parah")
        
    case 4:
        print ("Kenyang dikit")
        
    case 5:
        print ("Agak kenyang")
        
    case 6:
        print ("Agak laper")
        
    case 7:
        print ("Laper dikit")
        
    case 8:
        print ("Laper parah")
        
    case 9:
        print ("Laper banget")
        
    case 10:
        print ("Gak ada Energi")
        
    case _: 
        print ("Udah kembali aja deh ke rumah")


print ("\n --- Batas --- \n")




print ("\n Percabangan Dasar \n")

a = 9

if a > 5:
    print (f"Besar, angka = {a}")
    
else:
    print (f"Kecil, angka = {a}")


print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan \n")

b = 3

if b > 5:
    print (f"Besar, angka = {b}")
    
elif b < 5:
    print (f"Kecil, angka = {b}")
    
else:
    print (f"Semula, angka = {b}")


print ("\n --- Batas --- \n")




print ("\n Nested Percabangan If level 1 (Elif) \n")


a = 10
cek = True

if cek:
    if a > 5:
        print (f"Besar, nilai = {a}")
        
    elif a < 5:
        print (f"Kecil, nilai = {a}")
        
else:
    print (f"Semula, nilai = {a}")
    
    
print ("\n --- Batas --- \n")




b = 2
cek = True

if cek:
    if b > 5:
        print (f"Besar, nilai = {b}")
        
    elif b < 5:
        print (f"Kecil, nilai = {b}")
        
else:
    print (f"Semula, nilai = {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n Nested Percabangan If level 1 (Else) \n")


c = 9
cek = True

if cek:
    if c > 5:
        print (f"Besar, nilai = {c}")
        
    else:
        print (f"Kecil, nilai = {c}")
        
else:
    print (f"Semula, nilai = {c}")
    
    
print ("\n --- Batas --- \n")




d = 3
cek = True

if cek:
    if d > 5:
        print (f"Besar, nilai = {d}")
        
    else:
        print (f"Kecil, nilai = {d}")
        
else:
    print (f"Semula, nilai = {d}")
    
    
print ("\n --- Batas --- \n")




print ("\n Nilai Rapor Sederhana \n")


nilai = 100

if nilai >= 90:
    print (f"A, nilai = {nilai}")
    
elif nilai >= 80:
    print (f"B, nilai = {nilai}")
    
elif nilai >= 75:
    print (f"C, nilai = {nilai}")
    
elif nilai >= 70:
    print (f"D, nilai = {nilai}")
    
elif nilai >= 60:
    print (f"E, nilai = {nilai}")
    
elif nilai >= 50:
    print (f"F, nilai = {nilai}")
    
else:
    print (f"Jelek semua nilainya, nilai = {nilai}")
    
    
print ("\n --- Batas --- \n")




print ("\n Skor UTBK dan SNBT \n")


skor = 1000

if skor >= 900:
    print (f"A, nilai = {skor}")
    
elif skor >= 800:
    print (f"B, nilai = {skor}")
    
elif skor >= 750:
    print (f"C, nilai = {skor}")
    
elif skor >= 700:
    print (f"D, nilai = {skor}")
    
elif skor >= 600:
    print (f"E, nilai = {skor}")
    
elif skor >= 500:
    print (f"F, nilai = {skor}")
    
else:
    print (f"Jelek amat nilainya, nilai = {skor}")


print ("\n --- Batas --- \n")




print ("\n Percabangan Nested level 2 (Usia Produktif Manusia) \n")


usia = 19
cek = True

if cek:
    if usia >= 15 and usia <= 64:
        print (f"Masuk usia produktif, dan usia = {usia}")
        
    elif usia > 64:
        print (f" lanjut dan usia = {usia}")
        
    else:
        print (f"Bukan usia produktif, dan usia = {usia}")
        
else:
    print (f"Masih dibawah usia produktif, dan usia = {usia}")
    

print ("\n --- Batas --- \n")




print ("\n Percabangan Nested level 3 (Join ke member JKT48) \n")


umur = 18
cek = True

if cek:
    if umur >= 13 and umur <= 19:
        print (f"Kamu boleh ikut audisi JKT48, dan usia = {umur}")
        
    elif umur > 19:
        print (f"Kamu sudah matang, gabung ke JKT48, dan usia = {umur}")
        
    else:
        print (f"Gak lolos audisi JKT48, usia = {umur}")
        
else:
    print (f"Belum bisa ikut audisi JKT48, usia = {umur}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar \n")


for a in range (8):
    print (f"Urutan ke - {a}")
    
    
print ("\n --- Batas --- \n")




for b in range (6):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- Batas --- \n")




for c in range (9):
    print (f"Urutan ke - {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar \n")


a = 5

while a < 10:
    print (f"Urutan ke - {a}")
    a = a + 1
    
    
print ("\n --- Batas --- \n")




b = 8

while b < 16:
    print (f"Urutan ke - {b}")
    b = b + 1
    
    
print ("\n --- Batas --- \n")




c = 5

while c < 10:
    print (f"Urutan ke - {c}")
    c = c + 1
    
    
print ("\n --- Batas --- \n")




print ("\n For Nested \n")


for a in range (5):
    for b in range (5):
        print (f"Urutan ke - {a} dan Urutan ke - {b}")
        
        
print ("\n --- Batas --- \n")




for c in range (4):
    for d in range (4):
        print (f"Urutan ke - {c} dan Urutan ke - {d}")
        
        
print ("\n --- Batas --- \n")




for e in range (3):
    for f in range (3):
        print (f"Urutan ke - {e} dan Urutan ke - {f}")
        
        
print ("\n --- Batas --- \n")




print ("\n Fungsi dasar \n")


def dasar ():
    print ("Hello World")
    
dasar ()


print ("\n --- Batas --- \n")




def der ():
    print ("Hello World Indonesia")
    
der ()


print ("\n --- Batas --- \n")




def tart ():
    print ("Dart")
    print ("Sert")
    print ("Rart")
    print ("Dran")
    
    
tart ()


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Parameter \n")


def daf (nama):
    print ("Hello " + nama + " dari Jakarta")
    
daf ("Run")
daf ("Rurt")
daf ("Fart")
daf ("Sert")
daf ("Dan")
daf ("Rust")


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Parameter 2 \n")


def der (nama):
    print (f"Halo {nama} dari Tangerang")
    
der ("Fun")
der ("Has")
der ("Hef")
der ("Runner")
der ("Hujan")


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Return \n")


def tambah (a, b):
    return a + b
    
hasil = tambah (10, 3)
print ("Tambah =", hasil)


print ("\n --- Batas --- \n")




def deng (nama):
    return f"Halo {nama} dari Fx Sudirman"
    
hasil = deng ("Michie JKT48")
print (hasil)


print ("\n --- Batas --- \n")




print ("\n Error Handling \n")


try:
    hasil = 10 / 0
    print (hasil)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("Berhasil 100%")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")





print ("\n Error Handling 1 \n")

try:
    hasil = 20 / 0
    print (hasil)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("Berhasil 100%")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 2 \n")

try:
    hasil = 30 / 0
    print (hasil)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("Berhasil 100%")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 3 \n")

try:
    hasil = 10 + 9
    print (hasil)
    
except SyntaxError:
    print ("Gagal")
    
else:
    print ("Berhasil 100%")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 4 \n")

try:
    hasil = 10 + 4
    print (hasil)
    
except SyntaxError:
    print ("Gagal")
    
else:
    print ("Berhasil 100%")

finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")
