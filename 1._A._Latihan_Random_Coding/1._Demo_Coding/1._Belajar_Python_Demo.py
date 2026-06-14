# Belajar Python Dasar

print ("Hello World")

print ("\n --- Batas --- \n")




print ("\n Variabel dan F String \n")

nama = "Habib Muzakki"
sekolah = "MAN 2 KOTA SERANG"
kelas = "Kelas 12 Agama"
asal = "Bukittinggi"
suku = "Minangkabau"
marga = "Piliang"
tinggal = "Kota Serang, Banten"

detail = f"Saya {nama}, dan saya alumni kelas {kelas} dan dari alumni sekolah {sekolah} dan asal saya dari {asal} dan suku saya dari {suku} dan marga saya adalah {marga} dan tempat tinggal di {tinggal}"

print (detail)


print ("\n --- Batas --- \n")




print ("\n Tipe data pemrograman \n")

teks = "Halo Dunia"
angka = 12
desimal = 12.34
char = 'A'
cek = True

dani = f"""
- Nama    : {teks}
- Angka   : {angka}
- Desimal : {desimal}
- Char    : {char}
- Cek     : {cek}

"""

print (dani)


print ("\n --- Batas --- \n")




print ("\n Switch Case 1 \n")

warna = "Merah"

match (warna):
    
    case "Merah":
        print ("Merah")
        
    case _:
        print ("Warna Lain")


print ("\n --- batas --- \n")




print ("\n Switch Case 2 \n")

kondisi = 2

match (kondisi):
    
    case 1:
        print ("Oke")
        
    case 2:
        print ("Mantap")
        
    case 3:
        print ("Udah oke banget")
        
    case 4:
        print ("Sedang kok")
        
    case _:
        print ("Biasa aja")
        
        
print ("\n --- batas --- \n")




print ("\n Switch Case 3 \n")


cek = "Senang"

match (cek):
    
    case "Senang":
        print ("Senang")
        
    case "Bahagia":
        print ("Bahagia")
        
    case "Sedih":
        print ("Sedih")
        
    case "Marah":
        print ("Marah")
        
    case "Kesal":
        print ("Kesal")
        
    case _:
        print ("Masih ada waktu dan tetap berusaha lagi")
        

print ("\n --- batas --- \n")




print ("\n Percabangan dasar \n")

a = 9

if a > 5:
     print (f"Besar, a = {a}")  
else:
     print (f"Kecil, a = {a}")
     
     
print ("\n --- Batas --- \n")



print ("\n Percabangan Lanjutan \n")

b = 4

if b > 5:
     print (f"besar, b = {b}")
     
elif b < 5:
     print (f"Kecil, b = {b}")
     
else:
     print (f"sama saja, b = {b}")

    
print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan 2 \n")

c = 9

if c > 5:
    print (f"Besar, c = {c}")
    
elif c < 5:
    print (f"Kecil, c = {c}")
    
else:
    print (f"Sama saja, c = {c}")


print ("\n --- Batas --- \n")




print ("\n Percabangan Nested Majemuk Kompleks 1 \n")

usia = 10
uang = 3000

if usia >= 17 and uang >= 5000:
     if cek == True:
          print (f"Udah oke, usia = {usia} dan uang = {uang}")
     
     elif usia <= 17 and uang <= 5000:
          print (f"Belum, usia = {usia} dan uang = {uang}")  
          
else:
     print (f"Masih belum dong sama sekali, usia = {usia} dan uang = {uang}")
     
     
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested Majemuk Kompleks \n")

usia = 19
cek = True

if usia >= 19 and usia <= 64:
    if cek == True:
        print (f"Sudah masuk usia produktif, usia = {usia}")
    
    elif usia > 64:
        print (f"Sudah tua dong, usia = {usia}")
        
    else:
        print (f"Remaja dong usia = {usia}")
        
else:
    print (f"Masih balita dong, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n Nested if 1 \n")

a = 10
cek = True

if cek:
     if a > 5:
          print (f"Besar, a = {a}")
          
     elif a < 5:
          print (f"Kecil, a = {a}")
          
