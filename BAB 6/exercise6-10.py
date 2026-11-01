angka_favorit = {
    "Adib": [7, 10, 21],
    "Budi": [3, 8],
    "Siti": [5, 9],
    "Andi": [2, 6, 12],
    "Rina": [4, 11]
}

for nama, angka in angka_favorit.items():
    print("\nAngka favorit", nama, ":")

    for nomor in angka:
        print("-", nomor)