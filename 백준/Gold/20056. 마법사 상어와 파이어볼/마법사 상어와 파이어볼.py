
def move_ball():
    for y in range(n):
        for x in range(n):
            # 칸에 공이 하나 있을때
            if len(board[y][x]) != 0:
                ln = len(board[y][x])   # 공갯수
                for i in range(ln):
                    # 질량, 속력, 방향을 받아온 뒤 공이 실제 움직여야할 칸 갯수 계산
                    m,s,d = board[y][x][i]
                    real_move_block = s%n
                    ny,nx = y,x
                    for _ in range(real_move_block):
                        # 행과 열의 기존 위치에 따라 경우의 수를 나누고 따로 계산해줌.
                        # 행부터
                        if ny == 0 and (d==0 or d == 1 or d == 7):
                            ny = n-1
                        elif ny == n-1 and (d==3 or d ==4 or d == 5):
                            ny = 0
                        else:
                            ny = ny + dir[d][0]

                        # 열
                        if nx == 0 and (d==5 or d == 6 or d == 7):
                            nx = n-1
                        elif nx == n-1 and (d==1 or d == 2 or d == 3):
                            nx = 0
                        else:
                            nx = nx + dir[d][1]

                    next_board[ny][nx] += [(m,s,d)]
                board[y][x] = []

    for y in range(n):
        for x in range(n):
            if len(next_board[y][x]) != 0:
                board[y][x] = next_board[y][x]
                next_board[y][x] = []


def spread_ball():
    for y in range(n):
        for x in range(n):
            # 공이 여러개라면 흩뿌려야함.
            if len(board[y][x]) > 1:
                # 공갯수, 질량합, 속력합, 방향 배열
                ln = len(board[y][x])
                sum_m = 0
                sum_s = 0
                dir_judge = [0]*ln
                flag1 = False   # 모두 짝수인지 판단
                flag2 = False   # 모두 홀수인지 판단

                for i in range(ln):
                    m,s,d = board[y][x][i]
                    sum_m += m
                    sum_s += s
                    dir_judge[i] = d

                # 각 공의 질량과 속력을 구해줌.
                each_ball_m = sum_m//5
                each_ball_s = sum_s // ln

                # 새로구한 공질량이 0일때
                if each_ball_m == 0:
                    board[y][x] = []
                    continue

                # 짝수인지판단
                for a in dir_judge:
                    if a % 2 == 1:
                        break
                else:
                    flag1 = True
                # 홀수 인지 판단
                for a in dir_judge:
                    if a % 2 == 0:
                        break
                else:
                    flag2 = True

                if (flag1 or flag2):
                    for d in range(0,7,2):
                        next_board[y][x] += [(each_ball_m,each_ball_s,d)]
                else:
                    for d in range(1,8,2):
                        next_board[y][x] += [(each_ball_m,each_ball_s,d)]

    for y in range(n):
        for x in range(n):
            if len(next_board[y][x]) != 0:
                board[y][x] = next_board[y][x]
                next_board[y][x] = []




if __name__=='__main__':
    n, m, k = map(int,input().split())                      # n 맵크기, m 공 갯수, k 명령갯수

    board = [[[] for _ in range(n)] for _ in range(n)]      # 맵 (3차원배열)
    next_board = [[[] for _ in range(n)] for _ in range(n)] # 계산용 맵
    dir = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]   # 방향
    ball = [0]*(m+1)

    for i in range(1,m+1):
        r,c,m,s,d = map(int,input().split())            # 위치 : (r,c) m 질량, s 속력, d 방향
        board[r-1][c-1] = [(m,s,d)]                     # 각 공의 질량 속력 방향만 저장

    for _ in range(k):
        # 공 이동
        move_ball()

        # 공 분해
        spread_ball()

    ans = 0
    for y in range(n):
        for x in range(n):
            if len(board[y][x]) > 0:
                ln = len(board[y][x])
                for i in range(ln):
                    ans += board[y][x][i][0]

    print(ans)