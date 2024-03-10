if __name__=='__main__':
    n, m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    next_board = [[0]*n for _ in range(n)]
    dir = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
    cloud = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
    water_copy_bug_dir = [(-1,-1),(-1,1),(1,1),(1,-1)]

    for turn in range(m):
        d, s = map(int,input().split())

        previous_cloud = []
        # 구름 이동 및 비내리기
        for cy,cx in cloud:

            ny = (cy+s*dir[d-1][0]+n)%n
            nx = (cx+s*dir[d-1][1]+n)%n

            board[ny][nx] += 1

            previous_cloud.append((ny,nx))

        # 물복사 버그 마법
        v = [[0]*n for _ in range(n)]
        for cy, cx in previous_cloud:
            water = 0
            v[cy][cx] = 1
            for d in range(4):
                ny = cy + water_copy_bug_dir[d][0]
                nx = cx + water_copy_bug_dir[d][1]

                if 0<=ny<n and 0<=nx<n and board[ny][nx] > 0:
                    water += 1

            board[cy][cx] += water

        cloud = []
        for i in range(n):
           for j in range(n):
               # if board[i][j] >= 2 and (i,j) not in previous_cloud:
               if board[i][j] >= 2 and v[i][j] ==0 :
                   cloud.append([i,j])
                   board[i][j] -= 2

    ans = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 :
                ans += board[i][j]

    print(ans)
