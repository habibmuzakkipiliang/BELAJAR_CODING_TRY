console.log ("Hello World")

console.log ("\n --- Batas --- \n")




console.log ("\n Variabel dasar \n")

var nama = "Hai Indonesia"
console.log (nama)


console.log ("\n --- Batas --- \n")




console.log ("\n Tipe data pemrograman \n")

var teks = "Tes tulisan"
var angka = 12
var desimal = 42.23
var char = 'A'
var cek = true
var daftar = [
    "1. Toyota",
    "2. Daihatsu",
    "3. Mitsubishi",
    "4. Ford",
    "5. Mercedes Benz",
]

var detail = `

- Teks : ${teks}
- Angka : ${angka}
- Desimal : ${desimal}
- Char : ${char}
- Cek : ${cek}
- Daftar : 

`

console.log (detail)


for (a = 0; a < daftar.length; a++) {
    console.log (daftar [a])
}


console.log ("\n --- Batas --- \n")



console.log ("\n Objek \n")

var data = {
    "nama" : "John Doe",
    "asal" : "Amerika",
    "umur" : 30,
    "pekerjaan" : "Programmer",
}

console.log ("Nama :", data ["nama"])

console.log ("Asal :", data ["asal"])

console.log ("Umur :", data ["umur"])

console.log ("Pekerjaan :", data ["pekerjaan"])

console.log ("\n --- Batas --- \n")




console.log ("\n Operator dasar \n")

var x = 10
var y = 5

console.log ("Tambah =", x + y)
console.log ("Kurang =", x - y)
console.log ("Kali =", x * y)
console.log ("Bagi =", x / y)
console.log ("Modulus =", x % y)
console.log ("Pangkat =", x ** y)

console.log ("\n --- Batas --- \n")




console.log ("\n Operator Perbandingan \n")

console.log ("Hasil =", x > y)
console.log ("Hasil =", x < y)
console.log ("Hasil =", x == y)
console.log ("Hasil =", x != y)
console.log ("Hasil =", x >= y)
console.log ("Hasil =", x <= y)


console.log ("\n --- Batas --- \n")




console.log ("\n Operator Logika \n")           


console.log ("Hasil =", (x > y) && (x < y))
console.log ("Hasil =", (x > y) || (x < y))
console.log ("Hasil =", (!x))
console.log ("Hasil =", (!y))


console.log ("\n --- Batas --- \n")




console.log ("\n Switch Case 1 \n")


var nomor = 9

switch (nomor) {
    
    case 1:
        console.log ("1")
        break
        
    case 2:
        console.log ("2")
        break
        
    case 3:
        console.log ("3")
        break
        
    case 4:
        console.log ("4")
        break
        
    case 5:
        console.log ("5")
        break
        
    case 6:
        console.log ("6")
        break
        
    case 7:
        console.log ("7")
        break
        
    case 8:
        console.log ("8")
        break
        
    case 9:
        console.log ("9")
        break
        
    case 10:
        console.log ("10")
        break
        
    default:
    console.log ("Semula")
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan dasar \n")


var a = 10


if (a > 5) {
    console.log (`Besar, a = ${a}`)
}

else {
    console.log (`Kecil, a = ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Lanjutan 1 \n")


var r = 9

if (r > 5) {
    console.log (`Besar, r = ${r}`)
}

else if (r < 5) {
    console.log (`Kecil, r = ${r}`)
}

else {
    console.log (`Semula, r = ${r}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan lanjutan 2 \n")


var e = 3

if (e > 5) {
    console.log (`Besar, e = ${e}`)
}

else if (e < 5) {
    console.log (`Kecil, e = ${e}`)
}

else {
    console.log (`Sama saja, e = ${e}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 1 \n")


var r = 9
var cek = true

if (cek) {
    if (r > 5) {
        console.log (`Besar, r = ${r}`)
    }
    
    else if (r < 5) {
        console.log (`Kecil, r = ${r}`)
    }
}

else {
    console.log (`Sama saja, r = ${r}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n Percabangan Nested 2 \n")


var e = 3
var cek = true

if (cek) {
    if (e > 5) {
        console.log (`Besar, e = ${e}`)
    }
    
    else {
        console.log (`Kecil, e = ${e}`)
    }
}

else {
    console.log (`Sama saja, e = ${e}`)
}


console.log ("\n --- Batas --- \n")
