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
daftar.push ("12. Hurricane")
daftar.push ("13. Spitfire")
daftar.push ("14. WW2")
daftar.push ("15. WW1")
daftar.push ("16. Teater Pasifik WW2")



// Hapus Elemen

daftar.pop ("14. WW2")
daftar.pop ("15. WW1")
daftar.pop ("16. Teater Pasifik WW2")



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




console.log ("\n Operator Perbandingan dan logika \n")

var x = 10
var y = 6

var banding = `
Hasil : ${x > y}
Hasil : ${x < y}
Hasil : ${x >= y}
Hasil : ${x <= y}
Hasil : ${x == y}
Hasil : ${x != y}


----------------


Hasil : ${x > y && x < y}
Hasil : ${x < y || x > y}
Hasil : ${! x > y}
Hasil : ${! x < y}
Hasil : ${! x}
Hasil : ${!y}
`


console.log (banding)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan percabangan dasar \n")

function dasar (a) {
    
    if (a >= 5) {
        console.log (`Besar, angka a = ${a}`)
    }
    
    else {
        console.log (`Kecil, angka a = ${a}`)
    }
}

dasar (10)
dasar (5)
dasar (2)
dasar (8)
dasar (5)
dasar (3)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan dasar 2 \n")

function er (b) {
    
    if (b >= 5) {
        console.log (`Besar, angka b = ${b}`)
    }
    
    else {
        console.log (`Kecil, angka b = ${b}`)
    }
}

er (10)
er (7)
er (5)
er (3)
er (6)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan Lanjutan \n")

function rt (c) {
    
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

rt (10)
rt (9)
rt (5)
rt (1)
rt (3)
rt (7)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan Lanjutan 2 \n")

function tr (d) {
    
    if (d >= 5) {
        console.log (`Besar, angka d = ${d}`)
    }
    
    else if (d >= 5) {
        console.log (`Kecil, angka d = ${d}`)
    }
    
    else {
        console.log (`Sama saja, angka d = ${d}`)
    }
}

tr (10)
tr (4)
tr (8)
tr (5)
tr (3)
tr (11)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan Nested 1 \n")

function lo (f) {
    
    cek = true
    
    if (f >= 5) {
        if (cek) {
            console.log (`Besar, angka f = ${f}`)
        }
    }
    
    else {
        console.log (`Kecil, angka f = ${f}`)
    }
}

lo (10)
lo (8)
lo (5)
lo (7)
lo (4)
lo (3)


console.log ("\n --- Batas --- \n")
