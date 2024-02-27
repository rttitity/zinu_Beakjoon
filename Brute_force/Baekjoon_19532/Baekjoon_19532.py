'''
# ZeroDivisionError 오류 코드
import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

y = ((a * f) - (d * c)) // ((a * e) - (d * b))
x = (c - (b * y)) // a

print(int(x), int(y))

'''

'''
# 위 문제풀이와 풀이방법은 동일하나 왜 이 방법은 되고 위에 방법은 안되는지 모르겠음....
import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split())

print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))
'''


# 시간이 훨씬 더 소요되는 모든 경우의 수를 찾는 브루트 포스 문제풀이 방법
import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

for x in range(-999,1000):
    for y in range(-999,1000):
        if ((((a*x) + (b*y)) == c) and (((d*x) + (e*y) == f))):
            print(x, y)




