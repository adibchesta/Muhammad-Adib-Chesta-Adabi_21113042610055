class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restoran: {self.restaurant_name}")
        print(f"Jumlah pelanggan: {self.number_served}")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("Warung Nusantara", "Masakan Indonesia")

print(f"Jumlah awal pelanggan: {restaurant.number_served}")

restaurant.number_served = 20
print(f"Jumlah pelanggan: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Setelah diubah: {restaurant.number_served}")

restaurant.increment_number_served(10)
print(f"Setelah ditambah: {restaurant.number_served}")