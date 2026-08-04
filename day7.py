'''
Usage of else with for --> the else 
#for with else...
work_log=[0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak=0
current_streak=0
for day in work_log:
    if day ==1:
        #print(day)
        current_streak=current_streak+1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
            
    else:
        current_streak=0#streak break
else:
    print(f'Longest Streak is {longest_streak}')
#In this case when the entire loop execution is done we get result of
#else block
#same program with break usage

work_log=[0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak=0
current_streak=0
for day in work_log:
    if day ==1:
        #print(day)
        current_streak=current_streak+1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
            break
    else:
        current_streak=0#streak break
else:
    print(f'Longest Streak is {longest_streak}')
#for-else with Notifications scenario
notifications=[0,0,0,1,0]
for notifications in notifications:
    if notifications == 1:
        print("unread notification")
        break
else:
    print("All Caught up")
#try to make notifications from user --> list of integers
notifications=list(map(int,input('Enter values-->0 or 1:').split(',')))
print(notifications)
for notifications in notifications:
    if notifications == 1:
        print('unread notification')
        break
else:
    print('All Caught up')'''
#while -->it relies on Condition,it will be completely executed until the
#condition is satisified...
'''
syntax while:
while<condition>:
    statement(s)...
    .......
    .......

while True:
    print("Yes")

#It runs an infinite loop we need to press Ctrl+c
i=0 #initialised statement
while i<=10:
    print(10-i)
    i=i+1 #count
#Get the counter from 10 to 1
i=10
while i>=1:
    print(i)
    i=i-1
'''
#banking scenario -->PIN authentication if more than 3 attempts
#Account locked..
pin="9390"
max_attempts=3
current_attempts=0
while current_attempts <= max_attempts:
    entered_pin=input("enter the pin:")
    if entered_pin==pin:
        
        print("login successfully")
        break
        #continue #it holds for this condition and skips to the next part of 
    else:
        print("enter pin is wrong..try again carefully")
        current_attempts += 1
else:
    print("Account locked,try after 24 hours...")
    
    
    
    
