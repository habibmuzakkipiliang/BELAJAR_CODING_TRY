// Latihan kode JavaScript 


console.log ("\n Latihan kode JavaScript \n")


console.log ("Hello World")




console.log ("\n Variabel dan Tipe data pemrograman \n")


var angka = 34
var teks = "Teks aja"
var desimal = 34.23
var char = 'A'
var cek = true
var daftar = [
    
    "1. F4F Wildcat",
    "2. SBD Dauntless",
    "3. F4U Corsair",
    "4. F6F Hellcat",
    "5. P-51 Mustang",
    "6. P-38 Lightning",
    "7. SB2C Helldiver",
    "8. B-29 Superfortress",
    "9. B-17 Flying Fortress",
    "10. A-20 Havoc",
    "11. B-25 Mitchell",
    "12. PBY Catalina",
    
    ]
    
    
detail = `
- Angka   : ${angka}
- Teks    : ${teks}
- Desimal : ${desimal}
- Char    : ${char}
- Cek     : ${cek}
- Daftar  : 

`


console.log (detail)
    
    
for (a = 0; a < daftar.length; a++) {
    console.log (daftar [a])
}
    
    
console.log ("\n --- Batas --- \n")




console.log ("\n Dictionary \n")


var data = {
    "nama" : "Alan John",
    "asal" : "Amerika Serikat",
    "kerja" : "Software Engineer",
    "coding" : "HTML, CSS, JavaScript dan Python",
    
}


console.log ("Nama :", data ["nama"])

console.log ("Asal :", data ["asal"])

console.log ("Kerja :", data ["kerja"])

console.log ("Coding :", data ["coding"])


console.log ("\n --- Batas --- \n")




console.log ("\n Profil Habib Muzakki \n")


var nama = "Habib Muzakki"
var panggil = "Habib"
var marga = "Piliang"
var kelas = "12 Agama (Keagamaan)"
var absen = 15
var asal  = "Banten"
var kota = "Serang"
var sekolah = "MAN 2 KOTA SERANG"
var darah = "B"
var coding = "HTML, CSS, JavaScript"
var lomba = "Finalis OSN-K Informatika tahun 2025"
var usia = "19 tahun"
var suku = "Minangkabau"
var tinggi = "172 cm"
var berat = "60 kg"


var detail = `

- Nama lengkap   : ${nama}
- Nama panggilan : ${panggil}
- Marga          : ${marga}
- Kelas          : ${kelas}
- Absen          : ${absen}
- Asal           : ${asal}
- Kota           : ${kota}
- Sekolah        : ${sekolah}
- Golongan darah : ${darah}
- Coding         : ${coding}
- Lomba          : ${lomba}
- Usia           : ${usia}
- Suku           : ${suku}
- Tinggi badan   : ${tinggi}
- Berat badan    : ${berat}


`


console.log (detail)


console.log ("\n --- Batas --- \n")




console.log ("\n Operator Dasar \n")


var x = 20
y = 5

console.log ("Tambah =", x + y)
console.log ("Kurang =", x - y)
console.log ("Kali =", x * y)
console.log ("Bagi =", x / y)
console.log ("Pangkat =", x ** y)

console.log ("Modulus =", x % y)


console.log ("\n --- Batas --- \n")




console.log ("\n Operator Perbandingan \n")


console.log ("Hasil =", x > y)
console.log ("Hasil =", x < y)
console.log ("Hasil =", x >= y)
console.log ("Hasil =", x <= y)
console.log ("Hasil =", x == y)
console.log ("Hasil =", x != y)


console.log ("\n --- Batas --- \n")




console.log ("\n Operator Logika \n")


console.log ("Hasil =", (x > y) && (x < y))
console.log ("Hasil =", (x < y) || (x > y))
console.log ("Hasil =", (!x))
console.log ("Hasil =", (!y))


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




console.log ("\n Logika 1 \n")


var a = 9

if (a > 5) {
    console.log (`Besar, a = ${a}`)
}

else {
    console.log (`Kecil, a = ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Logika 2 \n")


var b = 3

if (b > 5) {
    console.log (`Besar, b = ${b}`)
}

else if (b < 5) {
    console.log (`Kecil, b = ${b}`)
}

else {
    console.log (`Sama saja, b = ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Logika Ladder \n")


var skor = 90

if (skor >= 95) {
    console.log (`A, skor = ${skor}`)
}

else if (skor >= 90) {
    console.log (`B, skor = ${skor}`)
}

else if (skor >= 80) {
    console.log (`C, skor = ${skor}`)
}

else if (skor >= 70) {
    console.log (`D, skor = ${skor}`)
}

else if (skor >= 60) {
    console.log (`E, skor = ${skor}`)
}

else if (skor >= 50) {
    console.log (`F, skor = ${skor}`)
}

else {
    console.log (`Sama saja, skor = ${skor}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Logika Nested 1 \n")


var f = 9
var cek = true

if (cek) {
    if (f > 5) {
        console.log (`Besar, f = ${f}`)
    }
    
    else if (f < 5) {
        console.log (`Kecil, f = ${f}`)
    }
}

else {
    console.log (`Sama saja, f = ${f}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Logika Nested 2 \n")


var k = 3
var cek = true

if (cek) {
    if (k > 5) {
        console.log (`Besar, k = ${k}`)
    }
    
    else {
        console.log (`Kecil, k = ${k}`)
    }
}

else {
    console.log (`Sama saja, k = ${k}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Logika Nested, usia produktif manusia \n")


var usia = 19
var cek = true

if (cek) {
    if ((usia >= 15) && (usia <= 64)) {
        console.log (`Sudah masuk usia produktif manusia, usia = ${usia}`)
    }
    
    else if (usia > 64) {
        console.log (`Sudah lanjut usia, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum masuk usia produktif, usia = ${usia}`)
    }
}

else {
    console.log (`Masih kecil usia nya, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")
