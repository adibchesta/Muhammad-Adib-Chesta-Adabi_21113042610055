pesanan_sandwich = ["ayam", "daging", "keju"]
sandwich_selesai = []

while pesanan_sandwich:
    sandwich = pesanan_sandwich.pop()

    print("Saya sedang membuat sandwich", sandwich)
    sandwich_selesai.append(sandwich)

print("\nSandwich yang sudah dibuat:")

for sandwich in sandwich_selesai:
    print(sandwich)
    