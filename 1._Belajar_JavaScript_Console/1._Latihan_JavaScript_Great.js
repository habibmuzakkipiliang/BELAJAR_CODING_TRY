// Hello World By JavaScript

console.log ("\n Hello World By JavaScript \n")


console.log ("Hello World")


console.log ("\n --- Batas --- \n")




// Sintaks dasar

console.log ("\n Sintaks dasar \n")


var v = "Vibe JKT48"

console.log ("String = ", v)


console.log ("\n --- Batas --- \n")




var teks = "Semangat member JKT48"

console.log ("Teks =", teks)


console.log ("\n --- Batas --- \n")




var angka = 34

console.log ("Angka =", angka)


console.log ("\n --- Batas --- \n")




var desimal = 34.2

console.log ("Desimal =", desimal)


console.log ("\n --- Batas --- \n")




// Profil singkat aja 

console.log ("\n Profil singkat aja \n")


var nama = "James Drake"
var kerja = "Developer, Programmer, dan Software Engineer"
var asal = "Amerika Serikat"
var etnis = "Inggris - Amerika Serikat"
var coding = "HTML, CSS, JavaScript dan Python"
var usia = "30 tahun"
var perusahaan = "Google"


console.log ("Nama :", nama)
console.log ("Kerja :", kerja)
console.log ("Asal :", asal)
console.log ("Etnis :", etnis)
console.log ("Coding :", coding)
console.log ("Usia :", usia)
console.log ("Perusahaan :", perusahaan)


console.log ("\n --- Batas --- \n")




// Template Literals (Backtick)

console.log ("\n Template Literals (Backtick) \n")


var a = "Anti Null"

console.log (`Entity Minecraft ${a}`)


console.log ("\n --- Batas --- \n")




var b = "Slender Elmo"

console.log (`Entity Minecraft ${b}`)


console.log ("\n --- Batas --- \n")




var c = "Herobrine"

console.log (`Entity Minecraft ${c}`)


console.log ("\n --- Batas --- \n")




var d = "Entity 303"

console.log (`Entity Minecraft yaitu ${d}`)


console.log ("\n --- Batas --- \n")




// Membedakan Var, Let dan Const

console.log ("\n Membedakan Var, Let dan Const \n")


// Pakai var

console.log ("\n Pakai Var \n")

var string = "Halo Dunia"
var integer = 45
var float = 34.33
var kosong = null
var char = 'B'

console.log ("String =", string)
console.log ("Integer =", integer)
console.log ("Float =", float)
console.log ("Kosong =", kosong)
console.log ("Char =", char)


console.log ("\n --- Batas --- \n")




// Pake Let 

console.log ("\n Pake Let  \n")


let string_1 = "Halo Dunia"
let integer_1 = 45
let float_1 = 34.33
let kosong_1 = null
let char_1 = 'B' 


console.log ("String 1 =", string_1)
console.log ("integer 1 =", integer_1)
console.log ("Float 1 =", float_1)
console.log ("Kosong 1 =", kosong_1)
console.log ("Char 1 =", char_1)


console.log ("\n --- Batas --- \n")




// Pake Const

console.log ("\n Pake Const \n")


const string_2 = "Halo Dunia"
const integer_2 = 45
const float_2 = 34.33
const kosong_2 = null
const char_2 = 'B'


console.log ("String 2 =", string_2)
console.log ("integer 2 =", integer_2)
console.log ("Float 2 =", float_2)
console.log ("Kosong 2 =", kosong_2)
console.log ("Char 2 =", char_2)


console.log ("\n --- Batas --- \n")




// Operator dasar

console.log ("\n Operator dasar \n")


var x = 10
var y = 5

console.log ("Tambah =", x + y)
console.log ("Kurang =", x - y)
console.log ("Kali =", x * y)
console.log ("Pangkat =", x ** y)
console.log ("Bagi =", x / y)
console.log ("Modulus =", x % y)


console.log ("\n --- Batas --- \n")




// Operator perbandingan 

console.log ("\n Operator perbandingan \n")


console.log ("Hasil =", x > y)
console.log ("Hasil =", x < y)
console.log ("Hasil =", x >= y)
console.log ("Hasil =", x <= y)
console.log ("Hasil =", x == y)
console.log ("Hasil =", x != y)



console.log ("\n --- Batas --- \n")




// Operator logika

console.log ("\n Operator logika \n")


