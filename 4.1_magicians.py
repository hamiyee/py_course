# for loop
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    message_hello = f'{magician.title()}, that was a great trick!'
    message_bye = f"I can't wait to see your next trick, {magician.title()}.\n"
    print(message_hello)
    print(message_bye)

print('Thank you, everyone. That was a great magic show!')
