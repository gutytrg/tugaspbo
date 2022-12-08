print("Kalkulator Luas")

while True:
    print("Menu : " + "\n 1. Persegi" + "\n 2. Lingkaran" + "\n 3. Segitiga" + "\n 4. Keluar")
    pilihan = input("Masukkan Pilihan Anda : ")
    if pilihan == '1':
        while True:
            Sisi = float(input("Masukkan Panjang Panjang : "))
            Luas_Persegi = Sisi * Sisi
            print("Luas Persegi : ")
            print(Luas_Persegi)
            konfirmasi = input("Masih ingin menghitung luas persegi? (y/n) :")
            if konfirmasi == "y":
                print("")
            else:
                break
    elif pilihan == '2':
        while True:
            Jari = float(input("Masukkan Jari-Jari Lingkaran : "))
            Luas_Lingkaran = 3.14*Jari*Jari
            print("Luas Lingkaran : ")
            print(Luas_Lingkaran)
            konfirmasi = input("Masih ingin menghitung luas lingkaran? (y/n) :")
            if konfirmasi == "y":
                print("")
            else:
                break
    elif pilihan == '3':
        while True:
            Alas = float(input("Masukkan Panjang Alas : "))
            Tinggi = float(input("Masukkan Tinggi Segitiga : "))
            Luas_Segitiga = 1/2*(Alas*Tinggi)
            print("Luas Segitiga : ")
            print(Luas_Segitiga)
            konfirmasi = input("Masih ingin menghitung luas segitiga? (y/n) :")
            if konfirmasi == "y":
                print("")
            else:
                break
    elif pilihan == '4':
        break
    else:
        print("Perintah Tidak Dapat di Lakukan")
        konfirmasi = input("Tekan tombol apapun untuk lanjut.")