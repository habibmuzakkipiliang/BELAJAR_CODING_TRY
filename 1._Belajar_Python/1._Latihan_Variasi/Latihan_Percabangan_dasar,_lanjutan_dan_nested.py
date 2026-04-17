# Percabangan dasar, Switch Case, lanjutan dan nested 

print ("\n Percabangan Dasar, Switch Case, Lanjutan dan Nested \n")


print ("\n Percabangan dasar \n")


a = 9

if a > 5:
    print ("Besar")
    
else:
    print ("Kecil")
    
    
print ("\n --- Batas --- \n")




b = 4

if b > 5:
    print ("Besar")
    
else:
    print ("Kecil")
    
    
print ("\n --- Batas --- \n")




print ("\n Switch Case \n")


a = 5

match (a):
    
    case 1:
        print ("1")
        
    case 2:
        print ("2")
        
    case 3:
        print ("3")
        
    case 4:
        print ("4")
        
    case 5:
        print ("5")
        
    case 6:
        print ("6")
        
    case _:
        print ("Semula")
        
        
print ("\n --- Batas --- \n")




print ("\n Switch Case 1 \n")


b = 1

match (b):
    
    case 1:
        print ("Iya")
        
    case 2:
        print ("Tidak")
        
    case _:
        print ("Semula")
        
        
print ("\n --- Batas --- \n")




print ("\n Switch Case 2 \n")


kondisi = 3

match (kondisi):
    
    case 1:
        print ("Laper dan haus banget")
        
    case 2:
        print ("Laper dan haus dikit")
        
    case 3:
        print ("Laper dan haus sedang")
        
    case 4:
        print ("Kenyang dikit dan agak mending")
        
    case 5:
        print ("Kenyang poll dan stabil")
        
    case _:
        print ("Gak apa - apa kok")
        
        
print ("\n --- Batas --- \n")




print ("\n Switch Case 3 \n")


nilai = 100

match (nilai):
    
    case 100:
        print ("Mantap Jiwa")
        
    case 95:
        print ("Mantap dikit")
        
    case 90:
        print ("Mantap sedang")
        
    case 85:
        print ("B +")
        
    case 80:
        print ("B")
        
    case 75:
        print ("C")
        
        
print ("\n --- Batas --- \n")




print ("\n Percabangan Lanjutan \n")


a = 9

if a > 5:
    print ("Besar")
    
elif a < 5:
    print ("Kecil")
    
else:
    print ("Basic")
    
    
print ("\n --- Batas --- \n")




b = 3

if b > 5:
    print ("Besar")
    
elif b < 5:
    print ("Kecil")
    
else:
    print ("Basic")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Tangga Lanjutan \n")

a = 10

if a > 7:
    print ("Besar")
    
elif a == 6:
    print ("6")
    
elif a == 5:
    print ("5")
    
elif a == 4:
    print ("4")

elif a == 3:
    print ("3")
    
elif a == 2:
    print ("2")
    
elif a == 1:
    print ("1")
    
else:
    print ("Semula")


print ("\n --- Batas --- \n")




print ("\n Percabangan Tangga Lanjutan 2 \n")


b = 2

if b > 7:
    print ("Besar")
    
elif b == 6:
    print ("6")
    
elif b == 5:
    print ("5")
    
elif b == 4:
    print ("4")
    
elif b == 3:
    print ("3")
    
elif b == 2:
    print ("2")
    
elif b == 1:
    print ("1")
    
else:
    print ("Semula")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 1 level 1 \n")

a = 9
cek = True

if (cek):
    if a > 5:
        print ("Besar")
        
    elif a < 5:
        print ("Kecil")
        
else:
    print ("Basic")
    
    
print ("\n --- Batas --- \n")




b = 3 
cek = True

if (cek):
    if b > 5:
        print ("Besar")
        
    elif b < 5:
        print ("Kecil")
        
else:
    print ("Basic")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested 2 level 1 \n")


a = 9
cek = True

if (cek):
    if a > 5:
        print ("Besar")
        
    else:
        print ("Kecil")
    
else:
    print ("Basic")
    
    
print ("\n --- Batas --- \n")




b = 3
cek = True

if (cek):
    if b > 5:
        print ("Besar")
        
    else:
        print ("Kecil")
        
else:
    print ("Basic")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested level 2 \n")


umur = 17
sim = True

if (sim):
    if umur >= 17:
        print ("Boleh ambil sim dan tes")
        
    elif umur < 17:
        print ("Belum boleh ambil sim dan tes")
        
else:
    print ("Jangan sama sekali")
    
    
print ("\n --- Batas --- \n")





print ("\n Percabangan Nested level 2 (Member JKT48) \n")


usia = 18
cek = True

if (cek):
    if usia >= 13:
        print ("Boleh ikut audisi dan gabung JKT48")
        
    elif usia < 13:
        print ("Gak boleh ikut audisi JKT48")
        
else:
    print ("Jangan dulu ikut")
    
    
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested level 2 (Kerja IT dan Teknologi dan Coding) \n")


usia = 19
cek = True

if (cek):
    if usia >= 25:
        print ("Boleh kerja dan gabung")
        
    elif usia < 25:
        print ("Gak boleh kerja dulu")
        
else:
    print ("Jangan dulu ya")


print ("\n --- Batas --- \n")




print ("\n Percabangan Nested level 2 (Teknologi dan Coding) \n")


usia = 23
cek = True

if (cek):
    if usia >= 20:
        print ("Boleh dan Gabung")
        
    elif usia < 20:
        print ("Gak bisa dulu")

else:
    print ("Pindah yang lain")


print ("\n --- Batas --- \n")




print ("\n Percabangan Nested level 3 (member JKT48 tahap 2) \n")


umur = 15
cek = True

if (cek):
    if umur >= 13 and umur <= 17:
        print ("Boleh gabung dan ikut audisi JKT48")
        
    elif umur > 17:
        print ("Lebih dari cukup nih untuk gabung ya guys")
        
    else:
        print ("Sabar dulu ya teman - teman bagi masih dibawah 13 tahun")
        
else:
    print ("Jangan ikut sama sekali")
    
 
print ("\n --- Batas --- \n")




print ("\n Percabangan Nested level 3 (SIM) \n")


umur = 19
sim = True

if (sim):
    if umur >= 17 and umur <= 25:
        print ("Boleh punya dan ambil SIM")
        
    elif umur > 25:
        print ("Sudah matang mentalnya")
        
    else:
        print ("Belum boleh punya SIM")
        
else:
    print ("Jangan dulu ya")


print ("\n --- Batas --- \n")




print ("\n Percabangan Nested Level 3 (Usia dalam produktif kerja) \n")


usia = 26
cek = True

if (cek):
    if usia >= 25 and usia <= 45:
        print ("Usia yang produktif dan mateng")
        
    elif usia > 45:
        print ("Bukan usia produktif, sudah mau tua")
        
    else:
        print ("Belum masuk usia produktif, masih muda")
        
else:
    print ("Remaja banget")
    
    
print ("\n --- Batas --- \n")