h, m = input().split()
H = int(h)
M = int(m)

M = M - 45
if M < 0:
    H = H - 1
    M = M + 60
if H < 0:
    H = H + 24

print(H, M)