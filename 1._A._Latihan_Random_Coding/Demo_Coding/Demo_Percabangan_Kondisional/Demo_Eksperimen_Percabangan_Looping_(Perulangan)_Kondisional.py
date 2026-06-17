print ("\n Demo Percabangan Looping (Perulangan) Kondisional \n")


print ("\n Switch Case 1 \n")

warna = "Merah"

match (warna):
    
    case "Merah":
        print ("Merah")
        
    case _: 
        print ("Warna lain")
        
        
print ("\n --- Batas --- \n")




print ("\n Switch Case 2 \n")

hari = "Senin"

match (hari):
    
    case "Senin":
        print ("Senin")
        
    case "Selasa":
        print ("Selasa")
        
    case "Rabu":
        print ("Rabu")
    
    case "Kamis":
        print ("Kamis")
        
    case "Jumat":
        print ("Jumat")
        
    case _:
        print ("Hari Libur")
        
        
print ("\n --- Batas --- \n")




print ("\n Switch Case 2 \n")

kondisi = 2

match (kondisi):
    
    case 1:
        print ("Senang")
        
    case 2:
        print ("Bahagia")
        
    case 3:
        print ("Oke")
        
    case 4:
        print ("Sedih")
        
    case 5:
        print ("Marah")
        
    case 6:
        print ("Kesal")
        
    case 7:
        print ("Jengkel")
        
    case _:
        print ("Biasa aja")
        
        
print ("\n --- Batas --- \n")




print ("\n Switch Case 3 \n")

hobi = "Wota JKT48"

match (hobi):
    
    case "Main Game":
        print ("Main Game")
        
    case "Wota JKT48":
        print ("Wota JKT48")
        
    case "Denger Musik":
        print ("Denger Musik")
        
    case "Denger Lagu JKT48":
        print ("Denger Lagu JKT48")
        
    case "Denger Lagu Padang":
        print ("Denger Lagu Padang")
        
    case "Nonton Film":
        print ("Nonton Film")
        
    case "Mancing":
        print ("Mancing")
    
    case "Santai di Rumah":
        print ("Santai di Rumah")
        
    case "Trafelling ke Kota Jakarta dan Fx Sudirman":
        print ("Trafelling ke Kota Jakarta dan Fx Sudirman")
        
    case _:
        print ("Masuk kerja lagi")
        
        
print ("\n --- Batas --- \n")




print ("\n Percabangan dasar \n")


a = 9

if a > 5:
    print (f"Besar, a = {a}")
    
else:
    print (f"Kecil, a = {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan 1 \n")

skor = 100

if skor >= 90:
    print (f"Oke, skor = {skor}")
    
elif skor >= 50:
    print (f"Setengah, skor = {skor}")
    
else:
    print (f"Jelek, skor = {skor}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan 2 \n")

nilai = 95

if nilai >= 90:
    print (f"Oke, nilai = {nilai}")
    
elif nilai >= 50:
    print (f"Setengah, nilai = {nilai}")
    
else:
    print (f"Jelek, nilai = {nilai}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Ladder \n")

nilai = 100

if nilai == 100:
    print (f"A++, nilai = {nilai}")
    
elif nilai == 95:
    print (f"A+, nilai = {nilai}")
    
elif nilai == 90:
    print (f"A, nilai = {nilai}")
    
elif nilai == 85:
    print (f"B+, nilai = {nilai}")
    
elif nilai == 80:
    print (f"B, nilai = {nilai}")
    
elif nilai == 75:
    print (f"C, nilai = {nilai}")
    
elif nilai == 70:
    print (f"D, nilai = {nilai}")
    
else:
    print (f"E, nilai = {nilai}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabagan Nested 1 \n")

usia = 20
cek = True

if cek:
    if usia >= 17:
        print (f"Boleh ambil SIM, usia = {usia}")
        
    else:
        print (f"Masih kecil usianya")
        
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 2 \n")

login = True
token = False

if login == True:
    if token == True:
        print ("Oke, Lanjut")
        
    else:
        print ("Token salah")
        
