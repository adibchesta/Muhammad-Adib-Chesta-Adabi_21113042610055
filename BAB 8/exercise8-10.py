def send_messages(pesan, pesan_terkirim):
    while pesan:
        isi = pesan.pop()
        print(isi)
        pesan_terkirim.append(isi)


daftar_pesan = [
    "Semangat kuliahnya!",
    "Jangan lupa mengerjakan tugas.",
    "Tetap konsisten belajar Python."
]

pesan_terkirim = []

send_messages(daftar_pesan[:], pesan_terkirim)

print("\nList pesan asli:")
print(daftar_pesan)

print("\nList pesan terkirim:")
print(pesan_terkirim)