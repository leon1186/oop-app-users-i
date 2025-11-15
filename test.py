# your User class goes here
class Dog:
    def __init__(self, name, breed, color, sound):
        self.name = name
        self.breed = breed
        self.color = color
        self.sound = sound

    def __str__(self):
        return f"I am a {self.color} {self.breed} dog named {self.name} and I say {self.sound}!"

    def speak(self):
        print(f">> {self.sound}")
        
    def fetch(self, item):
        print(f">> {self.name} fetched the {item}")

fido = Dog("Fido", "Pointer", "white", "woof!")
print(fido) # this is a much more descriptive output! This text comes from the __str__() instance method

lassie = Dog("Lassie", "Collie", "golden", "ruff!")
print(lassie)