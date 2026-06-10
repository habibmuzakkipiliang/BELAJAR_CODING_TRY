// Fungsi Error Handling Spesial Member JKT48

console.log ("\n Fungsi Error Handling Spesial Member JKT48 \n")


function bonus () {
    
    try {
        var hasil = 10 / 0
        console.log ("Hasil =", hasil)
    }
    
    catch (SyntaxError) {
        console.log ("Gagal")
    }
    
    finally {
        console.log ("Selesai dong")
    }
    
    
    console.log ("\n --- Batas --- \n")
}

bonus ()




function error_e () {
   
   try {
       var hasil = 20 / 0
       console.log ("Hasil =", hasil)
   } 
   
   catch (SyntaxError) {
       console.log ("Gagal")
   }
   
   finally {
       console.log ("Selesai dong")
   }
   
   
   console.log ("\n --- Batas --- \n")

}

error_e ()




function error_k () {
    
    try {
        var hasil = 100 / 0
        console.log ("Hasil =", hasil)
    }
    
    catch (SyntaxError) {
        console.log ("Gagal")
    }
    
    finally {
        console.log ("Selesai dong")
    }
    
    
    console.log ("\n --- Batas --- \n")
}

error_k ()




function error () {
    
    try {
        var hasil = "Michie JKT48"
        console.log ("Hasil =", hasil)
    }
    
    catch (SyntaxError) {
        console.log ("Gagal")
    }
    
    finally {
        console.log ("Selesai dong")
    }
    
    
    console.log ("\n --- Batas --- \n")
    
}

error ()




function error_a () {
    
    try {
        var hasil = "Michie dan Fritzy JKT48"
        console.log ("Hasil =", hasil)
    }
    
    catch (SyntaxError) {
        console.log ("Gagal")
    }
    
    finally {
        console.log ("Selesai dong")
    }
    
    
    console.log ("\n --- Bats --- \n")
}

error_a ()




function error_b () {
    
    try {
        var hasil = "Freya dan Jessi JKT48"
        console.log ("Hasil =", hasil)
    }
    
    catch (SyntaxError) {
        console.log ("Gagal")
    }
    
    finally {
        console.log ("Selesai dong")
    }
    
    
    console.log ("\n --- Batas --- \n")
}

error_b ()