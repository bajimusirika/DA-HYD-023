#data=['codegnan','baji','python','java']#input
#output should be as follows
'''
0:codegnan
1:saketh
2:python
3:java'''
'''
data = ['codegnan', 'saketh', 'python', 'java']

for i in range(len(data)):
    print(i, ":", data[i])
    '''
'''
Lists,Tuples..
#List -->Mutable,Ordered,Heterogenous
#index(),count(),copy(),sort(),reverse()
details=['codegnan',7,2018,'Hyd']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21))#it returns first occurance
print(details.index(21,6))
#print(details.index('python'))#value error
print(details.count(21))
print(details.count('python'))#it returns 0 as we dont have it
'''
'''
#copt() -->shallow copy of the given collection
data = ['codegnan', 'Baji', 'python', 'Hyd']
new =data.copy()
print(new)
print(len(new))
print(type(new))

new[2]='Agentic AI'
print(new)
print(data)
data.append('Baji')
print(data)
print(new)
'''
'''
data=[1,4,5,[21,34,45],23]
print(data)
new=data.copy()
print(new)

new[3][2]='Agents' #whenever we make changes in nested list original will also be effected
print(new)
print(data)

new[1]='python'
print(new)
print(data)
'''
'''
marks=[14,24,-4,27,3]
print(marks)
#print(marks.sort()) #returns None
#print(marks) #returns ascending order
#marks.sort(reverse=True) #returns in Descending order...
#print(marks)
marks.insert(2,'code')
#marks.sort()
#reverse() -->returns in reverse order
marks.reverse()
print(marks)
print(marks[::-1])

#type(),len(),max(),min(),print() 
print(sorted('codegnan'))#returns list in ascending order
#print(sorted(['code','23',34,45])) #raises error

#Tuples --> Tuples are Indexex,Ordered,Heterogenous,Immutable collectin
#dimensions,coordinates,database records,we prefer() for tuple notation
a=()
print(type(a))
print(len(a))
dimensions =1.5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))
'''
#Operations -->Indexing,Slicing,Striding,Membership,Merging,Repetition
courses=('PFS','JFS',('DA','DS'),'Agentic AI',[100,6,6])
'''
print(courses)
print(len(courses))
print(courses[3][-2:])
#courses [2]=23 #tuples are immutable
courses[-1].append('codegnan')
print(courses)
#create a Nested tuple as above and work on slicing,striding and list functions
print('PFS' in courses)#Membership
d=courses*2 #Repetition
print(d)
e=courses+(2,3,4,5) #merging
print(e)

#Tuples Immutable -->count(),index()
#print(courses.index('AgenticAI')) #returns first occurance
print(courses.count('Agents'))
#print(courses.sort()) #AttributeError -->sort() is in Lists not in Tuples
print(sorted(courses[-1]))
#print(sorted(courses))#as we have mixed type
#Typecasting
d=tuple(sorted((23,12,3,4,5)))
print(d)

#accept group of integers space separated
a,b=map(list(int,input('Enter the values').split()))
print(a,b)

a=tuple(map(int,input('Enter the values').split()))
print(a)

print('9+4')
print(eval('9+4'))

a=eval(input("Enter a list"))# in this case u can exactly enter data as list
print(a)
print(type(a))'''
#Task:Take a user input as string ,do this in two ways..
'''
1)give the count of each repeating character
Test case 1:programming
o/p:r is repeating 2 times #count function
g is repeating 2 times
m is repeating 2 times

r is repeating 2 times
index=[1,4]
g is repeating 2 times
index=[3,10]
m is repeating 2 times
index=[6,7]
'''


