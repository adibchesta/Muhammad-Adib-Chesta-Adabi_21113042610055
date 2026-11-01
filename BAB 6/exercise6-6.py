bahasa_favorit = {
    "Adib": "Python",
    "Budi": "Java",
    "Siti": "Python"
}

peserta_polling = ["Adib", "Budi", "Siti", "Andi", "Rina"]

for nama in peserta_polling:
    if nama in bahasa_favorit:
        print("Terima kasih,", nama, "sudah mengikuti polling.")
    else:
        print(nama, "silakan ikuti polling.")