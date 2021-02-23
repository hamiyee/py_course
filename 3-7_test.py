# invite guests
guests = ['hamiyee', 'lsjgreen', 'koyou']
for guest in guests:
    message = f'Hi {guest.title()}, I want to invite you to dinner.'
    print(message)

print(f'\n{guests[0].title()} cannot go to dinner.\n')

guests[0] = 'harvey'
for guest in guests:
    message = f'Hi {guest.title()}, I want to invite you to dinner.'
    print(message)

print('\nI find a bigger dinner table, so I can invite more guests.\n')

guests.insert(0, 'hank')
guests.insert(2, 'jassie')
guests.append('lucy')

for guest in guests:
    message = f'Hi {guest.title()}, I want to invite you to dinner.'
    print(message)

print('\nSorry, now I can only invite two guests to dinner.\n')

for i in range(4):
    guest = guests.pop()
    print(f'Dear {guest.title()}, I can not invite you to dinner.')

del guests[0]
del guests[0]

print('')
print(guests)
