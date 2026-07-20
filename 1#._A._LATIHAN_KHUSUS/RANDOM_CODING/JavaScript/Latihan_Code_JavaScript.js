console.log ("Hello World")

console.log ("\n --- Batas --- \n")




var teks = "Halo Dunia"
console.log (teks)


var angka = 12
console.log (angka)


var desimal = 3.13
console.log (desimal)


console.log ("\n --- Batas --- \n")




console.log ("\n Tipe data pemrograman \n")

var nama = "Habib"
var angka = 12
var desimal = 3.14
var cek = true
var char = "A"
var kosong = null

var detail = `
- Nama     : ${nama}
- Angka    : ${angka}
- Desimal  : ${desimal}
- Boolean  : ${cek}
- Char     : ${char}   
- Kosong   : ${kosong}
`


console.log (detail)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan kalkulator \n")

function tambah (a, b) {
  return a + b
}


function kurang (x, y) {
  return x - y
}


function kali (k, l) {
  return k * l
}


function bagi (m, n) {
  return m / n
}


function pangkat (m, u) {
  return m ** u
}


function modulus (m, n) {
  return m % n
}

var hasil_1 = tambah(10, 5)
var hasil_2 = kurang(15, 5)
var hasil_3 = kali(10, 5)
var hasil_4 = bagi(10, 5)
var hasil_5 = pangkat(10, 5)
var hasil_6 = modulus(10, 5)


var detail = `
- Hasil tambah  : ${hasil_1}
- Hasil kurang  : ${hasil_2}
- Hasil kali    : ${hasil_3}
- Hasil bagi    : ${hasil_4}
- Hasil pangkat : ${hasil_5}
- Hasil modulus : ${hasil_6}
`


console.log (detail)


console.log ("\n --- Batas --- \n");




console.log ("\n Operator Perbandingan \n")

var x = 10
var y = 5

var detail = `
- Hasil  : ${x == y}
- Hasil  : ${x > y}
- Hasil  : ${x < y}
- Hasil  : ${x <= y}
- Hasil  : ${x >= y}
- Hasil  : ${x != y}
`

console.log (detail)


console.log ("\n --- Batas --- \n")




console.log ("\n Operator Logika \n")

detail = `
- Hasil  : ${x && y}
- Hasil  : ${x || y}
- Hasil  : ${!x}
`

console.log (detail)

console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Rumus bangun datar \n")


console.log ("\n Luas Persegi \n")

function persegi (s) {
  return s * s
}

var hasil_a = persegi(5)
console.log (hasil_a)


console.log ("\n --- Batas --- \n")




console.log ("\n Luas Persegi Panjang \n")

function persegi_panjang (p, l) {
  return p * l
}

var hasil_b = persegi_panjang(5, 10)
console.log (hasil_b)


console.log("\n --- Batas --- \n")




console.log ("\n Luas Segitiga \n")

function segitiga (a, t) {
  return a * t / 2
}

var hasil_c = segitiga (5, 10)
console.log (hasil_c)


console.log("\n --- Batas --- \n")




console.log("\n Luas Lingkaran \n")

function lingkaran (phi, r) {
  return phi * r * r
}


var hasil_d = lingkaran (3.14, 5)
console.log(hasil_d)


console.log("\n --- Batas --- \n")




console.log ("\n Luas layang-layang \n")

function layang_layang (d1, d2) {
  return (d1 * d2) / 2
}

var hasil_e = layang_layang (5, 10)
console.log(hasil_e)


console.log("\n --- Batas --- \n")




console.log("\n Luas Jajar Genjang \n")


function jajar_genjang (a, t) {
  return a * t
}


hasil_f = jajar_genjang (5, 10)
console.log (hasil_f)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Belah Ketupat \n")

function belah_ketupat (d1, d2) {
     return (d1 * d2) / 2
}

var hasil_g = belah_ketupat (5, 10)
console.log (hasil_g)


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 1 \n")

function hei (k) {

     switch (k) {
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

          case 5:
               console.log ("Angka 5")
               break

          default:
               console.log ("Angka tidak ditemukan")
               break
     }
}

hei (1)
hei (2)
hei (3)
hei (4)
hei (5)
hei (6)


console.log ("\n --- Batas --- \n")



console.log ("\n Switch Case 2 \n")

