pesanan_sandwich = [
    "ayam",
    "pastrami",
    "daging",
    "pastrami",
    "keju",
    "pastrami"
]

sandwich_selesai = []

print("Maaf, persediaan pastrami sedang habis.")

while "pastrami" in pesanan_sandwich:
    pesanan_sandwich.remove("pastrami")

while pesanan_sandwich:
    sandwich = pesanan_sandwich.pop()

    print("Saya sedang membuat sandwich", sandwich)
    sandwich_selesai.append(sandwich)

print("\nSandwich yang selesai dibuat:")

for sandwich in sandwich_selesai:
    print(sandwich)