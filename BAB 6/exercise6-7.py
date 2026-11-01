orang1 = {
    "nama_depan": "Budi",
    "nama_belakang": "Santoso",
    "umur": 19,
    "kota": "Solo"
}

orang2 = {
    "nama_depan": "Siti",
    "nama_belakang": "Aminah",
    "umur": 20,
    "kota": "Surabaya"
}

orang3 = {
    "nama_depan": "Andi",
    "nama_belakang": "Pratama",
    "umur": 18,
    "kota": "Jakarta"
}

people = [orang1, orang2, orang3]

for orang in people:
    print("\nNama:", orang["nama_depan"], orang["nama_belakang"])
    print("Umur:", orang["umur"])
    print("Kota:", orang["kota"])