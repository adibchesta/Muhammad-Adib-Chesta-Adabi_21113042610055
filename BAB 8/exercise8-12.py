def make_sandwich(*bahan):
    print("\nSandwich yang dipesan berisi:")

    for item in bahan:
        print(f"- {item}")


make_sandwich("Roti", "Telur", "Keju")
make_sandwich("Roti", "Ayam", "Selada", "Saus")
make_sandwich("Roti", "Daging", "Keju", "Tomat", "Mayones")