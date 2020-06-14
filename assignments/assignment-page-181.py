class Pet:
    name = ''
    owner = ''
    personality = ''
    collar = False
    
    def __init__(self, name, owner, personality, collar):
        self.name = name
        self.owner = owner
        self.personality = personality
        self.collar = collar

    def tag(self):
        tag = ''
        return tag
        
class Dog(Pet):
    fur_color = ''
    breed = ''

    def __init__(self, name, owner, personality, collar, fur_color, breed):
        self.name = name
        self.owner = owner
        self.personality = personality
        self.collar = collar
        self.fur_color = fur_color
        self.breed = breed

    def tag(self):
        tag = 'This pet is a dog.'
        return tag
        
    
class Cat(Pet):
    fur_color = ''
    fur_type = ''

    def __init__(self, name, owner, personality, collar, fur_color, fur_type):
        self.name = name
        self.owner = owner
        self.personality = personality
        self.collar = collar
        self.fur_color = fur_color
        self.fur_type = fur_type

    def tag(self):
        tag = 'This pet is a cat.'
        return tag

if __name__ == "__main__":
    dog = Dog('Thompson', 'Jimmy McPhearson', 'Hyper', True, 'Gold', 'Labrador Retriever')
    print('Name: {}\nOwner: {}\nPersonality: {}\nCollar: {}\nFur Color: {}\nBreed: {}\n'.format(dog.name, dog.owner, dog.personality, dog.collar, dog.fur_color, dog.breed))
    print(dog.tag())
    
    print('\n--\n')
    
    cat = Cat('Rosie', 'Ronda Fitzpatrick', 'Reserved', False, 'Black', 'Short')
    print('Name: {}\nOwner: {}\nPersonality: {}\nCollar: {}\nFur Color: {}\nFur Type: {}\n'.format(cat.name, cat.owner, cat.personality, cat.collar, cat.fur_color, cat.fur_type))
    print(cat.tag())
