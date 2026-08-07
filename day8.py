'''
Tokens -->keywords,identifiers,literals,operators,punctuators,variables
operators-->Numeric data (int,float,complex),bool
control flow -->if ,elif,else,for,while
Sequences-->strings,lists,sets,tuples,mapping(dict)
#Strings -->Group of characters,we use singlen or double or triple quotes
#for representation of strings...
#Strings are Immutable,Ordered,Indexed collection
name='Codegnan'
print(name)
print(type(name))
print(len(name))#len -->returns the number of items in container
#index() -->fetch the object(position) starts at 0 and ends at len(obj)-1
#we use [] representation
print(name[0])
print(name[5])
#print(name[25])#Index error -->as its out of range
#Negative Indexing -->-1 to len(obj)
print(name[-1])#it returns last character
print(name[-3])
#print(name[-33])#index error
#Slicing -->we can access group of characters(objects)
#we use [start:end] #start default-->0,start is included,end is excluded
print(name[:])#returns entire string
print(name[0:])#returns entire string
print(name[:4])#starts at oth index before 4th index
print(name[1:5])
name='Baji'
print(name)
print(name[:])
print(name[0:])
print(name[0:])
print(name[0:3])
name='python'

print(name[3:7])
print(name[7:3])#returns empty as strings are immutable
#Slicing is applicable from lower index to higher index
print(name[:45])#returns till end of the string
print(name[45:])
print(name[-1:-5])
print(name[-5:-1])
#print'on' from above string
print(name[4:])
print(name[4:6])
print(name[-2:])
print(name[1:-2])
print(name[2:-6])
#observe +ve,+ve,-ve,-ve&+ve,-ve all possibilities

#Striding -->[start:end:step]
course='DataAnalysis'
print(len(course))
#Data -->result
print(course[:4])
print(course[4:])
print(course[-3:])
print(course[::1])#returns all characters
print(course[::2])#includes start to ens skipping1 character
print(course[1:6:3])#[1:6] -->ataAn -->[1:6:3] -->aA
#tnys
print(course[2::3])
print(course[::-1])
print(course[::-2])
#task:Workout with all possibilities of slicing and striding on a example
name='codegnan'
#name[3]='w' #strings are immutable
#Operations on strings-->Indexing ,Concatenation,Repetition
print(name * 3)
print('*' * 25)#repetition

#Concatenation -> combing strings
data='baji'+'python'
print(data)
print('123' * 4)#Numeric String

print('code in codegnan')

for i in 'codegnan':
    print(i,':')
#in above case we get every character line by line
  
for i in 'codegnan':
    print(i,end=' ')

name="codegnan"
#Built-in functions -->len(),min(),max(),sorted()
print(len(name))
print(min(name))#alphabetical order ASCII ordering
print(ord('A'))
print(ord('a'))
print(chr(97))
print(max(name))
print(sorted(name))#returns a list by sorting all elements'''
#Methods on strings -->case -Conversions,Finding/Searching...
name='Codegnan data'
#case-conversions -->upper(),lower(),title(),capitalize()
a=name.upper()
print(a)
b=name.lower()
print(b)
#Capitalize() -->converts first letter to uppercase
c=name.capitalize()
print(c)
d=name.title()#converts every word first letter to uppercase
print(d)
#Task: A-Z
#use loops and strings to return A-Z


