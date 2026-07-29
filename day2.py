'''
Tokens -->Variables,Punctuators
Variables -->Named memory location,its a placeholder for data
#Rules are to be allowed

#MultiAssignment of variables
name,age,place = 'codegnan',7,'Hyd'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='------->')

#a,b = 2,4,5 #ValueError as too many values to unpack
#Reassigning variables

name = 'Codegnan'
a,b = 45,1.5
print(a,b)
a,b = b,a
print(a,b,sep=',')

#a,b = b,c #NameError as c is not identified
#print(a,b)

#Deleting the Variables -->
#del a
#]print(a)
#del a,b
#print(a,b)

#Punctuators --> [](lists),()(tuples),{}(Dict,sets)
name = 'Codegnan';age = 7;course = 'Data_Analysis'
print(name,age,course)


#Datatypes --> Numeric (int,float,complex),boolean,None,
          #-->Sequeences -->Lists,Tuples,Sets,Strings,
           #                Frozensets,mappings(dict)

#Numeric type -->int,float,complex

#int datatype -->quantity,age..
age = 7
print(age)
print(type(age))#type --> returns the datatype of object

print(type(234))

#quantity = 03 #it is not allowed
#print(quantity)

#float datatype --> temp,salary,price
price = 750.24;discount = 2.5
print(price,discount)
print(type(price))

#complex -->combination of real and imag
i2 = 4
data = 5 + i2
print(data)

data = 5 + 2j #j is imag representation
print(data)
print(type(data))

#Boolean --> True/False
valid = True
print(type(valid))
error = False
print(type(error))


#TypeCasting --> Converting one type to another type
#python by default follows Implicit Type
#Every built-in datatype is a built-in function
age = 35
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age) #returns True for existing data
print(d)
e = bool(0)
print(e)

#Float -->Typecasting
age = 35.75
print(type(age))
b = int(age)
print(b)
c = complex(age)
print(c)
d = bool(age)
print(d)
e = bool(0)
print(e)

#complex -->Typecasting
data = 2 + 5j
print(type(data))
d = bool(data)
print(d)
print(type(d))
'''
f = 45 + 2.5 + 2 + 3j + False
print(f)







