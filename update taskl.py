#1.student Marks Manager
'''
marks = []
for i in range(3):
    mark = int(input("Enter mark: "))
    marks.append(mark)
print("Original marks:", marks)
marks.insert(0, 90)
print(marks)
marks.extend([75, 85])
print(marks)
if 75 in marks:
    marks.remove(75)
remove = marks.pop()
print("Removed mark:", remove)
print("Final list:", marks)
print("Length:", len(marks))
'''
#2.Number list analyser
'''
numbers=[20,10,30,20,40,20]
numbers.sort()
print("Sorted list:", numbers)
print("Ascending values:")
for i in numbers:
    print(i)
numbers.reverse()
print("Reversed list:", numbers)
print("Descending values:")
for i in numbers:
    print(i)
num=int(input("Enter the number to search: "))
if num in numbers:
    print("Count:", numbers.count(num))
    print("First Index:", numbers.index(num))
else:
    print("Number not found")
print("Smallest number:", min(numbers))
print("Largest number:", max(numbers))
print("Sum:", sum(numbers))
'''
#3.Even and odd number seperator
'''numbers = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even:", even)
print("Odd:", odd)

print("First three numbers:", numbers[:3])
print("Last three numbers:", numbers[-3:])

backup = numbers.copy()
numbers.clear()

print("Original list:", numbers)
print("Backup:", backup)
'''
#4.Unique name manager
'''names=['Asha','Rahul','Asha','John','Rahul']
a=set(names)
print(a)
a.add('Baji')
print('Added:',a)
a.update(['Nirhya','Keerthi'])
print('Updated:',a)
if 'John' in names:
    a.remove('John')
    print('Removed:',a)
a.discard('Charan')
print('Discarded:',a)
for i in names:
    print(i)
'''
#5.Course student comparision
'''python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"} 
total_students = python_students.union(da_students)
print(f'Total Studens: {total_students}')
both = python_students.intersection(da_students)
print(f'Students learning both courses: {both}')
python = python_students.difference(da_students)
print(f'Students learning only python:{python}')
one_course = python_students.symmetric_difference(da_students)
print(f'Students learning only one course:{one_course}')
subset = da_students.issubset(python_students)
print(f'Subset: {subset}')
superset = python_students.issuperset(da_students)
print(f'Superset:{superset}')
disjoint = python_students.isdisjoint(da_students)
print(f'Disjoint:{disjoint}')

if da_students.issubset(python_students):
    print("DA is  subset of Python")
else:
    print("DA is not a subset of Python")
    
if python_students.issuperset(da_students):
    print("Python is superset of DA")
else:
    print("Python is not a superset of DA")  
if python_students.isdisjoint(da_students):
    print("Both sets are Disjoint")
else:
    print("Both sets are not Disjoint")

print("Union:")    
for i in python_students.union(da_students):
    print(i)
print("Intersection:")
for j in python_students.intersection(da_students):
    print(j)
'''
