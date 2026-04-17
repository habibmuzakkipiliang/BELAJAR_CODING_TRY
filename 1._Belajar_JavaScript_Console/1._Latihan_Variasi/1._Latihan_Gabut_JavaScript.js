// Bikin Hello World

console.log ("\n Bikin Hello World \n")


console.log ("Hello World")


console.log ("\n --- Batas --- \n")




// Profil Habib Muzakki (Variabel)

console.log ("\n Profil Habib Muzakki (Variabel) \n")


var nama = "Habib Muzakki"
var marga = "Piliang"
var kelas = "12 Agama"
var sekolah = "MAN 2 KOTA SERANG"
var angkatan = "34 ASCENDRIA"
var absen = 15
var coding = "HTML, CSS, Bootstrap, JavaScript dan Python"
var lomba = "OSN-S dan OSN-K Informatika"
var tinggi = "170 cm"
var berat = "60 kg"
var fans = "JKT48, AKB48 dan Rain Tree"
var oshi = "Michie, Fritzy, Olla, Christy, Marsha, Freya, Jessi, Muthe, Eli, Fiony, Mikaela, Yui Oguri (AKB48) dan Endo Rino (Rain Tree)"


console.log ("Nama lengkap :", nama)
console.log ("Marga :", marga)
console.log ("Kelas :", kelas)
console.log ("Sekolah :", sekolah)
console.log ("Angkatan :", angkatan)
console.log ("Absen :", absen)
console.log ("Coding :", coding)
console.log ("Lomba :", lomba)
console.log ("Tinggi badan :", tinggi)
console.log ("Berat badan :", berat)
console.log ("Fans :", fans)
console.log ("Oshi :", oshi)


console.log ("\n --- Batas --- \n")




// Objek Data Profil Habib Muzakki (Objek)

console.log ("\n Objek Data Profil Habib Muzakki (Objek) \n")


var data = {
    "nama" : "Habib Muzakki",
    "marga" : "Piliang",
    "kelas" : "12 Agama",
    "sekolah" : "MAN 2 KOTA SERANG",
    "angkatan" : "34 ASCENDRIA",
    "absen" : 15,
    "coding" : "HTML, CSS, Bootstrap, JavaScript dan Python",
    "lomba" : "OSN-S dan OSN-K Informatika",
    "tinggi" : "170 cm",
    "berat" : "60 kg",
    "fans" : "JKT48, AKB48 dan Rain Tree",
    "oshi" : "Michie, Fritzy, Olla, Christy, Marsha, Freya, Jessi, Muthe, Eli, Fiony, Mikaela, Yui Oguri (AKB48) dan Endo Rino (Rain Tree)",
}


console.log ("Nama lengkap :", data ["nama"])

console.log ("Marga :", data ["marga"])

console.log ("Kelas :", data ["kelas"])

console.log ("Sekolah :", data ["sekolah"])

console.log ("Angkatan :", data ["angkatan"])

console.log ("Absen :", data ["absen"])

console.log ("Coding :", data ["coding"])

console.log ("Lomba :", data ["lomba"])

console.log ("Tinggi badan :", data ["tinggi"])

console.log ("Berat badan :", data ["berat"])

console.log ("Fans :", data ["fans"])

console.log ("Oshi :", data ["oshi"])


console.log ("\n --- Batas --- \n")




// Tipe data dasar  

console.log ("\n Tipe data dasar \n")


var teks = "Hai Anak JKT48 yang cantik dan semangat"
var angka = 90
var desimal = 45.34
var cek_1 = true
var cek_2 = false
var char = 'A'
var kosong = null
var array = ["Michie JKT48", "Fritzy JKT48", "Olla JKT48", "Christy JKT48", "Marsha JKT48", "Freya JKT48", "Jessi JKT48", "Muthe JKT48", "Eli JKT48", "Fiony JKT48", "Mikaela JKT48", "Yui Oguri (AKB48)", "Endo Rino (Rain Tree)"]


console.log ("Teks :", teks)
console.log ("Angka :", angka)
console.log ("Desimal :", desimal)
console.log ("Cek 1 :", cek_1)
console.log ("Cek 2 :", cek_2)
console.log ("Char :", char)
console.log ("Kosong :", kosong)
console.log ("Array :", array)


console.log ("\n --- Batas --- \n")


console.log ("\n Oshi Idol Favorit saya : \n")


for (k = 0; k < array.length; k++) {
    console.log (array [k])
}


console.log ("\n --- Batas --- \n")




// Operator Dasar 

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




// Operator Perbandingan 

console.log ("\n Operator Perbandingan \n")


console.log ("Hasil =", x === y)
console.log ("Hasil =", x != y)
console.log ("Hasil =", x <= y)
console.log ("Hasil =", x >= y)
console.log ("Hasil =", x > y)
console.log ("Hasil =", x < y)


