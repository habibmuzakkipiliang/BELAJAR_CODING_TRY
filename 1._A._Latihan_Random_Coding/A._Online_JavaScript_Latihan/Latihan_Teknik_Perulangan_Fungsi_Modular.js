// Teknik Perulangan Fungsi Modular

console.log ("\n Teknik Perulangan Fungsi Modular \n")

for (a = 1; a < 11; a++) {
     console.log (`Urutan ke - ${a}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Perulangan 2 \n")

for (b = 10; b < 21; b++) {
     console.log (`Urutan ke - ${b}`)
}

console.log ("\n --- Batas --- \n")




console.log ("\n For Perulangan 3 \n")

for (c = 0; c < 15; c++) {
     console.log (`Urutan ke - ${c}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n While Perulangan 1 \n")

var a = 10

while (a < 20) {
     console.log (`Urutan ke - ${a}`)
     a++
}

console.log ("\n --- Batas --- \n")




console.log ("\n While Perulangan 2 \n")

var b = 15

while (b < 26) {
     console.log (`Urutan ke - ${b}`)
     b++
}


console.log ("\n --- Batas --- \n")




console.log ("\n While Perulangan 3 \n")

var c = 10

while (c < 26) {
     console.log (`Urutan ke - ${c}`)
     c++
}


console.log ("\n --- Batas --- \n")



console.log ("\n While Perulangan 4 \n")

var d = 10

while (d > 0) {
     console.log (`Hitung mundur, d = ${d}`)
     d--
}


console.log ("\n --- Batas --- \n")




console.log ("\n For Nested \n")

for (a = 0; a < 6; a++) {
     for (b = 0; b < 6; b++) {
          console.log (`Luar : ${a}, Dalam : ${b}`)
     }
}


console.log ("\n --- Batas --- \n")




console.log ("\n Teknik Iterasi For (Oshi saya) \n")

oshi = [
    "1. Michie JKT48 (UTAMA)",
    "2. Gracie JKT48 (UTAMA)",
    "3. Fritzy JKT48 (UTAMA)",
    "4. Lily JKT48 (UTAMA)",
    "5. Anindya JKT48 (UTAMA)",
    "6. Christy JKT48 (UTAMA)",
    "7. Freya JKT48 (UTAMA)",
    "8. Olla JKT48",
    "9. Jessi JKT48",
    "10. Fiony JKT48",
    "11. Muthe JKT48",
    "12. Marsha JKT48",
    "13. Eli JKT48",
    "14. Mikaela JKT48",
    "15. Ekin JKT48",
]

for (a = 0; a < oshi.length; a++) {
     console.log (oshi [a])
}


console.log ("\n --- Batas --- \n")




console.log ("\n Teknik Iterasi Kontrol Continue \n")

for (a = 1; a < 15; a++) {
     if (a == 5) {
          continue
     }

     console.log (`Urutan ke - ${a}`)
}

console.log ("\n --- Batas --- \n")



console.log ("\n Teknik Iterasi Kontrol Break \n")

for (b = 1; b < 25; b++) {
     if (b == 10) {
          break
     }

     console.log (`Urutan ke - ${b}`)
}


console.log ("\n --- Batas --- \n")




console.log ("\n List Iterasi Kontrol Continue \n")

var buah = [
     "Apel", 
     "Naga", 
     "Melon", 
     "Semangka", 
     "Nangka",
     "Jeruk",
     "Strawberi",
     "Salak",
     
     ]

for (var a of buah) {
     if (a == "Melon") {
          continue
     }

     console.log (a)
}


console.log ("\n --- Batas --- \n")




console.log ("\n List Iterasi Kontrol Break \n")

var buah = [
     "Apel", 
     "Naga", 
     "Melon", 
     "Semangka", 
     "Nangka",
     "Jeruk",
     "Strawberi",
     "Salak",
     
     ]

for (var b of buah) {
     if (b == "Melon") {
          break
     }

     console.log (b)
} 


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dasar \n")

function tan () {
     console.log ("Hello World")
}

tan ()


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan parameter 1 \n")

function yun (nama) {
     console.log (`Halo nama saya ${nama}, dari Jakarta Utara`)
}

yun ("Fakhri")
yun ("Hayyan")
yun ("Rayyan")
yun ("Dimas")
yun ("Mido")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Parameter 2 \n")

function tur (nama, asal, suku, budaya) {
     console.log (`Halo nama saya ${nama}, asal dari ${asal}, suku saya adalah ${suku}, dan budaya saya adalah ${budaya}`)
}

tur ("Frederick", "Jerman", "Jermanik Barat", "Jerman")
tur ("Louis", "Prancis", "Prancis", "Prancis")
tur ("Graciantsya", "Palembang", "Tionghoa", "Tionghoa")
tur ("Eri Erria", "Singkawang", "Tionghoa", "Tionghoa")


console.log ("\n --- Batas --- \n")



console.log ("\n Fungsi dengan Parameter \n")

function run (nama) {
     console.log (`Halo saya ${nama} dari Jakarta`)
}

run ("Rummer")
run ("Santer")
run ("Rus")
run ("Far")


console.log ("\n --- Batas --- \n")




console.log ("\n Fungsi dengan Return \n")

function tambah (x, y) {
     return x + y
}

hasil = tambah (10, 10)
console.log ("Tambah =", hasil)

console.log ("\n --- Batas --- \n")