from collections import deque
from copy import deepcopy

def heater_on():
    # 온풍기 배열 안에 있는 위치와 방향 가져오기
    for y,x,d in heater:
        check = [[0]*C for _ in range(R)]
        dq = deque()

        yy,xx = y + dir[d][0], x + dir[d][1]        # 바람 시작 위치
        dq.append((yy,xx,5))
        check[yy][xx] = 1

        if d == 1:              # 오른쪽 방향으로 온풍기 작용
            while dq:
                ay,ax,tp = dq.popleft()
                next_board[ay][ax] += tp

                nx = ax + 1

                for dy in (-1,0,1):
                    ny = ay + dy
                    # 범위내이고, 방문안했고, nx가 원래위치보다 4커진곳까지일때
                    if 0<=ny<R and 0<=nx<C and check[ny][nx] == 0 and nx <= xx + 4:
                        if dy == 0:                # 현재위치와 오른쪽 위치에 벽 확인
                            if wall[ay][ax][ny][nx] == 0 :
                                dq.append((ny, nx, tp - 1))
                                check[ny][nx] = 1
                        elif dy == 1:               # 현재위치와 우상단 벽 확인
                            if wall[ay][ax][ny][ax] == 0 and wall[ny][ax][ny][nx] == 0:
                                dq.append((ny, nx, tp - 1))
                                check[ny][nx] = 1
                        else:                       # 현재위치와 우하단
                            if wall[ay][ax][ny][ax] == 0 and wall[ny][ax][ny][nx] == 0:
                                dq.append((ny, nx, tp - 1))
                                check[ny][nx] = 1

        elif d == 2:  # 왼쪽 방향으로 온풍기 작용
            while dq:
                ay, ax, tp = dq.popleft()
                next_board[ay][ax] += tp

                nx = ax - 1

                for dy in (-1, 0, 1):
                    ny = ay + dy
                    # 범위내이고, 방문안했고, nx가 원래위치보다 4작아진곳까지일때
                    if 0 <= ny < R and 0 <= nx < C and check[ny][nx] == 0 and nx >= xx - 4:
                        if dy == 0:  # 현재위치와 오른쪽 위치에 벽 확인
                            if wall[ay][ax][ny][nx] == 0:
                                dq.append((ny, nx, tp - 1))
                                check[ny][nx] = 1
                        elif dy == 1:  # 현재위치와 좌상단 벽 확인
                            if wall[ay][ax][ny][ax] == 0 and wall[ny][ax][ny][nx]==0:
                                dq.append((ny, nx, tp - 1))
                                check[ny][nx] = 1
                        else:           # 현재위치와 좌하단 벽 확인
                            if wall[ay][ax][ny][ax] == 0 and wall[ny][ax][ny][nx]==0:
                                dq.append((ny, nx, tp - 1))
                                check[ny][nx] = 1
        elif d == 3:  # 위쪽 방향으로 온풍기 작용
            while dq:
                ay, ax, tp = dq.popleft()
                next_board[ay][ax] += tp

                ny = ay - 1

                for dx in (-1, 0, 1):
                    nx = ax + dx
                    # 범위내이고, 방문안했고, ny가 원래위치보다 4작아진곳까지일때
                    if 0 <= ny < R and 0 <= nx < C and check[ny][nx] == 0 and ny >= yy - 4:
                        if dx == 0:  # 현재위치와 위 위치 벽확인
                            if wall[ay][ax][ny][nx] == 0 :
                                dq.append((ny, nx, tp - 1))
                                check[ny][nx] = 1
                        elif dx == -1:  # 현재위치와 좌상단 벽확인
                            if wall[ay][ax][ay][nx] == 0 and wall[ay][nx][ny][nx]==0:
                                dq.append((ny, nx, tp - 1))
                                check[ny][nx] = 1
                        else:           # 현재위치와 우상단 벽확인
                            if wall[ay][ax][ay][nx] == 0 and wall[ay][nx][ny][nx]==0:
                                dq.append((ny, nx, tp - 1))
                                check[ny][nx] = 1


        else:  # 아래쪽 방향으로 온풍기 작용
            while dq:
                ay, ax, tp = dq.popleft()
                next_board[ay][ax] += tp

                ny = ay + 1

                for dx in (-1, 0, 1):
                    nx = ax + dx
                    # 범위내이고, 방문안했고, ny가 원래위치보다 4커진곳까지일때
                    if 0 <= ny < R and 0 <= nx < C and check[ny][nx] == 0 and ny <= yy + 4:
                        if dx == 0:  # 현재위치와 위 위치 벽확인
                            if wall[ay][ax][ny][nx] == 0:
                                dq.append((ny, nx, tp - 1))
                                check[ny][nx] = 1
                        elif dx == -1:  # 현재위치와 좌하단
                            if wall[ay][ax][ay][nx] == 0 and wall[ay][nx][ny][nx] == 0:
                                dq.append((ny, nx, tp - 1))
                                check[ny][nx] = 1
                        else:           # 현재위치와 우하단 벽확인
                            if wall[ay][ax][ay][nx] == 0 and wall[ay][nx][ny][nx] == 0:
                                dq.append((ny, nx, tp - 1))
                                check[ny][nx] = 1

    for i in range(R):
        for j in range(C):
            board[i][j] += next_board[i][j]
            next_board[i][j] = 0

