#elif keyword --> if-elif-else
'''
if <condition1>:
    statement(s)...
    ......
elif <condition2>:
    statement(s)...
    .......
elif <condition3>:
    statement(s)....
    ................
    ........
else:
    statement(s)...
    .......
'''
'''
marks = int(input("Enter the student marks:"))
if marks<0 and marks >100:
    print("Entered values should be greater than 1 and less than 100")
elif marks >= 90 and marks <=100:
    print("user has secured Grade A")
elif marks >= 80 and marks <=89:
    print("user has secured Grade B")
elif marks >= 70 and marks <=79:
    print("user has secured Grade C")
elif marks >= 60 and marks <=69:
    print("user has secured Grade D")
elif marks < 60:
        print("user has failed,study again")
else:
    print("No -ve values ")

#Task --> same usecase try with if-elif-else usage in other way
    
#Voter Eligibility checkcase -->make sure to satisfy all possible condition
#>=18 -->Access
#<18 --> no of years eligibility should tell
#negative values -->not acceptable
age = int (input("enter your age:"))
if age >=18 and age <=100:
    print("-----user has voter Eligibility------")
    print("-----Access Granted------")
elif age <18 and age >0:
    print("------user still need to get voter Eligibility---")
    print("------user need to wait for more",(18-age),"years----")
else:
    print("----only +ve values and less than 100 Acceptable----")
#output -->print()
#Output Formatting -->old style formatting (using commas)
#% usage (%f,%d),.format() usage,fstring notation
a,b=7,9
print(a)
print(b)
print(a,b)
name="Codegnan";batch="DataAnalyst"
print(name,batch)#by default sep is having space
print(name,batch,sep=',')
#end='\n',\t -->tab space
print(name,batch,end='\t')
print(a,b)
print(a,b,end='')
print('Hyd')'''
name='Codegnan';age=7;batch='DA-o23';place='Hyd'
'''
print(batch,'is in',name)
print(name,'is in',place,'age is',age,'years')
#Old style formatting -->%d -->integer,%s -->string,%f -->float
salary=25000
print("His salary is %d"%(salary))
print("His salary is %f"%(salary))
print("His salary is %.1f"%(salary))#%.1f --> rounding to 1 decimal
'''
#.format() usage
print("{} is in {}".format(name,place))#order matters
#fstring usage (more recommended)
print(f'{name} is in {place}')
print(f'{"baji"} is in {name}')
    
        


        
