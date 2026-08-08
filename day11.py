'''correct_code biryani= "159"

while True:
    code = input("Enter secret code: ")

    if code == correct_code:
        print("Correct")
        break
    else:
        print("Wrong")
'''

'''
import random

otp = 1234  
attempts = 0

while attempts < 7:
    if int(input("Enter OTP: ")) == otp:
        print("Verified")
        break
    attempts += 1
    print(f"Wrong. {7-attempts} left")
else:
    print("Blocked")'''
'''
count = 0

while True:
    food = input("Enter food: ")

    if food == "exit":
        print("Thank you for ordering!")
        print("Total orders:", count)
        break

    print(food, "added to order")
    count = count + 1
    '''
Secret="python"
Current=0
max_attempts=3
while Current<max_attempts:
    a=input()
    if(a==Secret):
        print("access again")
        break
    else:
        remaining=max_attempts-Current
        print(f"wrong guess or you have only")
        Current += 1
else:
        print("chances over")



