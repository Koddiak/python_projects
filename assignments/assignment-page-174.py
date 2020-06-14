class Pet:
    name = ''
    owner = ''
    personality = ''

    def __init__(self, name, owner, personality):
        self.name = name
        self.owner = owner
        self.personality = personality
        
class Dog(Pet):
    breed = ''
    collar = False

class Cat(Pet):
    fur_color = ''
    fur_type = ''