console.log ("\n --- Batas --- \n")




// Operator Logika 

console.log ("\n Operator Logika \n")


console.log ("Hasil =", (x > y) && (x > y))
console.log ("Hasil =", (x < y) || (x < y))
console.log ("Hasil =", (!x))
console.log ("Hasil =", (!y))


console.log ("\n --- Batas --- \n")




// Indexing Array (Tingkatan Kasta Di Zaman Belanda VOC) 

console.log ("\n Indexing Array (Tingkatan Kasta Di Zaman Belanda VOC) \n")


var data = [
    
    "1. Eropa (Belanda)",
    "2. Tionghoa",
    "3. India",
    "4. Arab",
    "5. Pribumi",
    
    ]
    
    
console.log (data [0])
console.log (data [1])
console.log (data [2])
console.log (data [3])
console.log (data [4])


console.log ("\n --- Batas --- \n")




// Array dengan Looping For

console.log ("\n Array dengan Looping For \n")


var data = [
    
    "1. Teknik Informatika",
    "2. Sistem Informasi",
    "3. Teknologi Informasi",
    "4. Teknik Komputer",
    "5. Ilmu Komputer",
    "6. Data Science",
    "7. Data Analyst",
    "8. AI dan Machine Learning",
    
    ]
    
    
for (b = 0; b < data.length; b++) {
    console.log (`Jurusan Kuliah IT : ${data [b]}`)
}


console.log ("\n --- Batas --- \n")




// Switch Case 

console.log ("\n Switch Case  \n")


var hari = 3

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
        
    default:
    console.log (" Hari Libur")
}


console.log ("\n --- Batas --- \n")




// Rapor Sekolah SMA

console.log ("\n Rapor Sekolah SMA \n")


var nilai = 95

if (nilai >= 100) {
    console.log ("A+")
}

