# grade checker
'''
marks =int(input("Enter marks:"))
#if marks >0 and marks <= 100:
if marks >= 90 and marks<=100:
    
    print("Grade:A")
    print("Remark:Outstanding!")
elif marks >= 80 and marks <=89:
    
    print("Grade:B")
    print("Remark:Excellent!")
elif marks >= 70 and marks <=79:
    
    print("Grade:C")
    print("Remark:Good!")
elif marks >= 60 and marks <=69:
    
    print("Grade:D")
    print("Remark:Fair!")
elif marks >= 50 and marks <=59:
   
    print("Grade:E")
    print("Remark:Poor!")
elif marks < 50:
   
    print("Grade:F")
    print("Remark:Failed!")
else:
    print("Invalid marks entered")
    
# even number

n=int(input("Enter a number:"))
if n==0:
    print("Zero neither even nor odd")
elif n<0:
    if n%2==0:
        print(" negative even number")
    else:
        print(" negative odd number")
elif n>0:
    if n%2==0:
        print("even number")
else:
    print("odd number")
    '''
# months
m=int(input("Enter a month number:"))
if m==12 or m==1 or m==2:
    print("season:Winter")
elif m==3 or m==4 or m==5:
    print("season:spring")
elif m==6 or m==7 or m==8:
    print("season:summer")
elif m==9 or m==10 or m==11:
    print("season:autumn")
else:
    print("Invalid month entered")
    
        



