'''

Functions-->Arguments Usage (Variable length arguments)
        -->Keyword variable length arguments(**kwargs)
Exception Handling / scope of variables / Bulit in Functions
Exception handling -->It is a mechanism that helps to respond or make the flow
of execution in normal way ,without this errors will occur and disrup the
flow of program
Common Exceptions-->value Error ,TypeError,IndexError,AttributeError,
ZeroDivisionError...
Syntax:
try:
    #code that will cause the exception
except Exception as e:
    #code will catch the exception
finally:
    #runs irrespective or try/except...
    ...

#basic Exception handling
try:
    #a=10
    a=int(input('Enter value:'))
    result=20/a
    #print(result)
#except Exception as e:
    #print(e)#it returns the msg of errors
except ValueError:
    print(f'Invalid entry enter only integer values')
except ZeroDivisionError:
    print(f'Division by zero is not possible')
except NameError:
    print(f'Check the name of variable properly')
    
#similarl if we want to check other Errors --> IndexError,AttributeError
try:
    a=[10,20,30]
    print(a[5])
#except Exception as e:
    #print(e)#returns the message of Error
except IndexError:
    print(f'Check length of list properly and access elements')
except AttributeError:
    print(f'Dont rush write the name properly')

#handling exceptions at a time
try:
    a=[10,20,30]
    a.append(24)
    print(a[5])
except (IndexError,AttributeError) as e:
    print(e)
    a=list(map(int,input('Enter').split(',')))
    print(a)

#BMI-->bmi=(weight)
#Feet -->12 inches --> 1 inch ->2.4cm
while True:
    try:
        weight=int(input('Enter the weight in kgs:'))
        height=int(input('Enter the height in metres:'))
        #write my logical condition
        if weight>0 and height>0:
            break #stops the flow of execution of program
            #continue #skips the current iteration and proceed for rmng item
            #print('Bye')
        else:
            print('Make sure to enter only correct values')
    except ValueError:
        print(f'Make sure to enter weight as interger only,height also as number')
bmi=((weight)/(height)**2)
print(bmi)
#Use Exception Handling along with jumping statement in
#Functions BMI Task
'''
#scope of Variables -->Scope is basically the region/area where it is accessiable
#local,Global scope
#Global Keyword,Enclosing Scope(Nested Functions nonlocal keyword)
'''
#Local Scope -->variables defined inside the function accessible inside

def display():
    """Usage of Local Scope"""
    name='codegnan'
    print(name)
display()
#print(name)#raises Error

#Global Scope -->Defined outside and can be accessible anywhere
#in the script
place ='Hyd'
def display():
    """Usage of Local&Global Scope"""
    name='codegnan'
    print(name)
    print(f'{name} is in {place}')
display()
print(place)

#Modifying global variable inside the function and accesible outside the function
count=0
def data():
    """Usage of global keyword"""
    global count
    count=count+5
    print(f'value inside function is {count}')
data()
print(f'value outside function is {count}')

#Local variable has high priority over global variable
count=20
def data():
    """Usage of local vs global variable"""
    count=5#local variable
    count=count+5
    print(f'value inside function is {count}')
data()
print(f'value outside function is {count}')

#Enclosing scope(nonlocal keyword)
def outer():
    """Outer function with local variable"""
    count=5
    def inner():
        """Nested Function"""
        nonlocal count
        count=count+10
        print(f'value inside is {count}')
    inner()
    print(f'value outside is {count}')
outer()
'''
#Built-in Functions -->variables Builtinscope
len=56
print(len+4)

print(len('codegnan')) #TypeError -->Never ever use Builtin functions as Identify

