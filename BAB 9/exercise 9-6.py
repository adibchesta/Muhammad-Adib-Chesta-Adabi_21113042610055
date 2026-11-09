class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Matcha"]

    def show_flavors(self):
        print("Daftar rasa es krim:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream = IceCreamStand("Ice Cream House", "Dessert")

ice_cream.show_flavors()