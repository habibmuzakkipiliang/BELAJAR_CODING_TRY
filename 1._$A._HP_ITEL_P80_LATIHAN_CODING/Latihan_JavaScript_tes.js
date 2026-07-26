console.log ("\n bikin Hello World \n")


console.log ("Hello World")


console.log ("\n --- batas --- \n")




console.log ("\n Variabel dasar \n")

var nama = "Habib Muzakki"
console.log (nama)


var angka = 12
console.log (angka)


var desimal = 3.14
console.log (desimal)


console.log ("\n --- batas --- \n")




console.log ("\n Tipe data pemrograman \n")

var teks = "Ini contoh aja"
var angka = 12
var desimal = 3.19
var cek = true
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




console.log  ("\n Profil Habib Muzakki \n")

var nama = "Habib Muzakki"
var akrab = "Habib"
var marga = "Piliang"
var asal = "Kota Serang, Banten"
var kuliah = "Universitas Harkat Negeri Tegal"
var jurusan = "D4 Vokasi Teknik Informatika"
var alumni = "MAN 2 KOTA SERANG (KELAS AGAMA) tahun 2026 ini"
var coding = "HTML, CSS, JavaScript dan Python"
var lomba = "Finalis OSN-K Informatika 2025"


var profil = `
- Nama lengkap   : ${nama}
- Nama panggilan : ${akrab}
- Marga          : ${marga}
- Asal           : ${asal}
- Jurusan        : ${jurusan}
- Alumni         : ${alumni}
- Coding         : ${coding}
- Lomba          : ${lomba}
`

console.log (profil)


console.log ("\n --- batas --- \n")




console.log ("\n Dictionary (Meme) \n")

data = {
    "nama" : "Erling Haaland",
    "asal" : "Norwegia",
    "kerja" : "Programmer dan ",
    "coding" : "HTML, CSS, JavaScript dan Python"
}

console.log ("Nama :", data ["nama"])

console.log ("Asal :", data ["asal"])

console.log ("Kerja :", data ["kerja"])

console.log ("Coding :", data ["coding"])


console.log ("\n --- batas --- \n")




console.log ("\n Array \n")

dar = [
    
    "1. Android 17",
    "2. Android 16",
    "3. Android 15",
    "4. Android 14",
    "5. Android 13",
    
    ]
    
    
for (a = 0; a < dar.length; a++) {
    console.log (dar [a])
}
    
    
console.log ("\n --- batas --- \n")




console.log ("\n Kalkulator Dasar dalam Fungsi \n")


function tambah (x, y) {
    return x + y
}


function kurang (e, r) {
    return e - r
}


function kali (s, t) {
    return s * t
}


function pangkat (s, d) {
    return s ** d
}


function bagi (d, f) {
    return d / f
} 


function modulus (e, k) {
    return e % k
}


hasil_1 = tambah (10, 10)
hasil_2 = kurang (10, 5)
hasil_3 = kali (10, 10)
hasil_4 = pangkat (10, 3)
hasil_5 = bagi (10, 5)
hasil_6 = modulus (10, 5)


var hitung = `
- Tambah  = ${hasil_1}
- Kurang  = ${hasil_2}
- Kali    = ${hasil_3}
- Pangkat = ${hasil_4}
- Bagi    = ${hasil_5}
- Modulus = ${hasil_6}
`

console.log (hitung)


console.log ("\n --- batas --- \n")




console.log ("\n Operator Perbandingan \n")

var x = 15
var y = 10

banding = `
- Hasil = ${x > y}
- Hasil = ${x < y}
- Hasil = ${x >= y}
- Hasil = ${x <= y}
- Hasil = ${x == y}
- Hasil = ${x != y}
`


console.log (banding)


console.log ("\n --- batas --- \n")




console.log ("\n Operator Logika \n")

var logic = `
- Hasil = ${x > y && x < y}
- Hasil = ${x < y || x > y}
- Hasil = ${! (x > y)}
- Hasil = ${! (x < y)}
`

console.log (logic)


console.log ("\n --- batas --- \n")



console.log ("\n Fungsi + Swich Case dengan Int")

