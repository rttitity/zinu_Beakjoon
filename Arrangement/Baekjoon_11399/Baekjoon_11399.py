import sys

N = int(input())                                                            # 자연수 갯수 N
N_list = list(map(int, sys.stdin.readline().split()))                       # 각 사람들이 돈을 인출하는데 걸리는 시간 입력

N_list.sort()

sum_time = 0
result = 0
for i in N_list:
    sum_time = i + sum_time
    result += sum_time
    #print(sum_time)
print(result)
