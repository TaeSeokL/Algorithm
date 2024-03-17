from collections import deque
from copy import deepcopy

def heater_on():
    # 온풍기 배열 안에 있는 위치와 방향 가져오기 -> 모두 같은 원리이지만 방향 별로 ny,nx 업데이트 방식, 범위, 벽 확인할 곳 등 수정
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

    # 온풍기 효과로 누적된 온도 보드에 더해주기
    for i in range(R):
        for j in range(C):
            board[i][j] += next_board[i][j]
            next_board[i][j] = 0

# 온도 조절 후 가장자리 온도 삭제해주는 함수
def temp_on():
    # 칸마다 인접한 칸 확인 후 높은 곳에서 낮은 곳으로 온도 이동
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0 :
                diff = 0            # diff를 누적해서 원래 board[i][j]에 저장되어 있던 값에 빼주어서 업데이트할거임.
                for d in range(1,5):
                    ni = i + dir[d][0]
                    nj = j + dir[d][1]
                    # 범위내이고 현재값이 더 크고 벽이 없을때만 계산
                    if 0<=ni<R and 0<=nj<C and board[i][j] > board[ni][nj] :
                        if wall[i][j][ni][nj] == 0:
                            next_board[ni][nj] += (board[i][j]-board[ni][nj])//4
                            diff += (board[i][j]-board[ni][nj])//4

                next_board[i][j] += board[i][j] - diff

    # 가장 바깥쪽칸 확인하며 0이 아닌칸만 -1씩 감소
    # 여기서 네 모서리가 중복될 수 있기 때문에 r은 1부터 R-1까지만 돌아줌.
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
    R,C,K = map(int,input().split())                            # R x C 맵크기, K 검사온도
    board = [list(map(int,input().split())) for _ in range(R)]  # 맵정보
    dir = [0,(0,1),(0,-1),(-1,0),(1,0)]                         # 방향갱신
    wall_quan = int(input())                                    # 벽 갯수

    # 벽정보, 4차원 배열로 정의해주고 wall[출발y][출발x][도착y][도착x] 형태로 사용했음. -> 정의 법을 잘 기억하자
    wall = [[[[0]*C for _ in range(R)] for _ in range(C)] for _ in range(R)]

    # 벽 정보를 표시해줌. 출발지와 도착지를 바꿔서도 표시해줘야함.
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
    ans = 0              # 정답변수

    # 온풍기 저장 : (온풍기 위치, 온풍기 방향)
    # 조사해야할 위치 저장
    for i in range(R):
        for j in range(C):
            if board[i][j] == 5:
                res.append((i,j))
                board[i][j] = 0
            elif board[i][j] != 0:
                heater.append((i,j,board[i][j]))
                board[i][j] = 0

    while True:
        next_board = [[0] * C for _ in range(R)]  # 온풍기 효과 적용 배열

        # 온풍기 작동
        heater_on()

        # 온도 조절 및 가장자리 처리
        temp_on()
        board = deepcopy(next_board)

        # 초콜릿 섭취
        ans += 1
        if ans > 100 :  # 문제조건 : 100 초과면 101 출력 후 종료
            print(101)
            exit(0)

        # 조사해야할 위치가 K 이하면 다시 반복, 모두 K 이상이면 종료
        for y,x in res:
            if board[y][x] < K:
                break
        else:
            print(ans)
            exit(0)
