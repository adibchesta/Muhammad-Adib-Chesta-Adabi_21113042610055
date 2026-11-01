favorite_places = {
    "Adib": ["Bali", "Yogyakarta", "Bandung"],
    "Budi": ["Malang", "Bromo"],
    "Siti": ["Lombok", "Bali"]
}

for nama, tempat in favorite_places.items():
    print("\nTempat favorit", nama, ":")

    for lokasi in tempat:
        print("-", lokasi)