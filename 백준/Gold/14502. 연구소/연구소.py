from copy import deepcopy
from collections import deque

def virus(board):
    virus_lst = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                virus_lst.append((i,j))

    while virus_lst:
        # 바이러스 퍼져나가기
        y,x = virus_lst.popleft()
        for dy,dx in ((-1,0),(0,1),(1,0),(0,-1)):
            ny,nx = y + dy, x + dx
            if 0<=ny<n and 0<=nx<m and board[ny][nx] == 0:
                board[ny][nx] = 2
                virus_lst.append((ny,nx))

    return board

def calculate_warningzone(board):
    global warning_area
    global safety_area
    safety = 0
    warning = 0     # 위험지역넓이
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                warning += 1

                if warning > warning_area:
                    return

    if warning<warning_area:
        warning_area = warning
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    safety += 1

        safety_area = safety

if __name__=='__main__':
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    test_board = deepcopy(board)
    empty_index = []    # 빈칸 인덱스 리스트
    warning_area = 1000000
    safety_area = 0


    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                empty_index.append((i,j))

    l = len(empty_index)
    for i in range(l):
        wall1_y, wall1_x = empty_index[i]
        test_board[wall1_y][wall1_x] = 1
        for j in range(i+1, l):
            wall2_y, wall2_x = empty_index[j]
            test_board[wall2_y][wall2_x] = 1
            for z in range(j+1,l):
                wall3_y, wall3_x = empty_index[z]
                test_board[wall3_y][wall3_x] = 1

                # 바이러스 퍼져나가기
                test_board2 = deepcopy(test_board)
                arr = virus(test_board2)

                # 위험지대 계산 and 최소값 갱신
                calculate_warningzone(arr)

                test_board[wall3_y][wall3_x] = 0
            test_board[wall2_y][wall2_x] = 0
        test_board[wall1_y][wall1_x] = 0

    print(safety_area)