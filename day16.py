'''
s = input("Enter a string: ")

for ch in s:
    if s.count(ch) > 1:
        print(f"{ch} is repeating {s.count(ch)} times" )  
'''
'''
s = input("Enter a string: ")
visited = ""

for ch in s:
    if ch not in visited:
        indexes = []

        for i in range(len(s)):
            if s[i] == ch:
                indexes.append(i)

        if len(indexes) > 1:
            print(f"{ch} is repeating {len(indexes)} times")
            print(f"index = {indexes}")

        visited += ch
'''
'''
sequences -->Strijngs,Lists,Tuples,Set,Frozenset
Mapping ->Dictionary
'''
'''
#Sets -->A Set is a unique collection of objects,unordered,Mutable,
#Hashing,Unindexed,Unique,Heterogenous
#set(),{}
a={}
print(type(a))
stud_ids={123,345,234,564,234}
print(stud_ids)
print(len(stud_ids))
print(type(stud_ids))
#print(stud_isd[2]) #TypeError
print(234 in stud_ids)
print(stud_ids*2)#ser can't be repeated
print(stud_ids+stud_ids)#two sets cannot be merged

#data ={12,3,4,5,[12,3,4],'baji'}
#print(data)#No lists inside a set (hashing technique) Lists are Mutabledata ={12,3,4,5,(12,3,4),'baji'}
data ={12,3,4,5,(12,3,4),'baji'}
print(data)
print(len(data))
for i in data:
    print(i)'''
#Methode on sets -->add(),update(),remove(),discard(),pop()
names={'sri','baji','keerthi','nithya'}
#print(len(names))
#add() will insert an element into te set(it can be anywhere but only unique)
names.add('vishnu')
print(names)
#names.add('baji','poll')
#print(names)
names.add(('sita','charan'))
print(names)
da_names={'mani','akash','baji','lachu'}
#update() we can update multiple elements (set)
'''names.update(da_names)
print(names)
print(len(names))
print(da_names)
print(len(da_names))
da_names.update(names)
print(len(names))
print(len(da_names))
#remove(),discard(),pop(),clear()
#remove() removes an element from the set (it must be a member)
da_names.remove('baji')
print(da_names)
#da_names.remove('baji')
#discard() will remove an element if its present else it ignores
da_names.discard('codegnan')
da_names.pop()
print(da_names)
print(da_names.pop())
print(da_names)
da_names.clear()
print(da_names)
da_names.add('bala')
print(da_names)
da_names.update(['baji','bala'])
print(da_names)
#copy()
d=da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)'''
#mathematical operations -->union(),intersection(),difference(),symmetric_id:
#issubset(),issuperset(),isdisjoint()
da_23={12,23,34,4,23,36}
da_24={34,46,47,36}
#event=da_23.union(da_24)
'''event=da_23 | da_24#union
print(event)
print(len(event))
#common=da_23.intersection(da_24)
common=da_23 & da_24#intersection
print(common)
print(len(common))
common=da_23.intersection_update(da_24)
print(common)#it returns None
print(da_23)#common elements are finally stored
print(da_23)
print(da_24)
#differnce() removes commmon elements and prints remaining elments from first sequence
#diff=da_23.difference(da_24)
#print(diff)
#f=d_23-d_24
#print(f)
#symmetric_difference() -->removes common elements and print all remg
#elements from two sets
symm=da_23.symmetric_difference(da_24)
#print(symm)
h=da_23^da_24
#print(h)
#issubset() -->checks for all elements to be present in other set
da_24.remove(46)
da_24.remove(47)
print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))
#isdisjoint() returns False for sets having common elements
print(da_23.isdisjoint(da_24))'''
#Length of Unique student ids in a class,where user can enter first input
#he should be giving number of student_ids,he will enter student_ids
n=int(input())
student_ids=input().split()
#print(student_ids)
result=set(student_ids)
print(result)
print(len(result))
