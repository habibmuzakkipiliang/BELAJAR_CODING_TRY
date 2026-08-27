# bikin nama formulir

nama = input ("Masukkan nama =")
asal = input ("Masukkan asal daerah =")
usia = int (input ("Masukkan usia kamu ="))
cek = input ("Masukkan status kamu (true dan false) =")
sekolah = input ("Masukkan asal sekolah kamu =")
coding = input ("Masukkan coding kamu =")
alumni = input ("Masukkan alumni kamu =")
kelas = input ("Masukkan kelas kamu =")

form = f"""
--- Profil Kamu ---

- Nama     : {nama}
- Asal     : {asal}
- Usia     : {usia}
- Cek      : {cek}
- Sekolah  : {sekolah}
- Coding   : {coding}
- Alumni   : {alumni}
- Kelas    : {kelas}
"""

print (form)


print ("\n --- batas --- \n")



a = int (input ("A : "))

if a >= 5:
     print (f"angka besar, a = {a}")

else:
     print (f"angka kecil, angka a = {a}")


print ("\n --- batas --- \n")




# Fungsi dengan percabangan dasar

def un (k):

     if k >= 5:
          print (f"angka k besar, angka k = {k}")

     else:
          print (f"angka k kecil, angka k = {k}")

un (10)
un (9)
un (8)
un (7)
un (6)
un (5)
un (4)
un (3)
un (2)
un (1)


print ("\n --- batas --- \n")



nama = input ("Masukkan nama kamu : ")

halo = f"Halo nama saya {nama} dari Kota Serang, Indonesia"