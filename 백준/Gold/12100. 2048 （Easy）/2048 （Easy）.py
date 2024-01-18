from copy import deepcopy

# 내가 짠거  백준에서 안됨
# def left(board):
#     new_board = [[0]*n for _ in range(n)]
#     for x in range(n):
#         j = 0  # 새배열 포인터
#         flag = 0 # 합침 여부 플래그
#         for i in range(n):
#             # 만약 원배열의 숫자가 있고 새 배열에 숫자가 없을때
#             # 새배열로 숫자 복사 후 원배열 방문 표시 해줌.
#             if board[x][i] != 0 and new_board[x][j] == 0:
#                 new_board[x][j] = board[x][i]
#                 board[x][i] = 0
#                 # j가 0이 아니고 합친 적없고 전숫자와 현재숫자가 같을때 합쳐줌
#                 # 합쳤으니 포인터는 그대로 있어야함 왜냐면, 새배열에 포인터 위치가 0 이 되기 때문
#                 if j != 0 and flag == 0 and new_board[x][j] == new_board[x][j-1]:
#                     new_board[x][j-1], new_board[x][j] = new_board[x][j-1]*2, 0
#                     flag = 1
#                     continue
#                 j += 1
#     return new_board
#
# def right(board):
#     new_board = [[0]*n for _ in range(n)]
#     for x in range(n):
#         j = n-1  # 새배열 포인터
#         flag = 0 # 합침 여부 플래그
#         for i in range(n-1,-1,-1):
#             # 만약 원배열의 숫자가 있고 새 배열에 숫자가 없을때
#             # 새배열로 숫자 복사 후 원배열 방문 표시 해줌.
#             if board[x][i] != 0 and new_board[x][j] == 0:
#                 new_board[x][j] = board[x][i]
#                 board[x][i] = 0
#                 # j가 n-1이 아니고 합친 적없고 전숫자와 현재숫자가 같을때 합쳐줌
#                 # 합쳤으니 포인터는 그대로 있어야함 왜냐면, 새배열에 포인터 위치가 0 이 되기 때문
#                 if j != n-1 and flag == 0 and new_board[x][j] == new_board[x][j+1]:
#                     new_board[x][j+1], new_board[x][j] = new_board[x][j+1]*2, 0
#                     flag = 1
#                     continue
#                 j -= 1
#
#     return new_board
#
# def up(board):
#     new_board = [[0] * n for _ in range(n)]
#     for x in range(n):
#         j = 0  # 새배열 포인터
#         flag = 0  # 합침 여부 플래그
#         for i in range(n):
#             # 만약 원배열의 숫자가 있고 새 배열에 숫자가 없을때
#             # 새배열로 숫자 복사 후 원배열 방문 표시 해줌.
#             if board[i][x] != 0 and new_board[j][x] == 0:
#                 new_board[j][x] = board[i][x]
#                 board[i][x] = 0
#                 # j가 0이 아니고 합친 적없고 전숫자와 현재숫자가 같을때 합쳐줌
#                 # 합쳤으니 포인터는 그대로 있어야함 왜냐면, 새배열에 포인터 위치가 0 이 되기 때문
#                 if j != 0 and flag == 0 and new_board[j][x] == new_board[j-1][x]:
#                     new_board[j-1][x], new_board[j][x] = new_board[j-1][x] * 2, 0
#                     flag = 1
#                     continue
#                 j += 1
#     return new_board
#
# def down(board):
#     new_board = [[0] * n for _ in range(n)]
#     for x in range(n):
#         j = n - 1  # 새배열 포인터
#         flag = 0  # 합침 여부 플래그
#         for i in range(n - 1, -1, -1):
#             # 만약 원배열의 숫자가 있고 새 배열에 숫자가 없을때
#             # 새배열로 숫자 복사 후 원배열 방문 표시 해줌.
#             if board[i][x] != 0 and new_board[j][x] == 0:
#                 new_board[j][x] = board[i][x]
#                 board[i][x] = 0
#                 # j가 n-1이 아니고 합친 적없고 전숫자와 현재숫자가 같을때 합쳐줌
#                 # 합쳤으니 포인터는 그대로 있어야함 왜냐면, 새배열에 포인터 위치가 0 이 되기 때문
#                 if j != n - 1 and flag == 0 and new_board[j][x] == new_board[j+1][x]:
#                     new_board[j+1][x], new_board[j][x] = new_board[j+1][x] * 2, 0
#                     flag = 1
#                     continue
#                 j -= 1
#
#     return new_board

