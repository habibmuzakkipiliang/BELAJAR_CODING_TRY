// JavaScript Task

console.log ("Hello World")


console.log ("\n --- Batas --- \n")



console.log ("\n Variabel dan Tipe data pemrograman \n")


var nama = "Tes 1"
var angka = 34
var desimal = 44.23
var huruf = 'A'
var cek = true
var daftar = [
    
    "1. Mobil",
    "2. Motor", 
    "3. Kereta Api",
    "4. Bajai",
    
    ]


detail = `

- Nama    : ${nama}
- Angka   : ${angka}
- Desimal : ${desimal}
- Huruf   : ${huruf}
- Cek     : ${cek}
- Daftar  : 

`

console.log (detail)


for (a = 0; a < daftar.length; a++) {
    console.log (daftar [a])
}


console.log ("\n --- Batas --- \n")




console.log ("\n Dictionary \n")


var data = {
    "nama" : "Alan John",
    "asal" : "Amerika Serikat",
    "kerja" : "Software Engineer",
    "coding" : "HTML, CSS, JavaScript dan Python",
    
}


console.log ("Nama :", data ["nama"])

console.log ("Asal :", data ["asal"])

console.log ("Kerja :", data ["kerja"])

console.log ("Coding :", data ["coding"])


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




console.log ("\n Percabangan Dasar 1 \n")


var b = 3

if (b > 5) {
    console.log (`Besar, b = ${b}`)
}

else {
    console.log (`Kecil, b = ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan 1 \n")


var c = 9

if (c > 5) {
    console.log (`Besar, c = ${c}`)
}

else if (c < 5) {
    console.log (`Kecil, c = ${c}`)
}

else {
    console.log (`Sama saja,  c = ${c}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan 2 \n")


var d = 3 

if (d > 5) {
    console.log (`Besar, d = ${d}`)
}

else if (d < 5) {
    console.log (`Kecil, d = ${d}`)
}

else {
    console.log (`Sama saja, d = ${d}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 1 \n")


var skor = 9
var cek = true

if (cek) {
    if (skor > 5) {
        console.log (`Besar, skor = ${skor}`)
    }
    
    else if (skor < 5) {
        console.log (`Kecil, skor = ${skor}`)
    }
}

else {
    console.log (`Sama saja, skor = ${skor}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 2 \n")


var skor = 3
var cek = true

if (cek) {
    if (skor > 5) {
        console.log (`Besar, skor = ${skor}`)
    }
    
    else {
        console.log (`Kecil, skor = ${skor}`)
    }
}


else {
    console.log (`Sama saja, skor = ${skor}`)
}