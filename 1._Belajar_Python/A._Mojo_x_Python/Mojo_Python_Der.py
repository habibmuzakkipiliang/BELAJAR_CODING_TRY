def main ():
    
    # Hello World di Mojo (Python)
    
    print ("\n Hello World di Mojo (Python) \n")
    
    print ("Hello Mojo")
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Hello World di Mojo dengan Variabel
    
    print ("\n Hello World di Mojo dengan Variabel \n")
    
    
    lot = "Halo Mojo Variabel"
    print ("Let :", lot)
    
    
    vin = "Halo Mojo Variabel"
    print ("Var :", vin)
    
    
    cot = "Halo Mojo Constant"
    print ("Const :", cot)
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Contoh Sintaks dasar di Mojo
    
    print ("\n Contoh Sintaks dasar di Mojo \n")
    
    
    teks = "Halo aku lagi belajar Mojo"
    angka = 10
    desimal = 3.14
    benar = True
    salah = False
    
    print ("Teks :", teks)
    print ("Angka :", angka)
    print ("Desimal :", desimal)
    print ("Benar :", benar)
    print ("Salah :", salah)
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    # String F
    
    print ("\n String F \n")
    
    
    v = "Indonesia"
    
    print (f"Halo {v}")
    
    
    h = "Malaysia"
    
    print (f"Halo {h}")
    
    
    k = "Singapura"
    
    print (f"Halo {k}")
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    
    # Tipe data dasar di Mojo
    
    print ("\n Tipe data dasar di Mojo \n")
    
    a = "Halo Mojo"
    b = 12
    c = 3.14
    d = True
    
    print ("String :", a)
    print ("Integer :", b)
    print ("Float :", c)
    print ("Boolean :", d)
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Operasi dasar di Mojo
    
    print ("\n Operasi dasar di Mojo \n")
    
    x = 10
    y = 5 
    
    print ("Penjumlahan =", x + y)
    print ("Pengurangan =", x - y)
    print ("Perkalian =", x * y)
    print ("Pembagian =", x / y)
    print ("Modulus =", x % y)
    print ("Pangkat =", x ** y)
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Operasi Perbandingan di Mojo
    
    print ("\n Operasi Perbandingan di Mojo \n")
    
    print ("Hasil =", x > y)      
    print ("Hasil =", x < y)      
    print ("Hasil =", x == y)  
    print ("Hasil =", x != y)
    print ("Hasil =", x >= y)
    print ("Hasil =", x <= y)
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Operasi Logika di Mojo
    
    print ("\n Operasi Logika di Mojo \n")
    
    
    print ("Hasil =", (x > y) and (x < y))
    
    print ("Hasil =", (x < y) or (x > y))
    
    print ("Hasil =", not x)
    
    print ("Hasil =", not y)
    
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Percabangan Dasar 
    
    print ("\n Percabangan Dasar \n")
    
    
    a = 8
    
    if a > 5:
        print ("Besar")
        
    else:
        print ("Kecil")
        
        
    print  ("\n --- Batas --- \n")
    
    
    
    b = 3
    
    if b > 5:
        print ("Besar")
        
    else:
        print ("Kecil")
        
        
    print  ("\n --- Batas --- \n")
    
    
    
    # Percabangan Lanjutan
    
    print ("\n Percabangan Lanjutan \n")
    
    a = 9
    
    if a > 5:
        print ("Besar")
        
    elif a < 5:
        print ("Kecil")
        
    else:
        print ("Semula")
        
        
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Percabangan Nested 1
    
    print ("\n Percabangan Nested \n")
    
    a = 9
    cek = True
    
    if (cek):
        if a > 5:
            print ("Besar")
            
        elif a < 5:
            print ("Kecil")
            
    else:
        print ("Semula")
        
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    # Percabangan Nested 2
    
    print ("\n Percabangan Nested \n")
    
    a = 3
    cek = True
    
    if (cek):
        if a > 5:
            print ("Besar")
            
        else:
            print ("Kecil")
            
    else:
        print ("Semula")
        
    
    print  ("\n --- Batas --- \n")
    
    
    
    
    # For dasar
    
    print ("\n For Dasar \n")
    
    for i in range (6):
        print ("i", i)
     
     
    for a in range (6):
        print ("a", a)
        
    
    for e in range (6):
        print ("e", e)
        
        
    for j in range (6):
        print ("j", j)
        
        
    for u in range (6):
        print ("u", u)
        
        
    print  ("\n --- Batas --- \n")
    
    
    
    
    # While Dasar
    
    print ("\n While Dasar \n")
    
    
    a = 0
    
    while a < 6:
        print ("a", a)
        a = a + 1
        
        
    b = 0 
    
    while b < 6:
        print ("b", b)
        b = b + 1
        
        
    c = 0
    
    while c < 6:
        print ("c", c)
        c = c + 1
        
        
    d = 0
    
    while d < 6:
        print ("d", d)
        d = d + 1
        
        
    e = 0
    
    while e < 6:
        print ("e", e)
        e = e + 1
        
        
    print  ("\n --- Batas --- \n")
    
    
main ()