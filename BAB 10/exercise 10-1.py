from pathlib import Path

path = Path("learning_python.txt")

# Membaca seluruh isi file
contents = path.read_text()
print(contents)

print("\nMembaca file per baris:")

# Membaca file per baris
for line in contents.splitlines():
    print(line)