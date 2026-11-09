from random import choice

lottery_items = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    'A', 'B', 'C', 'D', 'E'
]

winning_ticket = []

while len(winning_ticket) < 4:
    item = choice(lottery_items)

    if item not in winning_ticket:
        winning_ticket.append(item)

print("Tiket yang memenangkan hadiah:")
print(winning_ticket)

print("Jika tiketmu memiliki 4 kombinasi yang sama, kamu menang!")