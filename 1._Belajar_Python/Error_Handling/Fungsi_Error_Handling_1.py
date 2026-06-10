# Fungsi Error Handling

print ("\n Fungsi Error Handling \n")


def bonus ():
    
    try:
        hasil = 10 / 0
        print ("Hasil =", hasil)
        
    except ZeroDivisionError:
        print ("Gagal")
        
    else:
        print ("Hore mantap")
        
    finally:
        print ("Selesai dong")
    
    
    print ("\n --- Batas --- \n")
    
bonus ()




def error_d ():
    
    try:
        hasil = 50 / 0
        print ("Hasil =", hasil)
        
    except ZeroDivisionError:
        print ("Gagal")
        
    else:
        print ("Hore mantap")
        
    finally:
        print ("Selesai dong")
    
    
    print ("\n --- Batas --- \n")
    
error_d ()




def error ():
    
    try:
        hasil = "Michie JKT48"
        print ("Hasil =", hasil)
        
    except SyntaxError:
        print ("Gagal")
        
    else:
        print ("Hore mantap")
        
    finally:
        print ("Selesai dong")
    
    
    print ("\n --- Batas --- \n")
    
error ()




def error_e ():
    
    try:
        hasil = "Michie dan Fritzy JKT48"
        print ("Hasil =", hasil)
        
    except SyntaxError:
        print ("Gagal")
        
    else:
        print ("Hore mantap")
        
    finally:
        print ("Selesai dong")
    
    
    print ("\n --- Batas --- \n")
    
error_e ()