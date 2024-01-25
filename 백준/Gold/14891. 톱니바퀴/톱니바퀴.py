from collections import deque

# 톱니 돌리는 함수
def rotate(n,d):
    # 새로운 배열 생성 후에 원배열값을 가져온다.
    # 로직대로 시계 반시계를 구현하면됨.
    arr = [0] * 8
    if d == 1:      # 시계
        for i in range(8):
            if i == 0:
                arr[i] = board[n][7]
            else:
                arr[i] = board[n][i-1]

    else:           # 반시계
        for i in range(8):
            if i == 0:
                arr[7] = board[n][0]
            else:
                arr[i-1] = board[n][i]

    # 방문체크 꼭 해주고, 원배열을 갱신해줌.
    check_lst[n] = 1
    board[n] = arr

# 회전해야하는 톱니와 뱡향을 입력받고 양옆의 톱니도 회전해야하는지 판단하는 함수
def check(n,d):
    # 0번 톱니는 1번확인 / 1번 톱니는 0번, 2번 확인 / 2번 톱니는 1번, 3번 확인 / 3번 톱니는 2번 확인
    # 방문 리스트가 0이고 톱니의 맞닿은 부분이 서로 다를때만 회전한다. 조건 충족시 큐에 추가.
    if n == 0 :
        if check_lst[n+1] != 1 and board[n][2] != board[n+1][6] :
            dq.append((n+1,-d))
    elif n == 1:
        if check_lst[n-1] != 1 and board[n-1][2] != board[n][6] :
            dq.append((n-1,-d))
        if check_lst[n+1] != 1 and board[n][2] != board[n+1][6]:
            dq.append((n+1,-d))
    elif n == 2:
        if check_lst[n-1] != 1 and board[n-1][2] != board[n][6] :
            dq.append((n-1,-d))
        if check_lst[n+1] != 1 and board[n][2] != board[n+1][6]:
            dq.append((n+1,-d))
    else:
        if check_lst[n-1] != 1 and board[n-1][2] != board[n][6] :
            dq.append((n-1,-d))

if __name__=='__main__':
    N = 4                                   # 톱니의 갯수
    board = []                              # 톱니의 초기 정보
    dq = deque()                            # 회전시켜야하는 톱니와 방향을 추가하는 큐
    check_lst = [0] * N                     # 한번회전 시킨 톱니는 더이상 회전 안하므로 방문처리리스트

    # 입력받기
    for _ in range(N):
        arr = list(map(int,input()))
        board.append(arr)
    k = int(input())

    # 회전 명령의 갯수만큼 반복문
    for _ in range(k):
        # 회전할 톱니와 방향을 받아옴.
        n, d = map(int,input().split())

        # 회전하기 전에 양옆에 맞닿은 톱니의 상태를 확인 후에
        # 돌려야할지말지 결정하고 회전시켜줌
        check(n - 1, d)
        rotate(n-1,d)

        # 만약 위 명령에서 큐에 회전해야할 톱니가 추가되었을 경우 똑같잉
        # 톱니 상태 확인후에 회전시킴
        while dq:
            n,d = dq.popleft()
            check(n, d)
            rotate(n,d)
        # 회전 명령이 한번 끝난 후에는 방문 리스트 초기화해줘야함.
        check_lst = [0] * N

    # 정답 계산 기준은 문제에 나와있으므로 참고
    res = 0
    for i in range(4):
        if board[i][0] == 1:
            res += 2**i
    print(res)