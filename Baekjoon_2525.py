t, m = input().split()
x = int(input())
M = int(m)
T = int(t)
M = M + x

if M > 59:
    T = T + M//60
    M = M - 60*(M//60)
if T > 23:
    T = T - 24

print(T, M)