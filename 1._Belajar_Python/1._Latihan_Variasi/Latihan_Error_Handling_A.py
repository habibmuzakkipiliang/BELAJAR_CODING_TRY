# Error Handling

print ("\n Error Handling \n")


try:
    hasil = 10 / 0
    print (hasil)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("Mantap jiwa")
    
finally:
    print ("Selesai dong")
    
    
print ("\n --- Batas --- \n")




try:
    hasil = "Tes Aja"
    print (hasil)
    
except SyntaxError:
    print ("Gagal")
    
else:
    print ("Mantap jiwa")
    
finally:
    print ("Selesai dong")