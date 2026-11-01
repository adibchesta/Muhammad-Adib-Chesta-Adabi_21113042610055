def make_album(penyanyi, judul_album):
    return {
        "penyanyi": penyanyi,
        "judul_album": judul_album
    }


while True:
    print("\nMasukkan informasi album.")
    print("Ketik 'q' untuk berhenti.")

    penyanyi = input("Nama penyanyi: ")
    if penyanyi.lower() == "q":
        break

    judul_album = input("Judul album: ")
    if judul_album.lower() == "q":
        break

    album = make_album(penyanyi, judul_album)
    print(album)