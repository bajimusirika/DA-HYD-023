'''
Constructor -->Instance methods-->public Attributes
Encapusulation
constructor-->it is a special method(__init__())

class Cars:
        """Understanding the usage of OOP"""
        def __init__(self,brand,name,price,color):
            self.brand=brand
            self.name=name
            self.price=price
            self.color=color
            
        
        #Methods(behaviour)
        def details(self):
            print(f'Car Brand is {self.brand}')
            print(f'Car Model name is {self.name}')
            print(f'Car Color is {self.color}')
            print(f'Car Price is {self.price}')
u1 = Cars("Tata","Nexon","9Lakhs","Blue")
u1.details()

class Cars:
        """Understanding the usage of  Constuctor in OOP"""
        def __init__(self):
            self.brand="BMW"
            self.name="Sedans"
            self.price="50Lakhs"
            self.color="Black"
            
        
        #Methods(behaviour)
        def details(self):
            print(f'Car Brand is {self.brand}')
            print(f'Car Model name is {self.name}')
            print(f'Car Color is {self.color}')
            print(f'Car Price is {self.price}')
u1=Cars()
print(u1.brand,u1.name,u1.price,u1.color)
u1.details()

Encapsulation -->It is one of the main feature of OOP
It binds(bundles) the data (attributes) and the methods(behaviour)
into a single unit(class) -->multiple objects
-->Attributes -->public,pritected ,private
#public attributes-->Attributes defined inside the class(Constructor)
and can be modified outside the class

class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username):
        self.user=username #public attribute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
u1=CodegnanPortal("Bajimusirika")
u1.display()
u1.user="Baji Musirika"
u1.display()
print(u1.__dict__)
u2=CodegnanPortal("charan")
u2.display()
print(u2.__dict__)

#protected attributes -->we use single underscore before an
#attribute moreover it can be modified also outside the class
#and even accessible in subclasses...
class CodegnanPortal:
    """CodegnanPortal with Users"""
    def __init__(self,username,_otp):
        self.user=username #public attribute
        self._otp=_otp #protected attribute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has receives OTP is {self._otp}')
u1 = CodegnanPortal("Baji",23456)
u1.display()
u1._otp=3456
u1.display()

#modify
class CodegnanPortal:
    """CodegnanPortal with Users"""
    def __init__(self,username,_otp,password):
        self.user=username #public attribute
        self._otp=_otp #protected attribute
        self.__password=password
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has receives OTP is {self._otp}')
        #print(f'Student password is {self.__password}')
u1 = CodegnanPortal("Baji",23456,"baji@2004")
print(u1.__dict__)
print(u1._CodegnanPortal__password) #NameMangling
'''
#In above case we use Namemangling 
class CodegnanPortal:
    """CodegnanPortal with Users"""
    def __init__(self,username,_otp,password):
        self.user=username #public attribute
        self._otp=_otp #protected attribute
        self.__password=password
    #Usage of getter() method
    def get_password(self):
        return "******"
    #to modify the password we use setter() method
    def set_password(self,new_password):
        if len(new_password) < 6:
            print("Wrong password not satisfied 6 characters")
        else:
            self.__password=new_password
            print("Now password is updated")
u1=CodegnanPortal("Baji",23456,"baji@2004")
print(u1.get_password())
u1.set_password("Charan")
u1.set_password("Srikanth") #compulsory morethan 6
print(u1.get_password())