def left(board):
    for x in range(n):
        j = 0 # 포인터
        for i in range(1,n):
            # 현재 검사 위치에 0이 아닌 숫자가 들어있을대
            # 임시변수 tmp에 옮기고 0으로 바꿔줌.
            if board[x][i] != 0:
                tmp = board[x][i]
                board[x][i] = 0

                # 현재 포인터의 위치에 아무 숫자도 안들어있을때
                # tmp를 넣어줌. = 왼쪽으로 땡격줌
                if board[x][j] == 0 :
                    board[x][j] = tmp
                # 현재 포인터의 위치에 있는 숫자가 tmp와 같을때
                # 합쳐줌. 포인터 1 증가 시켜줌
                elif board[x][j] == tmp:
                    board[x][j] *= 2
                    j += 1
                else:
                    # 현재 포인터의 위치에 숫자가 존재하고 그 숫자가 검사하고 있는 숫자와 다를때
                    # 포인터를 1증가 시키고 거기에 숫자를 넣어줌
                    j += 1
                    board[x][j] = tmp
    return  board

def right(board):
    for x in range(n):
        j = n-1 # 포인터
        for i in range(n-2,-1,-1):
            if board[x][i] != 0:
                tmp = board[x][i]
                board[x][i] = 0
                if board[x][j] == 0 :
                    board[x][j] = tmp
                elif board[x][j] == tmp:
                    board[x][j] *= 2
                    j -= 1
                else:
                    j -= 1
                    board[x][j] = tmp
    return  board

def up(board):
    for x in range(n):
        j = 0 # 포인터
        for i in range(1,n):
            if board[i][x] != 0:
                tmp = board[i][x]
                board[i][x] = 0

                if board[j][x] == 0 :
                    board[j][x] = tmp
                elif board[j][x] == tmp:
                    board[j][x] *= 2
                    j += 1
                else:
                    j += 1
                    board[j][x] = tmp
    return  board

def down(board):
    for x in range(n):
        j = n-1 # 포인터
        for i in range(n-2,-1,-1):
            if board[i][x] != 0:
                tmp = board[i][x]
                board[i][x] = 0
                if board[j][x] == 0 :
                    board[j][x] = tmp
                elif board[j][x] == tmp:
                    board[j][x] *= 2
                    j -= 1
                else:
                    j -= 1
                    board[j][x] = tmp
    return  board

def dfs(L,board):
    global max_val
    if L == 5:
        # 5번 이동하고 최대값 갱신
        cnt = 0
        for x in board:
            cnt = max(max(x),cnt)

        if cnt > max_val:
            max_val = cnt

    else:
        for i in range(4):
            # 케이스별로 다 다르기 때문에 보드를 복사해서 넣어준다
            copy_board = deepcopy(board)
            if i == 0: # 상
                dfs(L+1,up(copy_board))
            elif i == 1: # 우
                dfs(L + 1, right(copy_board))
            elif i == 2: # 하
                dfs(L + 1, down(copy_board))
            else: # 좌
                dfs(L + 1, left(copy_board))


if __name__=='__main__':
    n = int(input()) # 보드크기
    arr = [list(map(int,input().split())) for _ in range(n)] # 보드
    max_val = 0

    dfs(0,arr)
    print(max_val)


