class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis makanan: {self.cuisine_type}")


restaurant1 = Restaurant("Warung Bu Siti", "Masakan Jawa")
restaurant2 = Restaurant("Pizza House", "Makanan Italia")
restaurant3 = Restaurant("Sushi Bar", "Makanan Jepang")

restaurant1.describe_restaurant()
print()

restaurant2.describe_restaurant()
print()

restaurant3.describe_restaurant()