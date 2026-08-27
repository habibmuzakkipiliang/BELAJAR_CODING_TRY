// Hello World

console.log ("Hello World")


console.log ("\n --- batas --- \n")




// Variabel dasar

var contoh = "Hello World dong"
console.log (contoh)


var contoh_1 = 12
console.log (contoh_1)


var contoh_3 = 12.12
console.log (contoh_3)


console.log ("\n --- batas --- \n")



// Tipe data pemrograman

var teks = "Hello World dong guys"
var angka = 12
var desimal = 1.12
var cek = true
var kosong = null

var tipe = `
- Teks     : ${teks}
- Angka    : ${angka}
- Desimal  : ${desimal}
- Cek      : ${cek}
- Kosong   : ${kosong}
`

console.log (tipe)


console.log ("\n --- batas --- \n")



// Cek jenis tipe data pemrograman

var tipek = `
- Teks     : ${typeof (teks)}
- Angka    : ${typeof (angka)}
- Desimal  : ${typeof (desimal)}
- Cek      : ${typeof (cek)}
- Kosong   : ${typeof (kosong)}
`

console.log (tipek)

console.log ("\n --- batas --- \n")



// Fungsi dengan kalkulator dasar

function tambah (x, y) {
     return x + y
}


function kurang (x, y) {
     return x - y
}


function kali (x, y) {
     return x * y
}


function bagi (x, y) {
     return x / y
}


function modulus (x, y) {
     return x % y
}


console.log ("Hasil tambah =", tambah (10, 5))
console.log ("Hasil kurang =", kurang (10, 5))
console.log ("Hasil kali =", kali (10, 10))
console.log ("Hasil bagi =", bagi (10, 2))
console.log ("Hasil modulus =", modulus (10, 9))


console.log ("\n --- batas --- \n")




// Operator bandingkan

function banding_1 (x, y) {
     return x > y
}


function banding_2 (x, y) {
     return x < y
}


function banding_3 (x, y) {
     return x == y
}


function banding_4 (x, y) {
     return x != y
}


console.log ("Hasil banding =", banding_1 (10, 4))
console.log ("Hasil banding =", banding_2 (30, 34))
console.log ("Hasil banding =", banding_3 (45, 24))
console.log ("Hasil banding =", banding_4 (45, 23))


console.log ("\n --- batas --- \n")




// fungsi dengan percabangan dasar

function tes (f) {

     if (f >= 5) {
          console.log (`Angka f besar, angka f = ${f}`)
     }

     else {
          console.log (`Angka f kecil, angka f = ${f}`)
     }
}

tes (1)
tes (2)
tes (3)
tes (4)
tes (5)
tes (6)
tes (7)
tes (8)
tes (9)
tes (10)


console.log ("\n --- batas --- \n")




// Fungsi dengan percabangan dasar 2

function der (s) {

     if (s > 0) {
          console.log (`angka positif, angka s = ${s}`)
     }

     else {
          console.log (`angka negatif, angka s = ${s}`)
     }
}

der (10)
der (9)
der (8)
der (7)
der (6)
der (5)
der (4)
der (3)
der (2)
der (1)


console.log ("\n --- batas --- \n")




// For dasar

for (a = 0; a < 11; a++) {
     console.log (`urutan ke - ${a}`)
}

console.log ("\n --- batas --- \n")




// For dasar 2

for (k = 0; k < 15; k++) {
     console.log (`urutan ke - ${k}`)
}


console.log ("\n --- batas --- \n")




// For dasar

for (u = 0; u < 11; u++) {
     console.log (`urutan ke - ${u}`)
}


console.log ("\n --- batas --- \n")



// While dasar 1

var a = 1

while (a < 11) {
     console.log (`urutan ke - ${a}`)
     a++
}


console.log ("\n --- batas --- \n")




// While dasar 2

var b = 11

while (b > 0) {
     console.log (`urutan ke - ${b}`)
     b--
}


console.log ("\n --- batas --- \n")




// Do While

var h = 1

do {
     console.log (`urutan ke - ${h}`)
     h++
}

while (h < 11)


console.log ("\n --- batas --- \n")