from pathlib import Path
import json

path = Path("favorite_number.json")

if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)

    print(f"Aku tahu angka favorit kamu! Angkanya adalah {favorite_number}.")

else:
    favorite_number = input("Masukkan angka favorit kamu: ")

    contents = json.dumps(favorite_number)
    path.write_text(contents)

    print("Angka favorit berhasil disimpan!")