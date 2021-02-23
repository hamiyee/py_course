# sort list
resortes = ['Japan', 'NewYork', 'London', 'Spanish', 'China']
print('This is the original list:')
print(resortes)

print('\nThis is the sorted list:')
print(sorted(resortes))

print('\nThis is the original list again:')
print(resortes)

resortes.reverse()
print('\nThis is the reversed list:')
print(resortes)

resortes.reverse()
print('\nThis is the re-reversed list:')
print(resortes)

resortes.sort()
print('\nThis is the sorted list by sort():')
print(resortes)

resortes.sort(reverse=True)
print('\nThis is the reverse-sorted list by sort():')
print(resortes)
