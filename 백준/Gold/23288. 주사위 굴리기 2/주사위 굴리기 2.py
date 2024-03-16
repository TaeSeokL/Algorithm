from collections import deque
def dir_is_possible():
    global d,y,x

    ny = y + dir[d][0]
    nx = x + dir[d][1]

    if 0<=ny<n and 0<=nx<m:
        y, x = ny, nx
        return
    else:
        # 오른쪽일때
        if d == 1:
            d = 2
        # 왼쪽
        elif d == 2:
            d = 1
        # 위쪽
        elif d == 3:
            d = 4
        # 아래쪽
        else:
            d = 3

        ny = y + dir[d][0]
        nx = x + dir[d][1]
        y, x = ny, nx
        return

def move_dice():
    global d,y,x,ans
    global dicelr, diceud

    # 주사위 실제 이동
    # 오른쪽으로 이동함.
    if d == 1:
        dicelr.append(dicelr.popleft())
        diceud[1], diceud[3] = dicelr[1], dicelr[3]
    # 왼쪽으로 이동함.
    elif d == 2:
        dicelr.appendleft(dicelr.pop())
        diceud[1], diceud[3] = dicelr[1], dicelr[3]
    # 위쪽으로 이동함.
    elif d == 3:
        diceud.appendleft(diceud.pop())
        dicelr[1], dicelr[3] = diceud[1], diceud[3]
    # 아래쪽으로 이동함.
    else:
        diceud.append(diceud.popleft())
        dicelr[1], dicelr[3] = diceud[1], diceud[3]
    # 주사위 밑 숫자
    down_num = dicelr[1]

    # 점수 구하기 위한 BFS 돌아주기
    board_num = board[y][x]             # 현재위치 보드 숫자
    board_num_cnt = 1                   # 현재위치 보드 숫자랑 이어진 갯수
    dq = deque()                        # 탐색큐
    check = [[0]*m for _ in range(n)]   # 방문체크

    dq.append((y,x))
    check[y][x] = 1

    while dq:
        ay, ax = dq.popleft()

        for i in range(1,5):
            dy = ay + dir[i][0]
            dx = ax + dir[i][1]

            if 0<=dy<n and 0<=dx<m and check[dy][dx] == 0 and board[dy][dx] == board_num:
                dq.append((dy,dx))
                check[dy][dx] = 1

                board_num_cnt += 1
    # 점수구하기
    ans += board_num*board_num_cnt

    # 주사위 밑 숫자와 보드 숫자 크기 비교 후 방향 조정해주기
    if down_num > board_num :   # 주사위 밑 숫자가 더 클때 = 시계방향 90도
        # 현재 방향이 순서대로 오 왼 위 밑 일때
        if d == 1:
            d = 4
        elif d == 2:
            d = 3
        elif d == 3:
            d = 1
        else:
            d = 2
    elif down_num < board_num : # 보드 숫자가 더 클때 = 반시계방향 90도
        if d == 1:
            d = 3
        elif d == 2:
            d = 4
        elif d == 3:
            d = 2
        else:
            d = 1

if __name__=='__main__':
    n, m, k = map(int,input().split())      # n m 맵크기, k 이동횟수

    board = [list(map(int,input().split())) for _ in range(n)]  # 맵정보
    dir = [0,(0,1),(0,-1),(-1,0),(1,0)]                         # 동서북남

    y, x = 0, 0                  # 초기 위치
    d = 1                        # 방향변수 오 왼 위 밑 1 2 3 4
    dicelr = deque([4,6,3,1])    # 주사위 왼오 관리배열 / 왼 밑 오 윗 0 1 2 3(인덱스)
    diceud = deque([2,6,5,1])    # 주사위 위밑 관리배열 / 뒷 밑 앞 윗 0 1 2 3

    ans = 0

    for turn in range(k):
        # 현재 이동방향 이동 가능한지 확인
        dir_is_possible()
        # 주사위 이동 후 점수 획득
        move_dice()

    print(ans)
