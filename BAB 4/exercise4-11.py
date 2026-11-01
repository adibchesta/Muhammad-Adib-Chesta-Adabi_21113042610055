pizza_saya = ['pepperoni', 'keju', 'daging']
pizza_teman = pizza_saya[:]

pizza_saya.append('jamur')
pizza_teman.append('ayam')

print("Pizza favorit saya:")
for rasa in pizza_saya:
    print(rasa)

print("\nPizza favorit teman saya:")
for rasa in pizza_teman:
    print(rasa)