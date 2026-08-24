'''
OOP-->Class,Object,Methods (__init__())
Encapsulation -->public,protected,priavte
Inherutance-->It is one of key feature of OOP where we inheritance
the properties (attributes/methods) from one class to another
class (base class(parent class)-->derived class(child class))
Whatsapp-->Personal User,Business User(Catalog),Community admin
Features -->Code Reusability ,Avoiding Code Duplication,
Code Maintainability,Polymorphism(Method Overriding(super()),
Method Overloading,Operator Overloading __add__,__str__)

Types:single Inheritance (Finger Print)
-->one child class inheriting properties from one parent class
Multiple Inheritance(Mother,Father-->child)-->one child
class inheriting properties from two parent classes
Multilevel Inheritance (Grandparent-->parent-->child)
level by level
Hierarchical Inheritance-->multiple child classes
inheriting properties from single parent
Hybrid Inheritance-->It can carry one or more type of inheritances
syntax:
Single Inheritance:
    statement(s)..
    .....
class Derivedclass(baseclass):
    ...........
    .......

#Whatsapp Scenario-->Personal User,Business User
class User:
    """single Inheritance usage"""
    def send_message(self):
        print('Sending Message')
    def voice_call(self):
        print('Making Voice Calls')
    def video_call(self):
        print('Making Video Calls')
class BusinessUser(User):
    pass
    def create_catalog(self):
        print("Display Products Catalog")
u1=BusinessUser()
print(dir(u1))
u1.send_message()
u1.video_call()
u1.voice_call()
u1.create_catalog()

#Social media login-->users-->update_users
class users:
    """Single Inheritance usage"""
    company='Codegnan'#class attribute
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def full_name(self):
        return self.fname + self.lname
#u1=users("Baji","Musirika")
#print(u1.full_name())
#print(u1.company)
class Update_users(users):
    def update_name(self):
        return self.fname.title()+" "+self.lname.title().strip()
u1=Update_users("Baji","Musirika")
print(u1.company)
print(u1.full_name())
print(u1.update_name())
u2=users("sai","charan")
print(u2.full_name())
print(u2.company)

#What if we have constructor in child class also...
#Father -->kid(property)
class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self):
        self.property=100000
    def father_property(self):
        print(f'Father Property is {self.property}')
#class kid(Father):
    #pass
class Kid(Father):
    """Now childclass will have Constructor"""
    def __init__(self):
        #self.property=200000
        self.cash=200000
    def kid_property(self):
        print(f'Kid property is {self.property}')
obj=Kid()
obj.father_property()
obj.kid_property()
#in above case it is giving same value for Father also as 2 lakhs..when we gave property as same 
#attribute in both class
#parent class is having constructor or child is having constructor so constructor overriding is happening
#to avoid constructor overriding to start super()-->super().__init__()
#-->super().__init__()
#-->super().method() method overriding
#Constructor Overriding -->super usage()
#In above case
'''
class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self):
        self.property=1000000
    def father_property(self):
        print(f'Father Property is {self.property}')
class Kid(Father):
    """Now childclass will have Constructor"""
    def __init__(self):
        super().__init__()#calling superclass constructor
        self.cash=200000
    def kid_property(self):
        print(f'Kid property is {self.cash}')
        print(f'kid Final Property is {self.cash + self.property}')
obj=Kid()
obj.father_property()
obj.kid_property()