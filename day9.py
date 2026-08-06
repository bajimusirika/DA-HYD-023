'''price = list(map(int, input().split(',')))

total = 0
for i in price:
    total += i

print(total)
password = input("Enter password: ")

upper = lower = digit = special = 0

for ch in password:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1
    elif '0' <= ch <= '9':
        digit += 1
    else:
        special += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Special Characters:", special)
email=input().split()
for mail in email:
    print(mail.split("@")[1])'''
series_name = input("Enter Netflix series name: ")
episodes = int(input("Enter number of episodes watched: "))

print("Series:", series_name)
print("Episodes watched:")

for i in range(1, episodes + 1):
    print("Episode", i)


