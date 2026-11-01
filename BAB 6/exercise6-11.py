cities = {
    "Jakarta": {
        "negara": "Indonesia",
        "populasi": "Sekitar 10 juta jiwa",
        "fakta": "Merupakan ibu kota Indonesia pada masa lalu dan pusat ekonomi nasional"
    },

    "Tokyo": {
        "negara": "Jepang",
        "populasi": "Sekitar 14 juta jiwa di wilayah administrasi Tokyo",
        "fakta": "Terkenal dengan transportasi umum yang maju"
    },

    "Paris": {
        "negara": "Prancis",
        "populasi": "Sekitar 2 juta jiwa di wilayah kota administratif",
        "fakta": "Terkenal dengan Menara Eiffel"
    }
}

for nama_kota, informasi in cities.items():
    print("\nNama kota:", nama_kota)
    print("Negara:", informasi["negara"])
    print("Populasi:", informasi["populasi"])
    print("Fakta:", informasi["fakta"])