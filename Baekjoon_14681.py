X = int(input())
Y = int(input())

if X > 0:
    if Y > 0:
        print("1")
    elif Y < 0:
        print("4")
elif X < 0:
    if Y > 0:
        print("2")
    elif Y < 0:
        print("3")