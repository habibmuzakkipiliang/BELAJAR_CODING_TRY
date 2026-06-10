// Hello World

console.log ("Hello World")


console.log ("\n ----- Batas --- \n")




// Sintaks dasar dan variabel dasar

var nama = "Habib Muzakki"
var usia = 18
var kelas = 12
var absen = 15
var cek = true
var cek_1 = false 
var des = 34.56
var des_1 = 36.78


console.log ("Nama :", nama)
console.log ("Usia :", usia)
console.log ("Kelas :", kelas)
console.log ("Absen :", absen)
console.log ("Cek :", cek)
console.log ("Cek_1 :", cek_1)
console.log ("Des :", des)
console.log ("Des_1", des_1)


console.log ("\n ----- Batas --- \n")




// Pakai Let

let teks_a = "Teks aja sih"
let angka_a = 234
let desimal_a = 23.23
let huruf_a = 'A'
let bool_a = true


console.log ("Teks a :", teks_a)
console.log ("Angka a :", angka_a)
console.log ("Desimal a :", desimal_a)
console.log ("Huruf a :", huruf_a)
console.log ("Bool a :", bool_a)


console.log ("\n ----- Batas --- \n")




// Pakai const 

const teks_b = "Teks Cek"
const angka_b = 90
const desimal_b = 56.35
const huruf_b = 'B'
const bool_b = false


console.log ("Teks b :", teks_b)
console.log ("Angka b :", angka_b)
console.log ("Desimal b :", desimal_b)
console.log ("Huruf b :", huruf_b)
console.log ("Bool b :", bool_b)


console.log ("\n ----- Batas --- \n")




// Pakai var 

var teks_c = "Teks tes"
var angka_c = 234
var desimal_c = 23.23
var huruf_c = 'C'
var bool_c = true


console.log ("Teks c :", teks_c)
console.log ("Angka c :", angka_c)
console.log ("Desimal c :", desimal_c)
console.log ("Huruf c :", huruf_c)
console.log ("Bool c :", bool_b)


console.log ("\n ----- Batas --- \n")




// Tipe data dasar

var nama = "Loker Baru"
var angka = 12
var des = 22.45
var cek = true
var cek_1 = false
var char = 'A'
var none = null


console.log (nama)
console.log (angka)
console.log (des)
console.log (cek)
console.log (cek_1)
console.log (char)
console.log (none)


console.log ("\n ----- Batas --- \n")




// Profil singkat pembuat kode

var nama = "Habib Muzakki Piliang"
var marga = "Piliang"
var asal = "Indonesia"
var umur = 18
var tinggi = "170 cm"
var berat = "60 kg"
var hobi = "Ngoding, JKT48, Rain Tree (Non Grup 48), AKB48, Nonton Creepypasta Minecraft Jundy Juns dan Main Game Offline"
var coding = "HTML, CSS, JavaScript dan Python"
var suku = "Minangkabau"
var agama = "Islam"
var pekerjaan = "Pelajar"
var sekolah = "MAN 2 Kota Serang"
var kelas = "12 Agama"


console.log ("Nama :", nama)
console.log ("Marga :", marga)
console.log ("Asal :", asal)
console.log ("Umur :", umur)  
console.log ("Tinggi badan :", tinggi)
console.log("Berat badan :", berat)
console.log ("Hobi :", hobi)
console.log ("Suku :", suku)
console.log ("Agama :", agama)
console.log ("Pekerjaan :", pekerjaan)
console.log ("Sekolah :", sekolah)
console.log ("Kelas :", kelas)


console.log ("\n ----- Batas --- \n")




// Operasi Hitung

var x = 10
var y = 5


console.log ("Tambah :", x + y)
console.log ("Kurang :", x - y)
console.log ("Kali :", x * y)
console.log ("Pangkat :", x ** y)
console.log ("Bagi :", x / y)
console.log ("Modulus :", x % y)


console.log ("\n ----- Batas --- \n")




console.log ("Hasil :", x > y)
console.log ("Hasil :", x < y)
console.log ("Hasil :", x <= y)
console.log ("Hasil :", x >= y)
console.log ("Hasil :", x == y)
console.log ("Hasil :", x != y)


console.log ("\n ----- Batas --- \n")




console.log ("Hasil :", (x > y) && (x < y))
console.log ("Hasil :", (x < y) || (x > y))
console.log ("Hasil :", ! x)
console.log ("Hasil :", ! y)


console.log ("\n ----- Batas --- \n")




// Manipulasi String

var a = "Smurf Badai"
console.log (`Halo ${a}`)


var b = "Smurf Petani"
console.log (`Halo ${b}`)


var c = "Smurf Kekar"
console.log (`Halo ${c}`)


