console.log ("\n Fungsi dengan Percabangan Dasar \n")

function run (j) {
    
    if (j >= 5) {
        console.log (`Besar, angka j = ${j}`)
    }
    
    else {
        console.log (`Kecil, angka j = ${j}`)
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




console.log ("\n Fungsi dengan Percabangan Lanjutan \n")

function er (w) {
    
    if (w >= 8) {
        console.log (`Besar, angka w = ${w}`)
    }
    
    else if (w >= 5) {
        console.log (`Tengah, angka w = ${w}`)
    }
    
    else {
        console.log (`Kecil, angka w = ${w}`)
    }
}

er (10)
er (9)
er (8)
er (7)
er (6)
er (5)
er (4)
er (3)
er (2)
er (1)


console.log ("\n --- batas --- \n")




console.log ("\n Nested 1 \n")

function wer (s) {
    
    cek = true
    
    if (s >= 5) {
        if (cek) {
            console.log (`Besar, angka s = ${s}`)
        }
    }
    
    else {
        console.log (`Kecil, angka s = ${s}`)
    }
}

wer (10)
wer (9)
wer (8)
wer (7)
wer (6)
wer (5)
wer (4)
wer (3)
wer (2)
wer (1)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan pembagian nilai rapor \n")

function rapor (d) {
    
    if (d >= 90) {
        console.log (`A, nilai = ${d}`)
    }
    
    else if (d >= 80) {
        console.log (`B, nilai = ${d}`)
    }
    
    else if (d >= 70) {
        console.log (`C, nilai = ${d}`)
    }
    
    else if (d >= 60) {
        console.log (`D, nilai = ${d}`)
    }
    
    else if (d >= 50) {
        console.log (`E, nilai = ${d}`)
    }
    
    else {
        console.log (`Jelek, nilai = ${d}`)
    }
}

rapor (95)
rapor (90)
rapor (80)
rapor (70)