# Program menentukan bentuk bangun datar (2D)

print ("\n Program menentukan bentuk bangun datar (2D) \n")


a = int (input ("Sisi 1 :"))
b = int (input ("Sisi 2 :"))
c = int (input ("Sisi 3 :"))
d = int (input ("Sisi 4 :"))


if a > 0 and b > 0 and c > 0 and d > 0:
    
    if a == b == c == d:
        print ("Persegi")
        
    elif ((a == c and b == d) or (a == b and c == d) or (a == d and a == c)):
        print ("Persegi Panjang")
        
    else:
        print ("Bentuk lain")
        
else:
    print ("Gak boleh negatif atau 0")