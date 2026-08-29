'''
polymorphism-->It is also of one key feature of OOP,
poly-->many
morph-->forms
Methods with same name can take different parameters (arguments--list),
-->Method Overloading(compile time polymorphism)
-->Method Overriding (Run-time)
-->Operator Overloading(+,*)(__add__,__str__)
HotStar
->Free User-->can watch the movies with advertisements
->premium User-->can watch premium content without advertisements
->VIP-->live content,streaming quality
'''
'''
#Method Overloading :
class HotStar:
    """Understanding polymorphism"""
    def watch():
        print(f'User logged into Hotstar...Opening some page')
    def watch(self,movie):
        self.movie=movie
        print(f'User watching {self.movie}')
app=HotStar()
app.watch("irumudi")
'''
#1)Method usage with default arguments
#2)Method usage with variable length arguments(*args)
#3)Method usage with type of arguments
'''
class Hotstar:
    """Method usage with default arguments"""
    def watch(self,movie=None):
        if movie is None:
            print(f'User logged into Hotstar...checking')
        else:
            self.movie=movie
            print(f'User started watching {self.movie}')
app=Hotstar()
app.watch()
app.watch("Aarya")
'''
'''
class Hotstar:
    """Method usage with default arguments"""
    def watch(self,*movie):
        if len(movie)==0:
            print(f'User logged into Hotstar...checking')
        else:
            for m in movie:
                print(f'User started watching {m}')
app=Hotstar()
app.watch()
app.watch("Aarya","vikram")
'''
'''
#Method overloading with type of arguments usage
#Hotstar -->one movie at a time
        -->multiple movies at a time 
'''
'''
class HotStar:
    """Method Overloading with type of arguments usage"""
    def watch(self,content):
        if isinstance(content,str):
            print(f'User watching {content}')
        elif isinstance(content,list):
            print(content)
            for movie in content:
                print(movie)
app=HotStar()
app.watch("Avengers")
app.watch(["Salaar", "Pushpa 2", "Devara"])
'''
'''
#Method overriding -->It happens in the scenario of Inheritance,where if child class is having
method name same as parent class thats where overriding
#we can use super() or if we create different objects
'''
'''
class Freeuser:
    """Understanding method overriding"""
    def watch(self):
        print(f'Use logged into Homepage...')
class Premiumuser(Freeuser):
    """Using Inheritance"""
    def watch(self,movie):
        self.movie=movie
        print(f'User watching {self.movie}')
obj=Premiumuser()
obj.watch("vikram")
obj2=Freeuser()
obj2.watch()

#In above usecase we can create different objects to access same
class Freeuser:
    """Understanding method overriding"""
    def watch(self):
        print(f'Use logged into Homepage...')
class Premiumuser(Freeuser):
    """Using Inheritance"""
    def watch(self,movie):
        super().watch()
        self.movie=movie
        print(f'User watching {self.movie}')
obj=Premiumuser()
obj.watch("vikram")
'''
#Operator Overloading-->Operators (+,-,*,/) -->Operators will behave in a different way as per user defined objects...
# + (Addition,Concatenation,Merging)
'''
print(3+4)
print('code'+'gnan')
print([23,45]+[4,5])
#print(3.__add__(4))
a=25;b=3
a=[12,3,4];b=[3,4,5]
print(a.__add__(b))
print(a.__len__())
print(a.__mul__(2))
'''
#let's apply the above scenario HotStar WatchHistory
'''
class WatchHistory:
    """Define the number of hours"""
    def __init__(self,hours):
        self.hours=hours
varun=WatchHistory(100)
print(varun.hours)
akash=WatchHistory(120)
print(akash.hours)
#print(varun + akash)
print(varun.hours + akash.hours)
'''
#But the preferable way is usage of __add__()
class WatchHistory:
    """Define the number of hours"""
    def __init__(self,hours):
        self.hours=hours
    def __add__(self,other):
        return self.hours + other.hours
    def __str__(self):
        return f'WatchHistory is {self.hours}'
varun=WatchHistory(100)
print(varun)
print(varun.hours)
akash=WatchHistory(50)
print(akash)
print(varun+akash)