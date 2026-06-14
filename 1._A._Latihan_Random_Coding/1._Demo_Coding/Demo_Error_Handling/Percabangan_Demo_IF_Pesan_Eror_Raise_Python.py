print ("\n Percabangan Dasar \n")


a = -5

try:
    if a < 0:
        raise ("Gak boleh Minus")
        
    if a > 5:
        print (f"Besar, nilai = {a}")
        
    else:
        print (f"Kecil, nilai = {a}")
        
except:
    print (f"Gak boleh minus, a = {a}")
    
    
print ("\n --- batas --- \n")




print ("\n Percabangan Dasar 2 \n")


b = 10

try:
    if b < 0:
        raise ("Gak boleh minus")
        
    if b > 5:
        print (f"Besar, b = {b}")
        
    else:
        print (f"Kecil, b = {b}")
        
except:
    print (f"Gak boleh minus, b = {b}")
    
    
print ("\n --- batas --- \n")




print ("\n Percabangan Lanjutan \n")


es = -10


try:
    if es < 0:
        raise ("Gak boleh minus")
        
    if es > 5:
        print (f"Besar, es = {es}")
        
    elif es < 5:
        print (f"Kecil, es = {es}")
        
    else:
        print (f"Sama saja, es = {es}")
        
except:
    print (f"Gak boleh minus, es = {es}")
    
    
print ("\n --- batas --- \n")




print ("\n Rapor Nilai, percabangan ledder \n")


nilai = -10

try:
    if nilai < 0:
        raise ("Gak boleh minus")
        
    if nilai >= 90:
        print (f"A, nilai = {nilai}")
        
    elif nilai >= 80:
        print (f"B, nilai = {nilai}")
        
    elif nilai >= 70:
        print (f"C, nilai = {nilai}")
        
    else:
        print (f"Biasa aja, nilai = {nilai}")
        
except:
    print (f"Gak boleh minus, nilai = {nilai}")