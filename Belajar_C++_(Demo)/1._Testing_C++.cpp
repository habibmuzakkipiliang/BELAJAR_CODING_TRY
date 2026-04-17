#include <iostream>
using namespace std;

int main () {
	
	//  Tes Program C++ Sederhana 
	
	cout << "Hello World by C++ \n" << endl;
	
	
	string selamat = "Selamat kembali Habib, di Windows 11 Pro yang sudah diperbaiki mandiri di rumah selama bulan puasa 2026 (HP Elitebook 8440p, RAM 8 GB, SSD Samsung Ovo 496 GB \n";
	
	cout << selamat << endl;
	
	
	
	
	string tes = "Semangat, untuk ujian akhir sekolah dan belajar IT nya \n";
	
	cout << tes << endl;
	
	
	
	
	string tes_1 = "Semangat belajar Coding Python dan JavaScript (HTML dan CSS) \n";
	
	cout << tes_1 << endl;
	
	
	cout << "\n --- Batas --- \n" << endl;
	
	
	
	
	cout << "FANS (WOTA) IDOL & OSHI (MEMBER FAVORIT) \n" << endl;
	
	
	string idol = "Grup Idol Favorit: JKT48 | AKB48 | Rain Tree \n";
	
	cout << idol << endl;
	
	
	
	string oshi[] = {
	    
	        "1. Michie JKT48 (Utama)",
            "2. Fritzy JKT48 (Utama)",
            "3. Anindya JKT48 (Utama)",
            "4. Christy JKT48 (Utama)",
            "5. Freya JKT48",
            "6. Olla JKT48", 
            "7. Jessi JKT48",
            "8. Fiony JKT48",
            "9. Muthe JKT48",
            "10. Marsha JKT48",
            "11. Eli JKT48",
            "12. Mikaela JKT48",
            "13. Yui Oguri (AKB48)",
            "14. Endo Rino (Rain Tree)",
	    
	    };
	    
	    
	int jumlahOshi = sizeof(oshi) / sizeof(oshi[0]);
	    
	    
	for (int a = 0; a < jumlahOshi; a++) {
	    cout << oshi [a] << endl;
	}
	
	
	return 0;
}
