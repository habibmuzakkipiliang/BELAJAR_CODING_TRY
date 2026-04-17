print ("\n Mini Project Python \n")


print ("\n Data Variabel dasar \n")


nama = "Habib Muzakki"
panggilan = "Habib"
kelas = "12 Agama"
absen = 15
sekolah = "MAN 2 KOTA SERANG"
coding = "HTML, CSS, JavaScript dan Python"
tinggi = "170 cm"
berat = "60 kg"


print ("Nama lengkap :", nama)
print ("Nama panggilan :", panggilan)
print ("Kelas :", kelas)
print ("Absen :", absen)
print ("Sekolah :", sekolah)
print ("Coding :", coding)
print ("Tinggi badan :", tinggi)
print ("Berat badan :", berat)


print ("\n", f"Halo, saya {nama}, dipanggil {panggilan}, dari kelas {kelas}, absen ke- {absen}, coding yang saya pelajari adalah {coding}, tinggi badan saya adalah {tinggi}, dan berat badan saya adalah {berat}")


print ("\n --- Batas --- \n")


# Kalkulator Pertambahan sederhana

print ("Kalkulator Penjumlahan")

a = 8
b = 5

print ("Hasil = ", a + b)




x = 15
y = 10

print ("Hasil =", x + y)


print  ("\n --- Batas --- \n")




# Kalkulator pengurangan  sederhana

print ("Kalkulator Pengurangan")

c = 20
d = 5

print ("Hasil =", c - d)



f = 25
e = 5

print ("Hasil =", f - e)




e = 50
r = 40
k = 30

print ("Hasil =", e - r - k)



print  ("\n --- Batas --- \n")




# Kalkulator Perkalian

print ("Kalkulator Perkalian")

r = 10
g = 50

print ("Hasil =", r * g)




f = 80
i = 10
j = 20

print ("Hasil =", f * i * j)


print ("\n --- Batas --- \n")




# Kalkulator Pangkat 

print ("\n Kalkulator Pangkat \n")

r = 10
m = 5


print ("Hasil =", r ** m)




y = 15 
u = 5

print ("Hasil =", y ** u)


print  ("\n --- Batas --- \n")




# Kalkulator Modulus

print ("\n Kalkulator Modulus \n")

y = 8
j = 5

print ("Hasil =", y % j)



k = 3
j = 3 

print ("Hasil =", k % j)



print ("\n --- Batas --- \n")



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
    
    
    
    m = 10
    h = 5
    k = 34
    
    print ("Hasil =", m * h * k)

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
            
            
            
            
    b = "Yes"
    
    match (b):
        
        case 1:
            print ("Yes")
            
        case 2:
            print ("No")
            
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
    
    
    
    for d in range (6):
        print ("d", d)
        
        
        
    print ("\n --- Batas --- \n")
    
    
    
    for e in range (6):
        print ("e", e)
    
    
    
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
    
    
    
    c = 0
    
    while c < 6:
        print ("c", c)
        c = c + 1
        
        
    print ("\n --- Batas --- \n")
    
    
    d = 0
    
    while d < 6:
        print ("d", d)
        d = d + 1
        
        
    print ("\n --- Batas --- \n")
    
    
    e = 0
    
    while e < 6:
        print ("e", e)
        e = e + 1
    
perc ()



print ("\n --- Batas --- \n")




def func ():
    
    
    # For Nested
    
    print ("\n For Nested \n")
    
    
    for a in range (2):
        for b in range (3):
            print ("a", a, "b", b)
            
            
            
    print ("\n --- Batas --- \n")
    
    
    
    for c in range (2):
        for d in range (3):
            print ("c", c, "d", d)
            
            
func ()