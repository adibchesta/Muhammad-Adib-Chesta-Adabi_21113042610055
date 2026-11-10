from pathlib import Path
import json

favorite_number = input("Masukkan angka favorit kamu: ")

path = Path("favorite_number.json")
contents = json.dumps(favorite_number)
path.write_text(contents)

print("Angka favorit berhasil disimpan!")