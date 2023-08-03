class Calculator:

    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.operation = None

    def get_nums(self):
        self.num1 = int(input('What is your first number? '))
        self.num2 = int(input('What is your second number? '))

    def get_operation(self):
        self.operation = input('What operation would you like to perform?\n\
        (add, subtract, multiply, divide, modulo): ')

    def do_op(self):
        if self.operation == 'add':
            return self.add()
        elif self.operation == 'subtract':
            return self.sub()
        elif self.operation == 'multiply':
            return self.mul()
        elif self.operation == 'divide':
            return self.div()
        elif self.operation == 'modulo':
            return self.mod()

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def mod(self):
        return self.num1 % self.num2


def main():
    calc = Calculator()
    calc.get_nums()
    print('')
    calc.get_operation()
    print('')
    print(calc.do_op())


if __name__ == '__main__':
    main()
