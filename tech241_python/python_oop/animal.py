class Animal:

    def __init__(self):  # Runs when the class is initialised
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print('One breath at a time, in and out')

    def eat(self):
        print('Nom Nom Nom')

    def procreate(self):
        print('Time to find a mate')

    def move(self):
        print('Onwards and upwards')
