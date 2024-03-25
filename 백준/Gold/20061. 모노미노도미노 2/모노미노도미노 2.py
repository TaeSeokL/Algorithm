def green(t,y,x):
    # 쌓을 곳을 찾는 변수
    pgy = 5
    if t == 1:
        for gy in range(5,-1,-1):
            if green_board[gy][x] == 1:
                pgy = gy - 1
        green_board[pgy][x] = 1
    elif t == 2:
        for gy in range(5,-1,-1):
            if green_board[gy][x] == 1 or green_board[gy][x+1] == 1:
                pgy = gy - 1
        green_board[pgy][x], green_board[pgy][x + 1] = 1, 1
    else:
        for gy in range(5,-1,-1):
            if green_board[gy][x] == 1:
                pgy = gy - 1
        green_board[pgy][x], green_board[pgy-1][x] = 1,1

def green_score():
    global ans
    gy = 5
    while gy > 0 :
        # 현재 보고 있는 행이 전부 1일때
        if green_board[gy][0] == 1 and green_board[gy][1] == 1 and green_board[gy][2] == 1 and green_board[gy][3] == 1:
            ans += 1
            green_board[gy][0],green_board[gy][1],green_board[gy][2],green_board[gy][3] = 0,0,0,0

            for ggy in range(gy,0,-1):
                for gx in range(4):
                    green_board[ggy][gx], green_board[ggy-1][gx] = green_board[ggy-1][gx], green_board[ggy][gx]
        else:
            gy -= 1

def green_forbidden():
    # 몇 행 없애야하는지 파악
    cnt = 0
    for gy in range(2):
        for gx in range(4):
            if green_board[gy][gx] == 1:
                cnt += 1
                break

    # 행 없애주기
    for dd in range(1,cnt+1):
        green_board[-dd][0], green_board[-dd][1],green_board[-dd][2],green_board[-dd][3] = 0,0,0,0

    # 행 채워주기
    for gy in range(5,cnt-1,-1):
        for gx in range(4):
            green_board[gy][gx], green_board[gy-cnt][gx] = green_board[gy-cnt][gx],green_board[gy][gx]

def blue(t,y,x):
    pbx = 5
    if t == 1:
        for bx in range(5,-1,-1):
            if blue_board[y][bx] == 1:
                pbx = bx - 1
        blue_board[y][pbx] = 1
    elif t == 2:
        for bx in range(5,-1,-1):
            if blue_board[y][bx] == 1 :
                pbx = bx - 1
        blue_board[y][pbx], blue_board[y][pbx - 1] = 1, 1
    else:
        for bx in range(5,-1,-1):
            if blue_board[y][bx] == 1 or blue_board[y+1][bx] == 1:
                pbx = bx - 1
        blue_board[y][pbx], blue_board[y+1][pbx] = 1, 1

def blue_score():
    global ans
    bx = 5
    while bx > 0 :
        # 현재 보고 있는 열이 전부 1일때
        if blue_board[0][bx] == 1 and blue_board[1][bx] == 1 and blue_board[2][bx] == 1 and blue_board[3][bx] == 1 :
            ans += 1
            blue_board[0][bx],blue_board[1][bx],blue_board[2][bx],blue_board[3][bx] = 0,0,0,0

            for bbx in range(bx,0,-1):
                for by in range(4):
                    blue_board[by][bbx], blue_board[by][bbx-1] = blue_board[by][bbx-1], blue_board[by][bbx]
        else:
            bx -= 1

def blue_forbidden():
    cnt = 0
    for bx in range(2):
        for by in range(4):
            if blue_board[by][bx] == 1:
                cnt += 1
                break

    for dd in range(1,cnt+1):
        blue_board[0][-dd],blue_board[1][-dd],blue_board[2][-dd],blue_board[3][-dd] = 0,0,0,0

    for bx in range(5,cnt-1,-1):
        for by in range(4):
            blue_board[by][bx], blue_board[by][bx-cnt] = blue_board[by][bx-cnt], blue_board[by][bx]

if __name__=='__main__':
    n = int(input())

    green_board = [[0]*4 for _ in range(6)]
    blue_board = [[0]*6 for _ in range(4)]
    ans = 0
    for _ in range(n):
        t,y,x = map(int,input().split())

        # [1] 블록 쌓기
        green(t,y,x)
        blue(t,y,x)

        # [2] 점수 획득 가능한지 확인 후 처리
        green_score()
        blue_score()

        # [3] 금지구역에 블록 있는지 확인 후 처리
        green_forbidden()
        blue_forbidden()

    cnt = 0
    for y in range(6):
        for x in range(4):
            if green_board[y][x] == 1:
                cnt += 1
            if blue_board[x][y] == 1:
                cnt += 1

    print(ans)
    print(cnt)