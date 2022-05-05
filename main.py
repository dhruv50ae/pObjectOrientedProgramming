from random import sample


class Dog():
    species = "Mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


myDog = Dog("Lab", "Alpha")
otherDog = Dog("Huskie", "Bravo")
print(otherDog.breed)
print(myDog.breed)
