# variables in python

a = 1  # int
b = 2  # int
c = 3.5  # float
hi = 'hello world!'  # string

print(hi)
print(type(hi))

name = input('What is your name? ')
age = input('How old are you? ')
dob = input('When were you born? ')
address = input('Where do you live? ')

print(f'\nHi {name},\n'
      f'you are {age} years old,\n'
      f'you were born on {dob},\n'
      f'and live in {address},\n'
      f'on your next birthday you\'ll turn {int(age) + 1}')

'''
This lets me write a
multi
line
comment
'''
