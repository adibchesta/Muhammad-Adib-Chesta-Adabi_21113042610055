jawaban_liburan = {}

while True:
    nama = input("Siapa nama kamu? ")
    tempat = input("Ke mana tempat liburan impianmu? ")

    jawaban_liburan[nama] = tempat

    ulangi = input("Apakah ingin mengizinkan orang lain menjawab? (ya/tidak): ")

    if ulangi.lower() == "tidak":
        break

print("\n===== HASIL POLLING =====")

for nama, tempat in jawaban_liburan.items():
    print(nama, "ingin berlibur ke", tempat)