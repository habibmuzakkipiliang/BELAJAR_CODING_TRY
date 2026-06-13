console.log ("\n Percabangan Dasar \n")


var a = -5

try {
    if (a < 0) {
        throw ("Gak boleh minus")
    }
    
    if (a > 5) {
        console.log (`Besar, a = ${a}`)
    }
    
    else {
        console.log (`Kecil, a = ${a}`)
    }
}

catch (Error) {
    console.log (`Gak boleh minus, a = ${a}`)
}


console.log ("\n --- batas --- \n")





console.log ("\n Percabangan Dasar 2 \n")


var b = 3

try {
    if (b < 0) {
        throw ("Gak boleh minus")
    }
    
    if (b > 5) {
        console.log (`Besar, b = ${b}`)
    }
    
    else {
        console.log (`Kecil, b = ${b}`)
    }
}

catch (Error) {
    console.log (`Gak boleh minus, b = ${b}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n Percabangan Lanjutan \n")


var es = -20

try {
    if (es < 0) {
        throw ("Gak boleh minus")
    }
    
    if (es > 5) {
        console.log (`Besar, es = ${es}`)
    }
    
    else if (es < 5) {
        console.log (`Kecil, es = ${es}`)
    }
    
    else {
        console.log (`Sama saja`)
    }
}

catch (Error) {
    console.log (`Gak boleh minus, es = ${es}`)
}


console.log ("\n --- batas --- \n")




console.log ("\n Rapor Nilai, Percabangan Ledder \n")


var nilai = -10

try {
    if (nilai < 0) {
        throw ("Gak boleh minus")
    }
    
    if (nilai >= 90) {
        console.log (`A, nilai = ${nilai}`)
    }
    
    else if (nilai >= 80) {
        console.log (`B, nilai = ${nilai}`)
    }
    
    else if (nilai >= 70) {
        console.log (`C, nilai = ${nilai}`)
    }
    
    else {
        console.log (`Biasa aja`)
    }
}

catch (Error) {
    console.log (`Gak boleh minus, nilai = ${nilai}`)
}