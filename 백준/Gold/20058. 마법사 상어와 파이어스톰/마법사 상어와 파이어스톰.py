from collections import deque

# 배열 회전하는 함수
# 전달받은 v로 회전할 정사각형의 크기를 계산해줌 = 2^v
# 그 다음 격자 전체를 순회하는 (r,c)를 v 간격으로 반복해줌. (r,c)는 회전하는 정사각형의 좌상단 인덱스임.
# 그 다음 (r,c)부터 회전하는 정사각형 크기만큼을 회전시켜줘야함. 여기서 중요한게 (r,c)에 따라
# 회전시작점의 기준좌표가 전부 달라지기 때문에 원점으로 좌표계를 변환한 다음 회전시키고, 다시 좌표계를 복구해주는게 중요함.
def ice_rotate(v):
    v = 2**v
    # 새로운 풀이, 목적지 좌표 기준 부분 회전 구현법
    # 부분 회전은 회전 시작점이 모두 다르기 때문에 (0,0) 기준 구현한 뒤 회전 시작점인 (r,c)를 각 좌표에 더해주기만 하면됨.
    # 이 방법 아주 괜찮은거 같음. 헷갈리면 알고리즘 개념노트 p45-48 보던지 (https://youtu.be/NHoMIsPOZUE?si=knxyxAnAfDlPWDxG) 이거보기
    for r in range(0,n,v):
        for c in range(0,n,v):
            for y in range(v):
                for x in range(v):
                    next_board[y+r][x+c] = board[v-1-x+r][y+c]

            # 내풀이 (좌표계 변환 후 회전 구현)
            # for y in range(r,r+v):
            #     for x in range(c,c+v):
            #         # 좌표계 변환
            #         oy = y - r
            #         ox = x - c
            #
            #         # 회전 구현
            #         ry = ox
            #         rx = v - oy - 1
            #
            #         # 좌표계 복구
            #         ry += r
            #         rx += c
            #
            #         next_board[ry][rx] = board[y][x]

    # 맵 갱신
    for i in range(n):
        for j in range(n):
            board[i][j] = next_board[i][j]

# 얼음 녹이는 함수
# 격자 전체 순회하며 주변에 얼음이 3개 이상 있으면 그대로 넣어주고 없으면 -1 해서 넣어줌.
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

# 제일 큰 얼음 덩어리 면적 찾는 함수 = bfs
def max_ice():
    global max_val
    # 방문 배열과 탐색큐
    check = [[0]*n for _ in range(n)]
    dq = deque()

    # 격자 전체를 순회하며 얼음이 있는 곳이 발견되면 탐색큐에 넣은 뒤, 방문체크해주고,
    # 그 위치를 기준으로 상하좌우로 뻗어나가며 덩어리를 탐색한다.
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and board[i][j] != 0:
                dq.append((i,j))
                check[i][j] = 1
                res = 1
                while dq:
                    y,x = dq.popleft()
                    # 상하좌우 뻗어나가다가
                    for d in range(4):
                        dy, dx = dir[d]
                        ny, nx = y + dy, x + dx
                        # 범위내이고, 방문안했고, 얼음 있으면, 큐에 추가
                        if 0<=ny<n and 0<=nx<n and check[ny][nx] == 0 and board[ny][nx] != 0:
                            dq.append((ny,nx))
                            check[ny][nx] = 1
                            res += 1

                # 덩어리 크기가 1이 아니고 최대값보다 크면 최대값 갱신
                if res != 1 and res > max_val:
                    max_val = res

if __name__=='__main__':
    n, q = map(int,input().split())                                 # 2**n 맵크기, q 명령갯수
    n = 2**n
    board = [list(map(int,input().split())) for _ in range(n)]      # 맵정보
    L = list(map(int,input().split()))                              # 명령정보
    dir = [(-1,0),(0,1),(1,0),(0,-1)]                               # 이동방향
    next_board = [[0]*n for _ in range(n)]                          # 회전 후 맵 저장 배열

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
