pengguna_saat_ini = ['Adib', 'Budi', 'Citra', 'Dina', 'Eka']

pengguna_baru = ['adib', 'Fajar', 'Gita', 'budi', 'Hana']

pengguna_saat_ini_kecil = []

for nama in pengguna_saat_ini:
    pengguna_saat_ini_kecil.append(nama.lower())

for nama in pengguna_baru:
    if nama.lower() in pengguna_saat_ini_kecil:
        print(f"Nama '{nama}' sudah digunakan. Silakan pilih nama lain.")
    else:
        print(f"Nama '{nama}' masih tersedia.")