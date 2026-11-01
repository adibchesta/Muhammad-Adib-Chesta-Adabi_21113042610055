hewan1 = {
    "jenis": "Kucing",
    "pemilik": "Adib"
}

hewan2 = {
    "jenis": "Anjing",
    "pemilik": "Budi"
}

hewan3 = {
    "jenis": "Kelinci",
    "pemilik": "Siti"
}

pets = [hewan1, hewan2, hewan3]

for hewan in pets:
    print("Jenis hewan:", hewan["jenis"])
    print("Pemilik:", hewan["pemilik"])
    print()