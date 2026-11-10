from pathlib import Path

path = Path("guest_book.txt")

while True:
    name = input("Masukkan nama kamu (ketik 'quit' untuk berhenti): ")

    if name.lower() == "quit":
        break

    reason = input("Kenapa kamu suka pemrograman? ")

    with path.open("a") as file:
        file.write(f"{name}: {reason}\n")

    print("Jawaban berhasil disimpan!\n")