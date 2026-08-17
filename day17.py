'''
Mapping -->Dictionary -->collection of key value pairs used to store
related data -->JSON,APIs,database records
dict() -->data ={} -->data={key:value}
Dictionary is Mutable,Indexed through keys,Ordered,Heterogenous,keys must be Uniquw
Keys must be Unique (int,strings,float values...)
'''

details={}
print(type(details))
details={'Id':'CGH4040','Name':'Baji',
         'Gender':'F','Age':22,
         'Batch':'DA23','place':'Hyd'}
print(details)
print(len(details))
'''
#Access the data from dictionary
#details[0] #keyError
print(details.keys())#it returns keys from the dictionary
print(details['Id'],details['Name'])
#if key name is not matching/invalid
#print(details['marks'])#keyError as marks is not present
details['marks']=[]
print(details)
print(type(details['marks']))
details['marks'].append(20)
print(details)
details['marks'].extend([15,20,25,20,20])
print(details)
#create a key value pair of pratice session
details['ps']=('Tuesday','Thursday','Saturday')
print(details.keys())
#Accessing 3rd day marks of student
print(details['marks'][2])
#Accessing 2nd day marks of student
print(details['ps'][1])
details['MI']=('Monday','Wednesday','Friday')
#operators -->Mutable ,indexing through keys,membership
print('Wednesday' in details)
print('MI' in details)#returns True as we have MI as key
for i in details:
    print(i)#it returns keys
for i in details.keys():
    print(f'key={i}')
    print(details[i])
for i in details.values():#returns value from dictionary
    print(i)
for i in details.items():
    print(i)
for key,value in details.items():
    print(f'key is {key}')
    print(f'value is {value}')
    
#update() -->updating the dictionary with key-values pairs
details.update({'marks':[],'ps':('Tuesday','Thursday','Saturday')})
print(details)
details['marks'].extend([25,30,20])
print(details)
marks=list(map(int,input('Enter marks:').split(',')))
print(marks)
details['marks'].extend(marks)
print(details)
'''
print(details.keys())
print(details.get('Name'))
print(details.get('Branch'))#it returns None as we dont have Branch as key
print(details.keys())

details.setdefault('Branch')#if key is not present it inserts into dict
print(details)
details['Branch']='CSE'
print(details)
print(details.setdefault('Name'))        
print(details.keys())
print(details.pop('Branch'))#we need to mention key
print(details.keys())
print(details.popitem())#pop item will removes last from the first
print(details.popitem())
del details['Id']
print(details.keys())
details.clear() #removes all elements from D
print(details)

#fromkeys()-->creates a dictionary from iterable(lists,tuples,sets,strings)
data=['baji','sri','charan']
b=dict.fromkeys(data)
print(b)
b['saketh']=31
print(b)
#Task:create a dictionary with your personal details,similar to your codegnan profile
