print("[KELAS G INFORMATIKA 21]")
print("<=== MENGHITUNG LUAS & VOLUME ===>")
print("= PBO =")

class Luas:
    def _init_(self):
        self.satu = angka1
        self.dua = angka2
    def persegi_panjang(self,):
        print(self.satu * self.dua)
    def lingkaran(self):
        print(self.satu * self.dua * self.dua)
    def segitiga(self):
        print(1/2 * (self.satu * self.dua))

class Volume:
    def _init_(self):
        self.satu = angka1
        self.dua = angka2
        self.tiga = angka3
    def kubus(self):
        print(self.satu**3)
    def balok(self):
        print(self.satu*self.dua*self.tiga)
    def tabung(self):
        print(self.satu*(self.dua**2)*self.tiga)
    
while True:
    print("\n1. hitung Luas \n2. hitung Volume \n3. Keluar")
    pilihan = int(input("Masukkan Pilihan : "))
    if pilihan == 1:
            print("\n> Persegi \n> Lingkaran \n> Segitiga \n> Kembali")
            pilihan = int(input("Masukkan Pilihan : "))
            if pilihan == 1:
                angka1 = float(input("Masukkan panjang persegi : "))
                angka2 = float(input("Masukkan lebar persegi : "))
                hasil = Luas()
                hasil.persegi_panjang()
                print("masih ingin lanjut?")
                print("-ya- untuk lanjut & -Tidak- untuk break")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break             
            elif pilihan == 2:
                angka1 = 3.14
                angka2 = float(input("Masukkan Jari-Jari Lingkaran : "))
                hasil = Luas()
                hasil.lingkaran()
                print("masih ingin lanjut?")
                print("-ya- untuk lanjut & -Tidak- untuk break")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            elif pilihan == 3:
                angka1 = float(input("Masukkan Tinggi Segitiga : "))
                angka2 = float(input("Masukkan Alas Segitiga : "))
                hasil = Luas()
                hasil.segitiga()
                print("masih ingin lanjut?")
                print("-ya- untuk lanjut & -Tidak- untuk break")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            elif pilihan == 4:
                break
            else:
                print("Perintah Tidak Ditemukan")
    elif pilihan == 2:
            print("\n> Kubus \n> Tabung \n> Kembali")
            pilihan = int(input("Masukkan Pilihan : "))
            if pilihan == 1:
                angka1 = float(input("Masukkan panjang rusuk : "))
                angka2 = 0
                angka3 = 0
                hasil = Volume()
                hasil.kubus()
                print("masih ingin lanjut?")
                print("-ya- untuk lanjut & -Tidak- untuk break")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break                                
            elif pilihan == 3:
                angka1 = 3.14
                angka2 = float(input("Masukkan Jari-Jari Lingkaran : "))
                angka3 = float(input("Masukkan Tinggi Tabung : "))
                hasil = Volume()
                hasil.tabung()
                print("masih ingin lanjut?")
                print("-ya- untuk lanjut & -Tidak- untuk break")
                tnya = input(": ")
                if tnya == "ya" :
                    print(pilihan)
                else:
                    break            
            elif pilihan == 5:
                break
            else:
                print("PERMINTAAN TIDAK DITEMUKAN")

    elif pilihan == 3:
        break
    else:
        print("PERMINTAAN TIDAK DITEMUKAN")