else:
     print (f"Sama saja, a = {a}")
     
     
print ("\n --- Batas --- \n")



print ("\n Nested 2 \n")

usia = 12
cek = True

if cek:
     if usia >= 15:
          print (f"Usia kamu oke kok, usia = {usia}")
          
     else:
          print (f"Usia kamu belum oke, usia = {usia}")
          
else:
     print (f"Belum sama sekali, usia = {usia}")
     
print ("\n --- Batas --- \n")




print ("Percabangan Ladder \n")

nilai = 90

if nilai >= 90:
     print (f"A++, nilai = {nilai}")
     
elif nilai >= 80:
     print (f"B, nilai = {nilai}")
     
elif nilai >= 70:
     print (f"C, nilai = {nilai}")
     
elif nilai >= 60:
     print (f"D, nilai = {nilai}")
     
elif nilai >= 50:
     print (f"E, nilai = {nilai}")
     
else:
     print (f"Sama saja, nilai = {nilai}")
     
     
print ("\n --- Batas --- \n")




print ("For Perulangan \n")

for a in range (1, 10):
     print (f"Urutan ke - {a}")
     
     
print ("\n --- Batas --- \n")




print ("\n For Perulangan 1 \n ")

for b in range (5, 20):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- Batas --- \n")




print ("\n For Perulangan 2 \n")

for c in range (25):
    print (f"Urutan ke - {c}")


print ("\n --- Batas --- \n")




print ("\n For Perulangan 3 \n")

for d in range (11):
    print (f"Urutan ke - {d}")
    
    
print ("\n --- batas --- \n")




print ("\n While Perulangan \n")

a = 10

while a < 20:
     print (f"Urutan ke - {a}")
     a += 1
     
print ("\n --- Batas --- \n")




print ("while Perulangan 2 \n")

b = 15

while b < 30:
     print (f"Urutan ke - {b}")
     b += 1 
     
print ("\n --- Batas --- \n")




print ("\n While Perulangan 3 \n")

c = 15

while c < 30:
    print (f"Urutan ke - {c}")
    c += 1
    
    
print ("\n --- batas --- \n")




print ("\n For Nested 1 \n")

for a in range (7):
     for b in range (7):
          print (f"Luar : {a} dan Dalam : {b}")
          
print ("\n --- Batas --- \n")




print ("\n For Nested 2 \n")


for x in range (7):
    for y in range (7):
        print (f"Luar : {x} dan Dalam : {y}")
        
        
print ("\n --- batas --- \n")




print ("\n For Nested 3 \n")

for k in range (4):
    for j in range (4):
        for b in range (4):
            for n in range (4):
                print (f"K : {k}, J : {j}, B : {b}, N : {n}")
            
            
print ("\n --- batas --- \n")




print ("\n Array Oshi JKT48 \n")

oshi = [
     "1. Michie JKT48",
     "2. Gracie JKT48",
     "3. Lily JKT48",
     "4. Fritzy JKT48",
     "5. Anindya JKT48",
     "6. Christy JKT48",
     "7. Freya JKT48",
]


oshi.append ("8. Olla JKT48")
oshi.append ("9. Jessi  JKT48")
oshi.append ("10. Fiony JKT48")
oshi.append ("11. Muthe JKT48")
oshi.append ("12. Marsha JKT48")
oshi.append ("13. Eli JKT48")
oshi.append ("14. Mikaela JKT48")
oshi.append ("15. Ekin JKT48")
print (oshi)


print (len (oshi))


print ("\n Oshi JKT48 \n")

for a in oshi:
     print (a)
     
print ("\n --- batas --- \n")




print ("\n Set \n")

der = {1, 2, 3, 4, 5, 6, 7}

print (der)

print ("\n --- batas --- \n")




print ("\n Tuple \n")

den = (1, 2, 3, 4, 5, 6, 7, 8)

print (den)

print ("\n --- batas --- \n")




print ("\n Dictionary \n")

