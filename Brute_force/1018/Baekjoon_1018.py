import sys

# 가로(M)와 세로(N)값 입력
N, M = map(int, sys.stdin.readline().split())

# 보드 상태 입력값
bord = []
for i in range(N):                                          # 반복문을 통하여 N번만큼 M줄의 체스보드의 상태를 입력받는다.
    bord.append(list(sys.stdin.readline()))

# 체스판을 칠할 가로와 세로줄의 시작점 범위를 지정하기 위해 M과 N에서 8을 빼준다.

x_line = M - 8                                              # 가로줄의 탐색범위
y_line = N - 8                                              # 세로줄의 탐색범위

# 체스판 상태를 확인할 (x, y) 시작지점이 'W'로 시작하는지 or 'B'로 시작하는지 경우를 나누어 바꿔칠할수를 셀거기 때문에
# 'W'로 시작할 경우의 수와  'B'로 시작할 경우의 변수를 나눠놓는다.

W_start = 0                                                 # 'W'로 시작할때 몇개를 바꿔야 하는지 셀 변수
B_start = 0                                                 # 'B'로 시작할때 몇개를 바꿔야 하는지 셀 변수

# 8*8 시작점 리스트
better_list = []                                            # 가장 최적의 시작점을 찾기 위해 각각의 (x, y)에서 시작했을때 바꾼 수를 비교하기 위해 리스트를 만든다.
#print(x_line, y_line)


# 8*8로 탐색할 범위를 지정하여 반복문을 돌린다.

for y_start in range(0, y_line+1):                          # 세로줄의 탐색범위만큼 반복
    for x_start in range(0, x_line+1):                      # 가로줄의 탐색범위만큼 반복

#시작이 'W' 일때
        for y in range(y_start, 8+y_start):                 # 탐색 시작범위부터 탐색범위 + 8만큼 상태값의 리스트 세로줄을 확인
            for x in range(x_start, 8+x_start):             # 탐색 시작범위부터 탐색범위 + 8만큼 상태값의 리스트 가로줄을 확인

                if (x+y)%2 == 0:                            # 체스판 가로행중 짝수행일때
                    if bord[y][x] == 'B':                   # 체스판 상태값이 검정이라면
                        W_start += 1                        # W 시작일 경우 바꿈 포인트 1 증가
                        #print("change", x, y)
                elif (x+y)%2 == 1:                          # 체스판 가로행중 홀수행일때
                    if bord[y][x] == 'W':                   # 체스판 상태값이 하양이라면
                        W_start += 1                        # W 시작일 경우 바꿈 포인트 1 증가
                        #print("change", x, y)

        #print("W시작점", x_start, y_start, W_start)
        better_list.append(W_start)                         # W시작 바꿈포인트를 비교 리스트에 넣어준 후
        W_start = 0                                         # W포인트 변수 초기화


#시작이 'B' 일때                                              위와 동일...
        for y in range(y_start, 8+y_start):
            for x in range(x_start, 8+x_start):

                if (x+y)%2 == 0:
                    if bord[y][x] == 'W':
                        B_start += 1
                        #print("change", x, y)
                elif (x+y)%2 == 1:
                    if bord[y][x] == 'B':
                        B_start += 1
                        #print("change", x, y)

#        print("B시작점", x_start, y_start, B_start)
        better_list.append(B_start)
        B_start = 0

#print(better_list)
print(min(better_list))                                     # 비교리스트중 가장 적은값 출력