console.log ("\n Demo Percabangan Looping (Perulangan) Kondisional \n")


console.log ("\n Switch Case 1 \n")

var warna = "Merah"

switch (warna) {
    
    case "Merah":
        console.log ("Merah")
        break
        
    default:
    console.log ("Warna lain")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 2 \n")

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
    console.log ("Hari Libur")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 3 \n")

var kondisi = 2 

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
        console.log ("Marah")
        break
        
    case 6:
        console.log ("Kesal")
        break
        
    case 7:
        console.log ("Jengkel")
        break
        
    default:
    console.log ("Biasa aja")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 4 \n")

var hobi = "Wota JKT48"

switch (hobi) {
    
    case "Main Game":
        console.log ("Main Game")
        break
        
    case "Wota JKT48":
        console.log ("Wota JKT48")
        break
        
    case "Denger Musik":
        console.log ("Denger Musik")
        break
        
    case "Denger Lagu JKT48":
        console.log ("Denger Lagu JKT48")
        break
        
    case "Denger Lagu Padang":
        console.log ("Denger lagu Padang")
        break
        
    case "Nonton Film":
        console.log ("Nonton Film")
        break
        
    case "Mancing":
        console.log ("Mancing")
        break
        
    case "Santai di Rumah":
        console.log ("Santai di rumah")
        break
        
    case "Trafelling ke Kota Jakarta dan Fx Sudirman":
        console.log ("Trafelling ke Kota Jakarta dan Fx Sudirman")
        break
        
    default:
    console.log ("Masuk kerja lagi")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Dasar \n")

var a = 9

if (a > 5) {
    console.log (`Besar, a = ${a}`)
}

else {
    console.log (`Kecil, a = ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan 1 \n")

var skor = 100

if (skor >= 90) {
    console.log (`Oke, skor = ${skor}`)
}

else if (skor >= 50) {
    console.log (`Setengah, skor = ${skor}`)
}

else {
    console.log (`Jelek, skor = ${skor}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan 2 \n")

var nilai = 95

if (nilai >= 90) {
    console.log (`Oke, nilai = ${nilai}`)
}

else if (nilai >= 50) {
    console.log (`Setengah, nilai = ${nilai}`)
}

else {
    console.log (`Jelek, nilai = ${nilai}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Ladder \n")

var nilai = 100

if (nilai == 100) {
    console.log (`A++, nilai = ${nilai}`)
}

else if (nilai == 95) {
    console.log (`A+, nilai = ${nilai}`)
}

else if (nilai == 90) {
    console.log (`A, nilai = ${nilai}`)
}

else if (nilai == 85) {
    console.log (`B+, nilai = ${nilai}`)
}

else if (nilai == 80) {
    console.log (`B, nilai = ${nilai}`)
}

else if (nilai == 75) {
    console.log (`C, nilai = ${nilai}`)
}

else if (nilai == 70) {
    console.log (`D, nilai = ${nilai}`)
}

else {
    console.log (`E, nilai = ${nilai}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 1 \n")


var usia = 20
var cek = true

if (cek) {
    if (usia >= 17) {
        console.log (`Boleh ambil SIM, usia = ${usia}`)
    }
    
    else {
        console.log (`Masih kecil usianya, usia = ${usia}`)
    }
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 2 \n")

var login = true
var token = false

if (login == true) {
    if (token == true) {
        console.log ("Bisa masuk sistem")
    }
    
    else {
        console.log ("Token salah")
    }
}

else {
    console.log ("Masih belum sih")
}


console.log ("\n --- Batas --- \n")





console.log ("\n Percabangan Nested 2 \n")

sim = true
usia = 19

if (sim == true) {
    if (usia >= 17) {
        console.log (`Boleh ikut dan bikin SIM, usia = ${usia}`)
    }
    
    else if (sim == false) {
        console.log (`Gak boleh bikin sim, usia = ${usia}`)
    }
}

else {
    console.log (`Masih belum cukup umur, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 3 \n")

var usia = 20
var cek = true

if (cek == true) {
    if (usia >= 19) {
        console.log (`Oke, usia = ${usia}`)
    }
    
    else if (cek == false) {
        console.log (`belum oke, usia = ${usia}`)
    }
}

else {
    console.log (`Masih belum oke, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 4 \n")

var usia = 15
var cek = true

if (usia >= 17) {
    if (cek == true) {
        console.log (`Boleh ambil SIM, usia = ${usia}`)
    }
    
    else if (usia < 17) {
        console.log (`Belum boleh ambil SIM, usia = ${usia}`)
    }
}

else {
    console.log (`Masih dibawah umur, umur = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 5 \n")

var usia = 19
var cek = true

if (usia >= 17) {
    if (cek == true) {
        console.log (`Boleh ambil SIM, usia = ${usia}`)
    }
    
    else {
        console.log (`Belum boleh ambil SIM, usia = ${usia}`)
    }
}

else {
    console.log (`Di lain waktu ambilnya, usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested Majemuk Kompleks \n")

var usia = 19
var uang = 500000

if ((usia >= 25) && (uang >= 30000000)) {
    if (cek == true) {
        console.log (`Uang anda cukup untuk hidup, usia = ${usia} dan uang = ${uang}`)
    }
    
    else if ((usia <= 25) && (usia <= 30000000)) {
        console.log (`Belum untuk kebutuhan, usia = ${usia} dan uang ${uang}`)
    }
    
    else {
        console.log (`Belum masih kecil kamu, usia = ${usia} dan uang ${uang}`)
    }
}

else {
    console.log (`Belum masih kurang banget, usia = ${usia} dan uang = ${uang}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested Majemuk Kompleks 2 \n")

var usia = 20
var uang = 500000

if ((uang >= 30000000) && (usia >= 25)) {
    if (cek == true) {
        console.log (`Dan sukses, uang = ${uang} dan usia = ${usia}`)
    }
    
    else if ((usia <= 25) && (uang <= 30000000)) {
        console.log (`Masih belum, usia = ${usia} dan uang = ${uang}`)
    }
}

else {
    console.log (`Belum sesuai, uang = ${uang} dan usia = ${usia}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Perulangan \n")

for (a = 1; a < 11; a++) {
    console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Perulangan 1 \n")

for (b = 5; b < 26; b++) {
    console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Perulangan 2 \n")

for (c = 0; c < 20; c++) {
    console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Perulangan 3 \n")

for (d = 10; d < 26; d++) {
    console.log (`Urutan ke - ${d}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n While Perulangan \n")

var a = 10

while (a < 31) {
    console.log (`Urutan ke - ${a}`)
    a++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While Perulangan 2 \n")

var b = 5

while (b < 20) {
    console.log (`Urutan ke - ${b}`)
    b++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While Perulangan 3 \n")

var c = 10 

while (c < 20) {
     console.log (`Urutan ke - ${c}`)
     c++
}


console.log ("\n --- Batas --- \n")
