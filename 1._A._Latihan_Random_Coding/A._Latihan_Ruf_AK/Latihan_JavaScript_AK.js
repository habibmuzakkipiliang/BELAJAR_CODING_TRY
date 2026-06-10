// Latihan JavaScript AK

console.log ("Hello World")


console.log ("\n --- Batas --- \n")




console.log ("\n Variabel Dasar dan Tipe data pemrograman \n")

var nama = "Habib Muzakki"
var panggil = "Habib"
var oshi = "Michie dan Gracie JKT48"
var angka = 12
var desimal = 23.12
var cek = true
var cek_1 = false
var kosong = null
var daftar = [
    
    "1. Stuka",
    "2. Hellcat",
    "3. Mustang",
    "4. Corsair",
    "5. ME 262",
    "6. Ilyushin",
    "7. Tupolev",
    
    ]
    
    
console.log ("\n --- Batas --- \n")   




var detail = `
- Nama    : ${nama}
- Panggil : ${panggil}
- Oshi    : ${oshi}
- Angka   : ${angka}
- Desimal : ${desimal}
- Cek     : ${cek}
- Cek 1   : ${cek_1}
- Kosong  : ${kosong}
- Daftar  : 
`

console.log (detail)



// Tambah Elemen

daftar.push ("8. T34")
daftar.push ("9. T55")
daftar.push ("10. Stuart")
daftar.push ("11. Sherman")
daftar.push ("12. WW2")
daftar.push ("13. WW1")
daftar.push ("14. Teater Pasifik WW2")



// Hapus Elemen

daftar.pop ("12. WW2")
daftar.pop ("13. WW1")
daftar.pop ("14. Teater Pasifik WW2")



for (a = 0; a < daftar.length; a++) {
    console.log (daftar [a])
}


console.log ("\n --- Batas --- \n")




console.log ("\n Objek \n")

var bio = {
    "tinggi" : 170,
    "berat" : 60,
    "cek" : true,
    "kosong" : null,
    "teks" : "Halo Michie dan Gracie JKT48",
    "desimal" : 23.23,
} 

console.log ("Tinggi :", bio ["tinggi"])
console.log ("Berat :", bio ["berat"])
console.log ("Cek :", bio ["cek"])
console.log ("Kosong :", bio ["kosong"])
console.log ("Teks :", bio ["teks"])
console.log ("Desimal :", bio ["desimal"])


console.log ("\n --- Batas --- \n ")




console.log ("\n Profil Habib Muzakki \n")

var nama = "Habib Muzakki"
var panggil = "Habib"
var asal = "Padang"
var tinggal = "Kota Serang"
var usia = "19 tahun"
var tinggi = "170 cm"
var berat = "60 kg"
var angka = 100
var desimal = 12.12
var cek_3 = true



var profil = `
- Nama lengkap   : ${nama}
- Nama panggilan : ${panggil}
- Asal           : ${asal}
- Tempat tinggal : ${tinggal}
- Tinggi badan   : ${tinggi}
- Berat badan    : ${berat}
- Angka          : ${angka}
- Desimal        : ${desimal}
- Cek 3          : ${cek_3}
`


console.log (profil)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi return dengan kalkulator dasar \n")

function tambah (a, b) {
    return a + b
}


function kurang (x, y) {
    return x - y
}


function kali (s, d) {
    return s * d
}


function bagi (r, t) {
    return r / t
}


function pangkat (t, r) {
    return r ** t
}


function modulus (j, q) {
    return j % q
}



hasil_1 = tambah (10, 10)
hasil_2 = kurang (15, 5)
hasil_3 = kali (10, 10)
hasil_4 = bagi (20, 5)
hasil_5 = pangkat (20, 2)
hasil_6 = modulus (10, 5)



console.log ("Tambah =", hasil_1)
console.log ("Kurang =", hasil_2)
console.log ("Kali =" ,hasil_3)
console.log ("Bagi =" ,hasil_4)
console.log ("Pangkat =" ,hasil_5)
console.log ("Modulus =" ,hasil_6)