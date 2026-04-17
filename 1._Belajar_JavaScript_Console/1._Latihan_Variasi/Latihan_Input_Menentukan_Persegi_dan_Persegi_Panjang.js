// Program menentukan bentuk bangun datar (2D)

console.log ("\n Program menentukan bentuk bangun datar (2D) \n")


var a = Number (prompt ("Sisi 1 : "))
var b = Number (prompt ("Sisi 2 : "))
var c = Number (prompt ("Sisi 3: "))
var d = Number (prompt ("Sisi 4 : "))


if ((a > 0) && (b > 0) && (c > 0) && (d > 0)) {
    
    if (a == b == c == d) {
        console.log ("Persegi")
    }
    
    else if ((a == c && b == d) || (a == b && c == d) || (a == d && a == c)) {
        console.log ("Persegi panjang")
    }
    
    else {
        console.log ("Bentuk lain")
    }
}

else {
    console.log ("Gak boleh negatif dan 0")
}