print ("\n Error Handling \n")


try:
    a = 10 / 0
    print (a)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("Berhasil")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 1 \n")

try:
    b = 20 / 0
    print (b)
    
except ZeroDivisionError:
    print ("Gagal")
    
else:
    print ("Berhasil")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 2 \n")


try:
    c = 10 + 10
    print (c)
    
except SyntaxError:
    print ("Gagal")
    
else:
    print ("Berhasil")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")




print ("\n Error Handling 3 \n ")


try:
    d = 20 + 20
    print (d)
    
except SyntaxError:
    print ("Gagal")
    
else:
    print ("Berhasil")
    
finally:
    print ("Selesai")
    
    
print ("\n --- Batas --- \n")
