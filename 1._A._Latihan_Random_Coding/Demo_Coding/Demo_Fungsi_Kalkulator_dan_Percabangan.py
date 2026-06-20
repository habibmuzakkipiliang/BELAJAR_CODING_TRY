print ("\n Fungsi Kalkulator dan Percabangan \n")


def kalkulator ():
    
    a = 10
    b = 5
    
    tambah  = a + b 
    kurang  = a - b 
    kali    = a * b 
    bagi    = a / b 
    pangkat = a ** b
    modulus = a % b 
    
    
    hasil_1 = a > b
    hasil_2 = a < b
    hasil_3 = a >= b
    hasil_4 = a <= b
    hasil_5 = a == b
    hasil_6 = a != b
    
    
    hasil_7 = a > b and a < b
    hasil_8 = a < b or a > b
    hasil_9 = not a
    hasil_10 = not b
    
    
    detail = f"""
    
    Tambah = {tambah}
    Kurang = {kurang}
    Kali   = {kali}
    Bagi   = {bagi}
    Pangkat = {pangkat}
    Modulus = {modulus}
    
    -------------------
    
    
    Hasil = {hasil_1}
    Hasil = {hasil_2}
    Hasil = {hasil_3}
    Hasil = {hasil_4}
    Hasil = {hasil_5}
    Hasil = {hasil_6}
    
    -------------------
    
    
    Hasil = {hasil_7}
    Hasil = {hasil_8}
    Hasil = {hasil_9}
    Hasil = {hasil_10}
    
    -------------------
    
    """
    
    print (detail)
    
    
kalkulator ()


print ("\n --- Batas --- \n")




print ("\n Fungsi Percabangan Dasar \n")

def des (a):
    
    if a > 5:
        print (f"Angka Besar, a = {a}")
        
    else:
        print (f"Angka kecil, a = {a}")
   
des (10)
des (3)
des (15)
des (4)
 
 
print ("\n --- Batas --- \n")




print ("\n Fungsi Percabangan Dasar 2 \n")


def en (b):
    
    if b > 5:
        print (f"Angka besar, b = {b}")
        
    else:
        print (f"Angka kecil, b = {b}")
        
en (10)
en (4)
en (8)
en (3)


print ("\n --- Batas --- \n")




print ("\n Fungsi Percabangan Lanjutan 1 \n")

def ran (c):
    
    if c > 5:
        print (f"Angka besar, c = {c}")
        
    elif c < 5:
        print (f"Angka kecil, c = {c}")
        
    else:
        print (f"Sama saja, c = {c}")
        
ran (10)
ran (3)
ran (7)
ran (3)


print ("\n --- Batas --- \n")




print ("\n Fungsi Percabangan Lanjutan 2 \n")

def kok (d):
    
    if d > 5:
        print (f"Angka besar, d = {d}")
        
    elif d < 5:
        print (f"Angka kecil, d = {d}")
        
    else:
        print (f"Sama saja, d = {d}")
        
kok (10)
kok (3)
kok (6)
kok (3)
kok (9)
kok (4)


print ("\n --- Batas --- \n")




print ("\n Fungsi Percabangan  Nested 1 \n")

def dek (usia):
    
    cek = True
    
    if usia >= 15:
        if cek == True:
            print (f"Boleh dong, usia = {usia}")
            
        elif usia <= 15:
            print (f"Belum dong, usia = {usia}")
            
    else:
        print (f"Masih belum dong, usia = {usia}")
        
dek (20)
dek (13)
dek (19)
dek (20)
dek (10)
        
        
print ("\n --- Batas --- \n")




print ("\n Fungsi Percabangan Nested 2 \n")

def jun (usia):
    
    cek = True
    
    if usia >= 5:
        if cek == True:
            print (f"Oke dong, usia = {usia}")
            
        else:
            print (f"Belum dong, usia = {usia}")
            
    else:
        print (f"Masih belum sama sekali, usia = {usia}")
        
jun (10)
jun (3)
jun (8)
jun (2)


print ("\n --- Batas --- \n")

