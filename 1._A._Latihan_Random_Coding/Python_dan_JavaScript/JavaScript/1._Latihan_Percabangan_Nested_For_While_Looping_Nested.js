console.log ("\n Profil Habib Muzakki Piliang \n")


var nama = "Habib Muzakki"
var panggil = "Habib"
var marga = "Piliang"
var suku = "Minangkabau"
var coding = "HTML, CSS, JavaScript dan Python"
var lomba = "Finalis OSN-K Informatika tahun 2025"
var alumni = "MAN 2 KOTA SERANG (tahun 2026)"
var kelas = "12 Agama (tahun 2026)"
var tinggi = "170 cm"
var berat = "60 kg"
var darah = "B"
var fans = "JKT48"
var oshi = "Michie, Gracie,  Fritzy, Anindya, Christy, Freya, Fiony JKT48"


var profil = `

- Nama lengkap   : ${nama}
- Nama panggilan : ${panggil}
- Marga          : ${marga}
- Suku           : ${suku}
- Coding         : ${coding}
- Lomba          : ${lomba}
- Alumni         : ${alumni}
- Kelas          : ${kelas}
- Tinggi badan   : ${tinggi}
- Berat badan    : ${berat}
- Golongan darah : ${darah}
- Fans           : ${fans}
- Oshi JKT48     : ${oshi}

`


console.log (profil)


console.log ("\n --- Batas --- \n")




console.log ("\n Tipe data pemrograman \n")


var teks = "Halo Guys"
var angka = 23
var desimal = 45.2
var cek = true
var kosong = null
var huruf = 'A'


var ner = `

- Teks    = ${teks}
- Angka   = ${angka}
- Desimal = ${desimal}
- Cek     = ${cek}
- Kosong  = ${kosong}
- Huruf   = ${huruf}

`

console.log (ner)


console.log ("\n --- Batas --- \n")




console.log ("\n Operator Dasar \n")


var x = 10
var y = 5


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
console.log ("Hasil =", x == y)
console.log ("Hasil =", x != y)
console.log ("Hasil =", x >= y)
console.log ("Hasil =", x <= y)


console.log ("\n --- Batas --- \n")




console.log ("\n Operator Logika \n")


console.log ("Hasil =", (x > y) && (x < y))
console.log ("Hasil =", (x < y) || (x > y))
console.log ("Hasil =", (! x))
console.log ("Hasil =", (! y))


console.log ("\n --- Batas --- \n")




console.log ("\n Array \n")


var far = [
    
    "1. Perang Dunia 1",
    "2. Perang Dunia 2",
    "3. Front Timur WW2",
    "4. Front Barat WW2",
    "5. Front Timur WW1",
    "6. Front Barat WW1",
    
    
    ]
    
    
for (a = 0; a < far.length; a++) {
    console.log (far [a])
}


console.log ("\n --- Batas --- \n")




console.log ("\n Dictionary \n")


var profil = {
    "nama" : "John Sam",
    "asal" : "Amerika Serikat",
    "kerja" : "Software Engineer",
    "usia" : "25 tahun",
    "coding" : "HTML, CSS, JavaScript dan Python",
}


console.log ("Nama :", profil ["nama"])

console.log ("Asal :", profil ["asal"])

console.log ("Kerja :", profil ["kerja"])

console.log ("Usia :", profil ["usia"])

console.log ("Coding :", profil ["coding"])


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case \n")


var hari = "Senin"

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




console.log ("\n Switch Case 1 \n")


var kondisi = 2