data = {
     "nama" : "Habib muzakki piliang",
     "asal" : "Bukitinggi",
     "tinggal" : "Kota Serang",
     "nomor" : 12,
     "tinggi" : 172,
     "berat" :  50,
}

print ("Nama :", data ["nama"])

print ("Asal :", data ["asal"])

print ("Tempat tinggal :", data ["tinggal"])

print ("Nomor :", data ["nomor"])

print ("Tinggi badan :", data ["tinggi"])

print ("Berat badan :", data ["berat"])


print ("\n --- batas --- \n")




print ("\n Fungsi dasar \n")

def dasar ():
     print ("Hello World")
     
dasar ()


print ("\n --- batas --- \n")




print ("\n Fungsi dasar 2 \n")

def der ():
     print ("Hello Jakarta")
     print ("Hello Bogor")
     print ("Hello Bandung")
     
der ()


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Parameter 1 \n")


def den (nama, kelas, asal):
    print (f"Halo, saya {nama}, dari kelas {kelas}, dan asal dari {asal}")
    
den ("Habib", "12 Agama", "Bukitinggi")
den ("Gema", "12 Agama", "Petir Serang")
den ("Rayyan", "11 IPA 4", "Tangerang")
den ("Fayyan", "12 IPA 5", "Jakarta Barat")


print ("\n --- batas --- \n")





print ("\n Fungsi dengan Parameter 2 \n")

def untuk (nama, tempat, suku):
     print (f"Halo saya {nama} dari {tempat} dan dari suku {suku}")
     
untuk ("Habib", "Jakarta", "Piliang")
untuk ("Hayyan", "Serang", "Jawa")
untuk ("Daffa", "Banten", "Sunda")
untuk ("Rayyan", "Semarang", "Jawa")


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Return \n")

def tambah (a, b):
     return a + b

hasil = tambah (10, 10)
print (hasil)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Return 1 \n")


def ral (nama):
    return f"Halo saya {nama} dari Jakarta Utara"
    
hasil = ral ("Rutter")
print (hasil)


print ("\n --- batas --- \n")




print ("\n Error Handling \n")


try:
    hasil = 10 / a
    print (hasil)
    
except:
    print ("Gagal")
    
finally:
    print ("Selesai")
    
    
print ("\n --- batas --- \n")





print ("\n Error Handling 2 \n")

try:
    hasil = 10 / 0
    print (hasil)
    
except ZeroDivisionError:
    print ("Gagal")
    
finally:
    print ("Selesai")
    
    
print ("\n --- batas --- \n")




print ("\n Error Handling 3 \n")

try:
    hasil = 10 + 10
    print (hasil)
    
except:
    print ("Gagal")
    
finally:
    print ("Selesai")
    
    
print ("\n --- batas --- \n")




print ("\n Percabangan Error Handling \n")

a = -50

try:
    if a < 0:
        raise ("Gagal")
        
    if a > 5:
        print (f"Lebih besar dong, angka = {a}")
        
    else:
        print (f"Lebih kecil, angka = {a}")
        
except:
    print (f"Gak boleh minus, angka = {a}")


print ("\n --- batas --- \n")




print ("\n Fungsi Percabangan Error Handling 2 \n")


def error (c):
    
    try:
        if c < 0:
            raise ("Gagal")
            
        if c > 5:
            print (f"Lebih Besar, angka = {c}")
            
        else:
            print (f"Lebih Kecil, angka = {c}")
            
    except:
        print (f"Gak boleh minus, a = {c}")
        
error (-10)
error (3)
error (-50)
error (10)


print ("\n --- batas --- \n")




print ("\n Fungsi Percabangan Error Handling \n")

def tes (b):
    
    try:
        if b < 0:
            raise ("Gagal")
            
        if b > 5:
            print (f"Oke, angka = {b}")
            
        else:
            print (f"Belum oke, angka = {b}")
            
    except:
        print (f"Gak boleh minus, b = {b}")
        
tes (-10)
tes (10)
tes (3)
tes (-50)
tes (-3)
tes (9)


print ("\n --- batas --- \n")