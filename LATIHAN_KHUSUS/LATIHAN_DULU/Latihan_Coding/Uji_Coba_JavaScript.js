console.log ("\n Bikin Hello World \n")

console.log ("Hello World")


console.log ("\n --- batas --- \n")




console.log ("\n Sintaks, Variabel dan Komen \n")

// Ini Komen

// Ini komen


var teks_1 = "Hello Ben"
console.log (teks_1)


var angka_1 = 12
console.log (angka_1)


console.log ("\n --- batas --- \n")




console.log ("\n Tipe data pemrograman \n")

var teks = "Halo Dunia"
var angka = 12
var desimal = 12.12
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




console.log ("\n Profil Habib Muzakki \n")

var nama = "Habib Muzakki"
var akrab = "Habib"
var asal = "Kota Serang"
var alumni = "MAN 2 KOTA SERANG (Kelas Agama)"
var coding = "HTML, CSS, JavaScript dan Python"
var jurusan = "D4 Vokasi Teknik Informatika"
var kuliah = "Harkat Negeri Tegal"

var profil = `
- Nama lengkap   : ${nama}
- Nama panggilan : ${akrab}
- Asal daerah    : ${asal}
- Alumni sekolah : ${alumni}
- Coding         : ${coding}
- Jurusan        : ${jurusan}
- Kuliah         : ${kuliah}
`

console.log (profil)


console.log ("\n --- batas --- \n")




console.log ("\n Operator Dasar \n")

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


function bagi (x, y) {
     return x / y
}


var hasil_1 = tambah (10, 10)
var hasil_2 = kurang (10, 5)
var hasil_3 = kali (10, 10)
var hasil_4 = pangkat (10, 3)
var hasil_5 = bagi (10, 5)


var hitung = `
- Tambah = ${hasil_1}
- Kurang = ${hasil_2}
- Kali   = ${hasil_3}
- Pangkat = ${hasil_4}
- Bagi    = ${hasil_5}
`

console.log (hitung)


console.log ("\n --- batas --- \n")




console.log ("\n Switch Case dengan Int \n")

function hun (f) {

     switch (f) {
          
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

hun (1)
hun (2)
hun (3)
hun (4)
hun (5)


console.log ("\n --- batas --- \n")
 



console.log ("\n Fungsi dengan Switch Case dengan Int \n")

function gun (k) {

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

          default:
               console.log ("Angka lain")
     }
}

gun (1)
gun (2)
gun (3)
gun (4)
gun (5)


console.log ("\n --- batas --- \n")



console.log ("\n Fungsi dengan Switch Case dengan String \n")

function fer (j) {

     switch (j) {

          case "Merah":
               console.log ("Warna merah")
               break

          case "Kuning":
               console.log ("Warna kuning")
               break

          case "Hijau":
               console.log ("Warna hijau")
               break

          default:
               console.log ("Warna lain")
     }
}


fer ("Merah")
fer ("Kuning")
fer ("Hijau")
fer ("Warna lain")


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Dasar \n")

function der (j) {

     if (j >= 5) {
          console.log (`Besar, angka j = ${j}`)
     }

     else {
          console.log (`Kecil, angka j = ${j}`)
     }
}

der (10)
der (9)
der (8)
der (7)
der (6)
der (5)
der (6)
der (5)
der (4)
der (3)
der (2)
der (1)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Lanjutan \n")

function wer (n) {

     if (n >= 8) {
          console.log (`Besar, angka n = ${n}`)
     }

     else if (n >= 5) {
          console.log (`Tengah, angka n = ${n}`)
     }

     else {
          console.log (`Kecil, angka n = ${n}`)
     }
}


wer (10)
wer (9)
wer (8)
wer (7)
wer (6)
wer (5)
wer (4)
wer (3)
wer (2)
wer (1)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Nilai rapor \n")

function nilai (v) {

     if (v >= 90) {
          console.log (`A, nilai = ${v}`)
     }

     else if (v >= 80) {
          console.log (`B, nilai = ${v}`)
     }

     else if (v >= 70) {
          console.log (`C, nilai = ${v}`)
     }

     else if (v >= 60) {
          console.log (`D, nilai = ${v}`)
     }
     
     else if (v >= 50) {
          console.log (`E, nilai = ${v}`)
     }

     else {
          console.log (`Jelek amat, nilai = ${v}`)
     }
}

nilai (100)
nilai (90)
nilai (80)
nilai (70)
nilai (60)
nilai (50)
nilai (40)


console.log ("\n --- batas --- \n")



console.log ("\n Fungsi dengan Percabangan nested 1 \n")

function fn (k) {

     if (k >= 8) {
          if (cek == true) {
               console.log (`Besar, angka k = ${k}`)
          }
     }

     else if (k >= 5) {
          console.log (`Kecil, angka k = ${k}`)
     }
}

fn (10)
fn (9)
fn (8)
fn (7)
fn (6)
fn (5)
fn (4)
fn (3)
fn (2)
fn (1)


console.log ("\n --- batas --- \n")


console.log ("\n Fungsi dengan Percabangan nested simbol \n")

function ger (j) {

     if (j >= 3 && j >= 2) {
          if (cek == true) {
               console.log (`Besar, angka j = ${j}`)
          }
     }

     else if (j >= 5 || j >= 2) {
          console.log (`Kecil, angka j = ${j}`)
     }
}

ger (10)
ger (9)
ger (8)
ger (7)
ger (6)
ger (5)
ger (4)
ger (3)
ger (2)
ger (1)


console.log ("\n --- batas --- \n")




console.log ("\n Error Handling \n")

try {
     var a = 10 / b
     console.log (a)
}

catch (Error) {
     console.log ("Gagal")
}

finally {
     console.log ("Berhasil")
}