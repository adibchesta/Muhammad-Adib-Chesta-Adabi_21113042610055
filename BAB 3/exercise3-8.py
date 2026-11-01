places = ['Japan', 'Switzerland', 'Turkey', 'South Korea', 'Australia']

print("List awal:")
print(places)

print("\nUrutan alfabetis sementara:")
print(sorted(places))

print("\nList awal lagi:")
print(places)

print("\nUrutan alfabetis terbalik sementara:")
print(sorted(places, reverse=True))

print("\nList awal lagi:")
print(places)

places.reverse()
print("\nList setelah reverse():")
print(places)

places.reverse()
print("\nList setelah reverse() lagi:")
print(places)

places.sort()
print("\nList setelah sort():")
print(places)

places.sort(reverse=True)
print("\nList setelah sort(reverse=True):")
print(places)