var d = "Smurf Genit"
console.log (`Halo ${d}`)


var e = "Smurf Run"
console.log (`Halo ${e}`)


console.log ("\n ----- Batas --- \n")




// Percabangan Dasar

var a = 10

if (a > 5) {
    console.log ("Besar")
}

else {
    console.log ("Kecil")
}


console.log ("\n ----- Batas --- \n")




// Percabangan Lanjutan

var b = 3

if (b > 5) {
    console.log ("Besar")
}

else if (b < 5) {
    console.log ("Kecil")
}

else {
    console.log ("Semula")
}


console.log ("\n ----- Batas --- \n")




// Percabangan Tangga Lanjutan

var f = 9

if (f > 8) {
    console.log ("Besar")
}

else if (f == 7) {
    console.log ("7")
}

else if (f == 6) {
    console.log ("6")
}

else if (f == 5) {
    console.log ("5")
}

else if (f == 4) {
    console.log ("4")
}

else if (f == 3) {
    console.log ("3")
}

else if (f == 2) {
    console.log ("2")
}

else if (f == 1) {
    console.log ("1")
}

else {
    console.log ("Semula")
}


console.log ("\n ----- Batas --- \n")




// Percabangan Nested 1 

var c = 7
var cek = true

if (cek) {
    if (c > 5) {
        console.log ("Besar")
    }
    
    else {
        console.log ("Kecil")
    }
}

else {
    console.log ("Semula")
}


console.log ("\n ----- Batas --- \n")




// Percabangan Nested 2

var d = 7
var cek = true

if (cek) {
    if (d > 5) {
        console.log ("Besar")
    }
    
    else if (d < 5) {
        console.log ("Kecil")
    }
}

else {
    console.log ("Semula")
}


console.log ("\n ----- Batas --- \n")



// Switch Case 1

var a = 2

switch (a) {

    case 1:
        console.log ("Iya")
        break

    case 2:
        console.log ("Tidak")
        break

    default:
        console.log ("Bingung")
}

console.log ("\n ----- Batas --- \n")




// Switch Case 2

var b = 5

switch (b) {

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
        console.log ("Bukan Hari Apa Apa")
}


console.log ("\n ----- Batas --- \n")




// For Dasar

for (a = 0; a < 5; a++) {
    console.log ("a", a)
}


console.log ("\n ----- Batas --- \n")




for (b = 0; b < 4; b++) {
    console.log ("b", b)
}


console.log ("\n ----- Batas --- \n")




for (c = 0; c < 6; c++) {
    console.log ("c", c)
}


console.log ("\n ----- Batas --- \n")




for (k = 0; k < 7; k++) {
    console.log ("k", k)
}


console.log ("\n ----- Batas --- \n")




for (j = 0; j < 6; j++) {
    console.log ("j", j)
}


console.log ("\n ----- Batas --- \n")




// For Nested 

for (a = 0; a < 3; a++) {
    for (b = 0; b < 2; b++) {
        console.log ("a", a, "b", b)
    }
}


console.log ("\n ----- Batas --- \n")




for (c = 0; c < 2; c++) {
    for (d = 0; d < 3; d++) {
        console.log ("c", c, "d", d)
    }
}


console.log ("\n ----- Batas --- \n")




for (e = 0; e < 5; e++) {
    for (f = 0; f < 2; f++) {
        console.log ("e", e, "f", f)
    }
}


console.log ("\n ----- Batas --- \n")




for (g = 0; g < 2; g++) {
    for (h = 0; h < 4; h++) {
        console.log ("g", g, "h", h)
    }
}


console.log ("\n ----- Batas --- \n")




for (i = 0; i < 3; i++) {
    for (j = 0; j < 3; j++) {
        console.log ("i", i, "j", j)
    }
}


console.log ("\n ----- Batas --- \n")




// While Dasar

var a = 0

while (a < 5) {
    console.log ("a", a)
    a++
}


console.log ("\n ----- Batas --- \n")




var b = 0

while (b < 5) {
    console.log ("b", b)
    b++
}


console.log ("\n ----- Batas --- \n")




var c = 0

while (c < 6) {
    console.log ("c", c)
    c++
}


console.log ("\n ----- Batas --- \n")




var d = 0

while (d < 4) {
    console.log ("d", d)
    d++
}


console.log ("\n ----- Batas --- \n")




var e = 0

while (e < 6) {
    console.log ("e", e)
    e++
}


console.log ("\n ----- Batas --- \n")




// Do While dasar

var a = 0

do {
    console.log ("a", a)
    a++
} while (a < 6)


console.log ("\n ----- Batas --- \n")




var b = 0

do {
    console.log ("b", b)
    b++
} while (b < 6)



var c = 0

