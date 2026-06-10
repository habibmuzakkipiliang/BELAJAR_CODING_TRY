// Latihan lagi error handling

console.log ("\n Latihan lagi Error Handling \n")


function latihan () {
    
    try {
        var hasil = 10 / 2
        console.log (hasil)
    }
    
    catch (Error) {
        console.log ("Gagal")
    }
    
    finally {
        console.log ("Selesai dong")
    }
    
    
    console.log ("\n --- Batas --- \n")
    
}

latihan ()




function latihan_1 () {
    
    try {
        var j = 10 +  10
        console.log (j)
    }
    
    catch (Error) {
        console.log ("Gagal")
    }
    
    finally {
        console.log ("Selesai dong")
    }
    
    
    console.log ("\n --- Batas --- \n")
}


latihan_1 ()





function latihan_2 () {
    
    try {
        var a = 10 / 0
        console.log (a)
    }
    
    catch (Error) {
        console.log ("Gagal dong :")
    }
    
    finally {
        console.log ("Selesai dong")
    }
    
    
    console.log ("\n --- Batas --- \n")
}

latihan_2 ()




function latihan_3 () {
    
    try {
        var r = 10 / 10
        console.log (r)
    }
    
    catch (Error) {
        console.log ("Gagal")
    }
    
    finally {
        console.log ("Selesai dong")
    }
    
    
    console.log ("\n --- Batas --- \n")
}

latihan_3 ()