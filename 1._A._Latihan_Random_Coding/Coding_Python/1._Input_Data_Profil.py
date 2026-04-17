# Input Data Profil dalam Program Sederhana di Python


print ("\n Input Data Profil dalam Program Sederhana  di Python \n")


nama = input ("Masukkan nama : ")
kelas = input ("Masukkan kelas :")
absen = int (input ("Masukkan nomor absen :"))
sekolah = input ("Masukkan sekolah :")
tinggi = input ("Masukkan tinggi badan :")
berat =  input ("Masukkan berat badan :")
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




print ("\n Percabangan Nested \n")


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
