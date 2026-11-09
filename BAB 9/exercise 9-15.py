from random import choice

lottery_items = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    'A', 'B', 'C', 'D', 'E'
]

my_ticket = [1, 'A', 5, 'C']

attempts = 0

while True:
    winning_ticket = []

    while len(winning_ticket) < 4:
        item = choice(lottery_items)

        if item not in winning_ticket:
            winning_ticket.append(item)

    attempts += 1

    if set(winning_ticket) == set(my_ticket):
        break

print("Tiket saya:", my_ticket)
print("Tiket pemenang:", winning_ticket)
print(f"Jumlah percobaan: {attempts}")