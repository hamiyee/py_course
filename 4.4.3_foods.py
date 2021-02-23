# copy list using slice
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 如果不使用切片，直接将my_foods赋值给friend_food，不能得到两个不同的列表

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print('\nMy friend\'s favorite foods are:')
print(friend_foods)
