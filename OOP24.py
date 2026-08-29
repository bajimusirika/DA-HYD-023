'''# git remote
class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self,property):
        self.property=property
    def father_property(self):
        print(f'Father Property is {self.property}')
class Kid(Father):
    """Now childclass will have Constructor"""
    def __init__(self,cash,property):
        self.cash=cash
        super().__init__(property)
    def kid_property(self):
        print(f'Kid property is {self.cash}')
        print(f'kid Final Property is {self.cash + self.property}')
obj=Kid(250000,1000000)
obj.kid_property()
obj.father_property()'''
'''
#what if child class is having same method name as
#parent class-->Method Overriding
#Area of square,rectangle
class Rectangle:
    """Method Overriding usage"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        print(f'Area of Rectangle is {self.x*self.y}')
class Square(Rectangle):
    def __init__(self,x):
        self.x=x
    def area(self):
        print(f'Area of Square is {self.x**2}')
obj=Square(7)
obj.area()
#obj.rarea()
'''
'''
class Square:
    """Method Overriding usage"""
    def __init__(self,x):
        self.x=x
    def area(self):
        print(f'Area of Square is {self.x**2}')
class Rectangle(Square):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        super().__init__(x)
    def area(self):
        super().area()
        print(f'Area of Rectangle is {self.x*self.y}')
x,y=map(int,input('enter the values:').split(','))
obj=Rectangle(x,y)
obj.area()
'''
#Multiple Inheritance
'''
class parent1:
    .....
class parent2:
    .....
class child(parent1,parent2):
    ....
'''
'''
class User:
    """First parent class with user features"""
    def voice_call(self):
        print("Making Voice Calls")
class Notifications:
    def notifications(self):
        print("Sending Notifications..")
class PremiumUser(User,Notifications):
    def Verification_badge(self):
        print("Blue Tick Verification done")
user=PremiumUser()
user.Verification_badge()
'''
#Multilevel Inheritance-->level by level
'''
class GrandParent:
    .....
class parent(GrandParent):
    ....
class child(Parent):
    .....
'''
'''
class User:
    def display_User(self):
        print("This is User class")
class BusinessUser(User):
    def display_BusinessUser(self):
        print("This is BusinessUser class")
class VerifyBusinessUser(BusinessUser):
    def display_VerifyBusinessUser(self):
        print("This is VerifyBusinessUser class")
obj = VerifyBusinessUser()
obj.display_User()  
obj.display_BusinessUser()   
obj.display_VerifyBusinessUser()
'''
'''
class Animal:
    def animal_info(self):
        print("This is an Animal")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")
dog = Dog()
dog.animal_info()
dog.bark()
cat = Cat()
cat.animal_info()
cat.meow()
'''
'''
class Vehicle:
    def vehicle_info(self):
        print("This is a Vehicle")
class Car(Vehicle):
    def car_info(self):
        print("This is a Car")
class Bike(Vehicle):
    def bike_info(self):
        print("This is a Bike")
class SportsCar(Car, Bike):
    def sports(self):
        print("Sports Car")
obj = SportsCar()
obj.vehicle_info()
obj.car_info()
obj.bike_info()
obj.sports()
'''
