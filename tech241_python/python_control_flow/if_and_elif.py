age = input('How old are you? ')

while True:
    try:
        age = int(age)
    except ValueError:
        age = input('Please write your name as an integer: ')
    else:
        if age < 1:
            age = input('That age is too low, try again: ')
        elif age > 117:
            age = input('That age is too high, try again: ')
        else:
            break

if age >= 18:
    print('You can watch any movie')
elif age >= 15:
    print('You can\'t watch 18 rated movies, but can watch any other movie')
elif age >= 12:
    print('You can\'t watch 18, or 15 rated movies, but can watch any other movie')
else:
    print('You can only watch U rated movies')
