from collections import deque

def ice_rotate(v):
    v = 2**v
    for r in range(0,n,v):
        for c in range(0,n,v):
            for y in range(r,r+v):
                for x in range(c,c+v):
                    # 좌표계 변환
                    oy = y - r
                    ox = x - c

                    # 회전 구현
                    ry = ox
                    rx = v - oy - 1

                    # 좌표계 복구
                    ry += r
                    rx += c

                    next_board[ry][rx] = board[y][x]

    # 맵 갱신
    for i in range(n):
        for j in range(n):
            board[i][j] = next_board[i][j]

def ice_melting():
    for i in range(n):
        for j in range(n):
            flag = 0
            for d in range(4):
                dy, dx = dir[d]
                ny, nx = i + dy, j + dx

                if 0<=ny<n and 0<=nx<n and board[ny][nx] != 0:
                    flag += 1

            if flag>= 3:
                next_board[i][j] = board[i][j]
            else:
                if board[i][j] > 0 :
                    next_board[i][j] = board[i][j] - 1
                else:
                    next_board[i][j] = 0

    # 맵 갱신
    for i in range(n):
        for j in range(n):
            board[i][j] = next_board[i][j]

def max_ice():
    global max_val
    check = [[0]*n for _ in range(n)]
    dq = deque()

    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and board[i][j] != 0:
                dq.append((i,j))
                check[i][j] = 1
                res = 1
                while dq:
                    y,x = dq.popleft()

                    for d in range(4):
                        dy, dx = dir[d]
                        ny, nx = y + dy, x + dx

                        if 0<=ny<n and 0<=nx<n and check[ny][nx] == 0 and board[ny][nx] != 0:
                            dq.append((ny,nx))
                            check[ny][nx] = 1
                            res += 1

                if res != 1 and res > max_val:
                    max_val = res

if __name__=='__main__':
    n, q = map(int,input().split())                                 # 2**n 맵크기, q 명령갯수
    n = 2**n
    board = [list(map(int,input().split())) for _ in range(n)]   # 맵정보
    L = list(map(int,input().split()))                              # 명령정보
    dir = [(-1,0),(0,1),(1,0),(0,-1)]                               # 이동방향
    next_board = [[0]*n for _ in range(n)]                  # 회전 후 맵 저장 배열

    ans = 0         # 남아있는 얼음양
    max_val = 0     # 남아있는 얼음 덩어리 중 가장 큰 것의 면적

    # 명령 처리
    for k in L:
        # 격자회전
        ice_rotate(k)
        # 얼음녹이기
        ice_melting()

    # 남아있는 얼음의 합 구하기
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                ans += board[i][j]

    # 최대 얼음 덩어리 면적 구하기
    max_ice()

    print(ans)
    print(max_val)

