'''marks = []
for i in range(3):
    mark = int(input("Enter mark: "))
    marks.append(mark)
print("Original marks:", marks)
marks.insert(0, 90)
marks.extend([75, 85])
print("After adding:", marks)
if 75 in marks:
    marks.remove(75)
removed = marks.pop()
print("Removed mark:", removed)
print("Final list:", marks)
print("Length:", len(marks))
'''
'''numbers = [20, 10, 30, 20, 40, 20]

numbers.sort()
print("Ascending:", numbers)

numbers.reverse()
print("Descending:", numbers)

n = int(input("Enter number to search: "))

if n in numbers:
    print("Count:", numbers.count(n))
    print("First index:", numbers.index(n))
else:
    print("Number not found")

print("Smallest:", min(numbers))
print("Largest:", max(numbers))
print("Total:", sum(numbers))'''

'''numbers = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even:", even)
print("Odd:", odd)

print("First 3:", numbers[:3])
print("Last 3:", numbers[-3:])

backup = numbers.copy()
numbers.clear()

print("Original:", numbers)
print("Backup:", backup)'''
'''names = ["Asha", "Rahul", "Asha", "John", "Rahul"]

names = set(names)

names.add("Meera")
names.update(["Arun", "Priya"])

if "John" in names:
    names.remove("John")

names.discard("David")

for name in names:
    print(name)'''

'''python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}

print("All students:", python_students.union(da_students))
print("Both courses:", python_students.intersection(da_students))
print("Only Python:", python_students.difference(da_students))
print("Only one course:", python_students.symmetric_difference(da_students))

print("DA subset of Python:", da_students.issubset(python_students))
print("Python superset of DA:", python_students.issuperset(da_students))
print("Disjoint:", python_students.isdisjoint(da_students))

print("\nStudents in both:")
for name in python_students.intersection(da_students):
    print(name)'''
