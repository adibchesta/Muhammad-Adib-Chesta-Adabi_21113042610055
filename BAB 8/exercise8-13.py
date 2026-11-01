def build_profile(nama_depan, nama_belakang, **informasi):
    informasi["nama_depan"] = nama_depan
    informasi["nama_belakang"] = nama_belakang

    return informasi


profil = build_profile(
    "Adib",
    "Chesta",
    jurusan="Teknik Industri",
    universitas="UNS",
    angkatan=2026
)

print(profil)