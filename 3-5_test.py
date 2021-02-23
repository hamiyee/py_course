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
