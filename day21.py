'''
OOP -->object oriented programming-->objects
-->Attributes(Data),Methods(Behaviour)
class,object ->A Class is a blueprint(template)for an object
An object is an instance (physical thing)which utilises the class
chair (object)-->wood,tools,dimensions(blueprint),carpenter
Ecommerce platform
-->Mobile ->price,Features(camera,storage,ram)
-->variables,def mobile()
-->Laptops -->price,features
-->variables,def laptop()
-->Gadgets-->price,Features
-->variables,def gadgets()
-->Electronic Items -->price,features
-->variables,def elect()
Features of OOP -->Modularity,Scalability,Encapsulation(binding data (attributes),
features to the  class)(objects)
Abstraction -->show only relevant information to the class(object)
Inheritance -->Acquring properties (attributes,methods)
single-->Fingerprint
Multiple-->parents(Mother,Father)-->child
Multilevel-->Grandparent-->parent-->child
poly orphism-->Method overloading,method overriding,operator overriding
'''
#syntax for class creation:
'''
class Class_Name:
    """Doc String"""
    attributes(characteristics)
    ............
    def func(self):(behaviour)
        ....
        ....
    ......
obj=Class_Name()

#student class with basic details
class Student:
    """Understanding the usage of OOP"""
    name="baji"
    id="CGH4040"
    gender="female"
    email_id="bajimusirika@gmail.com"
    #Methods(behaviour)
    def display(baji):
        print(f'Student name is {baji.name}')
        print(f'Student Id is {baji.id}')
        print(f'Student Mail is {baji.email_id}')
u1=Student()
print(u1)
#print(dir(u1))#directory (returns all available methods/attributes)
u1.display()
u2=Student()
u2.display()

#Student class for multiple objects
class Students:
    """Understanding the usage of OOP"""
    name=input("enter name")
    id=input("enter ID")
    gender=input("enter Gender")
    email_id=input("enter Mail id")
    #Methods(behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student Id is {self.id}')
        print(f'Student Mail is {self.email_id}')
u1=Students()
#print(u1)
#print(dir(u1))#directory (returns all available methods/attributes)
u1.display()
u2=Students()
u2.display()
print(u1.__dict__)#it returns empty dict
print(u2.__dict__)#it returns empty dict
'''
#Student class details with multiple objects
class Students:
        """Understanding the usage of OOP"""
        def data(self,name,id,gender,email_id):
            self.name=name
            self.id=id
            self.gender=gender
            self.email_id=email_id
        
        #Methods(behaviour)
        def display(self):
            print(f'Student name is {self.name}')
            print(f'Student ID is {self.id}')
            print(f'Student Mail is {self.email_id}')
u1=Students()
u1.data("baji","4040","female","bajimusirika@gmail.com")
u1.display()
print(u1.__dict__)
u2=Students()
u2.data("srikanth","4044","male","srikanth@gmail.com")
u2.display()
print(u2.__dict__)
#Create a class with car Brand name,price,color-->display()
