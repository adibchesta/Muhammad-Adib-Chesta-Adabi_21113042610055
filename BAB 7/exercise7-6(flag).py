aktif = True

while aktif:
    topping = input("Masukkan topping (quit untuk berhenti): ")

    if topping == "quit":
        aktif = False
    else:
        print("Topping ditambahkan:", topping)