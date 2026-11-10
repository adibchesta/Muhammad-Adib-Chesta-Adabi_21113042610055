while True:
    print("\nKalkulator Penjumlahan")
    print("Ketik 'q' untuk keluar.")

    angka1 = input("Masukkan angka pertama: ")

    if angka1.lower() == "q":
        break

    angka2 = input("Masukkan angka kedua: ")

    if angka2.lower() == "q":
        break

    try:
        hasil = int(angka1) + int(angka2)
        print(f"Hasil penjumlahan: {hasil}")

    except ValueError:
        print("Maaf, masukkan angka yang benar!")