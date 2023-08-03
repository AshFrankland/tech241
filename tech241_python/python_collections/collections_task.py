cool_things = [
    'RTX 4090',
    'Mercedes-AMG F1 W11 EQ Performance',
    'Mark LXXXV Iron Man Suit',
    'Twitter',
    'A ticket to the Silverstone GP']

print(cool_things)
print(type(cool_things))
print(cool_things[0])
print(cool_things[1])
print(cool_things[-1])

cool_things[0] = 'RTX 5090'
cool_things[-2] = 'Reddit'

print(cool_things)

cool_things.append('Flux Capacitor')

print(cool_things)

cool_things.remove('Reddit')

print(cool_things)

cool_things.pop()