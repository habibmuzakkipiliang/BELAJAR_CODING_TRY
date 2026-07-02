// Fungsi Error Handling

console.log ("\n Fungsi Error Handling \n")


function cekAngka (a) {
    try {
        if (a < 0) {
            throw ("Minus")
            console.log (`Angka salah ${a}`)
        }
        
        else {
            console.log (`Angka benar ${a}`)
        }
        
    }
    
    catch (Error) {
        console.log (`Gak boleh minus, a = ${a}`)
    }
}

cekAngka (-5)


console.log ("\n --- Batas --- \n")





function dasar (b) {
    try {
        if (b < 0) {
            throw ("Minus")
            console.log (`Angka Salah ${b}`)
        }
        
        else {
            console.log (`Angka benar, angka = ${b}`)
        }
    }
    
    catch (Error) {
        console.log (`Gak boleh minus, angka = ${b}`)
    }
}

dasar (10)