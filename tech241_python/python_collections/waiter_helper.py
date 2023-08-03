# The Menu

menu = {
    'starters': ['Soup of the Day', 'Prawn Cocktail', 'Garlic Mushrooms'],
    'mains': ['Stake and Ale Pie', 'Fish and Chips', 'Bangers and Mash'],
    'desserts': ['Ice Cream', 'Cheesecake', 'Syrup Sponge Cake']
}

print('Welcome to our restaurant, on our menu today we have:\n\
    For Starters:\n\
          {}\n\
          {}\n\
          {}.'.format(menu['starters'][0], menu['starters'][1], menu['starters'][2]))
print('    For Mains:\n\
          {}\n\
          {}\n\
          {}.'.format(menu['mains'][0], menu['mains'][1], menu['mains'][2]))
print('    For Desserts:\n\
          {}\n\
          {}\n\
          {}.'.format(menu['desserts'][0], menu['desserts'][1], menu['desserts'][2]))

print('')
user_starter = input('What would you like for your Starter?: ')
user_main = input('What would you like for your Main?: ')
user_dessert = input('What would you like for your Dessert?: ')

responses = []

response = 'You have ordered {} for your starter, \
{} for your main, \
and {} for your dessert.'.format(user_starter, user_main, user_dessert)

responses.append(response)
print('')
print(response)

print('')
user_starter = input('What would you like for your Starter?: ')
user_main = input('What would you like for your Main?: ')
user_dessert = input('What would you like for your Dessert?: ')

response = 'You have ordered {} for your starter, \
{} for your main, \
and {} for your dessert.'.format(user_starter, user_main, user_dessert)

responses.append(response)
print('')
print(response)

print('')
user_starter = input('What would you like for your Starter?: ')
user_main = input('What would you like for your Main?: ')
user_dessert = input('What would you like for your Dessert?: ')

response = 'You have ordered {} for your starter, \
{} for your main, \
and {} for your dessert.'.format(user_starter, user_main, user_dessert)

responses.append(response)
print('')
print(response)

# print(responses)
