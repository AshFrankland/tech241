# creating a class
class Dog:

    animal_kind = 'canine'

    def bark(self):
        if self.animal_kind == 'canine':
            return 'woof'


# instantiation of a class
fido = Dog()
lassie = Dog()

print(type(fido))
print(fido.bark())