console.log ("Hasil =", (x > y) && (x < y))
console.log ("Hasil =", (x < y) || (x > y))
console.log ("Hasil =", !y)
console.log ("Hasil =", !x)


console.log ("\n --- Batas --- \n")




// Tipe data dasar

console.log ("\n Tipe data dasar \n")


var string = "Halo Dunia"
var integer = 12
var float = 34.34
var kosong = null
var char = 'A'
var array = ["Ranger", "Police", "Hardcore", "Hard Mode"]

console.log ("String =", string)
console.log ("Integer =", integer)
console.log ("Float =", float)
console.log ("Kosong =", kosong)
console.log ("Char =", char)
console.log ("Array =", array)


console.log ("\n --- Batas --- \n")




// Percabangan dasar 

console.log ("\n Percabangan dasar \n")


var a = 9

if (a > 5) {
    console.log ("Besar")
}

else {
    console.log ("")
}


console.log ("\n --- Batas --- \n")




var b = 3

if (b > 5) {
    console.log ("Besar")
}

else {
    console.log ("Kecil")
}


console.log ("\n --- Batas --- \n")




// Percabangan Lanjutan 

console.log ("\n Percabangan Lanjutan \n")


var a = 9

if (a > 5) {
    console.log ("Besar")
}

else if (a < 5) {
    console.log ("Kecil")
}

