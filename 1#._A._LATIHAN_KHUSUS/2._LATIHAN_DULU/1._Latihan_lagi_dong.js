// Bikin latihan simpel dong

console.log ("Hello World")


console.log ("\n --- batas --- \n")



// Variabel dasar 

var a = "Habib Muzakki"
console.log (a)

var b = 12
console.log (b)


var c = 3.13
console.log (c)

console.log ("\n --- batas --- \n")




// Tipe data pemrograman 

var teks = "Halo dunia"
var angka = 12
var desimal = 1.12
var cek = true
var kosong = null

var tipe = `
- Teks   : ${teks}
- Angka  : ${angka}
- Desimal : ${desimal}
- Cek     : ${cek}
- Kosong  : ${kosong}
`

console.log (tipe)


console.log ("\n --- batas --- \n")




// Switch Case

function er (a) {

     switch (a) {

          case 1:
               console.log ("Angka 1")
               break

          case 2:
               console.log ("Angka 2")
               break

          case 3:
               console.log ("Angka 3")
               break

          case 4:
               console.log ("Angka 4")
               break

          default:
               console.log ("Angka lain")
     }
}

er (1)
er (2)
er (3)
er (4)
er (5)


console.log ("\n --- batas --- \n")





// Switch Case 2 

function fer (e) {

     switch (e) {

          case "Merah":
               console.log( "Warna merah" )
               break

          case "Kuning":
               console.log( "Warna kuning" )
               break

          case "Hijau":
               console.log( "Warna hijau" )
               break

          default:
               console.log( "Warna lain" )
     }
}

fer ("Merah")
fer ("Kuning")
fer ("Hijau")
fer ("Hitam")

console.log ("\n --- batas --- \n")



// Fungsi dengan percabangan dasar 

function dasar ( a ) {

     if (a >= 5) {
          console.log(`Besar, angka a = ${a}`)
     }

     else {
          console.log(`Kecil, angka a = ${a}`)
     }
}

dasar (10)
dasar (9)
dasar (8)
dasar (7)
dasar (6)
dasar (5)
dasar (4)
dasar (3)


console.log ("\n --- batas --- \n")



// Fungsi dengan Percabangan lanjutan 

function ru ( b ) {

     if (b >= 8) {
          console.log (`Besar, angka b = ${ b }`)
     }

     else if ( b >= 5 ) {
          console.log (`Tengah, angka b = ${ b }`)
     }

     else {
          console.log (`Kecil, angka b = ${ b }`)
     }
}

ru (10)
ru (9)
ru (8)
ru (7)
ru (6)
ru (5)
ru (4)
ru (3)
ru (2)
ru (1)


console.log ( "\n --- batas --- \n" )




// Fungsi dengan percabangan nested 

