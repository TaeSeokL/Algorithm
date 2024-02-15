from collections import deque
if __name__=='__main__':
    n,m,t = map(int,input().split())    # n = 반지름 갯수, m = 숫자갯수, t = 회전횟수
    dir = [(-1,0),(0,1),(1,0),(0,-1)]   # 상하좌우 탐색
    dq = deque()                        # 연쇄적인 탐색을 위한 큐

    # 원판 정보 , 인덱스가 (1,1) 부터 시작하므로 첫행 첫열 다 0으로 초기화.
    board = [[0]*(m+1)]
    for i in range(n):
        temp = [0] + list(map(int,input().split()))
        board.append(temp)

    # 회전 명령 횟수만큼 반복문
    for turn in range(t):
        x,d,k = map(int,input().split())    # x 배수의 원판을 모두 d방향으로 k번 회전

        # 시계 방향 회전
        if d == 0:
            for circle in range(x,n+1,x):
                for time in range(k):
                    board[circle].insert(1,board[circle].pop(-1))
        # 반시계 방향 회전
        else:
            for circle in range(x, n + 1, x):
                for time in range(k):
                    board[circle].append(board[circle].pop(1))

        # tmp는 숫자를 제거해야할 위치를 모두 저장한 배열이다.
        # check는 방문 여부를 체크하는 배열
        tmp = []
        check = [[0]*(m+1) for _ in range(n+1)]

        # 배열 전체에 대해서 하나하나 완전 탐색을 진행한다.
        for i in range(1,n+1):
            for j in range(1,m+1):
                # 방문 안했고 숫자가 있는곳만 체크
                # 현 위치의 숫자를 value에다 저장해두고 상하좌우로 탐색하며 비교한다.
                if check[i][j] == 0 and board[i][j] != 0:
                    value = board[i][j]
                    for d in range(4):
                        # 상하좌우 탐색
                        y ,x = i + dir[d][0], j + dir[d][1]

                        # 상하좌우 탐색 중, 탐색 위치가 범위내이고, 방문 안했고, 숫자가 있을때
                        # 만약 숫자가 같다면 현재 위치의 숫자를 제거해야하므로 tmp에 추가해주고 방문체크해준다. (i,j)
                        # 탐색 위치도 제거해야하므로 tmp에 추가해주고 연쇄적으로 일어날 수 있기에 탐색큐에 넣어준다. (y,x)
                        # 이때 같은 숫자가 모여있을때 (i,j)가 계속 추가될수 있으므로 체크하며 넣어줌.
                        if 1<=y<=n and 1<=x<=m and check[y][x] == 0 and board[y][x] != 0:
                            if value == board[y][x] :
                                if (i,j) not in tmp:
                                    tmp.append((i,j))
                                    check[i][j] = 1

                                tmp.append((y, x))
                                check[y][x] = 1
                                dq.append((y,x))

                    # 큐가 빌때까지 반복
                    while dq:
                        # 탐색해야하는 위치를 받아와서 상하좌우로 탐색해준다.
                        # 위의 로직과 똑같이 탐색 위치에서 똑같은 숫자가 발견되면 tmp에 추가, 방문 체크, 탐색큐에 추가해서
                        # 끝까지 탐색해준다.
                        y,x = dq.popleft()

                        for d in range(4):
                            ny, nx = y + dir[d][0], x + dir[d][1]
                            if 1 <= ny <= n and 1 <= nx <= m and check[ny][nx] == 0 and board[ny][nx] != 0:
                                if value == board[ny][nx] :
                                    tmp.append((ny,nx))
                                    check[ny][nx] = 1
                                    dq.append((ny,nx))

        # 내가 생각한 로직 기준으로 위 까지만 했을때 첫열과 마지막 열의 비교가 불가능한 상태이다.
        # 하지만 원반은 둥근 형태이기때문에 첫열과 마지막열이 연결되어 있고 이둘도 비교를 해야한다.
        # 이때는 위에서 방문체크가 모두 되어 있는 상태이기 때문에 단순 숫자값만 비교해서 같으면
        # 제거배열에 넣어주어야한다.
        for i in range(1,n+1):
            if board[i][1] != 0 and board[i][m] != 0 and board[i][1] == board[i][m]:
                tmp.append((i,1))
                tmp.append((i,m))

        # 만약 tmp 즉 제거해야할것이 있따면 모두 제거해줌.
        # 아니면 문제의 조건대로 모든 원판의 평균을 구한 뒤 값을 비교해서 +-1 씩 해준다.
        if tmp:
            for y,x in tmp:
                board[y][x] = 0
        else:
            res = []
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if board[i][j] != 0:
                        res.append(board[i][j])

            if len(res) == 0 :
                break
            else:
                avg = sum(res)/len(res)

                for i in range(1,n+1):
                    for j in range(1,m+1):
                        if board[i][j] != 0:
                            if board[i][j] > avg:
                                board[i][j] -= 1
                            elif board[i][j] < avg:
                                board[i][j] += 1

        # print('----------%d턴-----------'%turn)
        # for x in board:
        #     print(x)
        # print()

    # 답을 출력해준다.
    ans = 0
    for x in board:
        ans += sum(x)

    print(ans)