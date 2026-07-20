console.log ("\n Bikin Program JavaScript \n")


console.log ("\n Switch Case 1 \n")

function der (s) {
    
    switch (s) {
        
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
            
        default:
        console.log ("Angka lain")
    }
}


der (1)
der (2)
der (3)
der (4)
der (5)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan Percabangan Dasar \n")

function er (k) {
    
    if (k >= 5) {
        console.log (`Besar, angka k = ${k}`)
    }
    
    else {
        console.log (`Kecil, angka k = ${k}`)
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




console.log ("\n Fungsi dengan Percabangan Lanjutan \n")

function pe (e) {
    
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

pe (10)
pe (9)
pe (8)
pe (7)
pe (6)
pe (5)
pe (4)
pe (3)
pe (2)
pe (1)


console.log ("\n --- batas --- \n")




console.log ("\n Fungsi dengan percabangan nilai rapor \n")

function rapor (t) {
    
    if (t >= 90) {
        console.log (`A, nilai = ${t}`)
    }
    
    else if (t >= 80) {
        console.log (`B, nilai = ${t}`)
    }
    
    else if (t >= 70) {
        console.log (`C, nilai = ${t}`)
    }
    
    else if (t >= 60) {
        console.log (`D, nilai = ${t}`)
    }
    
    else if (t >= 50) {
        console.log (`E, nilai = ${t}`)
    }
    
    else {
        console.log (`Jelek amat, nilai = ${t}`)
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




console.log ("\n Fungsi dengan percabangan Nested 1 \n")

function fun (n) {
    
    cek = true
    
    if (n >= 5) {
        if (cek) {
            console.log (`Besar, angka n = ${n}`)
        }
    }
    
    else {
        console.log (`Kecil, angka n = ${n}`)
    }
}

fun (10)
fun (9)
fun (8)
fun (7)
fun (6)
fun (5)
fun (4)
fun (3)
fun (2)
fun (1)