else {
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




b = 3

if (b > 5) {
    console.log ("Besar")
}

else if (b < 5) {
    console.log ("Kecil")
}

else {
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




// Percabangan Nested dengan Else If 

console.log ("\n Percabangan Nested dengan Else If \n")

var a = 9
var cek = true

if (cek) {
    if (a > 5) {
        console.log ("Besar")
    }
    
    else if (a < 5) {
        console.log ("Kecil")
    }
}

else {
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




// Percabangan Nested dengan Else 

console.log ("\n Percabangan Nested dengan Else \n")


var a = 9
var cek = true

if (cek) {
    if (a > 5) {
        console.log ("Besar")
    }
    
    else {
        console.log ("Kecil")
    }
}

else {
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




var b = 3
var cek = true

if (cek) {
    if (b > 5) {
        console.log ("Besar")
    }
    
    else {
        console.log ("Kecil")
    }
}

else {
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




// Nilai dan Grade Rapor Lanjutan

console.log ("\n Nilai dan Grade Rapor Lanjutan \n")


var nilai = 90

if (nilai >= 95) {
    console.log ("A")
}

else if (nilai >= 90) {
    console.log ("B")
}

else if (nilai >= 80) {
    console.log ("C")
}

else if (nilai >= 70) {
    console.log ("D")
}

else if (nilai >= 60) {
    console.log ("E")
}

else if (nilai >= 60) {
    console.log ("F")
}

else {
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




// Percabangan Nested Level 3 (Join jadi member JKT48)

console.log ("\n Percabangan Nested Level 3 (Join jadi member JKT48) \n")


var usia = 18
var cek = true

if (cek) {
    if ((usia >= 13) && (usia <= 18)) {
        console.log ("Boleh  dan memenuhi syarat untuk gabung ke JKT48")
    }
    
    else if (usia > 18) {
        console.log ("Sudah lebih dari cukup")
    }
    
    else {
        console.log ("Jangan gabung dulu jika dibawah 13 tahun")
    }
}

else {
    console.log ("Kembali ke rumah")
}


console.log ("\n --- Batas --- \n")




// Percabangan Nested Level 3 (Kartu SIM)

console.log ("\n Percabangan Nested Level 3 (Kartu SIM) \n")


var usia = 18
var cek = true

if (cek) {
    if ((usia >= 17) && (usia <= 45)) {
        console.log ("Masih boleh pake SIM dan boleh bawa kendaraan")
    }
    
    else if (usia > 45) {
        console.log ("Udah tua jangan ya")
    }
    
    else {
        console.log ("Jangan dulu ya yang masih dibawah 17 tahun")
    }
}

else {
    console.log ("Kembali semula")
}


console.log ("\n --- Batas --- \n")




// Percabangan Nested level 3 (Usia Produktif Manusia)

console.log ("\n Percabangan Nested level 3 (Usia Produktif Manusia) \n")


var usia = 25
var cek = true

if (cek) {
    if ((usia >= 15) && (usia <= 64)) {
        console.log ("Usia Produktif manusia dan mampu")
    }
    
    else if (usia > 64) {
        console.log ("Bukan usia Produktif, dan sudah memasuki usia lanjut")
    }
    
    else {
        console.log ("Dibawah usia produktif")
    }
}

else {
    console.log ("Masih Kecil")
}


console.log ("\n --- Batas --- \n")




// Switch Case 

console.log ("\n Switch Case  \n")


var pilihan = 2

switch (pilihan) {
    
    case 1:
        console.log ("Iya")
        break
        
    case 2:
        console.log ("Tidak")
        break
        
    case 3:
        console.log ("Kadang - kadang")
        break
        
    default:
    console.log ("Semula")
    
}


console.log ("\n --- Batas --- \n")



// Switch Case 1 

console.log ("\n Switch Case 1 \n")


var hari = 1

switch (hari) {
    
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
    console.log ("Semula")
         
}


console.log ("\n --- Batas --- \n")




// For dasar

console.log ("\n For dasar \n")


for (a = 0; a < 6; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- Batas --- \n")




for (b = 0; b < 11; b++) {
    console.log (`Urutan ke -  ${b}`)
}


console.log ("\n --- Batas --- \n")




for (c = 0; c < 16; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- Batas --- \n")




// While dasar 

console.log ("\n While dasar \n")


var a = 5

while (a < 16) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- Batas --- \n")



var b = 16 

while (b < 26) {
    console.log (`Urutan ke - ${b}`)
    b++
}


console.log ("\n --- Batas --- \n")




var c = 26

while (c < 36) {
    console.log (`Urutan ke - ${c}`)
    c++
}


console.log ("\n --- Batas --- \n")




// Do While dasar

console.log ("\n Do While dasar \n")


var a = 5

do {
    console.log (`Urutan ke- ${a}`)
    a++
} while (a < 16)


console.log ("\n --- Batas --- \n")




var b = 10

do {
    console.log (`Urutan ke - ${b}`)
    b++
} while (b < 21)


console.log ("\n --- Batas --- \n")




var c = 15

do {
    console.log (`Urutan ke - ${c}`)
    c++
} while (c < 26)


console.log ("\n --- Batas --- \n")




// For Nested 

console.log ("\n For Nested  \n")


for (a = 0; a < 6; a++) {
    for (b = 0; b < 7; b++) {
        console.log (`Urutan ke - ${a} dan Urutan ke - ${b}`)
    }
}


console.log ("\n --- Batas --- \n")




for (c = 0; c < 5; c++) {
    for (d = 0; d < 5; d++) {
        console.log (`Urutan ke - ${c} dan Urutan ke - ${d}`)
    }
}


console.log ("\n --- Batas --- \n")




for (e = 0; e < 6; e++) {
    for (f = 0; f < 6; f++) {
        console.log (`Urutan ke - ${e} dan Urutan ke - ${f}`)
    }
}


console.log ("\n --- Batas --- \n")




// Indexing Array 

console.log ("\n Indexing Array \n")


var buah = [
    
    "1. Melon",
    "2. Apel",
    "3. Nangka",
    "4. Mangga",
    "5. Buah Naga",
    "6. Buah Kurma",
    "7. Salak",
    "8. Semangka",
    
    ]
    
    
console.log (buah [0])
console.log (buah [1])
console.log (buah [2])
console.log (buah [3])
console.log (buah [4])
console.log (buah [5])


console.log ("\n --- Batas --- \n")




// Array dengan Looping

console.log ("\n Array dengan Looping \n")


var minum = [
    
    "1. Es Tebak",
    "2. Es Campur",
    "3. Es Kuwut",
    "4. Es Buah Naga",
    "5. Es Krim",
    "6. Es Semangka",
    "7. Es Melon",
    "8. Es Coklat",
    "9. Es Kopi Susu",
    "10. Es Cincau",
    
    ]
    
    
for (a = 0; a < minum.length; a++) {
    console.log (minum [a])
}


console.log ("\n --- Batas --- \n")




// Array dengan Looping (Bonus)

console.log ("\n Array dengan Looping (Bonus) \n")


var tes = [
    
    "1. Windows",
    "2. Linux",
    "3. Macintosh",
    "4. Android",
    "5. iOS",
    "6. Wear OS",
    "7. Harmony OS",
    
    ]
    
    
for (s = 0; s < tes.length; s++) {
    console.log (tes [s])
}


console.log ("\n --- Batas --- \n")




// Objek Data Profil Orang

console.log ("\n Objek Data Profil Orang \n")


var data = {
    "nama" : "James Drake",
    "kerja" : "Developer, Programmer, dan Software Engineer",
    "asal" : "Amerika Serikat",
    "etnis" : "Inggris - Amerika Serikat",
    "coding" : "HTML, CSS, JavaScript dan Python",
    "usia" : "30 tahun",
    "perusahaan" : "Google",
}


console.log ("Nama lengkap : ", data ["nama"])

console.log ("Kerja :", data ["kerja"])

console.log ("Asal :", data ["asal"])

console.log ("Etnis :", data ["etnis"])

console.log ("Coding :", data ["coding"])

console.log ("Usia :", data ["usia"])

console.log ("Perusahaan :", data ["perusahaan"])


console.log ("\n --- Batas --- \n")




// Objek data harga dan jumlah barang (Bonus)

console.log ("\n Objek data harga dan jumlah barang (Bonus) \n")


var data = {
    
    "kursi" : {
        "harga" : "Rp 20.000",
        "jumlah" : 10,
    },
    
    
    "meja" : {
        "harga" : "Rp 50.000",
        "jumlah" : 15,
    },
    
    
    "ac" : {
        "harga" : "Rp 60.000",
        "jumlah" : 3,
    },
}


console.log (
    
    "\n Harga Kursi :", data ["kursi"] ["harga"],
    
    "\n Jumlah Kursi :", data ["kursi"] ["jumlah"],
    
    "\n Harga Meja :", data ["meja"] ["harga"],
    
    "\n Jumlah Meja :", data ["meja"] ["jumlah"],
    
    "\n Harga Air Condisioner :", data ["ac"] ["harga"],
    
    "\n Jumlah Air Condisioner :", data ["ac"] ["jumlah"],
     
    )
    
    
console.log ("\n --- Batas --- \n")




// Fungsi dasar

console.log ("\n Fungsi dasar \n")


function dasar () {
    console.log ("Halo Dunia")
}

dasar ()


console.log ("\n --- Batas --- \n")




// Fungsi dasar 2

console.log ("\n Fungsi dasar 2 \n")


function det () {
    console.log ("Halo Dunia")
    console.log ("Halo Indonesia")
    console.log ("Halo Tes")
    console.log ("Halo Simpel")
    console.log ("Halo Era")
}

det ()


console.log ("\n --- Batas --- \n")




// Fungsi dasar 3

console.log ("\n Fungsi dasar 3 \n")


function far () {
    console.log ("Halo Tsar")
}

far ()
far ()
far ()
far ()


console.log ("\n --- Batas --- \n")




// Fungsi dengan Parameter

console.log ("\n Fungsi dengan Parameter \n")


function gar (nama) {
    console.log ("Halo " + nama + " MAN 2 KOTA SERANG")
}

gar ("Hayyan")
gar ("Rayyan")
gar ("Arkan")
gar ("Zaki")
gar ("Fakhri")


console.log ("\n --- Batas --- \n")




// Fungsi dengan Parameter 1

console.log ("\n Fungsi dengan Parameter 1 \n")


function sar (nama) {
    console.log ("Halo " + nama + " Kelas 12 Agama")
}

sar ("Zaki")
sar ("Fauzan")
sar ("Fikri")
sar ("Yusuf")
sar ("Fakhri")
sar ("Fatih")


console.log ("\n --- Batas --- \n")




// Fungsi dengan Parameter (Bonus)

console.log ("\n Fungsi dengan Parameter (Bonus)\n")


function jar (nama, rating) {
    console.log (`${nama}, rating = ${rating}/10`)
}

jar ("Bensin", 10)
jar ("Solar", 9)
jar ("Avtur", 8)
jar ("Api", 8)
jar ("True", 9)
jar ("False", 9)


console.log ("\n --- Batas --- \n")




// Fungsi dengan return

console.log ("\n Fungsi dengan return \n")


function tambah (a, b) {
    return a + b
}

hasil = tambah (10, 20)
console.log ("Tambah =", hasil)


console.log ("\n --- Batas --- \n")




// Fungsi dengan return 1

console.log ("\n Fungsi dengan return 1 \n")


function kurang (x, y) {
    return x - y
}

hasil = kurang (10, 5)
console.log ("Kurang =", hasil)


console.log ("\n --- Batas --- \n")




// Fungsi dengan return (Bonus)

console.log ("\n Fungsi dengan return (Bonus) \n")


function rain (nama, rating) {
    return `${nama}, rating = ${rating}/10`
}

hasil = rain ("Habib", 9)
console.log (hasil)


console.log ("\n --- Batas --- \n")




// Fungsi dengan return (Tambahan)

console.log ("\n Fungsi dengan return (Tambahan) \n")


function erk (nama) {
    return "Halo " + nama
}

hasil = erk ("Roy")
console.log (hasil)

console.log ("\n --- Batas --- \n")




// Error Handling

console.log ("\n Error Handling \n")


try {
    var hasil = 10 / 0
    console.log (hasil)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




// Error Handling 1

console.log ("\n Error Handling 1 \n")


try {
    var hasil = "Tes aja"
    console.log (hasil)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




// Error Handling 2

console.log ("\n Error Handling 2 \n")


try {
    hasil = 20 + 20 / 0
    console.log (hasil)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




// Error Handling 3

console.log ("\n Error Handling 3 \n")


try {
    hasil = 20 / 0
    console.log (hasil)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




// Arrow Fungsi Modern dasar

console.log ("\n Arrow Fungsi Modern dasar \n")


var dasar = () => {
    console.log ("Hello World")
}

dasar ()


console.log ("\n --- Batas --- \n")




// Arrow Fungsi Modern dasar 1 

console.log ("\n Arrow Fungsi Modern dasar 1 \n")


var ser = () => {
    console.log ("Hello Dan")
    console.log ("Hello Rust")
    console.log ("Hello Rinner")
}

ser ()


console.log ("\n --- Batas --- \n")




// Arrow Fungsi Modern dasar 2

console.log ("\n Arrow Fungsi Modern dasar 2 \n")

var fars = () => {
    console.log ("Hello Dun")
}

fars ()
fars ()
fars ()


console.log ("\n --- Batas --- \n")




// Arrow Fungsi dengan Parameter 

console.log ("\n Arrow Fungsi dengan Parameter  \n")


var oshi = (nama) => {
    console.log ("Hello " + nama + " JKT48")
}

oshi ("Michie")
oshi ("Fritzy")
oshi ("Christy")
oshi ("Olla")
oshi ("Fiony")
oshi ("Eli")
oshi ("Marsha")
oshi ("Freya")
oshi ("Jessi")
oshi ("Muthe")
oshi ("Mikaela")


console.log ("\n --- Batas --- \n")




// Arrow Fungsi dengan Parameter 2

console.log ("\n Arrow Fungsi dengan Parameter 2 \n")


var gar = (nama) => {
    console.log ("Hello " + nama + " MAN 2 KOTA SERANG")
}

gar ("Hayyan")
gar ("Rayyan")
gar ("Arkan")
gar ("Zaki")
gar ("Fakhri")


console.log ("\n --- Batas --- \n")




// Arrow Fungsi dengan parameter 3

console.log ("\n Arrow Fungsi dengan parameter 3 \n")


var sar = (nama) => {
    console.log ("Hello " + nama + " Kelas 12 Agama")
}

sar ("Zaki")
sar ("Fauzan")
sar ("Fikri")
sar ("Yusuf")
sar ("Fakhri")
sar ("Fatih")


console.log ("\n --- Batas --- \n")




// Arrow Fungsi dengan Return 
console.log ("\n Arrow Fungsi dengan Return \n")


var tambah = (a, b) => {
    return a + b
}

hasil = tambah (10, 10)
console.log ("Tambah =", hasil)


console.log ("\n --- Batas --- \n")




var kurang = (x, y) => {
    return x - y
}

hasil = kurang (10, 5)
console.log ("Kurang =", hasil)


console.log ("\n --- Batas --- \n")




var pangkat = (f, k) => {
    return f ** k
}

hasil = pangkat (10, 2)
console.log ("Pangkat =", hasil)


console.log ("\n --- Batas --- \n")




// Arrow Fungsi dengan Return (Bonus)

console.log ("\n Arrow Fungsi dengan Return (Bonus) \n")


var dart = (nama, rating) => {
    return "Halo " + nama + "Rating = " + rating
}

hasil = dart ("Habib ", 10)
console.log (hasil)


console.log ("\n --- Batas --- \n")