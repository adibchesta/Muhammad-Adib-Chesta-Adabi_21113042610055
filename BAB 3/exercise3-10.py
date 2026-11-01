motorcycles = ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki']

print("List awal:")
print(motorcycles)

print("\nMengakses elemen:")
print(motorcycles[0])

print("\nMengubah elemen:")
motorcycles[1] = 'Ducati'
print(motorcycles)

print("\nMenambahkan elemen di akhir:")
motorcycles.append('BMW')
print(motorcycles)

print("\nMenyisipkan elemen:")
motorcycles.insert(1, 'Vespa')
print(motorcycles)

print("\nMenghapus elemen menggunakan del:")
del motorcycles[0]
print(motorcycles)

print("\nMenghapus elemen menggunakan pop():")
motorcycles.pop()
print(motorcycles)

print("\nMenghapus elemen berdasarkan nilai:")
motorcycles.remove('Suzuki')
print(motorcycles)

print("\nMengurutkan sementara:")
print(sorted(motorcycles))

print("\nMembalik urutan:")
motorcycles.reverse()
print(motorcycles)

print("\nJumlah elemen:")
print(len(motorcycles))