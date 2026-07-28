console.log ("\n Bikin Hello World \n")


console.log ("Hello World")


console.log ("\n --- batas --- \n")




console.log ("\n Variabel dasar dalam bentuk profil \n")

var nama = "Habib Muzakki"
var akrab = "Habib"
var asal = "Kota Serang, Banten"
var kuliah = "Universitas Harkat Negeri Tegal"
var jurusan = "D4 Vokasi Teknik Informatika"
var tinggi = "170 cm"
var lomba = "Finalis OSN-K Informatika"
var coding = "HTML, CSS, JavaScript dan Python"
var wota = "JKT48"


var profil = `
- Nama         : ${nama}
- Panggil      : ${akrab}
- Asal         : ${asal}
- Kuliah       : ${kuliah}
- Jurusan      : ${jurusan}
- Tinggi badan : ${tinggi}
- Lomba        : ${lomba}
- Coding       : ${coding}
- Wota         : ${wota}
`

console.log (profil)


console.log ("\n --- batas --- \n")




console.log ("\n Tipe data pemrograman \n")

var teks = "Contoh aja"
var angka = 15
var desimal = 3.14
var cek = true
var char = 'A'
var kosong = null


var tipe = `
- Teks    : ${teks}
- Angka   : ${angka}
- Desimal : ${desimal}
- Cek     : ${cek}
- Kosong  : ${kosong}
`


console.log (tipe)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Switch Case 1 \n")

function tan (a) {

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

          case 5:
               console.log ("Angka 5")
               break
          
          default:
               console.log ("Kembali ke angka 0")
     }
}

tan (1)
tan (2)
tan (3)
tan (4)
tan (5)
tan (6)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Switch Case 2 \n")

function hun (c) {

     switch (c) {

          case "Merah":
               console.log ("Warna Merah")
               break

          case "Kuning":
               console.log ("Warna Kuning")
               break

          case "Hijau":
               console.log ("Warna Hijau")
               break

          default:
               console.log ("Warna lain")
     }
}

hun ("Merah")
hun ("Kuning")
hun ("Hijau")
hun ("Hitam")


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Operator dasar \n")

function tambah (x, y) {
     return x + y
}


function kurang (l, y)  {
     return l - y
}


function kali (e, r) {
     return e * r
}

function bagi (k, l) {
     return k / l
}


function pangkat (w, r) {
     return w ** r
}


function modulus (w, h) {
     return w % h
}


hasil_1 = tambah (10, 10)
hasil_2 = kurang (10, 5)
hasil_3 = kali (10, 10)
hasil_4 = bagi (10, 5)
hasil_5 = pangkat (10, 3)
hasil_6 = modulus (10, 5)


hitung = `
- Hasil Tambah   : ${hasil_1}
- Hasil Kurang   : ${hasil_2}
- Hasil kali     : ${hasil_3}
- Hasil bagi     : ${hasil_4}
- Hasil pangkat  : ${hasil_5}
- Hasil Modulus  : ${hasil_6}
`

console.log (hitung)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Dasar \n")

function fungsi (a) {

     if (a >= 5) {
          console.log (`Besar, angka a = ${a}`)
     }

     else {
          console.log (`Kecil, angka a = ${a}`)
     }
}

fungsi (10)
fungsi (9)
fungsi (8)
fungsi (7)
fungsi (6)
fungsi (5)
fungsi (4)
fungsi (3)
fungsi (2)
fungsi (1)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Lanjutan \n")

function dasar (w) {

     if (w >= 8) {
          console.log (`Besar, angka w = ${w}`)
     }

     else if (w >= 5) {
          console.log (`Tengah, angka w = ${w}`)
     }

     else {
          console.log (`Kecil, angka w = ${w}`)
     }
}

dasar (10)
dasar (9)
dasar (8)
dasar (7)
dasar (6)
dasar (5)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Nilai Rapor \n")

function rapor (e) {

     if (e >= 90) {
          console.log (`A, nilai = ${e}`)
     }

     else if (e >= 80) {
          console.log (`B, nilai = ${e}`)
     }

     else if (e >= 70) {
          console.log (`C, nilai = ${e}`)
     }

     else if (e >= 60) {
          console.log (`D, nilai = ${e}`)
     }
     
     else if (e >= 50) {
          console.log (`E, nilai = ${e}`)
     }

     else {
          console.log (`Jelek amat, nilai = ${e}`)
     }
}

rapor (100)
rapor (95)
rapor (90)
rapor (80)
rapor (70)
rapor (60)
rapor (50)
rapor (40)


console.log ("\n ---- batas ---- \n")




console.log ("\n Fungsi dengan Percabangan Nested 1 \n")

function ref (y) {
    
    cek = true
    
    if (y >= 8) {
        if (cek == true) {
            console.log (`Besar, angka a = ${y}`)
        }
    }
    
    else {
        console.log (`Kecil, angka y = ${y}`)
    }
}

ref (10)
ref (9)
ref (6)
ref (5)
ref (4)
ref (3)


console.log ("\n --- batas --- \n")