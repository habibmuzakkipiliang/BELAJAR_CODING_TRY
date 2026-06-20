console.log ("\n Bikin Hello World dan Variabel \n")

console.log ("Hello World")


var gan = "Contoh Aja"
console.log (gan)


var fan = "Ayo ke Fx Sudirman"
console.log (fan)


console.log ("\n --- Batas --- \n")




console.log ("\n Tipe data Pemrograman \n")

var teks = "Contoh teks"
var angka = 13
var desimal = 23.12
var cek = true
var char = 'A'
var kosong = null


var detail = `
- Teks    : ${teks}
- Angka   : ${angka}
- Desimal : ${desimal}
- Cek     : ${cek}
- Char    : ${char}
- Kosong  : ${kosong}
`

console.log (detail)


console.log ("\n --- Batas --- \n")




console.log ("\n Array \n")

var bensin = [
    
    "1. Pertamax",
    "2. Pertamax Turbo",
    "3. Pertamax Dex",
    "4. Dexlite",
    "5. Pertalite",
    "6. Bio Solar",
    
    ]
    
    
for (a = 0; a < bensin.length; a++) {
    console.log (bensin [a])
}


console.log ("\n --- Batas --- \n")




console.log ("\n Dictionary \n")

var gok = {
    "nama" : "James",
    "usia" : 18, 
    "asal" : "Amrik",
    "cek" : true,
}

console.log ("Nama :", gok ["nama"])
console.log ("Usia :", gok ["usia"])
console.log ("Asal :", gok ["asal"])
console.log ("Cek :", gok ["cek"])


console.log ("\n --- Batas --- \n")





console.log ("\n Fungsi dengan Operator dasar \n")

function tambah (x, y) {
    return x + y
}


function kurang (a, b) {
    return a - b
}


function kali (e, r) {
    return e * r
}


function bagi (l, p) {
    return l / p
}


function modulus (w, k) {
    return w % k
}


function pangkat (v, h) {
    return v ** h
}


hasil_1 = tambah (10, 10)
hasil_2 = kurang (10, 5)
hasil_3 = kali (10, 10)
hasil_4 = bagi (20, 5)
hasil_5 = modulus (20, 5)
hasil_6 = pangkat (10, 4)


console.log ("Tambah =", hasil_1)
console.log ("Kurang =", hasil_2)
console.log ("Kali =", hasil_3)
console.log ("Bagi =", hasil_4)
console.log ("Modulus =", hasil_5)
console.log ("Pangkat =", hasil_6)


console.log ("\n --- Batas --- \n")




console.log ("\n Operator Perbandingan \n")

var x = 10
var y = 5

banding = `
- Hasil = ${x > y}
- Hasil = ${x < y}
- Hasil = ${x >= y}
- Hasil = ${x <= y}
- Hasil = ${x != y}
- Hasil = ${x == y}
`

console.log (banding)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Switch Case 1 \n")

function rar (a) {
    
    switch (a) {
        
        case 1:
            console.log ("Oke")
            break
            
        case 2:
            console.log ("Belum")
            break
            
        case 3:
            console.log ("Baru Mulai")
            break
            
        default:
        console.log ("Biasa aja")
    }
}

rar (2)
rar (1)
rar (3)
rar (4)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Switch Case 2, Lampu Rambu Lalu Lintas \n")

function lampu (b) {
    
    switch (b) {
        
        case "Merah":
            console.log ("Lampu Merah")
            break
            
        case "Kuning":
            console.log ("Lampu Kuning")
            break
            
        case "Hijau":
            console.log ("Lampu Hijau")
            break
            
        default:
        console.log ("Lampu warna lain")
    }
}

lampu ("Merah")
lampu ("Kuning")
lampu ("Hijau")
lampu ("Biru")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan Dasar \n")

function dasar (a) {
    
    if (a >= 5) {
        console.log (`Besar, angka a = ${a}`)
    }
    
    else {
        console.log (`Kecil, angka a = ${a}`)
    }
}

dasar (10)
dasar (4)
dasar (8)
dasar (3)
dasar (7)
dasar (2)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan dasar 1 \n")

function rer (b) {
    
    if (b >= 5) {
        console.log (`Besar, angka b = ${b}`)
    }
    
    else {
        console.log (`Kecil, angka b = ${b}`)
    }
}

rer (10)
rer (4)
rer (8)
rer (3)
rer (7)
rer (2)


console.log ("\n --- Batas --- \n")



console.log ("\n Fungsi dengan Percabangan Lanjutan \n")

function fer (c) {
    
    if (c >= 8) {
        console.log (`Besar, angka c = ${c}`)
    }
    
    else if (c >= 5) {
        console.log (`Sedang, angka c = ${c}`)
    }
    
    else {
        console.log (`Kecil, angka c = ${c}`)
    }
}

fer (10)
fer (8)
fer (7)
fer (5)
fer (4)
fer (3)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan Lanjutan 1 \n")

function des (d) {
    
    if (d >= 8) {
        console.log (`Besar, angka d = ${d}`)
    }
    
    else if (d >= 5) {
        console.log (`Sedang, angka d = ${d}`)
    }
    
    else {
        console.log (`Kecil, angka d = ${d}`)
    }
}

des (10)
des (8)
des (7)
des (5)
des (4)
des (3)


console.log ("\n --- Batas --- \n")



console.log ("\n Fungsi dengan Percabangan Tangga, Nilai Rapor \n")

function rapor (h) {
    
    if (h >= 95) {
        console.log (`A, nilai = ${h}`)
    }
    
    else if (h >= 90) {
        console.log (`B, nilai = ${h}`)
    }
    
    else if (h >= 80) {
        console.log (`C, nilai = ${h}`)
    }
    
    else if (h >= 70) {
        console.log (`D, nilai = ${h}`)
    }
    
    else if (h >= 60) {
        console.log (`E, nilai = ${h}`)
    }
    
    else if (h >= 50) {
        console.log (`F, nilai = ${h}`)
    }
    
    else {
        console.log (`Kecil banget, nilai = ${h}`)
    }
}

rapor (100)
rapor (90)
rapor (80)
rapor (70)
rapor (60)
rapor (50)
rapor (30)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan Nested \n")

function det (x) {
    
    if (x >= 8) {
        if (cek == true) {
            console.log (`Besar, angka x = ${x}`)
        }
        
        else if (x >= 5) {
            console.log (`Sedang, angka x = ${x}`)
        }
    }
    
    else {
        console.log (`Kecil, angka x = ${x}`)
    }
}

det (10)
det (9)
det (8)
det (7)
det (5)
det (3)
det (2)


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Percabangan Nested 1 \n")

function fer (y) {
    
    if (y >= 8) {
        if (cek == true) {
            console.log (`Besar, angka y = ${y}`)
        }
        
        else {
            console.log (`Sedang, angka y = ${y}`)
        }
    } 
    
    else {
        console.log (`Kecil, angka y = ${y}`)
    }
}

fer (10)
fer (9)
fer (8)
fer (7)
fer (5)
fer (3)
fer (4)