else if (nilai >= 95) {
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

else if (nilai >= 50) {
    console.log ("F")
}

else {
    console.log ("Jelek Amat")
}


console.log ("\n --- Batas --- \n")




// Percabangan Nested Level 3 (Usia untuk Produktif Manusia)

console.log ("\n Percabangan Nested Level 3 (Usia untuk Produktif Manusia) \n")


var usia = 30
var cek = true

if (cek) {
    if ((usia >= 15) && (usia <= 64)) {
        console.log (`Usia yang masih produktif tinggi sebagai manusia, dan berusia = ${usia} tahun`)
    }
    
    else if (usia > 64) {
        console.log (`Usia yang sudah lanjut atau tua dan berusia = ${usia} tahun`)
    }
    
    else {
        console.log (`Belum mencapai usia produktif manusia  dan berusia = ${usia} tahun`)
    }
}

else {
    console.log (`Sekarang masih kecil banget dan berusia = ${usia} tahun`)
}


console.log ("\n --- Batas --- \n")




// Percabangan Nested level 3 (Join member JKT48)

console.log ("\n Percabangan Nested level 3 (Join member JKT48) \n")


var usia = 19
var cek = true

if (cek) {
    if ((usia >= 13) && (usia <= 18)) {
        console.log (`Boleh daftar dan ikut audisi JKT48 dan berusia = ${usia} tahun`)
    }
    
    else if (usia > 18) {
        console.log (`Sudah dewasa untuk daftar dan ikut audisi JKT48 dan berusia = ${usia} tahun`)
    }
    
    else {
        console.log (`Masib dibawah umur dan belum saatnya daftar JKT48 dan berusia = ${usia} tahun`)
    }
}

else {
    console.log (`Mending di rumah aja deh dan berusia = ${usia} tahun`)
}


console.log ("\n --- Batas --- \n")




// For Nested 

console.log ("\n For Nested \n")


for (x = 0; x < 11; x++) {
    for (y = 0; y < 11; y++) {
        console.log (`Urutan x ke - ${x} dan Urutan y ke - ${y}`)
    }
}


console.log ("\n --- Batas --- \n")




for (a = 0; a < 11; a++) {
    for (b = 0; b < 11; b++) {
        console.log (`Urutan a ke - ${a} dan Urutan b ke - ${b}`)
    }
}


console.log ("\n --- Batas --- \n")




// Fungsi Dasar

console.log ("\n Fungsi Dasar \n")


function dasar () {
    console.log ("Hello Dear")
}

dasar ()


console.log ("\n --- Batas --- \n")




// Fungsi dasar 1

console.log ("\n Fungsi dasar 1 \n ")


function det () {
    console.log ("Hello World")
    console.log ("Hello Sert")
    console.log ("Hello Scot")
    console.log ("Hello Dert")
    console.log ("Hello Sart")
}

det ()


console.log ("\n --- Batas --- \n")




// Fungsi dasar 3

console.log ("\n Fungsi dasar 3 \n")


function gun () {
    console.log ("Hello Coding")
}

gun ()
gun ()
gun ()
gun ()


console.log ("\n --- Batas --- \n")




// Fungsi dengan parameter 

console.log ("\n Fungsi dengan parameter \n")


function dai (nama) {
    console.log ("Halo " + nama + " dari MAN 2 KOTA SERANG")
}

dai ("Habib")
dai ("Dankut")
dai ("Johan")
dai ("Faster")


console.log ("\n --- Batas --- \n")




// Fungsi dengan parameter 2 (Template Literals)

console.log ("\n Fungsi dengan parameter 2 (Template Literals) \n")


function der (nama) {
    console.log (`Halo ${nama} dari Kota Jakarta Pusat`)
}

der ("Fildza")
der ("Hayyan")
der ("Sam")
der ("Roy")
der ("Rafel")


console.log ("\n --- Batas --- \n")




// Fungsi dengan return

console.log ("\n Fungsi dengan return \n")


function tambah (x, y) {
    return x + y
}

hasil = tambah (10, 5)
console.log ("Tambah =", hasil)


console.log ("\n --- Batas --- \n")




// Fungsi dengan return 1

console.log ("\n Fungsi dengan return 1 \n")


function far (nama) {
    return "Halo " + nama + " Dari Provinsi Sumbar"
}

hasil = far ("Habib")
console.log (hasil)


console.log ("\n --- Batas --- \n")




// Fungsi dengan return 2 (Template Literals) 

console.log ("\n Fungsi dengan return 2 (Template Literals) \n")


function dar (nama) {
    return `Halo ${nama} dari Depok`
}

hasil = dar ("Habib")
console.log (hasil)


console.log ("\n --- Batas --- \n")




// Arrow Fungsi dasar 

console.log ("\n Arrow Fungsi dasar \n")


var dasar = () => {
    console.log ("Hello World")
}

dasar ()


console.log ("\n --- Batas --- \n")




// Arrow Fungsi 1 

console.log ("\n Arrow Fungsi 1 \n")


var dat = () => {
    console.log ("Hello World")
    console.log ("Hello Jun")
    console.log ("Hello Stanley")
    console.log ("Hello Tsar")
    console.log ("Runner Do Go")
}

dat ()


console.log ("\n --- Batas --- \n")




// Arrow Fungsi 2

console.log ("\n Arrow Fungsi 2 \n")


var det = () => {
    console.log ("Hello Coding")
}

det ()
det ()
det ()
det ()


console.log ("\n --- Batas --- \n")




// Arrow Fungsi dengan Parameter 1 

console.log ("\n Arrow Fungsi dengan Parameter \n")


var oshi = (nama) => {
    console.log ("Hello " + nama + " Dari JKT48")
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




// Arrow Fungsi dengan parameter 1

console.log ("\n Arrow Fungsi dengan parameter 1 \n")

 
var ser = (nama) => {
    console.log ("Hello " + nama + " Dari Banten")
}

ser ("Hayyan")
ser ("Rayyan")
ser ("Node")
ser ("Don")
ser ("Josh")


console.log ("\n --- Batas --- \n")




// Arrow Fungsi dengan parameter (Template Literals)

console.log ("\n Arrow Fungsi dengan parameter (Template Literals) \n")


var sert = (nama) => {
    console.log (`Halo ${nama} dari Jakarta Barat`)
}

sert ("John Kusjanto")
sert ("Hart Tjahja Wen")
sert ("Johan Tjohja Aeron")
sert ("Notch Hansel Aeron")
sert ("Lie Tian Wei")


console.log ("\n --- Batas --- \n")




// Arrow Fungsi dengan return

console.log ("\n Arrow Fungsi dengan return \n")


var tambah = (x, y) => {
    return x + y
}

hasil = tambah (10, 5)
console.log ("Tambah =", hasil)


console.log ("\n --- Batas --- \n")




// Arrow Fungsi dengan return 1 

console.log ("\n Arrow Fungsi dengan return 1  \n")


var mark = (nama) => {
    return "Halo " + nama + " Dari Kota Bukittinggi"
}

hasil = mark ("Don")
console.log (hasil)


console.log ("\n --- Batas --- \n")




// Arrow Fungsi dengan Return 2 (Template Literals)

console.log ("\n Arrow Fungsi dengan Return 2 (Template Literals) \n")


var en = (nama) => {
    return `Halo ${nama} dari Kota Lampung`
}

hasil = en ("Roy")
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
    var hasil = "Tes Dong"
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




// Error Handling 3

console.log ("\n Error Handling 3 \n")


try {
    var hasil = "Tes Aja"
    console.log (hasil)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}