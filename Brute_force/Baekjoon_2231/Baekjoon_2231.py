N = int(input())

number = N
N_number = 0        #N의 자리수

# N값 자리수 구하기
while number >= 1:
    number = number//10
    N_number += 1

# (N - x) ~ N 까지의 수 중 생성자 찾기
V = N - (N_number * 9)                  # N의 각 자리수 합에서 나올수 있는 최대 수를 빼서 범위를 최소화
if N < 18 :                             # 18 이하의 숫자는 아래 반복문에서 시작범위가 1보다 작으므로 V를 0으로 만들어주는 조건을 걸었다.
    V = 0

# i가 범위수 V부터 입력된 N의 범위까지 분해합을 찾는다.
for i in range(V, N):
    num = sum(map(int, str(i)))
    num_sum = i + num
    if num_sum == N:
        print(i)
        break
    if i == N-1:
        print(0)