function hai (l) {

     switch (l) {
          case "A":
               console.log ("Huruf A")
               break

          case "B":
               console.log ("Huruf B")
               break

          case "C":
               console.log ("Huruf C")
               break

          case "D":
               console.log ("Huruf D")
               break

          case "E":
               console.log ("Huruf E")
               break

          default:
               console.log ("Huruf tidak ditemukan")
               break
     }
}

hai ("A")
hai ("B")
hai ("C")
hai ("D")
hai ("E")
hai ("F")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabagan Dasar \n")

function dasar (a) {
     
     if (a >= 5) {
          console.log (`Angka besar, angka a = ${a}`)
     }

     else {
          console.log (`Angka kecil, angka a = ${a}`)
     }
}

dasar (10)
dasar (8)
dasar (7)
dasar (3)
dasar (5)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan Dasar 1 \n")

function der (b) {
    
    if (b >= 5) {
        console.log (`Angka besar , angka b = ${b}`)
    }
    
    else {
        console.log (`Angka kecil, angka b = ${b}`)
    }
}

der (10)
der (9)
der (6)
der (3)
der (2)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan Lanjutan \n")

function ran (c) {

     if (c >= 8) {
          console.log (`Angka besar, c = ${c}`)
     }

     else if (c >= 5) {
          console.log (`Angka setengah, c = ${c}`)
     }

     else {
          console.log (`Angka kecil, c = ${c}`)
     }

}

ran (10)
ran (8)
ran (6)
ran (4)
ran (2)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan Lanjutan \n")

function daf (c) {

     if (c >= 8) {
          console.log (`Besar, angka c = ${c}`)
     }

     else if (c >= 5) {
          console.log (`Setengah, angka c = ${c}`)
     }

     else {
          console.log (`Kecil, angka c = ${c}`)
     }
}

daf (1)
daf (4)
daf (2)
daf (6)
daf (9)
daf (3)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan percabangan nilai rapor \n")

function rapor (r) {

     if (r >= 90) {
          console.log (`A, nilai kamu = ${r}`)
     }

     else if (r >= 80) {
          console.log (`B, nilai kamu = ${r}`)
     }

     else if (r >= 70) {
          console.log (`C, nilai kamu = ${r}`)
     }

     else if (r >= 60) {
          console.log (`D, nilai kamu = ${r}`)
     }

     else if (r >= 50) {
          console.log (`E, nilai kamu = ${r}`)
     }

     else {
          console.log (`Jelek banget, nilai kamu = ${r}`)
     }
}

rapor (100)
rapor (90)
rapor (80)
rapor (70)
rapor (60)
rapor (50)
rapor (40)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Nested 1 \n")

function dask (k) {

     if (k >= 9) {
          if (cek == true) {
               console.log (`Besar, angka k = ${k}`)
          }

          else if (k >= 5) {
               console.log (`Kecil, angka k = ${k}`)
          }
     }

     else {
          console.log (`Lebih kecil, angka k = ${k}`)
     }
}

dask (10)
dask (8)
dask (9)
dask (7)
dask (5)
dask (3)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan percabangan nested 2 \n")

function runk (l) {

     if (l >= 5) {
          if (cek == true) {
               console.log (`Besar, angka l = ${l}`)
          }

          else {
               console.log (`Kecil, angka l = ${l}`)
          }
     }

     else {
          console.log (`Lebih kecil, angka l = ${l}`)
     }
}

runk (10)
runk (9)
runk (8)
runk (5)
runk (3)
runk (2)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Nested Majemuk \n")

function hun (usia, uang) {

     if (usia >= 19 && uang >= 100000) {
          if (cek == true) {
               console.log (`Usia dan uang kamu oke, uang = ${uang} dan usia = ${usia}`)
          }

          else if (usia >= 19 || uang <= 5000) {
               console.log (`Usia kamu mencukupi tapi uang gak cukup, uang = ${uang} dan usia = ${usia}`)
          }

          else {
               console.log (`Usia dan uang kamu belum cukup, uang = ${uang} dan usia = ${usia}`)
          }
     }

     else {
          console.log (`Lain kali kamu ikut, uang = ${uang} dan usia = ${usia}`)
     }
}

hun (20, 100000)
hun (19, 50000)
hun (12, 10000)
hun (25, 500000)


console.log ("\n --- batas --- \n")




console.log ("\n For Dasar \n")

for (a = 0; a < 10; a++) {
     console.log (`urutan ke - ${a}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n For dasar 1 \n")

for (b = 1; b < 11; b++) {
     console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- batas --- \n")



console.log ("\n For dasar 2 \n")

for (c = 5; c < 16; c++) {
     console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- batas --- \n")
