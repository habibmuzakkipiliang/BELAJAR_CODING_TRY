print ("\n Bikin Program Python \n")



print ("\n Switch Case 1 \n")

def tun (w):
    
    match (w):
        
        case 1:
            print ("Angka 1")
            
        case 2:
            print ("Angka 2")
            
        case 3:
            print ("Angka 3")
            
        case 4:
            print ("Angka 4")
            
        case _:
            print ("Angka lain")
            
            
tun (1)
tun (2)
tun (3)
tun (4)
tun (5)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan dasar \n")

def er (k):
    
    if k >= 5:
        print (f"Besar, angka k = {k}")
        
    else:
        print (f"Kecil, angka k = {k}")
        
        
er (10)
er (9)
er (8)
er (7)
er (5)
er (3)
er (2)
er (1)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan Lanjutan \n")

def tun (j):
    
    if j >= 8:
        print (f"Besar, angka j = {j}")
        
    elif j >= 5:
        print (f"Tengah, angka j = {j}")
        
    else:
        print (f"Kecil, angka j = {j}")
        
tun (10)
tun (9)
tun (8)
tun (7)
tun (6)
tun (5)
tun (4)
tun (3)
tun (2)
tun (1)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan Percabangan Nilai Rapor \n")

def rapor (t):
    
    if t >= 90:
        print (f"A, nilai = {t}")
        
    elif t >= 80:
        print (f"B, nilai = {t}")
        
    elif t >= 70:
        print (f"C, nilai = {t}")
        
    elif t >= 60:
        print (f"D, nilai = {t}")
        
    elif t >= 50:
        print (f"E, nilai = {t}")
    
    else:
        print (f"Jelek amat, nilai = {t}")
        
        
rapor (100)
rapor (90)
rapor (80)
rapor (70)
rapor (60)
rapor (50)
rapor (40)


print ("\n --- batas --- \n")




print ("\n Fungsi dengan percabangan Nested 1 \n")

def fun (m):
    
    cek = True
    
    if m >= 8:
        if cek:
            print (f"Besar, angka m = {m}")
            
    else:
        print (f"Kecil, angka m = {m}")
        
fun (10)
fun (9)
fun (8)
fun (7)
fun (6)
fun (5)
fun (4)
fun (3)
fun (2)
fun (1)