from pathlib import Path

# Mengambil lokasi folder tempat file Python berada
folder = Path(__file__).parent

files = ["cats.txt", "dogs.txt"]

for filename in files:
    path = folder / filename

    try:
        contents = path.read_text()
        print(f"\nIsi file {filename}:")
        print(contents)

    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan!")