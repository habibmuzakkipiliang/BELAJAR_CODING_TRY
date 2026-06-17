console.log ("\n Bikin Hello World \n")

console.log ("Hello World")


console.log ("\n --- Batas --- \n")




console.log ("\n Profil Habib Muzakki \n")


var nama = "Habib Muzakki"
var marga = "Piliang"
var kelas = "12 Agama (Keagamaan)"
var absen = "15"
var sekolah = "MAN 2 KOTA SERANG"
var coding = "HTML, CSS, JavaScript dan Python"
var lomba = "Finalis OSN-K Informatika tahun 2025"
var tinggi = "170 cm"
var berat = "60 kg"


var profil = `
- Nama         : ${nama}
- Marga        : ${marga}
- Kelas        : ${kelas}
- Absen        : ${absen}
- Sekolah      : ${sekolah}
- Coding       : ${coding}
- Lomba        : ${lomba}
- Tinggi badan : ${tinggi}
- Berat badan  : ${berat}

`


console.log (profil)


console.log ("\n --- Batas --- \n")




console.log ("\n Variabel dan Sintaks dasar \n")


var nama = "John Doe"

console.log (nama)


var kelas = "12 Agama"

console.log (kelas)


// Ini Komen


// Komen 1


// Komen 2


console.log ("\n --- Batas --- \n")




console.log ("\n Tipe data pemrograman \n")


var teks = "Halo Dunia"
var angka = 12
var desimal = 23.12
var cek = true
var kosong = null
var huruf = 'A'
var array = [
    
    "1. Bukittinggi",
    "2. Padang",
    "3. Padang Panjang",
    "4. Batusangkar",
    "5. Solok",
    "6. Payakumbuh",
    "7. Sijunjung",
    "8. Sitiung",
    "9. Timpeh",
    "10. Silaut",
    
    ]
    
    
console.log ("Teks =", teks)
console.log ("Angka =", angka)
console.log ("Desimal =", desimal)
console.log ("Cek =", cek)
console.log ("Kosong =", kosong)
console.log ("Huruf =", huruf)
console.log ("Array :")


for (a = 0; a < array.length; a++) {
    console.log (array [a])
}
    
    
console.log ("\n --- Batas --- \n")




console.log ("\n Dictionary \n")


var data = {
    "nama" : "Johan",
    "asal" : "Serang",
    "usia" : "25 tahun",
    "kerja" : "Software Engineer",
}


console.log ("Nama :", data ["nama"])

console.log ("Asal :", data ["asal"])

console.log ("Usia :", data ["usia"])

console.log ("Kerja :", data ["kerja"])


console.log ("\n --- Batas --- \n")




console.log ("\n Operasi Dasar \n")


var x = 50
var y = 5


console.log ("Tambah =", x + y)
console.log ("Kurang =", x - y)
console.log ("Kali =", x * y)
console.log ("Pangkat =", x ** y)
console.log ("Modulus =", x % y)


console.log ("\n --- Batas --- \n")




console.log ("\n Operasi Perbandingan \n")


console.log ("Hasil =", x > y)
console.log ("Hasil =", x < y)
console.log ("Hasil =", x <= y)
console.log ("Hasil =", x >= y)
console.log ("Hasil =", x == y)
console.log ("Hasil =", x != y)


console.log ("\n --- Batas --- \n")




console.log ("\n Operator Logika \n")


console.log ("Hasil =", (x > y) && (x < y))
console.log ("Hasil =", (x < y) || (x > y))
console.log ("Hasil =", (! x))
console.log ("Hasil =", (! y))


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 1 \n")


var nomor = 9

switch (nomor) {
    
    case 1:
        console.log ("1")
        break
        
    case 2:
        console.log ("2")
        break
        
    case 3:
        console.log ("3")
        break
        
    case 4:
        console.log ("4")
        break
        
    case 5:
        console.log ("5")
        break
        
    case 6:
        console.log ("6")
        break
        
    case 7:
        console.log ("7")
        break
        
    case 8:
        console.log ("8")
        break
        
    case 9:
        console.log ("9")
        break
        
    case 10:
        console.log ("10")
        break
        
    default:
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan dasar \n")


var a = 9

if (a > 5) {
    console.log (`Besar, nilai = ${a}`)
}

else {
    console.log (`Kecil, nilai = ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan dasar 2 \n")


var k = 3

if (k > 5) {
    console.log (`Besar, k = ${k}`)
}

else {
    console.log (`Kecil, k = ${k}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan \n")


var s = 9

if (s > 5) {
    console.log (`Besar, s = ${s}`)
}

else if (s < 5) {
    console.log (`Kecil, s = ${s}`)
}

else {
    console.log (`Sama saja, s = ${s}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan 2 \n")


var d = 3
 
if (d > 5) {
    console.log (`Besar, d = ${d}`)
}

else if (d < 5) {
    console.log (`Kecil, d = ${d}`)
}

else {
    console.log (`Sama saja, d = ${d}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 1 \n")


var x = 9
var cek = true

if (cek) {
    if (x > 5) {
        console.log (`Besar, x = ${x}`)
    }
    
    else if (x < 5) {
        console.log (`Kecil, x = ${x}`)
    }
}

else {
    console.log (`Sama saja, x = ${x}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 2 \n")


var y = 3
var cek = true

if (cek) {
    if (y > 5) {
        console.log (`Besar, y = ${y}`)
    }
    
    else {
        console.log (`Kecil, y = ${y}`)
    }
}

else {
    console.log (`Sama saja, y = ${y}`)
}


console.log ("\n --- Batas --- \n")