do {
    console.log ("c", c)
    c++
} while (c < 6)


console.log ("\n ----- Batas --- \n")




var c = 0

do {
    console.log ("c", c)
    c++
} while (c < 6)


console.log ("\n ----- Batas --- \n")




var d = 0

do {
    console.log ("d", d)
    d++
} while (d < 6)


console.log ("\n ----- Batas --- \n")




var e = 0

do {
    console.log ("e", e)
    e++
} while (e < 6)


console.log ("\n ----- Batas --- \n")




// Array Dasar

var ab = [1, 2, 3, 4, 5, 6, 7, 8]

console.log (ab)
console.log (ab [0])
console.log (ab [1])
console.log (ab [2])


console.log ("\n ----- Batas --- \n")




var cd = ["josua", "johan", "rust", "runter", "safrer", "Rainer"]

console.log (cd)
console.log (cd [0])
console.log (cd [1])
console.log (cd [2])


console.log ("\n ----- Batas --- \n")




// Array otomatis

var ch = ["Christy", "Olla", "Marsha", "Freya", "Muthe", "Mikaela"]

console.log (ch)

for (a = 0; a < ch.length; a++) {
    console.log ("-", ch [a])
}


console.log  ("\n ----- Batas --- \n")




var df = ["Const", "Let", "Var", "JavaScript", "Python", "Jansen"]

console.log (df)

for (c = 0; c < df.length; c++) {
    console.log (df [c])
}


console.log  ("\n ----- Batas --- \n")




var sd = ["Rir", "Run", "Rtu", "Far", "Ago", "RangeInt", "RangeFloat", "RangeString"]

console.log (sd)

for (d = 0; d < sd.length; d++) {
    console.log (sd [d])
}


console.log ("\n ----- Batas --- \n")




// Object JavaScript

var data = {
    "nama" : "Guido Hansel",
    "asal" : "Amerika serikat",
    "umur" : 25,
    "tinggi" : "170 cm",
    "berat" : "60 kg",
}


console.log ("Nama :", data ["nama"])

console.log ("Asal :", data ["asal"])

console.log ("Umur :", data ["umur"])

console.log ("Tinggi badan :", data ["tinggi"])

console.log ("Berat badan :", data ["berat"])


console.log ("\n ----- Batas --- \n")




// Fungsi dasar

function dasar () {
    console.log ("Halo Dunia")
}

dasar ()


console.log ("\n ----- Batas --- \n")




// Fungsi dasar 1

function daser () {
    console.log ("Halo Div")
}

daser ()


console.log ("\n ----- Batas --- \n")




// Fungsi dasar 2

function name () {
    console.log ("Halo Dunia")
    console.log ("Halo World")
    console.log ("Halo Sun")
    console.log ("Saf")
}

name ()


console.log ("\n ----- Batas --- \n")




// Fungsi dasar 3

function jim () {
    console.log ("Halo Notch")
}

jim ()
jim ()
jim ()
jim ()


console.log ("\n ----- Batas --- \n")




// Fungsi dasar 4

function dat () {
    console.log ("Hello World")
}

dat ()


console.log ("\n ----- Batas --- \n")




// Fungsi dengan parameter 

function ser (nama) {
    console.log ("Halo " + nama)
}

ser ("Dunia")
ser ("Rust")
ser ("Rumble")
ser ("Rar")


console.log ("\n ----- Batas --- \n")




// Fungsi dengan parameter 2

function tam (jun) {
    console.log ("Halo " + jun)
}

tam ("Rust")
tam ("Even")
tam ("Sar")
tam ("Eril")


console.log ("\n ----- Batas --- \n")




// Fungsi dengan parameter 3

function dem (name) {
    console.log ("Halo " + name)
}

dem ("Hurt")
dem ("Surf")
dem ("Ran")
dem ("Def")


console.log ("\n ----- Batas --- \n")




// Fungsi dengan return

function tambah (a, b) {
    return a + b
}

hasil = tambah (10, 7)
console.log (hasil)


console.log ("\n ----- Batas --- \n")




// Fungsi dengan return 2

function kurang (c, d) {
    return c - d
}

hasil = kurang (10, 5)
console.log (hasil)


console.log ("\n ----- Batas --- \n")




// Fungsi dengan return 3

function kali (d, f) {
    return d * f
}

hasil = kali (10, 5)
console.log (hasil)


console.log  ("\n ----- Batas --- \n")




// Fungsi dengan return 4

function pangkat (e, f) {
    return e ** f
}

hasil = pangkat (10, 3)
console.log (hasil)


console.log ("\n ----- Batas --- \n")




// Fungsi dengan return 5

function modulus (e, t) {
    return e % t
}

hasil = modulus (10, 3)
console.log (hasil)