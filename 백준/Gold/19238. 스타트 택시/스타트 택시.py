from collections import deque

def find_passanger():
    global ty,tx,f

    dq = deque()
    check = [[0]*n for _ in range(n)]

    dq.append((ty,tx,0))
    check[ty][tx] = 1

    pas = []
    while dq:
        y,x,df = dq.popleft()

        if board[y][x] != 0 and board[y][x] != -1:
            pas.append((y,x,board[y][x],df))

        for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
            ny = y + dy
            nx = x + dx

            if 0<=ny<n and 0<=nx<n and board[ny][nx] != -1 and check[ny][nx] == 0:
                dq.append((ny,nx,df+1))
                check[ny][nx] = 1

    if pas:
        pas.sort(key=lambda x:(x[3],x[0],x[1]))
        for y,x,num,df in pas:
            if df <= f:
                board[y][x] = 0
                f -= df
                ty,tx = y,x
                return num
    else:
        print(-1)
        exit(0)

def go_to_endpoint(num):
    global ty,tx,f

    dq = deque()
    check = [[0]*n for _ in range(n)]

    dq.append((ty,tx,0))
    check[ty][tx] = 1

    ey,ex = end_point[num]

    while dq:
        y,x,df = dq.popleft()

        if f - df < 0 :
            print(-1)
            exit(0)
        else:
            if (y,x) == (ey,ex):
                end_point[num] = True
                f = f+ df
                ty, tx = y,x
                return
            else:
                for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
                    ny = y + dy
                    nx = x + dx

                    if 0<=ny<n and 0<=nx<n and board[ny][nx] != -1 and check[ny][nx] == 0:
                        dq.append((ny,nx,df+1))
                        check[ny][nx] = 1

    print(-1)
    exit(0)

if __name__=='__main__':
    n, m, f = map(int,input().split())                          # n 격자 크기 / m 승객 수 / f 연료

    board = [list(map(int,input().split())) for _ in range(n)]  # 맵정보
    # 승객과 혼돈 방지를 위해 벽을 -1로 표기
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                board[r][c] = -1

    # 택시 초기 좌표
    ty, tx = map(int,input().split())
    ty -= 1
    tx -= 1

    # 각 승객들의 목적지 위치 저장 배열
    end_point = [True]
    for i in range(1,m+1):
        a,b,c,d = map(int,input().split())
        board[a-1][b-1] = i         # 출발지 표기
        end_point.append((c-1,d-1)) # 목적지 저장

    while True:
        # [1] 현재 택시 위치에서 가장 가까운 승객 찾기
        num = find_passanger()

        # [2] 이 승객을 데려다주기
        go_to_endpoint(num)

        # [3] 모든 승객 델따 줬는지 확인
        for i in range(1,m+1):
            if end_point[i] is not True:
                break
        else:
            print(f)
            exit(0)
