#include <iostream>
using namespace std;

int main () {
	
	
	cout << "\n Bikin Hello World \n" << endl;

	
	cout << "Hello World" << endl;
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n Tipe data Pemrograman \n" << endl;
	
	int angka = 12;
	float desimal = 34.24;
	string teks = "Halo Dunia ku";
	char huruf ='A';
	bool cek = true;
	
	
	cout << "Angka : " << angka << endl;
	cout << "Desimal : " << desimal << endl;
	cout << "Teks : " << teks << endl;
	cout << "Huruf : " << huruf << endl;
	cout << "Cek : " << cek << endl;
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n Variabel dasar \n" << endl;
	
 	
	string nama = "Halo Indonesia";
	
	cout << "Nama : " << nama << endl;
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n Operator dasar \n" << endl;
	
	
	int x = 10;
	int y = 5;
	
	
	cout << "Tambah = " << x + y << endl;
	cout << "Kurang = " << x - y << endl;
	cout << "Kali = " << x * y << endl;
	cout << "Pangkat = " << x / y << endl;
	cout << "Modulus = " << x % y << endl;
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n Operator Perbandingan \n" << endl;
	
	
	cout << "Hasil = " << (x > y) << endl;
	cout << "Hasil = " << (x < y) << endl;
	cout << "Hasil = " << (x <= y) << endl;
	cout << "Hasil = " << (x >= y) << endl;
	cout << "Hasil = " << (x == y) << endl;
	cout << "Hasil = " << (x != y) << endl;
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n Operator Logika \n" << endl;
	
	
	
	cout << "Hasil = " << ((x < y) && (x > y)) << endl;
	cout << "Hasil = " << ((x > y) || (x > y)) << endl;
	cout << "Hasil = " << (!x) << endl;
	cout << "Hasil = " << (!y) << endl;
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n Percabangan Dasar \n" << endl;
	
	int skor_1 = 9;
	
	if (skor_1 > 5) {
		cout << "Besar" << endl;
	}
	
	else {
		cout << "Kecil" << endl;
	}
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	
	cout << "\n Percabangan dasar 2 \n" << endl;
	
	int skor_2 = 3;
	
	if (skor_2 > 5) {
		cout << "Besar" << endl;
    }
    
    else {
    	cout << "Kecil" << endl;
	}
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n Percabangan Lanjutan \n" << endl;
	
	
	int skor_3 = 9;
	
	if (skor_3 > 5) {
		cout << "Besar" << endl;
	}
	
	else if (skor_3 < 5) {
		cout << "Kecil" << endl;
	}
	
	else {
		cout << "Sama saja" << endl;
	}
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n Percabangan Lanjutan 2 \n" << endl;
	
	int skor_4 = 3;
	
	if (skor_4 > 5) {
		cout << "Besar" << endl;
	}
	
	else if (skor_4 < 5) {
		cout << "Kecil" << endl;
	}
	
	else {
		cout << "Sama saja" << endl;
	}
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n Percabangan Nested 1 \n" << endl;
	
	int skor_5 = 9;
	bool cek_1 = true;
	
	if (cek_1) {
		if (skor_5 > 5) {
			cout << "Besar" << endl;
		}
		
		else if (skor_5 < 5) {
			cout << "Kecil" << endl;
		}
	}
	
	else {
		cout << "Sama saja" << endl;
	}
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n Percabangan Nested 2 \n" << endl;
	
	
	int skor_6 = 3;
	bool cek_2 = true;
	
	if (cek_2) {
		if (skor_6 > 5) {
			cout << "Besar" << endl;
		}
		
		else {
			cout << "Kecil" << endl;
		}
	}
	
	else {
		cout << "Sama saja" << endl;
	}
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n Percabangan Nested, usia produktif manusia \n" << endl;
	
	
	int usia = 19;
	bool cek_3 = true;
	
	if (cek_3) {
		if ((usia >= 15) && (usia <= 64))  {
			cout << "Sudah memasuki usia produktif" << endl;
		}
		
		else if (usia > 64) {
			cout << "Sudah lanjut usia" << endl;
		}
		
		else {
			cout << "Belum memasuki usia produktif" << endl;
		}
	}
	
	else {
		cout << "Masih kecil usianya" << endl;
	}
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n Percabangan Nested, usia daftar member JKT48 tahun 2026 \n" << endl;
	
	
	int usia_2 = 19;
	bool cek_4 = true;
	
	if (cek_4) {
		if ((usia_2 >= 13) && (usia <= 17)) {
			cout << "Sudah boleh daftar JKT48" << endl;
		}
		
		else if (usia_2 > 17) {
			cout << "Sudah lebih dari cukup untuk daftar JKT48" << endl;
		}
		
		else {
			cout << "Belum masih dibawah umur untuk daftar JKT48" << endl;
		}
	}
	
	else {
		cout << "Di lain waktu daftar JKT48" << endl;
	}
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n For dasar \n" << endl;
	
	
	for (int a = 0; a < 20; a++) {
		cout << "Urutan ke - " << a <<  endl;
	}	
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	cout << "\n For dasar 1 \n" << endl;
	
	
	for (int b = 0; b < 20; b++) {
		cout << "Urutan ke - " << b << endl;
	}
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	cout << "\n While dasar \n" << endl;
	
	int urut = 5;
	
	while (urut < 16) {
		cout << "Urutan ke - " << urut << endl;
		urut++;
	}
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n While dasar 1 \n" << endl;
	
	int urut_1 = 16;
	
	while (urut_1 < 26) {
		cout << "Urutan ke - " << urut_1 << endl;
		urut_1++;
	}
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	cout << "\n Do While dasar \n" << endl;
	
	int nilai = 15;
	
	do {
		cout << "Urutan ke - " << nilai << endl;
		nilai++;
	} while (nilai < 30);
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n Do While 1 dasar \n" << endl;
	
	
	int nilai_2 = 20;
	
	do {
		cout << "Urutan ke - " << nilai_2 << endl;
		nilai_2++;
	} while (nilai_2 < 30);
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "\n For Nested \n" << endl;
	
	
	for (int x = 0; x < 5; x++) {
		for (int y = 0; y < 5; y++) {
			for (int z = 0; z < 5; z++) {
				cout << "Urutan ke - " << x << "Urutan ke - " << y << "Urutan ke - " << z << endl;
			}
		}
	}
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	cout << "\n For Nested \n" << endl;
	
	
	for (int k = 0; k < 10; k++) {
		for (int h = 0; h < 10; h++) {
			for (int t = 0; t < 10; t++) {
				cout << "Urutan ke - " << k << "Urutan ke - " << h << "Urutan ke - " << t << endl;
			}
		}
	}
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	return 0;
}