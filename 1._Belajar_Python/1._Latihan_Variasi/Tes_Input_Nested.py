# Tes aja latihan

print ("\n Tes aja latihan \n")


a = int (input ("1 :"))
b = int (input ("2 :"))
c = int (input ("3 :"))
d = int (input ("4 :"))


if a > 0 and b > 0 and c > 0 and d > 0:
    
    if a == b == c == d:
        print ("Tes 1")
        
    elif ((a == b) or (b == c) or (c == d) or (a == d)):
        print ("Tes 2")
        
    else:
        print ("Bukan Tes 1")
        
else:
    print ("Bukan Tes 2")