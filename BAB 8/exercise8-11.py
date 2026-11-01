def send_messages(pesan, pesan_terkirim):
    while pesan:
        isi = pesan.pop()
        print(isi)
        pesan_terkirim.append(isi)


daftar_pesan = [
    "Belajar fungsi Python.",
    "Mengerjakan latihan.",
    "Menyelesaikan tugas."
]

pesan_terkirim = []

send_messages(daftar_pesan[:], pesan_terkirim)

print("\nList asli:")
print(daftar_pesan)

print("\nList arsip:")
print(pesan_terkirim)