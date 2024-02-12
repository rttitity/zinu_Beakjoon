a = int(input())
b = int(input())

x3 = b%10
x4 = (b%100 - x3)//10
x5 = b//100
print(a * x3)
print(a * x4)
print(a * x5)
print(a*b)