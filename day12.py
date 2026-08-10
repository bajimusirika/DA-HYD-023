'''
Strings -->CaseConversions,Searching &Finding,string testing methods,Replace,space removal
'''
'''
#searching ,Finding,Replacing,Joining...
a="codegnan"
print(len(a))
print(min(a))
print(max(a))

b=a.index('g')#it returns the index position
print(b)
c=a.index('n') #it returns only the first occurence
print(c)
d=a.index('n',6)#it returns the next occurence
print(d)
#e=a.index('n',8)#value etrror
#print(e)
#f=a.index('n',t)#value error
#print(f)
g=a.index('n',1,4)
print(g)

#rindex() -->returns last occurance
a='codegnan'
b=a.rindex('g')
print(b)
c=a.rindex('n')#here 'n' is occuring at 7th index
print(c)
#d=a.rindex('n',8)#it returns valueError
#print(d)

#count() -->returns the number of items object is repeating
print('codegnan'.count('n'))
print('code'.count('w'))#it returns 0 as we dont have 'w' in 'code'
print('cakshjasaksajs'.count('a'))

#find() -->first occurance but it avoid error returns -1 if substring is
#not found
print('codegnan'.find('r'))#it returns -1
print('codegnan'.find('n'))
print('codegnan'.rfind('n'))

a='Data'
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))
    
#Replacing,Splitting,Joining
#Strings are immutable
a='codegnan'
#a[4]='s'
print(a.replace('g','s'))
print(a)
a=a.replace('g','s')
print(a)
print('fghyuiki#ja#nams#njdh'.replace('#',''))
print(a.replace('x','Baji'))
a='code baji python'
print(len(a))
b=a.split()#by default if we have space it splits (returns list)
print(b)
print(len(b))
c='code','baji','python'
d = c.split()
print(d)
e=c.split(',')
print(e)
#join()
a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('BajiSri'))
print(' '.join('Baji'))

#string testing methods (boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()...
a='codegnan123'
print(a.isalnum())#returns True for alphanumeric strings else False
b='codegnan'
print(a.isalnum())
print(a.isalpha())#returns True only for alphabets
print(a.isdigit())#returns True only for digit string
print('8122466858'.isdigit())
print('1234'.isnumeric())#this has upper edge(numbers,fractions,romans)
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))

print('codegnan'.islower())
print('Codegnan'.isupper())
print('Codegnan python'.istitle())

#space removal -->strip() (removes leading and trailing spaces)
a='codegnan'
print(a.strip())
b=input("Enter the string:").strip().lower()
print(b)
'''
#zfill() filling with zeros as per the given numeric string
print('123'.zfill(4))
print('123'.zfill(7))
#center(),ljust(),rjust() -->Alignment of strings (check length and then
#modify the width accordingly)
print('hai'.center(6))
print('hai'.center(6,'#'))
print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))