def temp_on():
    # 칸마다 인접한 칸 확인 후 높은 곳에서 낮은 곳으로 온도 이동
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0 :
                diff = 0
                for d in range(1,5):
                    ni = i + dir[d][0]
                    nj = j + dir[d][1]

                    if 0<=ni<R and 0<=nj<C and board[i][j] > board[ni][nj] :
                        if wall[i][j][ni][nj] == 0:
                            next_board[ni][nj] += (board[i][j]-board[ni][nj])//4
                            diff += (board[i][j]-board[ni][nj])//4

                next_board[i][j] += board[i][j] - diff

    # 가장 바깥쪽칸 확인하며 0이 아닌칸만 -1씩 감소
    for r in range(1,R-1):
        # 첫 열
        if next_board[r][0] > 0:         next_board[r][0] -= 1
        # 마지막 열
        if next_board[r][C-1] > 0 :      next_board[r][C-1] -= 1

    for c in range(C):
        # 첫 행
        if next_board[0][c] > 0:         next_board[0][c] -= 1
        # 마지막 행
        if next_board[R-1][c] > 0:       next_board[R-1][c] -= 1



if __name__=='__main__':
    R,C,K = map(int,input().split())        # R x C 맵크기, K 검사온도
    board = [list(map(int,input().split())) for _ in range(R)]  # 맵정보
    dir = [0,(0,1),(0,-1),(-1,0),(1,0)]     # 방향갱신
    wall_quan = int(input())                # 벽 갯수
    wall = [[[[0]*C for _ in range(R)] for _ in range(C)] for _ in range(R)]  # 벽 정보, [[위치],[위치]] 형태로 저장. 이 배열형태가 있으면 벽이 있는 것
    for _ in range(wall_quan):
        y,x,t = map(int,input().split())
        y,x = y-1, x-1

        if t == 0:                  # 0 이면 위쪽에 벽
            wall[y][x][y-1][x] = 1
            wall[y-1][x][y][x] = 1
        else:                       # 1 이면 오른쪽에 벽
            wall[y][x][y][x+1] = 1
            wall[y][x+1][y][x] = 1


    heater = []          # 온풍기 배열 (위치,방향)
    res = []             # 조사해야하는 위치 배열
    ans = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] == 5:
                res.append((i,j))
                board[i][j] = 0
            elif board[i][j] != 0:
                heater.append((i,j,board[i][j]))
                board[i][j] = 0

    turn = 1
    while True:

        next_board = [[0] * C for _ in range(R)]  # 온풍기 효과 적용 배열

        heater_on()

        temp_on()
        board = deepcopy(next_board)

        ans += 1
        if ans > 100 :
            print(101)
            exit(0)

        for y,x in res:
            if board[y][x] < K:
                break
        else:
            print(ans)
            exit(0)

