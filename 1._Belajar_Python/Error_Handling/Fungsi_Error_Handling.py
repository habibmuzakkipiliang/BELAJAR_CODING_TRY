# Latihan lagi Error Handling

print ("\n Latihan lagi Error Handling \n")


def latihan ():
    
    try:
        a = 10 / 2
        print (a)
            
    except ZeroDivisionError:
        print ("Gagal dong")
    
    else:
        print ("Mantap jiwa, 100")
        
    finally:
        print ("Selesai")
        
        
    print ("\n --- Batas --- \n")
    
latihan ()





def latihan_1 ():
    
    try:
        a = 10 / 0 
        print (a)
        
    except ZeroDivisionError:
        print ("Gagal")
        
    else:
        print ("Nilai mantap jiwa, 100")
        
    finally:
        print ("Selesai dong")
        
        
    print ("\n --- Batas --- \n")
    
    
latihan_1 ()




def latihan_2 ():
    
    try:
        a = 19 / 3
        print (a)
        
    except ZeroDivisionError:
        print ("Gagal lagi")
        
    else:
        print ("Mantap jiwa, 100")
        
    finally:
        print ("Selesai")
        
        
    print ("\n --- Batas --- \n")
        

latihan_2 ()




def latihan_3 ():
    
    try:
        r = 50 / 0
        print (r)
        
    except ZeroDivisionError:
        print ("Gagal")
        
    else:
        print ("Mantap jiwa, 100")
        
    finally:
        print ("Selesai dong")
    
    
    print ("\n --- Batas --- \n")
    
latihan_3 ()