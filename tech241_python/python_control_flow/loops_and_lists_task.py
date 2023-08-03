import random

for i in range(0, 10):
    print('Hello')

list_names = []

for i in range(0, 3):
    name = input('What is your name? ')
    list_names.append(name)

list_names_lower = []

for name in list_names:
    list_names_lower.append(name.lower())

print(list_names_lower)

rand_nums = []

for i in range(0, 20):
    rand_nums.append(random.randint(0, 100))

for num in rand_nums:
    if num % 2 == 0:
        print(num)

all_sum = 0

for num in range(0, 101):
    all_sum += num

print(sum)

even_sum = 0
odd_sum = 0

for num in range(0, 101):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(even_sum)
print(odd_sum)
