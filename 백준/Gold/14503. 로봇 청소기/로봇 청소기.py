from collections import deque


if __name__=='__main__':
    n,m = map(int,input().split())                                # 맵 크기
    ry, rx, d = map(int,input().split())                          # 로봇청소기 초기위치, 방향
    board = [list(map(int,input().split())) for _ in range(n)]    # 초기 방정보
    clean_zone = 0                                                # 청소한 영역
    dq = deque()
    dq.append((ry,rx,d))
    dy_dx = [(-1,0),(0,1),(1,0),(0,-1)]

    while dq:
        y, x, d = dq.popleft()
        d_lst = [0]*4
        dd = d
        flag = False

        for i in range(4):
            dd = dd - 1
            if dd < 0 :
                dd = 3
            d_lst[i] = dd

        if board[y][x] == 0 :
            board[y][x] = 2
            clean_zone += 1

        for dir in d_lst:
            ny, nx = y+dy_dx[dir][0], x+dy_dx[dir][1]
            if 0<=ny<n and 0<=nx<m and board[ny][nx] == 0 :
                dq.append((ny,nx,dir))
                flag = True
                break

        if not flag:
            ny, nx = y-dy_dx[d][0], x - dy_dx[d][1]
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != 1:
                dq.append((ny,nx,d))
            else:
                print(clean_zone)
                exit()


    print(clean_zone)





