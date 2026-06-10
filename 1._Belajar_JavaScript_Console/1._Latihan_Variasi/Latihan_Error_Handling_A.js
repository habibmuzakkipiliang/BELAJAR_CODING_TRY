// Error Handling

console.log ("\n Error Handling \n")


try {
    var hasil = "Tes"
    console.log (hasil)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai dong")
}


console.log ("\n --- Batas -- \n")




try {
    var hasil = 10 / 0
    console.log (hasil)
}

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai dong")
}


console.log ("\n --- Batas -- \n")




try {
    hasil = 10 + 10 * 10
    console.log (hasil)
} 

catch (SyntaxError) {
    console.log ("Gagal")
}

finally {
    console.log ("Selesai dong")
}
