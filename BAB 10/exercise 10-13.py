from pathlib import Path
import json

path = Path("user_dictionary.json")

user = {
    "nama": input("Masukkan nama: "),
    "umur": input("Masukkan umur: "),
    "kota": input("Masukkan kota asal: ")
}

contents = json.dumps(user)
path.write_text(contents)

# Membaca kembali data
stored_user = json.loads(path.read_text())

print("\nInformasi yang berhasil disimpan:")
print(f"Nama: {stored_user['nama']}")
print(f"Umur: {stored_user['umur']}")
print(f"Kota: {stored_user['kota']}")