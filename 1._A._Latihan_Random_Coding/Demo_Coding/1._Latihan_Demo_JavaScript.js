// Latihan Demo JavaScript

console.log ("\n Bikin Hello World \n")


console.log ("Hello World")


console.log ("\n --- Batas --- \n")




console.log ("\n Variabel dasar \n")


var nama = "Habib Muzakki"
console.log (nama)


var angka = 23
console.log (angka)


var desimal = 23.1
console.log (desimal)


var char = 'A'
console.log (char)


var cek = true
console.log (cek)


var kosong = null
console.log (kosong)


console.log ("\n --- Batas --- \n")




console.log ("\n Membedakan Deklarasi Var, Const dan Let \n")


console.log ("\n Pakai Var \n")


var nama = "Halo Dunia"
var nomor = 12
var desimal = 23.21
var cek = true

var detail = `

- Nama    : ${nama}
- Nomor   : ${nomor}
- Desimal : ${desimal}
- Cek     : ${cek}

`


console.log (detail)


console.log ("\n --- Batas --- \n")




console.log ("\n Pakai Const \n")


const nomor_1 = 23
const cek_1 = true
const desimal_1 = 34.24
const nama_1 = "Halo Dunia"


const detail_1 = `

- Nama 1    : ${nama_1}
- Nomor 1   : ${nomor_1}
- Desimal 1 : ${desimal_1}
- Cek 1     : ${cek_1}

`

console.log (detail_1)


console.log ("\n --- Batas --- \n")




console.log ("\n Pakai Let \n")


let nomor_2 = 23
let cek_2 = true
let desimal_2 = 34.24
let nama_2 = "Halo Dunia"


const detail_2 = `

- Nama 1    : ${nama_2}
- Nomor 1   : ${nomor_2}
- Desimal 1 : ${desimal_2}
- Cek 1     : ${cek_2}

`

console.log (detail_2)


console.log ("\n --- Batas --- \n")




console.log ("\n Habib Muzakki Piliang \n")


var nama = "Habib Muzakki"
var panggil = "Habib"
var marga = "Piliang"
var asal = "Kota Bukittinggi"
var tinggal = "Kota Serang"
var suku = "Minangkabau"
var coding = "HTML, CSS, JavaScript dan Python"
var lomba = "Finalis OSN-K Informatika tahun 2025"
var alumni = "MAN 2 KOTA SERANG (tahun 2026)"
var kelas = "12 Agama (tahun 2026)"
var tinggi = "170 cm"
var berat = "60 kg"
var darah = "B"
var fans = "JKT48"
var oshi = "Michie, Gracie, Fritzy, Lily, Anindya, Christy, Freya JKT48"


var profil = `

- Nama lengkap    : ${nama}
- Nama panggilan  : ${panggil}
- Marga           : ${marga}
- Asal daerah     : ${asal}
- Tempat tinggal  : ${tinggal}
- Suku            : ${suku}
- Coding          : ${coding}
- Lomba           : ${lomba}
- Alumni          : ${alumni}
- Kelas           : ${kelas}
- Tinggi badan    : ${tinggi}
- Berat badan     : ${berat}
- Golongan darah  : ${darah}
- Fans            : ${fans}
- Oshi JKT48      : ${oshi}

`

console.log (profil)


console.log ("\n --- Batas --- \n")




console.log ("\n Tipe data pemrograman \n")


var teks = "Halo Dunia"
var angka = 22
var desimal = 23.22
var cek = true
var char = 'A'
var kosong = null


var tipe = `

- Teks    = ${teks}
- Angka   = ${angka}
- Desimal = ${desimal}
- Cek     = ${cek}
- Char    = ${char}
- Kosong  = ${kosong}

`


console.log (tipe)


console.log ("\n --- Batas --- \n")




console.log ("\n Operator dasar \n")


var x = 10 
var y = 5

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




console.log ("\n Array \n")


