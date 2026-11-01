guests = ['Andi', 'Budi', 'Eka', 'Dina', 'Citra', 'Fajar']

print("Maaf, meja makan yang baru ternyata tidak tersedia. Aku hanya bisa mengundang dua orang.")

removed_guest = guests.pop()
print(f"Maaf {removed_guest}, aku tidak bisa mengundangmu.")

removed_guest = guests.pop()
print(f"Maaf {removed_guest}, aku tidak bisa mengundangmu.")

removed_guest = guests.pop()
print(f"Maaf {removed_guest}, aku tidak bisa mengundangmu.")

removed_guest = guests.pop()
print(f"Maaf {removed_guest}, aku tidak bisa mengundangmu.")

print(f"Halo {guests[0]}, kamu tetap diundang.")
print(f"Halo {guests[1]}, kamu tetap diundang.")

del guests[0]
del guests[0]

print(guests)