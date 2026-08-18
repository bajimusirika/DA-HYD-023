n = 28
sum = 0

for i in range(1, n):
    if n % i == 0:
        print(i)
        sum = sum + i

print("Sum =", sum)

if sum == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

