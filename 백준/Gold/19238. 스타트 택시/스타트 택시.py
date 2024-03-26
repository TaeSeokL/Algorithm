from collections import deque

# 현재 택시 위치에서 가장 가까운 승객을 찾는다.
# 로직 : 현재 택시위치에서 태울 수 있는 승객을 모두 pas에 저장한 뒤 다중정렬을 통해 가장 가깝고, 행과 열이 가장 적은 승객을 찾는다.
def find_passanger():
    global ty,tx,f

    dq = deque()                            # 탐색큐
    check = [[0]*n for _ in range(n)]       # 방문배열

    dq.append((ty,tx,0))                    # 현재택시위치와 연료변수
    check[ty][tx] = 1                       # 방문처리

    pas = []                                # 태울 수 있는 손님 저장 / (y,x,손님번호,손님태우러가는데드는 연료)
    while dq:
        y,x,df = dq.popleft()

        # 만약 승객이다. pas에 추가
        if board[y][x] != 0 and board[y][x] != -1:
            pas.append((y,x,board[y][x],df))

        # 탐색
        for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
            ny = y + dy
            nx = x + dx

            # 범위내이고, 벽아니고, 방문 안했을때
            if 0<=ny<n and 0<=nx<n and board[ny][nx] != -1 and check[ny][nx] == 0:
                dq.append((ny,nx,df+1))
                check[ny][nx] = 1

    if pas:                                                 # 만약 태울 수 있는 승객이 있을 경우
        pas.sort(key=lambda x:(x[3],x[0],x[1]))                 # 연료, 행, 열 순으로 다중 정렬
        for y,x,num,df in pas:                                  # 하나씩 꺼내기
            if df <= f:                                         # 연료가 충분한지 확인하기
                board[y][x] = 0                                     # 승객 태우기
                f -= df                                             # 연료 업뎃
                ty,tx = y,x                                         # 택시 위치 업뎃
                return num
    else:                                                   # 태울 수 있는 승객이 없을 경우 -> 종료
        print(-1)
        exit(0)

# 승객을 태운 상태에서 목적지 까지 데려다 줄 수 있는지 확인하는 함수
def go_to_endpoint(num):
    global ty,tx,f

    dq = deque()                                # 탐색큐
    check = [[0]*n for _ in range(n)]           # 방문배열

    dq.append((ty,tx,0))                        # 현재 택시위치와 연료 변수
    check[ty][tx] = 1                           # 방문 체크

    ey,ex = end_point[num]                      # 현재 태운 승객의 목적지

    while dq:
        y,x,df = dq.popleft()

        if f - df < 0 :                     # 탐색 도중 연료가 부족할때 -> 종료,
            print(-1)
            exit(0)
        else:                               # 연료 충분할때
            if (y,x) == (ey,ex):                # 목적지에 도착했을때
                end_point[num] = True               # 도착체크
                f = f+ df                           # 연료 업뎃 ( f = f - df + 2*df) = f = f + df
                ty, tx = y,x                        # 택시 위치 업뎃 후 종료
                return
            else:                               # 목적지 아닐때 -> 계속 탐색
                for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
                    ny = y + dy
                    nx = x + dx
                    # 범위내, 벽아님, 방문안함.
                    if 0<=ny<n and 0<=nx<n and board[ny][nx] != -1 and check[ny][nx] == 0:
                        dq.append((ny,nx,df+1))
                        check[ny][nx] = 1

    # 큐가 빌때까지 코드 종료 혹은 함수 종료를 안했다는 뜻은
    # 연료가 충분하지만 목적지까지 도달 못했다는 소리 -> 즉 길이 막혀있다는 소리
    # 못데려다주니까 코드 종료하기
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
        board[a-1][b-1] = i                 # 출발지 표기
        end_point.append((c-1,d-1))         # 목적지 저장

    while True:
        # [1] 현재 택시 위치에서 가장 가까운 승객 찾기
        num = find_passanger()

        # [2] 이 승객을 데려다주기
        go_to_endpoint(num)

        # [3] 모든 승객 델따 줬는지 확인
        for i in range(1,m+1):
            if end_point[i] is not True:
                break
        else:   # 모든 승객 데려다 줬을 때
            print(f)
            exit(0)
