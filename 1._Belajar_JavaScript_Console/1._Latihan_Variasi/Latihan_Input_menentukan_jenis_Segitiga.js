// Program menentukan jenis segitiga 

console.log ("\n Program menentukan jenis segitiga \n")


var a = Number (prompt ("Sisi 1 : "))
var b = Number (prompt ("Sisi 2 : "))
var c = Number (prompt ("Sisi 3 : "))


if ((a + b > c) && (a + c > b) && (b + c > a)) {
    
    if ((a == b) && (b == c)) {
        console.log ("Segitiga sama sisi")
    }
    
    else if ((a == b) || (b == c) || (a == c)) {
        console.log ("Segitiga sama kaki")
    }
    
    else {
        console.log ("Segitiga Sembarang")
    }
}

else {
    console.log ("Bukan segitiga")
}