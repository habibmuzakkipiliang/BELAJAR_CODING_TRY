print ("\n Fungsi dengan Percabangan Dasar \n")


def run (h):
    
    if h >= 5:
        print (f"Besar, angka h = {h}")
        
    else:
        print (f"Kecil, angka h = {h}")
        
run (10)
run (9)
run (8)
run (7)
run (6)
run (5)
run (4)
run (3)
run (2)
run (1)


print ("\n --- batas --- \n")





print ("\n Fungsi dengan Percabangan Lanjutan \n")

def un (e):
    
    if e >= 8:
        print (f"Besar, angka e = {e}")
        
    elif e >= 5:
        print (f"Tengah, angka e = {e}")
        
    else:
        print (f"Kecil, angka e = {e}")
        
un (10)
un (9)
un (8)
un (7)
un (6)
un (5)
un (4)
un (3)
un (2)
un (1)


print ("\n --- batas --- \n")





print ("\n Usia produktif manusia \n")

def usia (a):
    
    if a >= 15 and a <= 40:
        print (f"Sudah masuk produktif, usia = {a}")
        
    elif a > 40:
        print (f"Sudah tua, usia = {a}")
        
    else:
        print (f"Belum masuk produktif, usia = {a}")
        
usia (70)
usia (60)
usia (50)
usia (40)
usia (30)
usia (20)
usia (10)
usia (5)


print ("\n --- batas --- \n")





print ("\n Usia daftar JKT48 \n")

def hf (w):
    
    if w >= 13 and w <= 19:
        print (f"Boleh daftar JKT48, usia = {w}")
        
    elif w > 19:
        print (f"Sudah lebih dari cukup, usia = {w}")
        
    else:
        print (f"Belum boleh daftar JKT48, usia = {w}")
        
hf (20)
hf (19)
hf (18)
hf (17)
hf (16)
hf (15)
hf (14)
hf (13)
hf (12)
hf (11)
hf (10)


print ("\n --- batas --- \n")





print ("\n Nested \n")

def ruk (e):
    
    cek = True
    
    
    if e >= 5:
        if cek:
            print (f"Besar, angka e = {e}")
            
    else:
        print (f"Kecil, angka e = {e}")
        
ruk (10)
ruk (7)
ruk (6)
ruk (5)
ruk (4)
ruk (3)
ruk (2)
ruk (1)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Angka Terbesar \n")

def besar (x, y):
    
    if x > y:
        return x
        
    else:
        return y
        
        
print (besar (10, 7))
print (besar (8, 17))
print (besar (12, 6))
print (besar (3, 12))
print (besar (23, 4))


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Angka terkecil \n")

def kecil (x, y):
    
    if x > y:
        return x
        
    else:
        print y
        
print (kecil (10, 8))
print (kecil (4, 23))
print (kecil (12, 4))
print (kecil (12, 5))
print (kecil (3, 12))


print ("\n --- batas --- \n")






print ("\n For Dasar \n")

for a in range (1, 11):
    print (f"Urutan ke - {a}")
    
    
print ("\n --- batas --- \n")




print ("\n For dasar 1 \n")


for b in range (11):
    print (f"Urutan ke - {b}")
    
    
print ("\n --- batas --- \n")




print ("\n While dasar \n")

a = 1

while a < 11:
    print (f"Urutan ke - {a}")
    a = a + 1
    
    
print ("\n --- batas --- \n")




print ("\n Array \n")

dr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dr.append (11)
dr.append (12)
dr.append (13)
dr.append (14)
dr.append (15)


for a in dr:
    print (a)
    
    
print ("\n --- batas --- \n")