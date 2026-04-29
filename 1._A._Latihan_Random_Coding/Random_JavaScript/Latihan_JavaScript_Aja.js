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




var a = 10


if (a > 5) {
    console.log (`Besar, a = ${a}`)
}

else {
    console.log (`Kecil, a = ${a}`)
}


console.log ("\n --- Batas --- \n")
