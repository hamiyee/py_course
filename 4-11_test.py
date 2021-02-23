# learn slice using
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('onion')
friend_foods.append('garlic')

print('My favorite pizzas are:')
print(list(pizza for pizza in my_foods))

print('\nMy friend\'s favorite pizzas are:')
print(list(pizza for pizza in friend_foods))
