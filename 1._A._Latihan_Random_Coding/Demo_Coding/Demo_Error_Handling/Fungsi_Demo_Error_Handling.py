# Fungsi Error Handling 

print ("\n Fungsi Error Handling \n")


def cek_angka (a):
    try:
        if a < 0:
            raise ("Minus")
            print (f"Angka salah {a}")
            
        else:
            print (f"Angka benar")
            
    except:
        print (f"Gak boleh minus, a = {a}")
    
    
cek_angka (-5)


print ("\n --- Batas --- \n")




print ("\n Fungsi Error Handling 2 \n")

def dasar (b):
    try:
        if b < 0:
            raise ("Minus")
            print (f"Angka salah, angka = {b}")
            
        else:
            print (f"Angka benar, angka = {b}")
            
    except:
        print (f"Gak boleh minus, angka = {b}")
        
        
print ("\n --- Batas --- \n")
