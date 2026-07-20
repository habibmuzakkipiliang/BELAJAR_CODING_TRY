console.log ("\n Bikin Program Sederhana JS \n")

console.log ("Hello World")


console.log ("\n --- batas --- \n")



console.log ("\n Tipe data pemrograman \n")

var teks = "Halo dunia"
var angka = 12
var desimal = 12.1
var cek = true
var kosong = null

var detail = `
- Teks : ${teks}
- Angka : ${angka}
- Desimal : ${desimal}
- Cek     : ${cek}
- Kosong  : ${kosong}
`

console.log (detail)


console.log ("\n --- batas --- \n")




console.log ("\n Profil Habib Muzakki \n")

var nama = "Habib Muzakki"
var akrab = "Habib"
var asal = "Kota Serang, Banten"
var coding = "HTML, CSS, JavaScript dan Python"
var kuliah = "Universitas Harkat Negeri Tegal"
var prodi = "D4 Vokasi Informatika"
var lomba = "Finalis OSN-K Informatika 2025"

var profil = `
- Nama lengkap   : ${nama}
- Nama panggilan : ${akrab}
- Asal daerah    : ${asal}
- Coding         : ${coding}
- Kuliah         : ${kuliah}
- Prodi          : ${prodi}
- Lomba          : ${lomba}
`

console.log (profil)

console.log ("\n --- batas --- \n")




console.log ("\n Array \n")

var daf = ["Halo", "Tes", "Fast", "Green", "Job"]

for (a = 0; a < daf.length; a++) {
     console.log (daf [a])
}


console.log ("\n --- batas --- \n")




console.log ("\n Array 1 \n")

var hun = ["Fan", "Ran", "Creeper", "Skeleton", "Wither", "XP"]

for (b = 0; b < hun.length; b++) {
     console.log (hun [b])
}


console.log ("\n --- batas --- \n")




console.log ("\n Array 3 \n")

var fun = ["Wither", "Hostile Mob", "Mob", "Monster", "Golem", "Dead Golem", "Main kart"]

for (c = 0; c < fun.length; c++) {
     console.log (fun [c])
}


console.log ("\n --- batas --- \n")




console.log ("\n Dictionary \n")

var data = {
     "wahana" : "Bianglala",
     "tipe" : "Roda",
     "status" : "Oke",
     "tinggi" : 20,
}

console.log ("Wahana :", data ["wahana"])
console.log ("Tipe :", data ["tipe"])
console.log ("Status :", data ["status"])
console.log ("Tinggi :", data ["tinggi"])


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Dasar \n")

function dasar (j) {

     if (j >= 5) {
          console.log (`Besar, angka j = ${j}`)
     }

     else {
          console.log (`Kecil, angka j = ${j}`)
     }
}

dasar (10)
dasar (9)
dasar (8)
dasar (6)
dasar (5)
dasar (3)
dasar (2)
dasar (1)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Lanjutan \n")

function der (j) {

     if (j >= 8) {
          console.log (`Besar, angka j = ${j}`)
     }

     else if (j >= 5) {
          console.log (`Tengah, angka j = ${j}`)
     }

     else {
          console.log (`Kecil, angka j = ${j}`)
     }
}

der (10)
der (9)
der (8)
der (7)
der (5)
der (4)
der (3)
der (2)


console.log ("\n --- batas --- \n")




console.log ("\n Nested 1 \n")

function eril (l) {

     if (l >= 8) {
          if (cek == true) {
               console.log (`Besar, angka l = ${l}`)
          }
     }

     else if (l >= 5) {
          console.log (`Kecil, angka l = ${l}`)
     }
}

eril (10)
eril (9)
eril (8)
eril (7)
eril (6)
eril (5)
eril (4)


console.log ("\n --- batas --- \n")



console.log ("\n Percabangan Nested dengan Simbol \n")

function un (m) {

     if (m >= 8 && m >= 5) {
          if (cek == true) {
               console.log (`Besar, angka m = ${m}`)
          }
     }

     else if (m > 5 || m > 3) {
          console.log (`Kecil, angka m = ${m}`)
     }
}

un (10)
un (9)
un (8)
un (7)
un (6)
un (5)
un (4)


console.log ("\n --- batas --- \n")