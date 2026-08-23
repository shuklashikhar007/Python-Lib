class Animal:
    def __int__(self,name):
        self.name = name
class Dog(Animal):
    def __init__(self,name,breed):
        super().__int__(name) # pass the credientials to 
        # inital parent class yahi se
        self.breed = breed
dog = Dog("Buddy","Golden Retriever")
print(dog.name)
print(dog.breed)