else:
    print ("Masih belum sih")
    
    
print ("\n --- Batas --- \n")





print ("\n Percabangan Nested 3 \n")

sim = True
usia = 19


if sim == True:
    if usia >= 17:
        print (f"Boleh ikut dan bikin sim, usia = {usia}")
        
    elif sim == False:
        print (f"Gak boleh bikin sim, usia = {usia}")
        
else:
    print (f"Masih belum, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 4 \n")

tol = True
loket = False

if tol == True:
    if loket == True:
        print ("Boleh login tol")
        
    else:
        print ("Salah login")
        
else:
    print ("Masih belum bisa")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 3 \n")

usia = 20
cek = True

if cek == True:
    if usia >= 19:
        print (f"Oke, usia = {usia}")
        
    elif cek == False:
        print (f"Belum Oke, usia = {usia}")
        
else:
    print (f"Masih belum dong")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 4 \n")

usia = 19
cek = True

if usia >= 17:
    if cek == True:
        print (f"Boleh ambil SIM, usia = {usia}")
        
    elif usia < 17:
        print (f"Belum boleh ambil SIM, usia = {usia}")
        
else:
    print (f"Masih kecil usianya, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 5 \n")

usia = 16
cek = True

if usia >= 17:
    if cek == True:
        print (f"Boleh punya SIM, usia = {usia}")
        
    else:
        print (f"Belum boleh punya sim, usia = {usia}")
        
else:
    print (f"Di lain waktu ya, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested Majemuk Kompleks \n")

usia = 19
uang = 500000

if usia >= 16 and uang >= 30000000:
    if cek == True:
        print (f"Uang anda cukup untuk hidup, usia = {usia} dan uang = {uang}")
        
    elif usia <= 16 and uang <= 30000000:
        print (f"Belum untuk kebutuhan, usia = {usia} dan uang {uang}")
        
    else:
        print (f"Belum masih kecil kamu, usia = {usia} dan uang {uang}")
        
else:
    print (f"Belum masih kurang banget, usia = {usia} dan uang = {uang}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested Majemuk Kompleks 2 \n")

usia = 19
uang = 300000

if usia >= 25 and uang >= 30000000:
    if cek == True:
        print (f"Sudah sukses, usia = {usia} dan uang {uang}")
        
    elif usia <= 25 and uang <= 30000000:
        print (f"Belum sukses, usia = {usia} dan uang = {uang}")

else:
    print (f"Masih ada waktu, usia = {usia} dan uang = {uang}")


print ("\n --- Batas --- \n")




print ("\n For Perulangan \n")

for a in range (1, 11):
    print (f"Urutan ke - {a}")
    
    
print ("\n --- Batas --- \n")




print ("\n For Perulangan 1 \n")

for b in range (5, 26):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- Batas --- \n")





print ("\n For Perulangan 2 \n")

for c in range (20):
    print (f"Urutan ke - {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n For Perulangan 3 \n")

for d in range (10, 26):
    print (f"Urutan ke - {d}")
   

print ("\n --- Batas --- \n")




print ("\n While Perulangan 1 \n")

a = 10

while a < 20:
    print (f"Urutan ke - {a}")
    a += 1 
    
    
print ("\n --- Batas --- \n")
   
   
   
   
print ("\n While Perulangan 2 \n")

b = 20

while b < 30:
    print (f"Urutan ke - {b}")
    b += 1
    
    
print ("\n --- Batas --- \n")




print ("\n While Perulangan 3 \n")

c = 15

while c < 25:
    print (f"Urutan ke - {c}")
    c += 1
    
    
print ("\n --- Batas --- \n")




print ("\n While Perulangan 4 \n")

d = 20

while d < 35:
    print (f"Urutan ke - {d}")
    d += 1
    
    
print ("\n --- Batas --- \n")




print ("\n For Nested \n")

for a in range (4):
    for b in range (4):
        for c in range (4):
            for d in range (4):
                print (f"A : {a}, B : {b}, C : {c}, D : {d}")
                
                
print ("\n --- Batas --- \n")