function lan (f) {
    
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
            
        case 5:
            console.log ("Angka 5")
            break
            
        default:
        console.log ("Angka lain")
    }
}

lan (1)
lan (2)
lan (3)
lan (4)
lan (5)
lan (6)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi + Switch Case dengan String \n")

function stan (n) {
    
    switch (n) {
        
        case "Merah":
            console.log ("Warna Merah")
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

stan ("Merah")
stan ("Kuning")
stan ("Hijau")
stan ("Hitam")


console.log ("\n --- batas --- \n")





console.log ("\n Fungsi dengan percabangan dasar \n")

function kot (e) {
    
    if (e >= 5) {
        console.log (`Besar, angka e = ${e}`)
    }
    
    else {
        console.log (`Kecil, angka e = ${e}`)
    }
}

kot (10)
kot (9)
kot (7)
kot (6)
kot (5)
kot (4)
kot (3)
kot (2)
kot (1)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Lanjutan \n")

function dej (u) {
    
    if (u >= 8) {
        console.log (`Besar, angka u = ${u}`)
    }
    
    else if (u >= 5) {
        console.log (`Tengah angka u = ${u}`)
    }
    
    else {
        console.log (`Kecil, angka u = ${u}`)
    }
}

dej (10)
dej (9)
dej (8)
dej (7)
dej (6)
dej (5)
dej (4)
dej (3)
dej (2)
dej (1)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Nilai Rapor \n")

function rapor (d) {
    
    if (d >= 95) {
        console.log (`A, nilai = ${d}`)
    }
    
    else if (d >= 90) {
        console.log (`B, nilai = ${d}`)
    }
    
    else if (d >= 80) {
        console.log (`C, nilai = ${d}`)
    }
    
    else if (d >= 70) {
        console.log (`D, nilai = ${d}`)
    }
    
    else if (d >= 60) {
        console.log (`E, nilai = ${d}`)
    }
    
    else if (d >= 50) {
        console.log (`F, nilai = ${d}`)
    }
    
    else {
        console.log (`Jelek amat, nilai = ${d}`)
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

function run (e) {
    
    cek = true
    
    if (e >= 5) {
        if (cek) {
            console.log (`Besar, angka e = ${e}`)
        }
    }
    
    else {
        console.log (`Kecil, angka e = ${e}`)
    }
}

run (10)
run (9)
run (8)
run (7)
run (6)
run (5)
run (4)
run (3)
run (2)
run (1)


console.log ("\n --- batas --- \n")




console.log ("\n For dasar 1 \n")

for (a = 0; a < 10; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n For dasar 2 \n")

for (b = 1; b < 11; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n While dasar 1 \n")

a = 1

while (a < 11) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- batas --- \n")




console.log ("\n While dasar 1 \n")

b = 10

while (b > 0) {
    console.log (`Urutan ke - ${b}`)
    b--
}


console.log ("\n --- batas --- \n")




console.log ("\n Do While dasar \n")

a = 1

do {
    console.log (`Urutan ke - ${a}`)
    a++
}

while (a < 11)


console.log ("\n --- batas --- \n")




console.log ("\n For Nested 1 \n")

for (w = 1; w < 4; w++) {
    for (r = 1; r < 4; r++) {
        console.log (`Luar : ${w} dan Dalam : ${r}`)
    }
}


console.log ("\n --- batas --- \n")




console.log ("\n For Nested 2 \n")

for (x = 1; x < 3; x++) {
    for (y = 1; y < 3; y++) {
        for (z = 1; z < 3; z++) {
            console.log (`x : ${x}, y : ${y}, z : ${z}`)
        }
    }
}


console.log ("\n --- batas --- \n")




console.log ("\n Error Handling 1 \n")

try {
    var a = 10 / K
    console.log (a)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- batas --- \n")




console.log ("\n Error Handling 2 \n")

try {
    var b = 20 + 20
    console.log (b)
}

catch (Error) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Error Handling Throw \n")

function ron (e) {
    
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
        console.log (`Gak boleh minus, angka e = ${e}`)
    }
}

ron (-10)
ron (-11)
ron (-4)
ron (-3)
ron (10)
ron (8)
ron (5)
ron (2) 
ron (3)
ron (1)


console.log ("\n --- batas --- \n")
