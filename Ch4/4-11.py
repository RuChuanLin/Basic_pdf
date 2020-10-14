my_pizzas = ['pizza hot', 'domino', 'napoli']
friend_pizzas = my_pizzas[:]
# ---------------------------------------------------------------------------------------------------------------------
my_pizzas.append('有知心(芝心)')
# ---------------------------------------------------------------------------------------------------------------------
friend_pizzas.append('半熟起司塔')
# ---------------------------------------------------------------------------------------------------------------------
print("My favorite pizza are:")
for my_pizza in my_pizzas:
    print(my_pizza)

print("\nMy friend's favorite pizza are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)





