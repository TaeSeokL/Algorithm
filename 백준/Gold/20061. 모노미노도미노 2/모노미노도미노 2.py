# 초록보드와 파란보드를 나눠서 구현했으므로 로직은 동일하다 그러므로 주석은 초록보드처리코드에만 달겠다.

# 블럭을 쌓는 함수
def green(t,y,x):
    # 쌓을 곳을 찾는 변수
    pgy = 5

    # 1x1 블럭이 들어 왔을때, 입력받은 위치(x)는 유지하고 y만 바꾸면서 놓을 수 있는 위치를 찾는다.
    # 중간에 블럭을 발견하면 바로 그 전 위치로 변수를 갱신해준다.
    if t == 1:
        for gy in range(5,-1,-1):
            if green_board[gy][x] == 1:
                pgy = gy - 1
        green_board[pgy][x] = 1
    # 1x2 블럭이 들어 왔을때, y만 바꾸면서 입력받은 위치(x, x+1)는 유지하며 놓을 수 있는 위치를 찾는다.
    # 중간에 블럭을 발견하면 바로 그 전 위치로 변수 갱신
    elif t == 2:
        for gy in range(5,-1,-1):
            if green_board[gy][x] == 1 or green_board[gy][x+1] == 1:
                pgy = gy - 1
        green_board[pgy][x], green_board[pgy][x + 1] = 1, 1
    # 2x1 블럭이 들어 왔을때, 동일
    else:
        for gy in range(5,-1,-1):
            if green_board[gy][x] == 1:
                pgy = gy - 1
        green_board[pgy][x], green_board[pgy-1][x] = 1,1

# 점수를 내는 함수
def green_score():
    global ans
    # 탐색 변수를 제일 마지막 행으로 설정해둔다.
    gy = 5
    while gy > 0 :
        # 현재 보고 있는 행이 전부 1일때, 정답 +1, 전부 0으로 만들어줌.
        if green_board[gy][0] == 1 and green_board[gy][1] == 1 and green_board[gy][2] == 1 and green_board[gy][3] == 1:
            ans += 1
            green_board[gy][0],green_board[gy][1],green_board[gy][2],green_board[gy][3] = 0,0,0,0

            # 그리고 그 즉시 그 위에 행들을 한칸씩 전부 내려준다. 점수가 낸 행부터 0행까지 한행씩 내려주기
            for ggy in range(gy,0,-1):
                for gx in range(4):
                    green_board[ggy][gx], green_board[ggy-1][gx] = green_board[ggy-1][gx], green_board[ggy][gx]
        # 정답이 아닐때는 그 위의 행을 검사하기 위해 -1해줌.
        else:
            gy -= 1

# 금지 영역에 있는 블록을 처리하는 함수
def green_forbidden():
    # 몇 행 없애야하는지 파악. 금지 영역에 몇개의 블록이 있는지 확인. 최대 2
    cnt = 0
    for gy in range(2):
        for gx in range(4):
            if green_board[gy][gx] == 1:
                cnt += 1
                break

    # 행 없애주기, 인덱싱 기법으로 없애준다. list[-1], list[-2] 이런식으로 제일 마지막꺼를 지워줄 수 있다.
    for dd in range(1,cnt+1):
        green_board[-dd][0], green_board[-dd][1],green_board[-dd][2],green_board[-dd][3] = 0,0,0,0

    # 행 채워주기. cnt에 따라 채워야하는 간격이 달라진다. cnt = 1이면 간격을 1 두고 스왑해야하고 2이면 간격 2 두고 스왑해야한다.
    # 범위는 문제 분석하다보니 나왔음. 5부터 cnt가 1일때는 1행까지봐야함. 2일때는 2행까지 봐야하니까 cnt -1 까지 반복문 돌아줌.
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
