
if __name__=='__main__':

    n = int(input())                                              # 맵크기
    board = [list(map(int,input().split())) for _ in range(n)]    # 맵정보

    # 방향에 따른 모래가 흩어지는 곳, 좌 하 우 상 (0,1,2,3)
    sand_update_idx = [[(-1, 1), (-2, 0), (-1, 0), (-1, -1), (0, -2), (1, -1), (1, 0), (2, 0), (1, 1),(0, -1)],
    [(-1, 1), (0, 2), (0, 1), (1, 1), (2, 0), (1, -1), (0, -1), (0, -2), (-1, -1),(1, 0)],
    [(1, -1), (2, 0), (1, 0), (1, 1), (0, 2), (-1, 1), (-1, 0), (-2, 0), (-1, -1),(0, 1)],
    [(1, 1), (0, 2), (0, 1), (-1, 1), (-2, 0), (-1, -1), (0, -1), (0, -2), (1, -1),(-1, 0)]]

    sand_update_rate = [1,2,7,10,5,10,7,2,1]                        # 모래 비율
    tornado_dir = [(0,-1),(1,0),(0,1),(-1,0)]                     # 토네이도 방향 (좌 하 우 상)
    tornado_d = 0                                                 # 토네이도 초기 방향
    ty,tx = n//2, n//2                                            # 토네이도 초기 위치
    ans = 0                                                       # 맵밖으로 나간 모래

    for step in range(1,n):
        for time in range(1,step*2+1):

            nty = ty + tornado_dir[tornado_d % 4][0]
            ntx = tx + tornado_dir[tornado_d % 4][1]

            total_sand = 0  # 업데이트된 모래 누적해주기
            ori_sand = board[nty][ntx]  # 원래모래 저장해두기
            # 여기서 맵처리
            for i in range(10):
                if i == 9:
                    board[nty][ntx] = 0
                    u_sand = ori_sand - total_sand
                    dy,dx = sand_update_idx[tornado_d%4][9]
                    uy = nty + dy
                    ux = ntx + dx
                    if 0<=uy<n and 0<=ux<n:
                        board[uy][ux] += u_sand
                    else:
                        ans += u_sand
                    continue

                # 모래 업데이트 할 곳 찾기
                dy,dx = sand_update_idx[tornado_d%4][i]
                uy = nty + dy
                ux = ntx + dx

                # 업데이트 될 모래
                u_sand = ori_sand * sand_update_rate[i]//100
                total_sand += u_sand

                # 다음 위치 범위파악
                if 0<=uy<n and 0<=ux<n:
                    board[uy][ux] += u_sand
                else:
                    ans += u_sand

            ty, tx = nty, ntx

            if (step*2) == time or (step) == time :
                tornado_d += 1

    # 첫번째 행 처리
    for _ in range(n):
        nty = ty + tornado_dir[0][0]
        ntx = tx + tornado_dir[0][1]

        total_sand = 0  # 업데이트된 모래 누적해주기
        ori_sand = board[nty][ntx]  # 원래모래 저장해두기
        # 여기서 맵처리
        for i in range(10):
            if i == 9:
                board[nty][ntx] = 0
                u_sand = ori_sand - total_sand
                dy, dx = sand_update_idx[tornado_d % 4][9]
                uy = nty + dy
                ux = ntx + dx
                if 0 <= uy < n and 0 <= ux < n:
                    board[uy][ux] += u_sand
                else:
                    ans += u_sand
                continue

            # 모래 업데이트 할 곳 찾기
            dy, dx = sand_update_idx[tornado_d % 4][i]
            uy = nty + dy
            ux = ntx + dx

            # 업데이트 될 모래
            u_sand = ori_sand * sand_update_rate[i] // 100
            total_sand += u_sand

            # 다음 위치 범위파악
            if 0 <= uy < n and 0 <= ux < n:
                board[uy][ux] += u_sand
            else:
                ans += u_sand

        ty, tx = nty, ntx

        if ty == 0 and tx == 0:
            break

    print(ans)

