from collections import deque

if __name__=='__main__':
    n,m = map(int,input().split())                                # 맵 크기
    ry, rx, d = map(int,input().split())                          # 로봇청소기 초기위치, 방향
    board = [list(map(int,input().split())) for _ in range(n)]    # 초기 방정보
    clean_zone = 0                                                # 청소한 영역
    dq = deque()                                                  # 로봇위치관리 큐
    dq.append((ry,rx,d))                                          # 초기 위치 추가
    dy_dx = [(-1,0),(0,1),(1,0),(0,-1)]                           # 상 우 하 좌

    # 큐가 빌때까지 반복
    while dq:
        # 로봇의 현재 위치 꺼내고
        # 반시계방향으로의 방향리스트 생성
        # 현재방향이 2(아래)라면 리스트 = [ 오른쪽(1), 위쪽(0), 왼쪽(3), 아래쪽(2) ] 으로 생성됨
        y, x, d = dq.popleft()
        d_lst = [0]*4
        dd = d
        flag = False            # 현재위치에서 주변에 청소안한 칸이 있을 경우 True로 바뀜

        for i in range(4):
            dd = dd - 1
            if dd < 0 :
                dd = 3
            d_lst[i] = dd

        # 현재 위치가 청소가 안되어있으면 청소하기
        if board[y][x] == 0 :
            board[y][x] = 2
            clean_zone += 1

        # 현재위치에서의 방향리스트(반시계방향) 참고해 주변 중 청소가 안된 곳이 있는지 체크
        # 만약 다음 위치가 청소가 안되어 있다면 그 방향으로 로봇을 움직이기 = 큐에 추가
        # 그다음 주변에 청소가 안된 곳이 있으므로 flag를 True로 바꿔줌.
        # 청소가 안된곳으로 바로 가야하기 때문에 break
        for dir in d_lst:
            ny, nx = y+dy_dx[dir][0], x+dy_dx[dir][1]
            if 0<=ny<n and 0<=nx<m and board[ny][nx] == 0 :
                dq.append((ny,nx,dir))
                flag = True
                break

        # flag가 False = 현재 위치에서 주변에 청소가 안된 곳이 없다라는 뜻
        # 그러면 후진을 해야하기 때문에 현재 바라보는 방향을 그대로 유지하며 한칸 뒤로 이동
        # 만약 거기가 벽이 아니다 = 후진이 가능하므로 현재위치르 큐에 업데이트해줌
        # 만약 거기가 벽이면 작동을 중지해야하므로 clean_zone을 출력하고 코드를 끝냄.
        if not flag:
            ny, nx = y-dy_dx[d][0], x - dy_dx[d][1]
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != 1:
                dq.append((ny,nx,d))
            else:
                print(clean_zone)
                exit()

    print(clean_zone)
