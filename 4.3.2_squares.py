# generate number list using range
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

squares_2 = [value ** 2 for value in range(1, 11)]
print(squares_2)
