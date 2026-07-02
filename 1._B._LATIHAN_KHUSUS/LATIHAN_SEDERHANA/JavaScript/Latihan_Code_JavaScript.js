console.log("Hello World");

console.log("\n --- Batas --- \n");

var teks = "Halo Dunia";
console.log(teks);

var angka = 12;
console.log(angka);

var desimal = 3.13;
console.log(desimal);

console.log("\n --- Batas --- \n");

console.log("\n Tipe data pemrograman \n");

var nama = "Habib";
var angka = 12;
var desimal = 3.14;
var cek = true;
var char = "A";
var kosong = null;

var detail = `
- Nama     : ${nama}
- Angka    : ${angka}
- Desimal  : ${desimal}
- Boolean  : ${cek}
- Char     : ${char}   
- Kosong   : ${kosong}
`;

console.log(detail);

console.log("\n --- Batas --- \n");

console.log("\n Fungsi dengan kalkulator \n");

function tambah(a, b) {
  return a + b;
}

function kurang(x, y) {
  return x - y;
}

function kali(k, l) {
  return k * l;
}

function bagi(m, n) {
  return m / n;
}

function pangkat(m, u) {
  return m ** u;
}

function modulus(m, n) {
  return m % n;
}

var hasil_1 = tambah(10, 5);
var hasil_2 = kurang(15, 5);
var hasil_3 = kali(10, 5);
var hasil_4 = bagi(10, 5);
var hasil_5 = pangkat(10, 5);
var hasil_6 = modulus(10, 5);

var detail = `
- Hasil tambah  : ${hasil_1}
- Hasil kurang  : ${hasil_2}
- Hasil kali    : ${hasil_3}
- Hasil bagi    : ${hasil_4}
- Hasil pangkat : ${hasil_5}
- Hasil modulus : ${hasil_6}
`;

console.log(detail);

console.log("\n --- Batas --- \n");

console.log("\n Fungsi dengan Rumus bangun datar \n");

console.log("\n Luas Persegi \n");

function persegi(s) {
  return s * s;
}

var hasil_a = persegi(5);
console.log(hasil_a);

console.log("\n --- Batas --- \n");

console.log("\n Luas Persegi Panjang \n");

function persegi_panjang(p, l) {
  return p * l;
}

var hasil_b = persegi_panjang(5, 10);
console.log(hasil_b);

console.log("\n --- Batas --- \n");

console.log("\n Luas Segitiga \n");

function segitiga(a, t) {
  return (a * t) / 2;
}

var hasil_c = segitiga(5, 10);
console.log(hasil_c);

console.log("\n --- Batas --- \n");

console.log("\n Luas Lingkaran \n");

function lingkaran(phi, r) {
  return phi * r * r;
}

var hasil_d = lingkaran(3.14, 5);
console.log(hasil_d);

console.log("\n --- Batas --- \n");

console.log("\n Luas layang-layang \n");

function layang_layang(d1, d2) {
  return (d1 * d2) / 2;
}

var hasil_e = layang_layang(5, 10);
console.log(hasil_e);

console.log("\n --- Batas --- \n");
