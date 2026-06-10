# Mini Project Python

print ("\n Mini Project Python \n")


# Input dan Output Sederhana

a = int (input ("Masukkan 1 + 1 = "))

if a == 2:
    print ("Benar")
    
else:
    print ("Salah")
    
print ("Hasil =", a)


print  ("\n ----- Batas --- \n")




b = int (input ("1 * 1 = ? "))

if b == 1:
    print ("Benar")
    
else:
    print ("Salah")
    
    
print ("Hasil =", b)


print ("\n --- Batas --- \n")




# Input Profil saya 

nama = input ("Nama kamu  ?")
kelas = input ("Dari kelas ?")
absen = input ("Absen ke berapa ?")
sekolah = input ("Dari sekolah mana ?")
coding = input ("Belajar coding apa aja ?")
tinggi = input ("Berapa tinggi badan kamu ??")
berat = input ("Berapa berat badan kamu ??")


print ("Nama :", nama)
print ("Kelas :", kelas)
print ("Absen :", absen)
print ("Sekolah :", sekolah)
print ("Coding :", coding)
print ("Tinggi badan :", tinggi)
print ("Berat badan :", berat)


print ("\n", f"Halo semuanya, saya {nama}, dari kelas {kelas}, absen ke {absen}, dari sekolah {sekolah}, saya belajar coding yaitu {coding}, tinggi badan saya adalah {tinggi}, dan berat badan adalah {berat}")


print ("\n --- Batas --- \n")




# Kalkulator Penjumlahan

print ("Kalkulator Penjumlahan")

a = int (input ("Angka a :"))
b = int (input ("Angka b :"))

print ("Hasil =", a + b)




c = int (input ("Angka c :"))
d = int (input ("Angka d :"))

print ("Hasil =", c + d)




e = int (input ("Angka e :"))
f = int (input ("Angka f :"))

print ("Hasil =", e + f)



print ("\n --- Batas --- \n")



# Fungsi dalam Kombinasi


print ("Fungsi dalam Kombinasi \n")


def tes ():
    
    print ("Kalkulator Fungsi dalam Penjumlahan \n")
    
    a = int (input ("Angka a : "))
    b = int (input ("Angka b : "))
    
    
    print ("Hasil =", a + b)
    
    
    
    
    c = int (input ("Angka c : "))
    d = int (input ("Angka d : "))
    e = int (input ("Angka e : "))
    
    
    print ("Hasil =", c + d + e)
    
    
tes ()


print  ("\n --- Batas --- \n")




# Fungsi dan kombinasinya

print ("\n Fungsi dan kombinasinya \n")


def tes ():
    
    print ("Kalkulator Fungsi Penjumlahan \n")

    a = 23
    b = 4
    
    
    print ("Hasil =", a + b)
    
    
    
    
    c = 30
    d = 44
    e = 35
    
    print ("Hasil =", c + d - e)
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    print ("Kalkulator Fungsi Perkalian")
    
    
    r = 30
    e = 45
    k = 50
    
    print ("Hasil = ", r * e * k)

tes ()


print  ("\n --- Batas --- \n")




# Fungsi dalam kombinasinya 2

print ("\n Fungsi dalam kombinasinya 2 \n")


def task ():
    
    print ("Percabangan dan Perulangan dalam Fungsi \n")
    
    print ("\n Percabangan Dasar \n")
    
    
    a = 9
    
    if a > 5:
        print ("Besar")
        
    else:
        print ("Kecil")
        
        
    print  ("\n --- Batas --- \n")
    
    
    
    
    b = 10
    
    if b > 5:
        print ("Besar")
        
    else:
        print ("Kecil")
        
        
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Percabangan Lanjutan 
    
    print ("Percabangan Lanjutan \n")
    
    
    c = 10
    
    if c > 5:
        print ("Besar")
        
    elif c < 5:
        print ("Kecil")
        
    else:
        print ("Semula")
        
      
    print  ("\n --- Batas --- \n")
    
    
    
    
    d = 4
    
    if d > 5:
        print ("Besar")
        
    elif d < 5:
        print ("Kecil")
        
    else:
        print ("Semula")
        
        
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Percabangan Tangga Lanjutan
    
    print ("Percabangan Tangga Lanjutan")
    
    g = 10
    
    if g > 7:
        print ("Besar")
        
    elif g == 6:
        print ("6")
        
    elif g == 5:
        print ("5")
        
    elif g == 4:
        print ("4")
        
    elif g == 3:
        print ("3")
        
    elif g == 2:
        print ("2")
        
    elif g == 1:
        print ("1")
        
    else:
        print ("Semula")
        
        
    print  ("\n --- Batas --- \n")
    
    
    
    
    
    # Percabangan Nested 
    
    print ("\n Percabangan Nested \n")
    
    e = 10
    cek = True
    
    if (cek):
        if e > 5:
            print ("Besar")
            
        else:
            print ("Kecil")
            
    else:
        print ("Semula")
        
        
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Percabangan Nested 1
    
    print ("\n Percabangan Nested 1 \n")
    
    f = 4
    cek = True
    
    if (cek):
        if f > 5:
            print ("Besar")
            
        elif f < 5:
            print ("Kecil")
            
    else:
        print ("Semula")
        
task ()


print ("\n --- Batas --- \n")




def jun ():
    
    # Switch Case di dalam fungsi 
    
    print ("Switch Case di dalam Fungsi \n")
    
    a = 4
    
    match (a):
        
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
            
        case _:
            print ("Semula")
            

jun ()


print ("\n --- Batas --- \n")



def perc ():
    
    # Perulangan For dan While di dalam Fungsi
    
    print ("Perulangan For dan While di dalam Fungsi \n")
    
    
    print ("\n Perulangan For dasar \n")
    
    
    for a in range (6):
        print ("a", a)
        
        
        
    print  ("\n --- Batas --- \n")
    
    
    
    for b in range (6):
        print ("b", b)
        
        
        
    print  ("\n --- Batas --- \n")
    
    
    
    for c in range (6):
        print ("c", c)
    
    
    
    print ("\n --- Batas --- \n")
    
    
    
    # Perulangan While dasar
    
    
    print ("\n Perulangan While dasar \n")
    
    
    a = 0
    
    while a < 6:
        print ("a", a)
        a = a + 1
        
        
        
    print ("\n --- Batas --- \n")
    
    
    
    b = 0
    
    while b < 6:
        print ("b", b)
        b = b + 1
        
        
        
    print ("\n --- Batas --- \n")
    
perc ()