function der (c) {

     cek = true

     if (c >= 5) {
          if (cek) {
               console.log (`Besar, angka c = ${ c }`)
          }
     }

     else {
          console.log (`Kecil, angka c = ${ c }`)
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




// Fungsi dengan percabangan nilai rapor

function nilai (r) {

     if (r >= 95) {
          console.log (`A, nilai = ${ r }`)
     }

     else if (r >= 90) {
          console.log (`B, nilai = ${ r }`)
     }

     else if (r >= 80) {
          console.log (`C, nilai = ${ r }`)
     }

     else if (r >= 70) {
          console.log (`D, nilai = ${ r }`)
     }

     else if (r >= 60) {
          console.log (`E, nilai = ${ r }`)
     }

     else if (r >= 50) {
          console.log (`F, nilai = ${ r }`)
     }

     else {
          console.log (`Jelek amat, nilai = ${ r }`)
     }
}

nilai (100)
nilai (90)
nilai (80)
nilai (70)
nilai (60)
nilai (50)
nilai (40)
nilai (30)
nilai (20)
nilai (10)


console.log( "\n --- batas --- \n" )



// Usia Produktif manusia 

function usia (l) {

     if (l >= 15 && l <= 40) {
          console.log (`Usia yang sudah produktif, usia = ${ l }`)
     }

     else if (l > 40) {
          console.log (`Sudah tua usiannya, usia = ${ l }`)
     }

     else {
          console.log (`Masih kecil usiannya, usia = ${ l }`)
     }
}

usia (60)
usia (50)
usia (40)
usia (30)
usia (20)
usia (10)
usia (5)


console.log( "\n --- batas --- \n" )




// Usia masuk JKT48 

function oshi (f) {

     if (f >= 13 && f <= 19) {
          console.log (`Usia yang sudah boleh daftar, usia = ${ f }`)
     }

     else if (f > 19) {
          console.log (`Sudah lebih dari cukup, usia = ${ f }`)
     }

     else {
          console.log (`Masih kecil usiannya, usia = ${ f }`)
     }
}

oshi (20)
oshi (19)
oshi (18)
oshi (17)
oshi (16)
oshi (15)
oshi (14)
oshi (13)
oshi (12)
oshi (11)


console.log ("\n --- batas --- \n")




// Usia masuk kerja manusia 

function kerja ( w ) {

     if (w >= 23 && w <= 40 ) {
          console.log (`Boleh kerja, usia = ${ w }`)
     }

     else if (w > 40) {
          console.log (`Sudah pensiun, usia = ${ w }` )
     }

     else {
          console.log (`Masih kecil usiannya, usia = ${ w }`)
     }
}

kerja (60)
kerja (50)
kerja (40)
kerja (30)
kerja (20)
kerja (10)
kerja (5)


console.log ("\n --- batas --- \n")




// For dasar 

for (a = 0; a < 11; a++) {
     console.log (`Urutan ke - ${a}`)
}

console.log ("\n --- batas --- \n")



// For dasar 2

for (b = 1; b < 11; b++) {
     console.log (`Urutan ke - ${ b }`)
}


console.log ("\n --- batas --- \n")



// While dasar 1 

var a = 1

while (a < 11) {
     console.log (`Urutan ke - ${a}`)
     a++
}

console.log ("\n --- batas --- \n")



// While dasar 2

b = 10

while (b > 0) {
     console.log (`Urutan ke - ${b}`)
     b--
}

console.log ("\n --- batas --- \n")



// Do While dasar 

var a = 1

do {
     console.log (`Urutan ke - ${ a }`)
     a++
}

while (a < 11)


console.log ("\n --- batas --- \n")




// Struktur data 1

var daf = [
     "Rusia",
     "Ukraina",
     "Turki",
     "Afrika",
     "Arab",
]

for (a = 0; a < daf.length; a++) {
     console.log (daf[a])
}


console.log ("\n --- batas --- \n")




// Struktur data 2 

var film = [
     "Simon",
     "Verta",
     "Blanca",
     "Baoqing Fox",
     "Ox Head",
]

for (b = 0; b < film.length; b++) {
     console.log (film[b])
}


console.log ("\n --- batas --- \n")




// For break

for (a = 0; a < 11; a++) {
     if (a == 7) {
          break
     }

     console.log (a)
}


console.log ("\n --- batas ---  \n")




// For continue

for (b = 0; b < 11; b++) {
     if (b == 5) {
          continue
     }

     console.log (b)
}


console.log ("\n --- batas --- \n")




// Array For Continue

var der = ["Halo Dunia", "Halo World", "Feastable", "Vin"]

for (var c of der) {
     if (c == "Halo World") {
          continue
     }

     console.log (c)
}


console.log ("\n --- batas --- \n")




// Array For Break

var fr = ["Ron", "Bet", "Ban", "Ver"]

for (var d of fr) {
     if (d == "Ban") {
          break
     }

     console.log (d)
}

console.log ("\n --- batas --- \n")




// Dictionary

var data = {
     "nama": "Habib Muzakki",
     "asal": "Kota Serang",
     "usia": 19,
     "cek": true,
}

console.log ("Nama :", data[ "nama" ])
console.log ("Asal :", data[ "asal" ])
console.log ("Usia :", data[ "usia" ])
console.log ("Cek :", data[ "cek" ])


console.log ("\n --- batas --- \n")




// Error Handling 

try {
     var h = 10 / a
     console.log (a)
}

catch (Error) {
     console.log("Gagal")
}

finally {
     console.log("Selesai")
}


console.log ("\n --- batas --- \n")




// Error Handling 

try {
     var t = 10 + 10
     console.log (t)
}

catch (Error) {
     console.log ("Gagal")
}

finally {
     console.log ("Selesai")
}


console.log ("\n --- batas --- \n")





// Error Handling + Percabangan dasar

function ver ( k ) {

     try {

          if (k < 0) {
               throw ("Gagal")
          }

          if (k >= 5) {
               console.log (`Besar, angka k = ${ k }`)
          }

          else {
               console.log (`Kecil, angka k = ${ k }`)
          }
     }

     catch ( Error ) {
          console.log (`Angka minus, angka = ${ k }`)
     }
}

ver (-10)
ver (-9)
ver (-5)
ver (-11)
ver (10)
ver (8)
ver (7)
ver (5)
ver (3)
ver (2)


console.log( "\n --- batas --- \n" )




// Error Handling + Percabangan Lanjutan

function fer ( e ) {

     try {

          if (e < 0) {
               throw ("Gagal")
          }

          if (e >= 8) {
               console.log (`Besar, angka e = ${e}`)
          }

          else if (e >= 5) {
               console.log (`Tengah, angka e = ${e}`)
          }

          else {
               console.log (`Kecil, angka e = ${e}`)
          }
     }

     catch (Error) {
          console.log (`Angka minus, angka e = ${ e }`)
     }
}

fer (-10)
fer (-15)
fer (-4)
fer (-6)
fer (-12)
fer (10)
fer (8)
fer (7)
fer (6)
fer (5)
fer (4)
fer (3)
fer (2)
fer (1)


console.log ("\n --- batas --- \n")



// Arrow fungsi 

var data = () => {
     console.log ("Hello World")
}

data ()


console.log ("\n --- batas --- \n")




// Arrow Fungsi 2 

var der = (nama) => {
     console.log (`Halo nama saya ${nama} dari Jakarta Utara`)
}

der ("Habib")
der ("fattan")
der ("Yunan")