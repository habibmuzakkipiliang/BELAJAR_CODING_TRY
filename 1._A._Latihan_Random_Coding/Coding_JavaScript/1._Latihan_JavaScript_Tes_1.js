// Latihan JavaScript Tes 1 


console.log ("\n Latihan JavaScript Tes 1 \n")



console.log ("\n Pertama dulu \n")


console.log ("Hello World")


console.log ("\n --- Batas --- \n")




console.log ("\n Sintaks dasar \n")


var teks = "Halo dunia"
console.log ("Teks :", teks)


var angka = 23
console.log ("Angka :", angka)


var desimal = 34.2
console.log ("Desimal :", desimal)


var huruf = 'A'
console.log ("Huruf :", huruf)


console.log ("\n --- Batas --- \n")




console.log ("\n Tipe data dasar \n")

var teks = "Halo Tes"
var angka = 23 
var desimal = 34.23
var cek = true
var cek_1 = false
var huruf = 'B'


console.log ("Teks :", teks)
console.log ("Angka :", angka)
console.log ("Desimal :", desimal)
console.log ("Cek :", cek)
console.log ("Cek 1 :", cek_1)
console.log ("Huruf :", huruf)


console.log ("\n --- Batas --- \n")




console.log ("\n Bedanya Pakai Deklarasi Var, Let, Const \n")


console.log ("\n Pakai Var \n")


var teks = "Halo Dunia"
var angka = 23
var desimal = 44.34
var char = 'A'
var cek = true


console.log ("Teks :", teks)
console.log ("Angka :", angka)
console.log ("Desimal :", desimal)
console.log ("Huruf :", char)
console.log ("Cek :", cek)


console.log ("\n --- Batas --- \n")




console.log ("\n Pakai Let \n")


let teks_1 = "Halo Dunia"
let angka_1 = 23
let desimal_1 = 44.34
let char_1 = 'A'
let cek_k = true


console.log ("Teks :", teks_1)
console.log ("Angka :", angka_1)
console.log ("Desimal :", desimal_1)
console.log ("Huruf :", char_1)
console.log ("Cek :", cek_k)


console.log ("\n --- Batas --- \n")




console.log ("\n Pakai Const \n")


let teks_2 = "Halo Dunia"
let angka_2 = 23
let desimal_2 = 44.34
let char_2 = 'A'
let cek_n = true


console.log ("Teks :", teks_2)
console.log ("Angka :", angka_2)
console.log ("Desimal :", desimal_2)
console.log ("Huruf :", char_2)
console.log ("Cek :", cek_n)


console.log ("\n --- Batas --- \n")




console.log ("\n Array \n")


var kos = [
    
    "1. Nangka",
    "2. Buah Naga",
    "3. Apel",
    "4. Salak",
    "5. Anggur"
    
    ]
    
    
for (a = 0; a < kos.length; a++) {
    console.log (kos [a])
}
    
    
console.log ("\n --- Batas --- \n")




console.log ("\n Dictionary \n")
    
    
var objek = {
    "kursi" : "Rp 55.000",
    "meja" : "Rp 50.000",
    "gelas" : "Rp 5.000",
    "piring" : "Rp 10.000",
}


console.log ("Kursi :", objek ["kursi"])

console.log ("Meja :", objek ["meja"])

console.log ("Gelas :", objek ["gelas"])

console.log ("Piring :", objek ["piring"])


console.log ("\n --- Batas ---")





var nama = "Habib Muzakki"
var kelas = "12 Agama"
var absen = "15"
var sekolah = "MAN 2 KOTA SERANG"
var coding = "HTML, CSS, JavaScript dan Python"
var lomba = "Finalis OSN-K Informatika tahun 2025"
var tinggi = "170 cm"
var berat = "60 kg"



var profil = `


----- Profil Saya ------

- Nama         : ${nama}
- Kelas        : ${kelas}
- Absen        : ${absen}
- Sekolah      : ${sekolah}
- coding       : ${coding}
- Lomba        : ${lomba}
- Tinggi badan : ${tinggi}
- Berat badan  : ${berat}

`


console.log (profil)


console.log ("\n --- Batas ---")




console.log ("\n Operator dasar \n")


x = 10
y = 5

console.log ("Tambah =", x + y)
console.log ("Kurang =", x - y)
console.log ("Kali =", x * y)
console.log ("Pangkat =", x ** y)
console.log ("Bagi =", x / y)
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
console.log ("Hasil =", (x > y) || (x > y))
console.log ("Hasil =", (!x))
console.log ("Hasil =", (!y))


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 1 \n")


var a = 5

