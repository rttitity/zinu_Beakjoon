import sys

N = int(input())
Nlist = list(map(int, sys.stdin.readline().split()))

print(min(Nlist))
print(max(Nlist))