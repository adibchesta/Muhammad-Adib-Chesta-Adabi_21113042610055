def make_album(penyanyi, judul_album, jumlah_lagu=None):
    album = {
        "penyanyi": penyanyi,
        "judul_album": judul_album
    }

    if jumlah_lagu is not None:
        album["jumlah_lagu"] = jumlah_lagu

    return album


print(make_album("Tulus", "Manusia"))
print(make_album("Hindia", "Menari dengan Bayangan"))
print(make_album("Sheila On 7", "Kisah Klasik", 10))