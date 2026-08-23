#Object Oriented programming in Python 
class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed
    def accelerate(self):
        self.speed += 10
    def show_speed(self):
        print(self.speed)
#self is same as this and refers to the current object 
# pointer to the current object is self (or this)
car1 = Car("Toyota",10)
car2 = Car("Honda", 20)
print(car1.brand)
print(car2.brand)
car1.accelerate()
car2.show_speed()




