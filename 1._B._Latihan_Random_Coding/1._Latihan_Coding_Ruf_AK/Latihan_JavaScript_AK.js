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


function pangkat (j, n) {
    return j ** n
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



console.log ("\n Fungsi dengan Switch Case 1 \n")

function ran (warna) {
    
    switch (warna) {
        
        case "Merah":
            console.log ("Warna Merah")
            break
            
        case "Kuning":
            console.log ("Warna Kuning")
            break
            
        case "Biru":
            console.log ("Warna Biru")
            break
            
        case "Hijau":
            console.log ("Warna Hijau")
            break
            
        default:
        console.log ("Warna lain")
    }
}

ran ("Merah")
ran ("Kuning")
ran ("Biru")
ran ("Hijau")
ran ("Hitam")
ran ("Ungu")


console.log ("\n --- Batas --- \n")

function rak (kondisi) {
    
    switch (kondisi) {
        
        case 1:
            console.log ("Senang")
            break
            
        case 2:
            console.log ("Bahagia")
            break
            
        case 3:
            console.log ("Oke")
            break
            
        case 4:
            console.log ("Sedih")
            break
            
        case 5:
            console.log ("Kesal")
            break
            
        case 6:
            console.log ("Marah")
            break
            
        default:
        console.log ("Biasa aja")
    }
}

rak (1)
rak (2)
rak (3)
rak (4)
rak (5)
rak (10)
rak (11)
rak (12)


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
    
    if (d >= 8) {
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




console.log ("\n Fungsi dengan Percabangan Tangga Ladder, Nilai Rapor Sekolah \n")

function rapor (n) {
    
    if (n >= 95) {
        console.log (`A, nilai = ${n}`)
    }
    
    else if (n >= 90) {
        console.log (`B, nilai = ${n}`)
    }
    
    else if (n >= 80) {
        console.log (`C, nilai = ${n}`)
    }
    
    else if (n >= 70) {
        console.log (`D, nilai = ${n}`)
    }
    
    else if (n >= 60) {
        console.log (`E, nilai = ${n}`)
    }
    
    else if (n >= 50) {
        console.log (`F, nilai = ${n}`)
    }
    
    else {
        console.log (`Jelek amat ya, nilai = ${n}`)
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


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan Nested 1 \n")

function lo (f) {
    
    cek = true
    
    if (cek) {
        if (f >= 5) {
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




console.log ("\n Fungsi dengan Percabangan Nested 2 \n")

function der (g) {
    
    cek = true
    
    if (cek) {
        if (g >= 5) {
            console.log (`Besar, angka g = ${g}`)
        }
    }
    
    else {
        console.log (`Kecil, angka g = ${g}`)
    }
}

der (10)
der (8)
der (4)
der (9)
der (3)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan Nested Majemuk Kompleks, Usia dan Uang \n")

function lop (usia, uang) {
    
    cek = true
    
    if (usia >= 18 && uang >= 5000) {
        if (cek) {
            console.log (`Uang kamu mencukupi ${uang} dan usia kamu ${usia} oke`)
        }
    }
    
    
    else {
        console.log (`Belum cukup sama sekali uang ${uang} dan usianya ${usia} juga`)
    }
}

lop (19, 6000)
lop (20, 10000)
lop (15, 3000)
lop (18, 5000)
lop (19, 7000)
lop (17, 6000)


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar \n")

for (a = 0; a < 11; a++) {
    console.log (`Urutan ke - ${a}`)
}




console.log ("\n For dasar 1 \n")

for (b = 1; b < 11; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar 3 \n")

for (c = 5; c < 21; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar, hitung maju \n")

var a = 1 

while (a < 11) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While dasar, hitung mundur \n")

var b = 20

while (b > 0) {
    console.log (`Urutan ke - ${b}`)
    b--
}


console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar, hitung maju \n")

var c = 1

do {
    console.log (`Urutan ke - ${c}`)
    c++
}

while (c < 16)


console.log ("\n --- Batas --- \n")




console.log ("\n Do While dasar, hitung mundur \n")

var d = 20 

do {
    console.log (`Urutan ke - ${d}`)
    d--
}

while (d > 0)


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 1 \n")

for (a = 0; a < 4; a++) {
    for (b = 0; b < 4; b++) {
        console.log (`Luar : ${a} dan Dalam : ${b}`)
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 2 \n")

for (x = 0; x < 4; x++) {
    for (y = 0; y < 4; y++) {
        console.log (`Luar : ${x} dan Dalam : ${y}`)
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested 4 \n")

for (k = 0; k < 4; k++) {
    for (f = 0; f < 4; f++) {
        for (j = 0; j < 4; j++) {
            console.log (`Kiri : ${k}, Tengah : ${f}, Kanan : ${j}`)
        }
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Parameter \n")

function nam (nama) {
    console.log (`Halo nama saya ${nama} dari Jakarta Utara`)
}

nam ("Rayyan")
nam ("Fayyan")
nam ("Rutter")
nam ("Fayyan")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Return \n")

function tambah (x, y) {
    return x + y
}

hasil = tambah (10, 10)
console.log ("Tambah =", hasil)


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling \n")

try {
    var hasil = 10 / A
    console.log (hasil)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Error Handling 2 \n")

try {
    var hasil = 10 + 10
    console.log (hasil)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log  ("\n --- Batas --- \n")




console.log ("\n Error Handling 3 \n")

try {
    var hasil = 20 / B 
    console.log (hasil)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Fungi dengan Throw Error Handling Percabangan dasar \n")

function hop (i) {
    
    try {
        if (i < 0) {
            throw ("Gagal")
        }
        
        if (i >= 5) {
            console.log (`Besar, angka i = ${i}`)
        }
        
        else {
            console.log (`Kecil, angka i = ${i}`)
        }
    }
    
    catch (Error) {
        console.log (`Angka i gak boleh minus = ${i}`)
    }
}

hop (10)
hop (8)
hop (3)
hop (7)
hop (-10)
hop (-3)
hop (-4)
hop (-2)


console.log ("\n --- Batas --- \n")
