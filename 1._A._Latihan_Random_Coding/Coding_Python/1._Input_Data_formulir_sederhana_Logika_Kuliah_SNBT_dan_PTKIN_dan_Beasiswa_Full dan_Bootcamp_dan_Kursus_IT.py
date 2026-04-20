# Input Data formulir sederhana Logika Kuliah SNBT dan UM PTKIN dan Beasiswa Full dan Bootcamp dan Kursus IT


print ("\n Input Data formulir sederhana Logika Kuliah SNBT dan UM PTKIN dan Beasiswa Full dan Bootcamp dan Kursus IT \n")


nama = input ("Masukkan nama kamu : ")
kelas = input ("Masukkan kelas kamu : ")
absen = int (input ("Masukkan nomor absen : "))
sekolah = input ("Masukkan sekolah kamu : ")
tinggi = input ("Masukkan tinggi badan kamu : ")
berat = input ("Masukkan berat badan kamu : ")
ujian = input ("Lokasi ujian SNBT : ")




profil = f""" 

- Nama         : {nama}
- Kelas        : {kelas}
- Nomor Absen  : {absen}
- Asal Sekolah : {sekolah}
- Tinggi badan : {tinggi}
- Berat badan  : {berat}
- Ujian SNBT   : {ujian}


- Terimakasih sudah isi data formulir di pelayanan kami

- Nikmati hidup kamu dengan tenang dan damai

"""

print (profil)


print ("\n --- Batas --- \n")




x = int (input ("Masukkan angka x : "))
y = int (input ("Masukkan angka y : "))


print ("\n Operasi Dasar \n")


print ("Tambah =", x + y)
print ("Kurang =", x - y)
print ("Kali =", x * y)
print ("Bagi =", x / y)
print ("Pangkat =", x ** y)
print ("Modulus =", x % y)


print ("\n --- Batas --- \n")




print ("\n Operasi Perbandingan \n")

print ("Hasil =", x > y)
print ("Hasil =", x < y)
print ("Hasil =", x == y)
print ("Hasil =", x != y)
print ("Hasil =", x >= y)
print ("Hasil =", x <= y)


print ("\n --- Batas --- \n")




print ("\n Operasi Logika \n")


print ("Hasil =", x > y and x < y)
print ("Hasil =", x > y or x < y)
print ("Hasil =", not x)
print ("Hasil =", not y)


print ("\n --- Batas --- \n")




print ("\n Logic masuk kuliah saat SNBT (Control Flow Ledder Logic) \n")


hasil = int (input ("Masukkan data kamu (HASIL SNBT) : "))


if hasil >= 90:
    print (f"Lulus dong,  berarti boleh kuliah, hasil = {hasil}")
        
elif hasil >= 80:
    print (f"Masih aman dong, tetap konsisten, hasil = {hasil}")
        
elif hasil >= 70:
    print (f"Tenang aja, masih ada jalur lain misalnya UM PTKIN dan Beasiswa IT lainnya, hasil = {hasil}")
        
elif hasil >= 60:
    print (f"Semangat dong, masih ada jalur lain lagi dong, hasil = {hasil}")
        
elif hasil >= 20:
    print (f"Sabar dan tenang, tapi masih ada jalur dan jalan lain dengan dibarengi usaha, hasil = {hasil}")
        
elif hasil >= 10:
    print (f"Ikut Bootcamp dan Beasiswa IT Swasta aja, hasil = {hasil}")
        
else:
    print (f"Gap year tahun depan, hasil = {hasil}")
    
    
print ("\n --- Batas --- \n")




print ("\n Ulang Kata biar semangat dong (For Looping) \n")


kata = input ("Masukkan kata kamu yang bikin semangat ya : ")


for a in range (50):
    print (f"{a + 1}, {kata}") 
    
print ("\n --- Batas --- \n")




print ("\n Hitung Angka Random sampai berapa (While Looping) \n")


b = int (input ("Masukkan angka random : "))

while b < 15:
    print (f"Urutan ke - {b}")
    b = b + 1