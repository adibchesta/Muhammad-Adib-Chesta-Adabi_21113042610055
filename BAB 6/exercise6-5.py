sungai = {
    "Nil": "Mesir",
    "Amazon": "Brasil",
    "Kapuas": "Indonesia"
}

for nama_sungai, negara in sungai.items():
    print("Sungai", nama_sungai, "berada di", negara)

print("\nNama sungai:")

for nama_sungai in sungai.keys():
    print(nama_sungai)