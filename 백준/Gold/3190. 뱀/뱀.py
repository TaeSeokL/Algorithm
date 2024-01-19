from collections import deque

def move():
    global ny,nx
    global ndir

    # 이동 전 한칸 전 위치 저장
    # 새로운 위치 갱신
    py, px = ny, nx
    ny, nx = ny + direction[ndir][0], nx+direction[ndir][1]

    # 다음 위치가 벽이거나 자기 자신의 몸일 경우
    # 게임 경과시간 출력 후 종료
    if arr[ny][nx] == -1 or arr[ny][nx] == 1:
        print(count+1)
        exit(0)

    # 새로운 위치가 사과일 경우
    if arr[ny][nx] == 2 :
        arr[ny][nx] = 1 # 현재 위치에 지렁이 표시
        dq.append((py,px)) # 꼬리정보 추가해주기
    # 새로운 위치가 사과가 아닐 경우
    else:
        arr[ny][nx] = 1 # 현재 위치에 지렁이 표시
        # 큐안에 꼬리정보가 있을 경우
        if dq:
            # 제일 끝 꼬리 삭제 하고
            # 새로운 꼬리 정보 추가해주기
            ry,rx = dq.popleft()
            arr[ry][rx] = 0
            dq.append((py,px))
        # 큐안에 꼬리정보가 없을 경우
        # 이전위치만 갱신해주면 됨.
        else:
            arr[py][px] = 0

def print_arr():
    print('-'*20)
    print('이동 후 배열')
    for x in arr:
        print(x)

if __name__=='__main__':
    n = int(input()) # 보드 크기
    arr = [[0]*(n+2) for _ in range(n+2)] # 보드 크기보다 2씩 더 크게 해서 인덱스와 좌표계를 통일
    k = int(input()) # 사과 갯수

    # 사과 입력받고 표시
    for _ in range(k):
        y, x = map(int,input().split())
        arr[y][x] = 2 # 사과는 2로 표시

    # 벽 표시
    for i in range(n+2):
        for j in range(n+2):
            if i == 0 or i == n+1:
                arr[i][j] = -1
            elif j == 0 or j == n+1:
                arr[i][j] = -1

    ny,nx = 1, 1  # 현재 위치
    count = 0  # 현재 경과 초
    direction = [(-1,0),(0,1),(1,0),(0,-1)] # 순서대로 상 우 하 좌
    ndir = 1 # 초기 방향은 오른쪽
    dq = deque() # 꼬리 위치 표시할 곳
    rotate = [] # 방향 전환 정보 저장 배열
    rotate_num = 0 # 방향 전환 정보 꺼내오는 변수

    L = int(input()) # 지렁이의 방향 전환 횟수

    for i in range(L):
        # s = 방향 전환해야할 초, 전환 방향 D = 오른쪽 90, L = 왼족 90
        # 저장하고 있다가 count == s 일때 전환한번 해주고
        # 계속 while 문을 돌아준다.
        s, d = input().split()
        rotate.append((s, d))

    while True:
        if rotate_num < L :
            s, d = rotate[rotate_num]
        # 방향 전환해야할 때면 전환해줌
        if count == int(s):
            # 오른쪽 90도 회전임. 현재방향에 +1 해주면됨.
            # 근데 만약 현재방향이 3이면 0으로 초기화
            if d == 'D':
                if ndir == 3:
                    ndir = 0
                else:
                    ndir += 1
            # 왼쪽 90도 회전
            elif d == 'L':
                if ndir == 0:
                    ndir = 3
                else:
                    ndir -= 1

            # 한번 움직여주고 카운트 세주고 다음 방향전환 받아야하니 while문 나와줌.
            move()
            # print_arr()
            count += 1
            rotate_num += 1
            continue

        move()
        # print_arr()
        count += 1






