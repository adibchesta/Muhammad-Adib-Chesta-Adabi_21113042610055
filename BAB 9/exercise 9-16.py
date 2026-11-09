import random

numbers = [10, 20, 30, 40, 50]

print("Daftar angka:", numbers)

print("Angka acak:", random.choice(numbers))

print("Angka acak antara 1 sampai 100:")
print(random.randint(1, 100))