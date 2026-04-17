# Program menentukan jenis segitiga 

print ("\n Program menentukan jenis segitiga \n")


a = int (input ("Sisi 1 :"))
b = int (input ("Sisi 2 :"))
c = int (input ("Sisi 3 :"))


if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        print ("Segitiga Sama Sisi")
        
    elif a == b or b == c or a == c:
        print ("Segitiga Sama Kaki")
            
    else:
        print ("Segitiga sembarang")
                
else:
    print ("Bukan segitiga")