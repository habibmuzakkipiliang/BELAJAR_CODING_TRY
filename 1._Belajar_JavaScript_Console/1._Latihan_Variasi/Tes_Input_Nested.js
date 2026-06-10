// Tes aja latihan

console.log ("\n Tes aja latihan \n")


var a = Number (prompt ("1 : "))
var b = Number (prompt ("2 : "))
var c = Number (prompt ("3 : "))
var d = Number (prompt ("4 : "))


if ((a > 0) && (b > 0) && (c > 0) && (d > 0)) {
    
    if (a == b == c == d) {
        console.log ("Tes 1")
    }
    
    else if ((a == b) || (b == c) || (c == d) || (a == d)) {
        console.log ("Tes 2")
    }
    
    else {
        console.log ("Bukan Tes 1")
    }
}

else {
    console.log ("Bukan Tes 2")
}