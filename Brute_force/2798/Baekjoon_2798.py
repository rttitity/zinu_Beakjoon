import sys
n, m = map(int, sys.stdin.readline().split())
Nlist = list(map(int, sys.stdin.readline().split()))
result =[]
x = []

for i in range(n):
#    print(Nlist[i], end=' ')
    for j in range(n):
       for k in range(n):
           if i != j and j != k and i != k:
#               print(Nlist[i], Nlist[j], Nlist[k])
                if (Nlist[i] + Nlist[j] + Nlist[k]) <= m :
                    result.append(Nlist[i] + Nlist[j] + Nlist[k])
#print(result)
#result1 = set(result)
#print(result1)
print(max(result1))

