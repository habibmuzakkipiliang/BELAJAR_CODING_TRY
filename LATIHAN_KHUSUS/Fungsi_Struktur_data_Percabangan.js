// Struktur data

var data = [
     "Halo Dunia",
     "Halo World",
     "Halo Fets",
     "Halo Jundy",
     "Halo Gundy",
     "Halo Rundy",
]

for (a = 0; a < data.length; a++) {
     console.log (data [a])
}


console.log ("\n --- batas --- \n")




// Array 1

var fer = [
     "Halo Dunk",
     "Halo Dri",
     "Halo dun",
     "Halo Der",
     "Halo Wer",
     "Halo Qwe",
     "Halo Ban",
     "Halo Dun"
]

for (b = 0; b < fer.length; b++) {
     console.log (fer [b])
}


console.log ("\n --- batas --- \n")



// For dasar

var der = [
     "Halo Just",
     "Halo DUst",
     "Halo Ampe",
     "Halo Guntime",
     "Halo Goodtime",
]

for (c = 0; c < der.length; c++) {
     console.log (der [c])
}


console.log ("\n --- batas --- \n")



// Array + Manipulasi data

var fer =  [
     "Halo China",
     "Halo Taiwan",
     "Halo Thailand",
     "Halo Malaysia",
     "Halo Indonesia",
     "Halo Brunei",
     "Halo Timor",
     "Halo Papua"
]

fer.push ("Halo Kamboja")
fer.push ("Halo Yen")
fer.push ("Halo Fer")
fer.push ("Halo Guntime")
fer.push ("Halo Der")


for (f of fer) {
     if (f == "Halo Fer") {
          continue
     }

     console.log (f)
}

console.log ("\n --- batas --- \n")




// Array 3

var ter = [
     "Halo Inkong",
     "Halo Rankong",
     "Halo Bust",
     "Halo Runway",
]

for (f = 0; f < ter.length; f++) {
     console.log (ter [f])
}


console.log ("\n --- batas --- \n")




// Fungsi dasar

function dasar () {
     console.log ("Hello World")
}

dasar ()


console.log ("\n --- batas --- \n")




// Function dengan parameter

function nama (sapa) {
     console.log (`Halo saya ${sapa} dari Jakarta Utara`)
}

nama ("Sapa")
nama ("Hayyan")
nama ("Vayyan")
nama ("Yun")


console.log ("\n --- batas --- \n")




// Fungsi return

function dek (sapa) {
     return `Halo saya ${sapa} dari Jakarta Utara`
}

console.log (dek ("Hayyan"))
console.log (dek ("Fayyan"))
console.log (dek ("Fayyan"))
console.log (dek ("Ron"))
console.log (dek ("jon"))
console.log (dek ("Koper"))



console.log ("\n --- batas --- \n")




// Fungsi return dengan operator dasar

function tambah (x, y) {
     return x + y
}


function kurang (x, y) {
     return x - y
}


function kali (x, y) {
     return x * y
}


function bagi (x, y) {
     return x / y
}


console.log ("Hasil tambah =", tambah (10, 3))
console.log ("Hasil kurang =", kurang (10, 5))
console.log ("Hasil kali =", kali (10, 10))
console.log ("Hasil bagi =", bagi (10, 2))


console.log ("\n --- batas --- \n")



// Error Handling

try {
     var a = 10 / mon
     console.log (a)
}

catch (Error) {
     console.log ("Gagal")
}

finally {
     console.log ("Selesai")
}


console.log ("\n --- batas --- \n")



// Error Handling

try {
     var b = 10 + 10
     console.log (b)
}

catch (Error) {
     console.log ("Gagal")
}

finally {
     console.log ("Selesai")
}


console.log ("\n --- batas --- \n")




// Fungsi dengan percabangan

function hal (d) {

     if (d >= 5) {
          console.log (`Angka d besar, angka d = ${d}`)
     }

     else {
          console.log (`Angka d kecil, angka d = ${d}`)
     }
}

hal (10)
hal (8)
hal (3)
hal (2)
hal (1)


console.log ("\n --- batas --- \n")