var perang = [
    
    "1. Front Timur WW1",
    "2. Front Barar WW1",
    "3. Front Timur WW2",
    "4. Front Barat WW2",
    "5. Front Afrika WW2",
    "6. Perang Pasifik WW2",
    "7. Perang Dunia 2",
    "8. Perang Dunia 1",
    
    ]
    
    
for (a = 0; a < perang.length; a++) {
    console.log (perang [a])
}


console.log ("\n --- Batas --- \n")




console.log ("\n Dictionary \n")


var biodata = {
    "nama" : "Harold Paul von Hindenburg",
    "asal" : "Jerman",
    "kerja" : "Programmer",
    "usia" : "25 tahun",
    "tinggi" : "175 cm",
    "berat" : "60 kg",
    "coding" : "HTML, CSS, JavaScript, Python, C++, Rust dan Go",
    "fans" : "AKB48, JKT48, K-Pop",
    "oshi" : "Michie JKT48, Lily JKT48, Fritzy JKT48, Yui Oguri AKB48",
}

console.log ("Nama :", biodata ["nama"])

console.log ("Asal :", biodata ["asal"])

console.log ("Kerja :", biodata ["kerja"])

console.log ("Tinggi badan :", biodata ["tinggi"])

console.log ("Berat badan :", biodata ["berat"])

console.log ("Coding :", biodata ["coding"])

console.log ("Fans :", biodata ["fans"])

console.log ("Oshi :", biodata ["oshi"])


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case \n")


var kondisi = 3

