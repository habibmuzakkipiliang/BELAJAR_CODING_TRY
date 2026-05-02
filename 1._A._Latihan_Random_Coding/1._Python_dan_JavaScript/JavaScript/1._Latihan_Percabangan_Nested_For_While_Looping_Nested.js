console.log ("\n Profil Habib Muzakki Piliang \n")


var nama = "Habib Muzakki"
var panggil = "Habib"
var marga = "Piliang"
var suku = "Minangkabau"
var coding = "HTML, CSS, JavaScript dan Python"
var lomba = "Finalis OSN-K Informatika tahun 2025"
var tinggi = "170 cm"
var berat = "60 kg"
var darah = "B"
var fans = "JKT48"
var oshi = "Michie, Fritzy, Anindya, Christy, Freya JKT48"


var profil = `

- Nama lengkap   : ${nama}
- Nama panggilan : ${panggil}
- Marga          : ${marga}
- Suku           : ${suku}
- Coding         : ${coding}
- Lomba          : ${lomba}
- Tinggi badan   : ${tinggi}
- Berat badan    : ${berat}
- Golongan darah : ${darah}
- Fans           : ${fans}
- Oshi JKT48     : ${oshi}

`


console.log (profil)


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case \n")


var hari = "Senin"

switch (hari) {
    
    case "Senin":
        console.log ("Senin")
        break
        
    case "Selasa":
        console.log ("Selasa")
        break
        
    case "Rabu":
        console.log ("Rabu")
        break
        
    case "Kamis":
        console.log ("Kamis")
        break
        
    case "Jumat":
        console.log ("Jumat")
        break
        
    default:
    console.log ("Libur")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan dasar \n")


var a = 9

if (a > 5) {
    console.log (`Besar, a = ${a}`)
}

else {
    console.log (`Kecil, a = ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan \n")


var k = 3

if (k > 5) {
    console.log (`Besar, k = ${k}`)
}

else if (k < 5) {
    console.log (`Kecil, k = ${k}`)
}

else {
    console.log (`Sama saja, k = ${k}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Ledder \n")


var s = 7

if (s >= 9) {
    console.log (`A, skor = ${s}`)
}

else if (s >= 8) {
    console.log (`B, skor = ${s}`)
}

else if (s >= 7) {
    console.log (`C, skor = ${s}`)
}

else if (s >= 6) {
    console.log (`D, skor = ${s}`)
}

else if (s >= 5) {
    console.log (`E, skor = ${s}`)
}

else {
    console.log (`Jelek, skor = ${s}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, usia produktif 1 \n")


var usia = 20
var cek = true

if (cek) {
    if ((usia >= 15) && (usia <= 64)) {
        console.log (`Sudah masuk usia produktif, usia = ${usia}`)
    }
    
    else if (usia > 64) {
        console.log (`Sudah lanjut usia, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum masuk usia produktif, usia = ${usia}`)
    }
}

else {
    console.log (`Masih kecil usianya, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested, usia produktif manusia 2 \n")


var usia = 13
var cek = true

if (cek) {
    if ((usia >= 15) && (usia <= 64)) {
        console.log (`Sudah masuk usia produktif, usia = ${usia}`)
    }
    
    else if (usia > 64) {
        console.log (`Sudah lanjut usia, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum masuk usia produktif, usia = ${usia}`)
    }
}

else {
    console.log (`Masih kecil usianya, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For dasar \n")


for (a = 0; a < 16; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- Batas --- \n")




for (b = 0; b < 21; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- Batas --- \n")




for (c = 0; c < 26; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- Batas --- \n")



console.log ("\n While dasar \n")


var a = 5

while (a < 21) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- Batas --- \n")




var b = 10

while (b < 21) {
    console.log (`Urutan ke - ${b}`)
    b++
}


console.log ("\n --- Batas --- \n")
