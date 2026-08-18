'''
Tokens,Datatypes-->control flow statements-->if,elif,else,for,while,break,continue..
procedure oriented programming
Functions -->A function is a block of code which performs a specific task
Its a reusable group of statements where we define using def keyword
Advantages-->code resuability,code maintainability,ease of debuggin,avoiding code duplication..
def fname(parameters): Function def
    """Doc String"""    Description
    statements(s).....
    .......                Function body
    return value(s).....
fname(args) Function call
'''
'''
#To perform sum of given objects
def add(a,b):
    """sum of objects"""
    c=a+b
    return c
print(add(12,3))#Addition
print(add('code','gnan'))#concatenation
print(add([12,5],[12,34]))#Merging
c,d=map(int,input("Enter value:").split(','))
print(c,d)
print(add(c,d))

def add(a,b):
    """sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,-34))#it returns along with None

name,age,salary="Baji",22,43000
#usage of return
def details():
    #return name,age,salary
    #return "codegnan"
    #return 12+10+5
    return
print(details())

There are 5 tyoes of arguments:
-->positional arguments
-->Default arguments
-->Keyword arguments
-->Variable length arguments(*args)
-->Keyword variable length arguments(**kwrags)

#positional arguments-->Number of arguments in function defn should
#match with function call (order has to be maintained)
#print(len(123,234)) this is as per built-in len(obj) will accept one argument
def details(name,place):
    """To store the details"""
    #name="codegnan"
    #place="Hyd"
    #return name,place
    print(f'Name is {name}')
    print(f'place is {place}')
#print(details("charan","sai"))
#print(details("sita","rama"))
#print(details("sita","home",40))#raises TypeError as only 2 arguments takes
c,d =map(str,input("Enter values:").split(','))
details(c,d)

#Default arguments -->we can make arguments as default but not first argument
#as default
#def grocery(item,price=35):
#def grocery(item="cheese",price=100):#we can also make all args as default
def grocery(item="Burger",price):#non default always follows default
    """usage of default aruguments"""
    print(f'The item is {item} and price is {price}')
grocery("Milk",32)
#grocery(32,"Milk")
grocery("Bread")#By default we have given price as 35
grocery("Bread",32)
grocery()
'''

#Keyword arguments -->whenever we want to specify the name of argument
def employee(name,salary,role,place="codegnan"):
    """Keyword arguments usage"""
    print(f'Employee name is {name},role is {role} and salary is {salary},works in {place}')
employee("charan",20000,"TL")
employee(salary=25000,role="DA",name="Baji")
employee("Gopi",80000,"IT","Wipro")

