# Latihan Project Sederhana Python yang kedua

print ("\n Latihan Project Sederhana Python yang kedua \n")

print ("Hello World")


print ("\n --- Batas --- \n")




print ("\n Input dan Output \n")

nama = input ("Nama kamu siapa ? ")
asal = input ("Dari mana asal kamu ? ")
kerja = input ("Kamu kerja apa ? ")
hobi = input ("Hobi kamu apa ? ")
tinggi = float (input ("Tinggi badan kamu berapa ? "))
berat = float (input ("Berat badan kamu berapa ? "))
usia = int (input ("Usia kamu berapa ? "))
coding = input ("Coding yang kamu bisa ? ")



profil = f""" 

Nama         : {nama}
Asal         : {asal}
Kerja        : {kerja}
Hobi         : {hobi}
Tinggi Badan : {tinggi}
Badan badan  : {berat}
Usia         : {usia}
Coding       : {coding}


"""


print (profil)


print ("\n --- Batas --- \n")




print ("\n Variabel dasar \n")


teks = "Halo Dunia"
print (teks)


angka = 18
print (angka)


desimal = 23.21
print (desimal)


kosong = None
print (kosong)


cek = True
print (cek)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Switch Case 1 \n")

def jon (hari):
    
    match (hari):
        
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
            
        case _:
            print ("Hari Libur")
            
jon (2)
jon (9)
jon (3)
jon (7)
jon (6)
jon (4)
jon (2)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Switch Case 2 \n")

def per (warna):
    
    match (warna):
        
        case "Merah":
            print ("Merah")
            
        case "Biru":
            print ("Biru")
            
        case "Kuning":
            print ("Kuning")
            
        case "Coklat":
            print ("Coklat")
         
        case "Biru Laut":
            print ("Biru Laut")
            
        case _:
            print ("Warna lain")
            
            
per ("Merah")
per ("Kuning")
per ("Coklat")
per ("Biru")
per ("Biru Laut")
per ("Aqua")
per ("Aquamarine")


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan percabangan \n")

def rush (a):
    
    if a > 5:
        print (f"Besar, angka a = {a}")
        
    else:
        print (f"Kecil, angka a = {a}")
        
        
rush (10)
rush (3)
rush (7)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Lanjutan \n")


def run (b):
    
    
    if b > 5:
        print (f"Besar, angka b = {b}")
        
    elif b < b:
        print (f"Kecil, angka b = {b}")
        
    else:
        print (f"Sama saja, angka = {b}")
        
        
run (10)
run (3)
run (9)
run (2)
run (10)


print ("\n --- Batas --- \n")




print ("\n Fungsi dengan Percabangan Nilai Rapor \n")

def tun (nilai):
    
    if nilai >= 90:
        print (f"A, nilai = {nilai}")
        
    elif nilai >= 80:
        print (f"B, nilai = {nilai}")
        
    elif nilai >= 70:
        print (f"C, nilai = {nilai}")
        
    elif nilai >= 60:
        print (f"D, nilai = {nilai}")
        
    elif nilai >= 50:
        print (f"E, nilai = {nilai}")
        
    else:
        print (f"Default, nilai = {nilai}")
        
        
tun (100)
tun (90)
tun (80)
tun (70)
tun (60)


print ("\n --- Batas --- \n")



print ("\n Fungsi dengan Percabangan Nested 1 \n")

def tes (usia):
     
     cek = True
     
     if usia >= 15:
          if cek == True:
               print (f"Usia kamu oke kok, usia = {usia}")
               
          elif usia <= 15:
               print (f"Usia kamu belum oke, usia = {usia}")
               
     else:
          print (f"Masih dibawah umur, usia = {usia}")
          
          
tes (20)
tes (14)
tes (28)
tes (23)


print ("\n --- Batas --- \n")