switch (kondisi) {
    
    case 1:
        console.log ("Aman")
        break
        
    case 2:
        console.log ("Baik")
        break
        
    case 3:
        console.log ("Senang")
        break
        
    case 4:
        console.log ("Bahagia")
        break
        
    case 5:
        console.log ("Oke")
        break
        
    default:
    console.log ("Biasa aja")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan dasar \n")


var a = 9

if (a > 5) {
    console.log (`Besar, a = ${a}`)
}

else {
    console.log (`Kecil, a = ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan \n")


var k = 3

if (k > 5) {
    console.log (`Besar, k = ${k}`)
}

else if (k < 5) {
    console.log (`Kecil, k = ${k}`)
}

else {
    console.log (`Sama saja, k = ${k}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Ledder \n")


var s = 7

if (s >= 9) {
    console.log (`A, skor = ${s}`)
}

else if (s >= 8) {
    console.log (`B, skor = ${s}`)
}

else if (s >= 7) {
    console.log (`C, skor = ${s}`)
}

else if (s >= 6) {
    console.log (`D, skor = ${s}`)
}

else if (s >= 5) {
    console.log (`E, skor = ${s}`)
}

else {
    console.log (`Jelek, skor = ${s}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 1 \n")


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




console.log ("\n Percabangan Nested 2 \n")


var d = 3
var cek = true

if (cek) {
    if (d > 5) {
        console.log (`Besar, d = ${d}`)
    }
    
    else {
        console.log (`Kecil, d = ${d}`)
    }
}

else {
    console.log (`Sama saja, d = ${d}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, usia produktif 1 \n")


var usia = 20
var cek = true

if (cek) {
    if ((usia >= 15) && (usia <= 64)) {
        console.log (`Sudah masuk usia produktif, usia = ${usia}`)
    }
    
    else if (usia > 64) {
        console.log (`Sudah lanjut usia, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum masuk usia produktif, usia = ${usia}`)
    }
}

else {
    console.log (`Masih kecil usianya, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, usia produktif manusia 2 \n")


var usia = 13
var cek = true

if (cek) {
    if ((usia >= 15) && (usia <= 64)) {
        console.log (`Sudah masuk usia produktif, usia = ${usia}`)
    }
    
    else if (usia > 64) {
        console.log (`Sudah lanjut usia, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum masuk usia produktif, usia = ${usia}`)
    }
}

else {
    console.log (`Masih kecil usianya, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")



console.log ("\n Percabangan Nested, masuk dan join jadi member JKT48 (1) \n")


var usia = 19
var cek = true

if (cek) {
    if ((usia >= 13) && (usia <= 17)) {
        console.log (`Boleh daftar JKT48, usia = ${usia}`)
    }
    
    else if (usia > 17) {
        console.log (`Sudah lebih dari cukup, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum cukup umur untuk daftar, usia = ${usia}`)
    }
}

else {
    console.log (`Di lain waktu daftarnya, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, Percabangan Nested, masuk dan join jadi member JKT48 (2) \n")


var usia = 10
var cek = true

if (cek) {
    if ((usia >= 13) && (usia <= 17)) {
        console.log (`Boleh daftar JKT48, usia = ${usia}`)
    }
    
    else if (usia > 17) {
        console.log (`Sudah lebih dari cukup, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum cukup umur untuk daftar, usia = ${usia}`)
    }
}

else {
    console.log (`Di lain waktu daftarnya, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")





console.log ("\n For dasar  1 \n")


for (a = 0; a < 16; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar 2 \n")


for (b = 0; b < 21; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar 3 \n")


for (c = 0; c < 26; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- Batas --- \n")



console.log ("\n While dasar 1 \n")


var a = 5

while (a < 21) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar 2 \n")


var b = 10

while (b < 21) {
    console.log (`Urutan ke - ${b}`)
    b++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar 3 \n")


var c = 3

while (c < 15) {
    console.log (`Urutan ke - ${c}`)
    c++
} 


console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar 1 \n")


var a = 3

do {
    console.log (`Urutan ke - ${a}`)
    a++
} while (a < 16)


console.log ("\n --- Batas --- \n")



console.log ("\n Do While dasar 2 \n")


var b = 5

do {
    console.log (`Urutan ke - ${b}`)
    b++
} while (b < 21)


console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar 3 \n")


var c = 10

do {
    console.log (`Urutan ke - ${c}`)
    c++
} while (c < 25)


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 1 \n")


for (a = 0; a < 5; a++) {
    for (b = 0; b < 5; b++) {
        for (c = 0; c < 5; c++) {
            console.log (`Urutan ke - ${a}, urutan ke - ${b}, urutan ke - ${c}`)
        }
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 2 \n")


for (x = 0; x < 6; x++) {
    for (y = 0; y < 6; y++) {
        for (z = 0; z < 6; z++) {
            console.log (`Urutan ke - ${x}, urutan ke - ${y}, urutan ke - ${z}`)
        }
    } 
}



console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 3 \n")


for (t = 0; t < 7; t++) {
    for (j = 0; j < 7; j++) {
        for (h = 0; h < 7; h++) {
            console.log (`Urutan ke - ${t}, urutan ke - ${j}, urutan ke - ${h}`)
        }
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dasar \n")


function dasar () {
    console.log ("Hello Tes")
}

dasar ()


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dasar 1 \n")

 
function nos () {
    console.log ("Hello Tes 1")
    console.log ("Hello Jan")
    console.log ("Hello Jer")
    console.log ("Ser Don")
}

nos ()


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Parameter \n")


function der (nama) {
    console.log (`Halo saya ${nama} dari Karawang`)
}

der ("Hanif")
der ("Hayyan")
der ("Roy")
der ("For")
der ("Fer")
der ("Iyan")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan parameter 1 \n")


function fer (nama) {
    console.log (`Halo aku ${nama} dari Jakarta`)
}

fer ("Johan")
fer ("Royan")
fer ("Notch")
fer ("Arthur")
fer ("Mobile")
fer ("Nuron")
fer ("Ring")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Return \n")


function tambah (x, y) {
    return x + y
}

var hasil = tambah (10, 8)
console.log ("Tambah =", hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Return 1 \n")


function ron (nama) {
    return `Halo saya ${nama} dari Jakarta Pusat`
}

var hasil = ron ("Habib")
console.log (hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi \n")

var tes = () => {
    console.log ("Hello Tes")
}

tes ()


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi 1 \n")


var tes = () => {
    console.log ("Hello 1")
    console.log ("Hello 2")
    console.log ("Hello 3")
    console.log ("Hello 4")
}

tes ()


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dengan Parameter \n")


var tes = (nama) => {
    console.log (`Halo saya ${nama}, dari Jakarta Utara`)
}

tes ("Hayyan")
tes ("Lan")
tes ("Kalce")
tes ("First")
tes ("Yon")
tes ("Yan")


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dengan parameter 2 \n")


var tes = (nama) => {
    console.log (`Halo, saya ${nama}, dari Jakarta Barat`)
}

tes ("Hui")
tes ("Vas")
tes ("Ras")
tes ("Run")
tes ("Roger")
tes ("Lan")


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dengan Return 1 \n")


var tes = (x, y) => {
    return x + y
}

var hasil = tes (10, 5)
console.log ("Tambah =", hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Arrow Fungsi dengan Return 2 \n")


var tes = (nama) => {
    return `Halo saya ${nama} dari Jakarta Barat`
}

var hasil = tes ("Habib")
console.log (hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 1 \n")

try {
    var hasil = 10 / 0
    console.log (hasil)
}


catch (Error) {
    console.log ("Gagal", Error)
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 2 \n")


try {
    var jun = 20 / 0
    console.log (jun)
}

catch (Error) {
    console.log ("Gagal", Error)
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 3 \n")


try {
    var hasil = 10 + 10
    console.log (hasil)
}

catch (Error) {
    console.log ("Gagal", Error)
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 4 \n")


try {
    var hasil = 20 + 20
    console.log (hasil)
} 

catch (Error) {
    console.log ("Gagal", Error)
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")
