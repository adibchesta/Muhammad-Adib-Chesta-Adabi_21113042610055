mahasiswa = {
    "nama": "Adib",
    "umur": 19,
    "jurusan": "Teknik Industri",
    "universitas": "UNS",
    "semester": 1,
    "hobi": ["Bermain game", "Olahraga"],
    "cita_cita": "baggain mama sama papa"
}

print("===== DATA MAHASISWA =====")
print("Nama       :", mahasiswa["nama"])
print("Umur       :", mahasiswa["umur"])
print("Jurusan    :", mahasiswa["jurusan"])
print("Universitas:", mahasiswa["universitas"])
print("Semester   :", mahasiswa["semester"])
print("Cita-cita  :", mahasiswa["cita_cita"])

print("Hobi:")
for hobi in mahasiswa["hobi"]:
    print("-", hobi)