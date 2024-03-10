from collections import deque
from copy import deepcopy

def find_block_group():
    # 한칸한칸마다 bfs를 돌려야함.
    check = [[0]*n for _ in range(n)]
    block_group_list = []
    dq = deque()

    for i in range(n):
        for j in range(n):
            temp = []
            # 기준 색깔 저장
            if check[i][j] == 0 and board[i][j] != -1 and board[i][j] != 0 and board[i][j] != -5:
                std_color = board[i][j]

                temp.append((i,j))
                dq.append((i,j))
                check[i][j] = 1

                while dq:
                    y,x = dq.popleft()

                    for d in range(4):
                        ny,nx = y + dir[d][0], x + dir[d][1]

                        if 0<=ny<n and 0<=nx<n and check[ny][nx] == 0 and board[ny][nx] != -1 and board[ny][nx] != -5 and (board[ny][nx] == std_color or board[ny][nx] == 0):
                            temp.append((ny,nx))
                            dq.append((ny,nx))
                            check[ny][nx] = 1

            if len(temp) >= 2:
                block_group_list.append(temp)

            for r in range(n):
                for c in range(n):
                    if board[r][c] == 0:
                        check[r][c] = 0

    sorting_list = []  # (블록그룹크기, 무지개블록갯수, 기준블록행이가장큰것, 기준블록열이 가장큰것)
    if block_group_list:
        for i in range(len(block_group_list)):
            rainbow_block = 0
            for y,x in block_group_list[i]:
                if board[y][x] == 0:
                    rainbow_block += 1

            sorting_list.append([len(block_group_list[i]),rainbow_block,block_group_list[i][0][0],block_group_list[i][0][1],i])

    else:
        print(ans)
        exit(0)

    sorting_list.sort(key = lambda x:(-x[0],-x[1],-x[2],-x[3]))
    proper_list_li = sorting_list[0][4]
    proper_list = block_group_list[proper_list_li]

    return proper_list

def gravity():
    for c in range(n):
        pp, np = n-1, n-1

        while True:
            # 현재가르치는 위치가 빈칸일때
            if board[pp][c] == -5 :
                # 현재 탐색 위치가 검은색블록이다
                if board[np][c] == -1:
                    np -= 1
                    pp = np
                elif board[np][c] == -5 :
                    np -= 1

                else:
                    board[pp][c], board[np][c] = board[np][c], board[pp][c]

            else:
                pp -= 1
                np = pp

            if np < 0:
                break

def rotate():
    for y in range(n):
        for x in range(n):
            next_board[y][x] = board[x][n-1-y]

if __name__=='__main__':

    n, m = map(int,input().split())     # n 맵크기, m 색 갯수

    board = [list(map(int,input().split())) for _ in range(n)]  # 맵 정보
    dir = [(-1,0),(0,1),(1,0),(0,-1)]                           # 이동배열
    ans = 0

    while True:
        # print('--------------턴시작전배열----------------')
        # for i in range(n):
        #     for j in range(n):
        #         print('%6d' % board[i][j], end=' ')
        #     print()
        # print('------------------------------')
        # 적합한 블록 그룹 찾기
        list = find_block_group()

        # 블록 삭제 및 점수 획득
        ans += len(list)**2
        for y,x in list:
            board[y][x] = -5

        # 중력 -> 회전 -> 중력
        gravity()

        next_board = [[0] * n for _ in range(n)]
        rotate()
        board = deepcopy(next_board)

        gravity()



