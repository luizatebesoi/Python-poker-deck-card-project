class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        pass

class Cat(Animal):
    def __init__(self, name, species, toy, breed):
        super().__init__(name, species)
        self.toy = toy
        self.breed = breed
    
blue = Cat('blue', 'cat', 'string', 'scottish fold')

print(blue.name)
print(blue.species)
print(blue.toy)
print(blue.breed)