switch (kondisi) {
    
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
        
    default:
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case  1 \n")


var hari = "Jumat"

switch (hari) {
    
    case "Senin":
        console.log ("Senin")
        break
        
    case "Selasa":
        console.log ("Selasa")
        break
    
    case "Rabu":
        console.log ("Rabu")
        break
        
    case "Kamis":
        console.log ("Kamis")
        break
        
    case "Jumat":
        console.log ("Jumat")
        break
        
    default:
    console.log ("Libur")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Dasar 1 \n")


var a = 9

if (a > 5) {
    console.log (`Besar, a = ${a}`)
}

else {
    console.log (`Kecil, a = ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Dasar 2 \n")


var b = 3

if (b > 5) {
    console.log (`Besar, b = ${b}`)
}

else {
    console.log (`Kecil, b = ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan 1 \n")


var c = 10

if (c > 5) {
    console.log (`Besar, c = ${c}`)
}

else if (c < 5) {
    console.log (`Kecil, c = ${c}`)
}

else {
    console.log (`Sama saja, c = ${c}`)
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




console.log ("\n Percabangan Ledder \n")


var rapor = 95

if (rapor >= 95) {
    console.log (`A, nilai = ${rapor}`)
}

else if (rapor >= 90) {
    console.log (`B, nilai = ${rapor}`)
}

else if (rapor >= 80) {
    console.log (`C, nilai = ${rapor}`)
}

else if (rapor >= 70) {
    console.log (`D, nilai = ${rapor}`)
}

else if (rapor >= 60) {
    console.log (`E, nilai = ${rapor}`)
}

else if (rapor >= 50) {
    console.log (`F, nilai = ${rapor}`)
}

else {
    console.log (`Jelek banget, nilai = ${rapor}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 1 \n")


var g = 10
var cek = true

if (cek) {
    if (g > 5) {
        console.log (`Besar, g = ${g}`)
    }
    
    else if (g < 5) {
        console.log (`Kecil, g = ${g}`)
    }
}

else {
    console.log (`Sama saja, g = ${g}`)
}


console.log ("\n --- Batas --- \n")





console.log ("\n Percabangan Nested 2 \n")


var e = 3
var cek = true

if (cek) {
    if (e > 5) {
        console.log (`Besar, e = ${e}`)
    }
    
    else {
        console.log (`Kecil, e = ${e}`)
    }
}

else {
    console.log (`Sama saja, e = ${e}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, usia produktif \n")


var usia = 19
var cek = true

if (cek) {
    if ((usia >= 15) && (usia <= 64)) {
        console.log (`Sudah masuk usia produktif, usia = ${usia}`)
    }
    
    else if (usia > 64) {
        console.log (`Sudah tua usianya, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum masuk usia produktif, usia = ${usia}`)
    }
}

else {
    console.log (`Masih balita usianya, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, usia join JKT48 \n")


var usia = 19
var cek = true

if (cek) {
    if ((usia >= 13) && (usia <= 18)) {
        console.log (`Sudah boleh join JKT48, usia = ${usia}`)
    }
    
    else if (usia > 18) {
        console.log (`Sudah lebih dari cukup, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum boleh masuk JKT48, usia = ${usia}`)
    }
}

else {
    console.log (`Di lain waktu daftarnya, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, standar tinggi cowok \n")


var tinggi = 170
var cek = true

if (cek) {
    if ((tinggi >= 163) && (tinggi <= 168)) {
        console.log (`Standar tinggi cowok, tinggi = ${tinggi}`)
    }
    
    else if (tinggi > 168) {
        console.log (`Ideal, tinggi cowok, tinggi = ${tinggi}`)
    }
    
    else {
        console.log (`Masih pendek, tinggi = ${tinggi}`)
    }
}

else {
    console.log (`Belum tinggi, tinggi = ${tinggi}`)
}


console.log ("\n --- Batas --- \n")




console.log("\n Percabangan Nested, berat badan standar cowok \n")


var berat = 60
var cek = true

if (cek) {
    if ((berat >= 55) && (berat <= 65)) {
        console.log (`Berat badan ideal, berat = ${berat}`)
    }
    
    else if (berat > 65) {
        console.log (`Obesitas, berat = ${berat}`)
    }
    
    else {
        console.log (`Kurus, berat = ${berat}`)
    }
}

else {
    console.log (`Kurus, berat = ${berat}`)
}


console.log ("\n --- Batas --- \n")



console.log ("\n For dasar \n")


for (a = 0; a < 10; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar 1 \n")


for (b = 2; b < 20; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- Batas --- \n")



console.log ("\n For dasar 2 \n")


for (c = 15; c < 30; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar 3 \n")


for (d = 10; d < 30; d++) {
    console.log (`Urutan ke - ${d}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar 5 \n")


for (e = 20; e < 30; e++) {
    console.log (`Urutan ke - ${e}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar 1 \n")


var a = 10

while (a < 20) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar 2 \n")


var b = 5

while (b < 30) {
    console.log (`Urutan ke - ${b}`)
    b++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar 3 \n")

var c = 15 

while (c < 30) {
    console.log (`Urutan ke - ${c}`)
    c++
}


console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar 1 \n")


var a = 5 

do {
    console.log (`Urutan ke - ${a}`)
    a++
} 

while (a < 15)


console.log ("\n --- Batas --- \n")




console.log ("\n Do While 2 \n")


var b = 10

do {
    console.log (`Urutan ke - ${b}`)
    b++
}


while (b < 30)


console.log ("\n --- Batas --- \n")




console.log ("\n Do While 3 \n")


var c = 15

do {
    console.log (`Urutan ke- ${c}`)
    c++
}


while (c < 30)


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 1 \n")


for (a = 0; a < 6; a++) {
    for (b = 0; b < 6; b++) {
        console.log (`Bagian luar a : ${a}, bagian dalam b : ${b}`)
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 2 \n")


for (x = 0; x < 6; x++) {
    for (y = 0; y < 6; y++) {
        console.log (`Bagian luar x : ${x}, Bagian dalam y : ${y}`)
    } 
}




console.log ("\n For Nested 3 \n")


for (d = 0; d < 6; d++) {
    for (e = 0; e < 6; e++) {
        console.log (`Bagian luar d : ${d}, Bagian dalam e : ${e}`)
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n Iterasi For Continue \n")


for (w = 0; w < 20; w++) {
    if (w == 10) {
        continue 
    }
    
    console.log (`Urutan ke - ${w}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Iterasi For Break \n")


for (h = 0; h < 20; h++) {
    if (h == 15) {
        break
    }
    
    console.log (`Urutan ke - ${h}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Array Iterasi For Continue \n")


var tank = [
    
    "1. Tiger I",
    "2. T90",
    "3. Panther IV",
    "4. Panther III",
    "5. M4 Sherman",
    "6. M3 Stuart",
    "7. Leopard I",
    "8. Leopard II",
    "9. T34",
    "10. T55",
    
    ]
    
    
for (e of tank) {
    if (e == "M4 Sherman") {
        continue
    }
    
    console.log (e)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Array Iterasi For Break \n")


var number = [
    
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    
    ]


for (a of number) {
    if (a == 5) {
        break
    }
    
    console.log (a)
}
    
    
console.log ("\n --- Batas --- \n")





console.log ("\n Error Handling 1 \n")


try {
    var hasil = 10 / A
    console.log (hasil)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")





console.log ("\n Error Handling 2 \n")


try {
    var hasil = 20 / k
    console.log (hasil)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 3 \n")


try {
    var hasil = 20 + 20
    console.log (hasil)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dasar 1 \n")


function dasar () {
    console.log ("Hello World")
}

dasar ()


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dasar 2 \n")


function eron () {
    console.log ("Hello Dun")
    console.log ("Hello Def")
    console.log ("Hello JKT48")
    console.log ("Hello Michie JKT48")
    console.log ("Hello Gracie JKT48")
    console.log ("Hello Fritzy JKT48")
    console.log ("Hello Lily JKT48")
    
}
    
eron ()


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dasar dengan parameter \n")


function far (nama) {
    console.log (`Saya ${nama}, dari Jakarta`)
}

far ("Hayyan")
far ("Fayyan")
far ("Rayyan")
far ("Rust")
far ("Rush")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dasar dengan Return 1 \n")


function tambah (a, b) {
    return a + b
}

hasil = tambah (10, 10)
console.log ("Tambah =", hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dasar dengan return 2 \n")


function fin (nama) {
    return `Halo saya ${nama}, dari Jakarta Barat`
}

hasil = fin ("Habib")
console.log (hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dasar \n")


var hasil = () => {
    console.log ("Hello World")
}

hasil ()


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dasar 2 \n")


var hasil = () => {
    console.log ("Hello Uranium")
    console.log ("Hello Fun")
    console.log ("Hellon Rust")
    console.log ("Hello Trop")
    console.log ("Jon Jello")
}

hasil ()


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dasar dengan Parameter \n")


var hasil = (nama) => {
    console.log (`Halo ${nama} dari Jakarta`)
}

hasil ("Dart")
hasil ("Truth")
hasil ("John")
hasil ("Ruft")
hasil ("Sor")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Error Handling \n")


function cekAngka (a) {
    try {
        if (a < 0) {
            throw ("Minus")
            console.log (`Angka minus, angka = ${a}`)
        }
        
        else {
            console.log (`Angka minus, angka = ${a}`)
        }
    }
    
    catch (Error) {
        console.log (`Gak boleh Minus = ${a}`)
    }
}

cekAngka (-5)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi Error Handling 2 \n")

 
function dasar (b) {
    try {
        if (b < 0) {
            throw ("Minus")
            console.log (`Angka minus, angka ${b}`)
        }
        
        else {
            console.log (`Angka benar, angka = ${b}`)
        }
    }
    
    catch (Error) {
        console.log (`Gak boleh Minus, angka = ${b}`)
    }
}

dasar (10)


console.log ("\n --- Batas --- \n")
