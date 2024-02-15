X = int(input())
N = int(input())
cash = 0
for i in range(N):
    a, b = input().split()
    A = int(a)
    B = int(b)
    cash += A * B
if cash == X:
    print("Yes")
else:
    print("No")