switch (a) {
    
    case 1:
        console.log ("Senin")
        break
        
    case 2:
        console.log ("Selasa")
        break
        
    case 3:
        console.log ("Rabu")
        break
        
    case 4:
        console.log ("Kamis")
        break
        
    case 5:
        console.log ("Jumat")
        break
        
    case 6:
        console.log ("Sabtu")
        break
        
    case 7:
        console.log ("Minggu")
        break
        
    default:
    console.log ("Biasa")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 2 \n")


var b = 3

switch (b) {
    
    case 1:
        console.log ("Iya")
        break
        
    case 2:
        console.log ("Tidak")
        break
        
    case 3:
        console.log ("Kadang-kadang")
        break
        
    case 4:
        console.log ("Salah")
        break
        
    default:
    console.log ("Biasa")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Dasar \n")


var a = 8

if (a > 5) {
    console.log (`Besar, nilai = ${a}`)
}

else {
    console.log (`Kecil, nilai = ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan \n")


var b = 3 

if (b > 5) {
    console.log (`Besar, nilai = ${b}`)
}

else if (b < 5) {
    console.log (`Kecil, nilai = ${b}`)
}

else {
    console.log (`Semula, nilai = ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan 1 \n")


var c = 9

if (c > 5) {
    console.log (`Besar, nilai = ${c}`)
}

else if (c < 5) {
    console.log (`Kecil, nilai = ${c}`)
}

else {
    console.log (`Semula, nilai = ${c}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nilai Rapor \n")


var skor = 90

if (skor >= 100) {
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
    console.log (`Jelek banget, skor = ${skor}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 1 \n")


var e = 8
var cek = true

if (cek) {
    if (e > 5) {
        console.log (`Besar, nilai = ${e}`)
    }
    
    else if (e < 5) {
        console.log (`Kecil, nilai = ${e}`)
    }
}

else {
    console.log (`Semula, nilai = ${e}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 2 \n")


var j = 3
var cek = true

if (cek) {
    if (j > 5) {
        console.log (`Besar, nilai = ${j}`)
    }
    
    else {
        console.log (`Kecil, nilai = ${j}`)
    }
}

else {
    console.log (`Semula, nilai = ${j}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, Join Member JKT48 tahun 2026 terbaru \n")


var usia = 15
var cek = true

if (cek) {
    if ((usia >= 13) && (usia <= 18)) {
        console.log (`Boleh join JKT48, usia = ${usia}`)
    }
    
    
    else if (usia > 18) {
        console.log (`Sudah lebih dari cukup untik gabung JKT48, usia = ${usia}`)
    }
    
    else {
        console.log (`Masih dibawah umur, usia = ${usia}`)
    }
}

else {
    console.log (`Join saat sudah cukup umur, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, usia produktif manusia di tahun 2026 terbaru \n")


var usia = 15
var cek = true

if (cek) {
    if ((usia >= 15) && (usia <= 64)) {
        console.log (`Usia yang produktif, usia =  ${usia}`)
    }
    
    else if (usia > 64) {
        console.log (`Sudah tua, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum mencapai usia produktif, usia = ${usia}`)
    }
}

else {
    console.log (`Masih belum cukup usia, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar \n")


for (a = 0; a < 11; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- Batas --- \n")



for (b = 0; b < 11; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- Batas --- \n")



for (c = 0; c < 11; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- Batas --- \n")



console.log ("\n While dasar \n")


a = 5

while (a < 11) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- Batas --- \n")



b = 10 

while (b < 16) {
    console.log (`Urutan ke - ${b}`)
    b++
}


console.log ("\n --- Batas --- \n")




c = 15

while (c < 21) {
    console.log (`Urutan ke - ${c}`)
    c++
}


console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar \n")

var a = 5

do {
    console.log (`Urutan ke - ${a}`)
    a++
} while (a < 11)


console.log ("\n --- Batas --- \n")




var b = 10 

do {
    console.log (`Urutan ke - ${b}`)
    b++
} while (b < 16)


console.log ("\n --- Batas --- \n")




var c = 20 

do {
    console.log (`Urutan ke - ${c}`)
    c++
} while (c < 26)


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested \n")


for (a = 0; a < 3; a++) {
    for (b = 0; b < 3; b++) {
        for (c = 0; c < 3; c++) {
            console.log (`Urutan ke - ${a}, Urutan ke - ${b}, Urutan ke - ${c}`)
        }
    }
}


console.log ("\n --- Batas --- \n")




for (d = 0; d < 4; d++) {
    for (e = 0; e < 4; e++) {
        for (s = 0; s < 4; s++) {
            console.log (`Urutan ke - ${d}, Urutan ke - ${e}, Urutan ke - ${s}`)
        }
    }
}


console.log ("\n --- Batas --- \n")




for (x = 0; x < 5; x++) {
    for (y = 0; y < 5; y++) {
        for (z = 0; z < 5; z++) {
            console.log (`Urutan ke - ${x}, Urutan ke - ${y}, Urutan ke - ${z}`)
        }
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dasar \n")


function dasar () {
    console.log ("Hello World")
}

dasar ()


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan parameter 1 \n") 


function dat (nama) {
    console.log (`Halo ${nama}, dari Jakarta`)
}

dat ("Hayyan")
dat ("Naren")
dat ("Sar")
dat ("Nares")
dat ("Rust")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan parameter 2 \n")


function ero (nama) {
    console.log (`Halo semuanya, saya ${nama}, dari Jakarta Utara`)
}

ero ("Rafel")
ero ("Rafa")
ero ("Rael")
ero ("Nael")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan return 1 \n")


function tambah (a, b) {
    return a + b
}

hasil = tambah (20, 20)
console.log ("Tambah =", hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan return 1 \n")


function aro (nama) {
    return `Halo saya ${nama}, asal dari Kota Serang`
}

var hasil = aro ("Habib")
console.log (hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dasar \n")


var hasil = () => {
    console.log ("Hello World")
}

hasil ()


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dengan parameter 1 \n")


var hasil = (nama) => {
    console.log (`Halo aku ${nama}, dari JKT48`)
}

hasil ("Michie")
hasil ("Fritzy")
hasil ("Anindya")
hasil ("Christy")
hasil ("Freya")


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dengan Return \n")


var hasil = (a, b) => {
    return a + b
}

var hasil_1 = hasil (20, 20)
console.log ("Tambah =", hasil_1)


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dengan return 1 \n")


var hasil = (nama) => {
    return `Halo saya ${nama}, dari Kota Serang`
}

var hasil_2 = hasil ("Habib")
console.log (hasil_2)


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 1 \n")


try {
    var a = 10 / 0
    console.log (a)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")





console.log ("\n Error Handling 2 \n")


try {
    var b = 20 / 0
    console.log (b)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 3 \n")


try {
    var c = 10 + 10
    console.log (c)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 4 \n")


try {
    var d = 30 + 30
    console.log (d)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")