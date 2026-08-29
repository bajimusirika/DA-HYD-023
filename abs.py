'''
OOP-->class(attributes,methods (Constructor,Instance Method)),
object creation/utilisation-->Encapsulation,Inheritance,Polymorohism
OOp-->Abstarction ,Usage of Class methods,Static Method
#Class methods-->these are termed by using @classmethod  decorator
it applies for entire class level dat,thereby every object utilisation will be modified
'''
'''
class Ecommerce:
    """Usage of classmethod & class attribute"""
    company="Flipkart" #class attribute
    delivery_charge=50 #class attribute
    @classmethod
    def update_delivery(cls):
        cls.delivery_charge=100
        print(f'New Delivery Charges {cls.delivery_charge}')
product=Ecommerce()
print(product.company)
print(product.delivery_charge)
print(Ecommerce.company)
print(Ecommerce.delivery_charge)
product.update_delivery()
print(product.delivery_charge)
Mobile=Ecommerce()
print(Mobile.delivery_charge)
'''
'''
#Applying Inheritance and usage of classmethod,classattributes
#banking scenario -->RBI -->SBI,HDFC....
class RBI:
    """Inheritance usage and classmethod"""
    available_cash=5000000
    @classmethod
    def rbi_cash(cls):
        print(f'Available Cash with RBI is {cls.available_cash}')
class SBI(RBI):
    pass
class HDFC(RBI):
    """Now we will also add some cash to it"""
    cash=3000000
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        #print(f'Total cash is {cls.cash+cls.available_cash}')
        print(f'Total cash is {HDFC.cash+RBI.available_cash}')
#a=SBI()
#print(a.available_cash)
#a.rbi_cash() 
#SBI.rbi_cash()
b=HDFC()
print(b.available_cash)
print(b.cash)
b.rbi_cash()
b.hdfc_cash()
'''
'''
#cash
class RBI:
    """Inheritance usage and classmethod"""
    cash=5000000
    @classmethod
    def rbi_cash(cls):
        print(f'Available Cash with RBI is {cls.cash}')
class SBI(RBI):
    pass
class HDFC(RBI):
    """Now we will also add some cash to it"""
    cash=3000000
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        print(f'Total cash is {cls.cash+RBI.cash}')
a=HDFC()
print(a.cash)
a.hdfc_cash()
a.rbi_cash() 
#If incase as above scenerio we have same name for class attributes in
#both parent and child classes,the best approach is to call
#the class attributes is using class names such as (RBI.cash)

#Static Method -->It doesnot depend either on the object or to the class
#we can create it using @staticmethod decorator
#it is mainly used as utility or helper functions
class Ecommerce:
    """Usage of Static Method"""
    @staticmethod
    def free_delivery(price):
        return price>500
u1=Ecommerce()
print(u1.free_delivery(450))
print(u1.free_delivery(1000))

#Now lets relate both class method and staticmethod in a single use
class Ecommerce:
    """Usage of class&static method"""
    platform="Flipkart"
    @classmethod
    def show_platform(cls):
        print("Welcome to platform")
        print(f'{cls.platform}')
    @staticmethod
    def free_delivery(price):
        #return price>500
        if price>500:
            print("You are eligible for Free Delivery")
        else:
            print("You need to pay Delivery")
user=Ecommerce()
#print(user.platform)
user.show_platform()
print(user.free_delivery(450))
print(user.free_delivery(1200))
'''
#Abstraction :It is also one of the key feature of OOP,where it shows
#only the relevant details to the user and hides the implementation features
#Instagram-->Uploading photo,Upload video,Reel
#when we need all child classes to follow same pattern
#we have abc module to implement abstraction
import abc
from abc import ABC,abstractmethod
class Content(ABC):
    @abstractmethod
    def upload(self):
        pass
class photo(Content):
    '''def upload(self):
        print("Compressing the Picture")
        print("Edit the Picture")
        print("photo uploaded sucessfully")'''
    pass #we made upload as abstract method mandatory it has be followed
class Video(Content):
    def upload(self):
        print("Encoding the Video")
        print("Video Editing is in process")
        print("Video uploaded sucessfully")
class Reel(Content):
    def upload(self):
        print("Adding Effects to the Reel")
        print("Reel is Edited")
        print("Reel uploaded sucessfully with tags...")
'''Contents=[Photo(),Video(),Reel()]
#print(Contents)
for content in Contents:
    content.upload()
    '''
obj=photo()
print(obj)#TypeError as we are not following the upload pattern
a=Video()
print(a.upload())