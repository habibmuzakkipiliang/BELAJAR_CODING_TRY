print ("\n Profil Habib Muzakki Piliang \n")


nama = "Habib Muzakki"
panggil = "Habib"
marga = "Piliang"
suku = "Minangkabau"
coding = "HTML, CSS, JavaScript dan Python"
lomba = "Finalis OSN-K Informatika tahun 2025"
tinggi = "170 cm"
berat = "60 kg"
darah = "B"
fans = "JKT48"
oshi = "Michie, Fritzy, Anindya, Christy, Freya JKT48"


profil = f"""

- Nama lengkap   : {nama}
- Nama panggilan : {panggil}
- Marga          : {marga}
- Suku           : {suku}
- Coding         : {coding}
- Lomba          : {lomba}
- Tinggi badan   : {tinggi}
- Berat badan    : {berat}
- Golongan darah : {darah}
- Fans           : {fans}
- Oshi JKT48     : {oshi}

"""


print (profil)


print ("\n --- Batas --- \n")




print ("\n Switch Case \n")


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
        print ("Libur")
        
        
print ("\n --- Batas --- \n")




print ("\n Percabangan dasar \n")


a = 9

if a > 5:
    print (f"Besar, a = {a}")
    
else:
    print (f"Kecil, a = {a}")


print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan \n")


k = 3

if k > 5:
    print (f"Besar, k = {k}")
    
elif k < 5:
    print (f"Kecil, k = {k}")

else:
    print (f"Sama saja, k = {k}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Ledder \n")

s = 7

if s >= 9:
    print (f"A, skor = {s}")
    
elif s >= 8:
    print (f"B, skor = {s}")
    
elif s >= 7:
    print (f"C, skor = {s}")
    
elif s >= 6:
    print (f"D, skor = {s}")
    
elif s >= 5:
    print (f"E, skor = {s}")
    
else:
    print (f"Jelek, skor = {s}")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested, usia produktif 1 \n")


usia = 19
cek = True

if cek:
    if usia >= 15 and usia <= 64:
        print (f"Sudah masuk usia produktif, usia = {usia}")
        
    elif usia > 64:
        print (f"Sudah lanjut usia, usia = {usia}")
        
    else:
        print (f"Belum masuk usia produktif, usia = {usia}")
        
else:
    print (f"Masih kecil usianya, usia = {usia}")
    
    
print ("\n --- Batas --- \n")
    
    
    
    
print ("\n Percabangan Nested, usia produktif manusia 2 \n")


usia = 13
cek = True

if cek:
    if usia >= 15 and usia <= 64:
        print (f"Sudah masuk usia produktif, usia = {usia}")
        
    elif usia > 64:
        print (f"Sudah lanjut usia, usia = {usia}")
        
    else:
        print (f"Belum masuk usia produktif, usia = {usia}")
        
else:
    print (f"Masih kecil usianya, usia = {usia}")
    
    
print ("\n --- Batas --- \n")




print ("\n For dasar \n")


for a in range (11):
    print (f"Urutan ke - {a}")
    
    
print ("\n --- Batas --- \n")




for b in range (21):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- Batas --- \n")




for c in range (26):
    print (f"Urutan ke - {c}")
    
    
print ("\n --- Batas --- \n")




print ("\n While dasar \n")


a = 5

while a < 21:
    print (f"Urutan ke - {a}")
    a = a + 1
    
    
print ("\n --- Batas --- \n")




b = 15 

while b < 31:
    print (f"Urutan ke - {b}")
    b = b + 1
    
    
print ("\n --- Batas --- \n")
