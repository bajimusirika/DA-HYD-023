'''
sequences-->Strings,Lists,Tuples,Sets
Mapping-->Dictionary
'''
'''
#Lists-->collection of heterogenous elements(items)
#List -->Indexed,Ordered,Mutable,Heterogenous,we use [] to store the data
marks =[35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)
#Operations:Indexing,Slicing,Striding,Membership,Merging,Repetition
'''
'''
#Nested lists-->A list inside another list
names=['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(names)

print(len(names))
print(names[0])
print(names[3])
print(names[-3])
print(type(names[0]))
print(names[0][:4])
print(names[0][4:])
#get the output as Cdga
print(names[0][::2])
names[0]=names[0][::-1]
print(names)
print(names[3])
print(len(names[3]))
print(names[3][2])
#Indexing ,Slicing -->Mutable
names[2]='python'
print(names)
#by indexing if we change the elements ,length of collection will remain same
names[4]=['codegnan','pfs','jfs']
print(names)
print(len(names))
print(names[3][1:3])
print(names[4][1:4])
print(names[4][0])
print(names[4][0][4:])
names[2:4]='Baji','Srikanth','chinna','sita'
print(names)
#In slicing whatever elements u pass as per logic length keeps on increase
names[3:6:2]=['python','java']
print(names)
'''
#create a nested list with strings ,lists and work on Indexing,Slicing,Striding
#added advantage if u cold add string functions also to it
#lists Functions -->append(),insert(),extend(),pop(),remove(),clear()
#index(),count(),copy(),sort(),reverse()
names=['codegnan','Baji']
#append()-->inserts single element to the end of the list
names.append('data')
#print(names)
#names.append('Analysis','agents')#type error
names.append(['analysis','agents'])
#print(names)
#append() will always increment the length of list by 1
#print(names[3])
#print(names[3].append('chatgpt'))#it returns None as append is applicable
#on list not print
#print(names[3])
print(names)
#extend()-->inserts multiple elements to the end of list
'''
names.extend('analysis')
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,75,35,25])
print(names)
#names.extend(35,45) TypeError
#print(names)
#insert(index,object)-->inserts given object before index
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4].['a','b'])#syntax Error
#print(names)
names.insert(-1,'AAA')
print(names)'''
#pop(),remove(),clear()
#pop()by default last,else given index
print(names.pop())
print(names)
names.pop(2)
print(names)
#remove() we can remove a specific value
names.extend([23,14,15])
print(names)
names.remove(14)
print(names)
#names.remove(14) valueError
del names[1:3]#del keyword will apply permanent changes
print(names)
names.clear()#clear() will remove all elements and returns empty list
print(names)
#data=['codegnan','baji','python','java']#input
#output should be as follows
'''
0:codegnan
1:saketh
2:python
3:java
'''
