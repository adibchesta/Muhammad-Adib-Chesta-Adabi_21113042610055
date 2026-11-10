from pathlib import Path
import json

path = Path(__file__).parent / "favorite_number.json"
contents = path.read_text()

favorite_number = json.loads(contents)

print(f"Aku tahu angka favorit kamu! Angkanya adalah {favorite_number}.")