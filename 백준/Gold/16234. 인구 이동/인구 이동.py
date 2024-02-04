from collections import deque

if __name__=='__main__':
    N, L, R = map(int,input().split())                              # N 맵크기, L,R 범위
    board = [list(map(int,input().split())) for _ in range(N)]      # 맵정보
    day = 0                                                         # 정답변수
    dq = deque()                                                    # 상하좌우탐색 큐
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    while True:
        flag = False                                # 인구가 이동했는지 안했는지 체크하는 변수
        check = [[0] * N for _ in range(N)]         # 방문체크하는 배열

        # 반복문으로 배열을 전부 탐색해준다.
        for i in range(N):
            for j in range(N):
                # 만약 현재 위치가 방문을 안했을 경우에 상하좌우틀 탐색하며 연합을 찾아간다.
                # temp = 현재 위치가 포함된 연합을 저장하는 배열
                # dq = 현재 위치를 계속 업데이트 하며 상하좌우 탐색할때 사용하는 큐
                # 리스트와 큐에 현재 국가를 추가해주고 방문 표시를 해준다.
                # 또한 인구이동을 계산하기 위해 연합의 총 인구를 저장하는 sum 변수도 만들어준다.
                if check[i][j] == 0:
                    temp = [(i,j)]
                    dq.append((i,j))
                    check[i][j] = 1
                    sum = board[i][j]

                    # 상하좌우 탐색 큐가 빌때까지 반복
                    # 이 큐가 다비었단 얘기는 한 연합에 대해서 더 추가할 국가가 없다는 것을 의미한다.
                    while dq:
                        y,x = dq.popleft()
                        for z in range(4):
                            ny = y + dy[z]
                            nx = x + dx[z]

                            # 만약에 인덱스 범위를 안벗어나고, 방문안했고, 현재와 탐색 위치의 인구차이가
                            # L 이상 R 이하라면 국경선이 열려서 연합으로 인정된다.
                            # 그때 다음 국가 탐색을 위하여 ny,nx를 큐에 추가해주고 방문체크.
                            # 또한 연합 저장배열에 더해주고 연합 총 인구수 변수에 인구를 더해준다.
                            if 0 <= ny < N and 0 <= nx < N and check[ny][nx] == 0:
                                if L <= abs(board[y][x] - board[ny][nx]) <= R:
                                    dq.append((ny, nx))
                                    check[ny][nx] = 1
                                    temp.append((ny,nx))
                                    sum += board[ny][nx]

                    # 한 연합에 대한 탐색이 끝났다면 연합에 포함된 국가수가 1 이상인 곳만 추린다.
                    # 연합이 있다는 것은 인구이동이 가능하단 뜻으로 flag를 수정해주고
                    # 각 국가의 인덱스를 받아와서 인구이동을 시켜준다.
                    if len(temp) > 1:
                        flag = True
                        for y,x in temp:
                            board[y][x] = sum//len(temp)

        # 만약 반복문 탐색 쭉 했는데 인구이동이 됐따면 날짜에 +1 더해주고
        # 아니면 날짜 출력 후 종료해준다.
        if flag:
            day += 1
        else:
            print(day)
            break

