'''
Identity Opearators -->checks the identity of an object -->id()

a=5
b=a
print(id(a))
print(id(b))
c=5
print(id(c))
print(a is c)
print(5==5)
a=[1,3,5,6]
b=a
print(id(a))
print(id(b))
c=[1,3,5,6]
print(id(c))
#As we have Lists(Mutable collection) both c and a lists will have different
#ids whereas values are same
print(c is a)#output False
print(c==a)#out[ut True
print(a is not c)
#Bitwise Operations --> we perform bitwise operations over operands
#& (and),| (or) ,^(XOR),shifting Operators(<<,>>)
#Number will be converted into binary format
print(5&3)#both 5 and 3 converted binary and bitwise and is performed
print(5|3)#bitwis1932e OR
print(5^3)#bitwise XOR
print(5 and 3)#here and is logical operator checks for both existance
#returns 5 in above case
print(5 or 3)#returns 3 in the case
#Leftshift Operator << ,Right shift Operator >>
print(5<1)#False comparsion
print(5<<1)#Left shift operation by 1 position
print(5>>1)#Right shift operation
print(15<<2)#convert 15 to binary and perform 2 times left shifting
print(15>>2)#sane 2 times right shifting

#Input formatting -->input(),int(input()),float(input())
#you know -->single input
#2or3 inputs-->map
#group of integers -->list(map(int,input().split(','))
names=input("Enter the names:").split(',')
print(names)
name1,name2=map(str,input("Enter the Friends Names:").split(','))
print(name1,name2)'''
#Tokens -->Numeric Datatypes -->Operators -->Flow of the progarm
#control Block statements-->they control the flow of the program
#when to execute,how to execute
#conditional statements -->if,else,elif (rely on condition to be executed)
#Repetition statements (Loops) --> for,while
#conditional statements --> if usage
'''
Syntax:
if <condition>:
    statement(s)...
    ......

#age=15
age=int(input("Enter your age"))
if age>18:
    print('your age',age)

age =int(input("Enter your age:"))
if age>18 and age in [19,21,20]:
         print('your age is',age)
print(age)
#else keyword -->if-else
else:
    statement(s)...
if-else usage as below:
if <condition>:
    statement(s)....
    ....
else:
    staement(S).....
    .....

#vote Eligiblity ->To check his/her voter eligibility and give access...
age=int(input("Enter your age:"))
if age>18:
    print("you have voter eligibility and age is",age)
    print("Access Granted")
else:
    age = 18-age
    #print("you dont have aligibility as your age is",age,"years")
    print("you need to wait for more",age,"years")'''
#same case let's use only nested --> if,else
if age>0:
    if age>18:
        print("you have voter eligibility and age is",age)
        print("Access Granted")
    else:
        age = 18-age
        #print("you dont have aligibility as your age is",age,"years")
        print("you need to wait for more",age,"years")
else:
    print("you have entered -ve values/zero enter only +ve")
'''
task:student marks and grade analyzer
90-100-->'A'
80-89-->'B'
70-79-->'c'
60-69-->'D'
>60-->fail
#also -ve cases should not be allowed and marks should not be greater than 100
    
