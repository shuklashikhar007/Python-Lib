class Animal:
    def speak(self):
        print("Some sound")
class Dog(Animal):
    def speak(self): # overiding
        print("Woof!")
class Cat(Animal):
    def speak(self): # python mai no use of virtual functions is required
        # yaha par sidha same name ka function banane se
        # we can override a function sidha yahi se
        print("Meow!") 
# polymorphism ->
# same name function behave differently for different objects
animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()

