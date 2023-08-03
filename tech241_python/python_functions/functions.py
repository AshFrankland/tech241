def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def mod(num1, num2):
    return num1 % num2


print('What are your two numbers?')
first = int(input('First number: '))
second = int(input('Second number: '))
print('What would you like to do with them?\n\
      (add, subtract, multiply, divide, or modulo)')
opp = input(': ')

if opp == 'add':
    print(add(first, second))
elif opp == 'subtract':
    print(sub(first, second))
elif opp == 'multiply':
    print(mul(first, second))
elif opp == 'divide':
    print(div(first, second))
elif opp == 'modulo':
    print(mod(first, second))
