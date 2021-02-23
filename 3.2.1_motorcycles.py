# learn modify element of list
motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# del motorcycles[0]
# print(motorcycles)

# del 方法删除元素后，不能再使用它
# del motorcycles[1]
# print(motorcycles)

# pop 删除元素后，还可以继续使用它
# popped_motorcycle = motorcycles.pop()

# print(motorcycles)
# print(popped_motorcycle)

# last_owned = motorcycles.pop()
# message = f'The last motorcycle I owned was a {last_owned.title()}.'
# print(message)

# remove可以根据值删除元素，并且可以继续使用它.但remove只能删除第一个值，如有多个重复，需用循环。
# motorcycles.remove('ducati')
# print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
message = f'\nA {too_expensive.title()} is too expensive for me.'
print(message)
