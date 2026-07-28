print ("Hello World")

nama = "habib muzakki"
print (nama)


angka = 12
print (angka)


desimal = 90.12
print (desimal)



print ("\n --- batas --- \n")




print ("\n Switch Case dengan Int \n")

def imt (j):

    match (j):

        case 1:
            print ("Angka 1")

        case 2:
            print ("Angka 2")

        case 3:
            print ("Angka 3")

        case 4:
            print ("Angka 4")

        case _:
            print ("Angka lain")
            

imt (1)
imt (2)
imt (3)
imt (4)
imt (5)



print ("\n --- batas --- \n")




print ("\n Switch Case dengan String \n")

def warna (k):

    match (k):

        case "Merah":
            print ("Warna merah")

        case "Kuning":
            print ("Warna kuning")

        case "Hijau":
            print ("Warna hijau")

        case _:
            print ("Warna lain")


warna ("Merah")
warna ("Kuning")
warna ("Hijau")
warna ("Hitam")


print ("\n --- batas --- \n")




print ("\n Array \n")

un = ["Woody", "Jessie", "Buzz" "Rex", "Sid"]

for i in un:
    print (i)



print ("\n --- batas --- \n")



for u in un:
    if u == "Jessie":
        break
    print (u)


print ("\n --- batas --- \n")




print ("\n Dictionary \n")

data = {
    "nama" : "Rayyan",
    "usia" : 19,
    "cek" : True,
}

print ("Nama :", data ["nama"])
print ("Usia :", data ["usia"])
print ("Cek :", data ["cek"])



print ("\n --- batas --- \n")



print ("\n OOP dasar \n")

class NP:

    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal


    def aksi (self):
        print (f"- Halo, nama saya {self.nama} dan berasal dari {self.asal}")


hasil_1 = NP ("Hayyan", "Jakarta")

hasil_1.aksi ()