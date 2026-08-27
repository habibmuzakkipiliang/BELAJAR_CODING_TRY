// Hello World

console.log ("Hello World")


console.log ("\n --- batas --- \n")



// variabel dasar

var a = "Hello World"
console.log (a)


var b = 12
console.log (b)


var c = 12.12
console.log (c)


var d = 12
console.log (d)


var e = null
console.log (e)



console.log ("\n --- batas --- \n")



// Tipe data pemrograman

var teks = "Halo Dunua"
var angka = 12
var desimal = 12.12
var cek = true
var kosong = null

var data = `
- Teks   : ${teks}
- Angka  : ${angka}
- Desimal : ${desimal}
- Cek     : ${cek}
- Kosong : ${kosong}
`

console.log (data)

console.log ("\n --- batas --- \n")




// Fungsi dengan operator dasar

function tambah (x, y) {
     return x + y
}

function kurang (x, y) {
     return x - y
}

function kali (x, y) {
     return x * y
}


function pangkat (x, y) {
     return x ** y
}


function modulus (x, y) {
     return x % y
}


console.log ("Hasil tambah =", tambah (10, 10))
console.log ("Hasil kurang =", kurang (10, 4))
console.log ("Hasil kali =", kali (10, 4))
console.log ("Hasil pangkat =", pangkat (10, 2))
console.log ("Hasil modulus =", modulus (10, 3))


console.log ("\n --- batas --- \n")



// Fungsi dengan angka terbesar

function fungsi (x, y) {
     if (x > y) {
          return x 
     }

     else {
          return y
     }
}

console.log ("Hasil besar =", fungsi (12, 8))
console.log ("Hasil besar =", fungsi (12, 2))
console.log ("Hasil besar =", fungsi (13, 3))
console.log ("Hasil besar =", fungsi (12, 2))
console.log ("Hasil besar =", fungsi (12, 1))
console.log ("Hasil besar =", fungsi (12, 2))
console.log ("Hasil besar =", fungsi (45, 1))

console.log ("\n --- batas --- \n")



// Fungsi dengan angka terkecil 

function kecil (x, y) {

     if (x < y) {
          return x
     }

     else {
          return y
     }
}

console.log ("Hasil kecil =", kecil (12, 2))
console.log ("Hasil kecil =", kecil (2, 12))
console.log ("Hasil kecil =", kecil (23, 1))
console.log ("Hasil kecil =", kecil (12, 1))
console.log ("Hasil kecil =", kecil (23, 2))
console.log ("Hasil kecil =", kecil (12, 4))


console.log ("\n --- batas --- \n")



// Percabangan dasar

var a = 10

if (a >= 5) {
     console.log (`Besar, angka a = ${a}`)
}

else {
     console.log (`Kecil, angka a = ${a}`)
}


console.log ("\n --- batas --- \n")



// Percabangan lanjutan

var b = 6

if (b >= 8) {
     console.log (`Besar, angka b = ${b}`)
}

else if (b >= 5) {
     console.log (`Tengah, angka b = ${b}`)
}

else {
     console.log (`Kecil, angka b = ${b}`)
}

console.log ("\n --- batas --- \n")



// Percabangan nested

var gun = 12
var cek = true

if (cek) {
     if (gun >= 8) {
          console.log (`Besar, angka gun = ${gun}`)
     }

     else if (gun >= 5) {
          console.log (`Kecil, angka gun = ${gun}`)
     }
}

else {
     console.log (`Kecil, angka gun = ${gun}`)
}


console.log ("\n --- batas --- \n")




// Nested kom

var uang = 5000
var cek = true

if (uang >= 10000 && uang <= 50000) {
     if (cek) {
          console.log (`Besar, uang = ${uang}`)
     }

     else if (uang > 50000) {
          console.log (`Uang mereka lebih banyak, uang = ${uang }`)
     }
}

else {
     console.log (`Kecil, uang = ${uang}`)
}


console.log ("\n --- batas --- \n")




// Usia produktif manusia

var usia = 12
var cek = true

if (usia >= 15 && usia <= 50) {
     if (cek) {
          console.log (`Usia kamu cukup sekarang = ${usia}`)
     }

     else {
          console.log (`Usia belum cukup, usia = ${usia}`)
     }
}

else {
     console.log (`usia kamu belum cukup, usia = ${usia}`)
}


console.log ("\n --- batas --- \n")



// Usia masuk kerja 

var usia = 12
var cek = true

if (usia >= 15 && usia <= 25) {
     if (cek) {
          console.log (`sudah masuk usia kamu, usia = ${usia}`)
     }

     else if (usia > 25) {
          console.log (`usia sudah lebih dari cukup, usia = ${usia}`)
     } 
}

else {
     console.log (`Sudah oke usia kamu, usia = ${usia}`)
}


console.log ("\n --- batas --- \n")




// For dasar

for (a = 0; a < 12; a++) {
     console.log (`Urutan ke- ${a}`)
}

console.log ("\n --- batas --- \n")



// For dasar 1

for (b = 1; b < 10; b++) {
     console.log (`urutan ke - ${b}`)
}


console.log ("\n --- batas --- \n")




// For dasar 

for (h = 0; h < 12; h++) {
     console.log (`Urutan ke - ${h}`)
}

console.log ("\n --- batas --- \n")



// for dasar ++

for (g = 5; g < 10; g++) {
     console.log (`urutan ke - ${g}`)
}

console.log ("\n --- batas --- \n")



// While dasar

var f = 1

while (f < 12) {
     console.log (`urutan ke - ${f}`)
     f++
}

console.log ("\n --- batas --- \n")



w = 10

while (w > 0) {
     console.log (`urutan ke - ${w}`)
     w--
}



k = 15

while (k > 0) {
     console.log (`urutan ke - ${k}`)
     k--
}


console.log ("\n --- batas --- \n")


// For dasar 2

var t = 1

do {
     console.log (`Urutan ke - ${t}`)
     t++
}

while (t < 10)


console.log ("\n --- batas --- \n")




// Fungsi dengan parameter 2 item

function fun (nama, asal, nomor) {
     console.log (`Halo nama saya ${nama}, dari ${asal} dan bernomor ${nomor}`)
}

fun ("Rayyn", "Paris", 12)
fun ("Gun", "Yun", 12)
fun ("Jun", "Jakarta Timur", 23)
fun ("Gun", "Jakarta TImur", 12)
fun ("Fun", "Bandung", 12)
fun ("Run", "Jakarta Barat", 34)
fun ("Kop", "Jakarta Selatan", 90)