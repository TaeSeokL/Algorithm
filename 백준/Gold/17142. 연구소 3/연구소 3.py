from collections import deque
from copy import deepcopy

def bfs(active_virus):
    # test_board를 원본 배열을 카피해준다.
    global test_board
    test_board = deepcopy(board)

    # 방문체크하는 배열
    check_board = [[0]*n for _ in range(n)]

    # 활성화 바이러스 표시하면서 탐색 큐에 레벨과 함께 추가
    # 여기서 레벨이 탐색에 걸린 시간이다.
    for y,x in active_virus:
        test_board[y][x] = -2
        check_board[y][x] = -2
        dq.append((y,x,0))

    # 큐가 빌때 까지 탐색
    while dq:
        # 현재 위치와 레벨
        y,x,L = dq.popleft()

        # 4방향을 돌며 탐색
        for i in range(4):
            ny, nx = y + dir[i][0] , x + dir[i][1]
            # 범위 체크
            if 0<=ny<n and 0<=nx<n:
                # 만약 다음 위치가 빈칸이거나, 현재 탐색 시간이 원래 저장되어잇는 탐색 시간보다 작을때
                # 탐색을 해야함 => 큐에 추카 후 탐색시간 갱신, 방문체크
                # *추가로 여기서 방문여부를 확인 안하는 것은 빈칸일 경우
                # 방문여부와 관계없이 더 적은 탐색시간을 저장하는 로직이기 때문이다.
                # 따라서 방문배열의 경우 비활성 바이러스들이 여러개 겹쳐있을때
                # 무한루프에 빠지는 것을 방지하기 위한 것이다.
                if test_board[ny][nx] == 0 or test_board[ny][nx] > L+1:
                    dq.append((ny,nx,L+1))
                    test_board[ny][nx] = L + 1
                    check_board[ny][nx] = 1

                # 비활성 바이러스를 발견했을때, 테스트보드의 값은 업데이트하지않고
                # 방문체크하고 탐색배열에만 추가해준다. = 무한루프 방지
                elif test_board[ny][nx] == -1 and check_board[ny][nx] == 0:
                    check_board[ny][nx] = 1
                    dq.append((ny,nx,L+1))

def dfs(L,S):
    global min_val
    global flag

    # m개만큼 선택했으면 bfs로 넘겨서 탐색하기
    if L == m:
        # bfs로 선택한 활성 바이러스 전달 후 바이러스 전염 시작하기
        bfs(activate_virus)

        # 전염 다 됐으면, 현재 전염 상태에서 탐색에 걸린 최대 시간 구하기
        # 만약 배열에 빈칸이 있으면 그 즉시 break,
        # 근데 break가 되지 않고 else: 로 넘어가면 == 빈칸을 모두 전염시킨 경우
        # flag를 True로 바꾸고 전체 최소시간을 갱신해준다.
        time = 0
        for x in test_board:
            if 0 in x:
                break
            time = max(time,max(x))
        else:
            flag = True
            if time < min_val:
                min_val = time

        # print('선택한 바이러스 위치 : ', activate_virus)
        # print('------------바이러스 퍼지고 난 뒤 배열-------------')
        # for i in range(n):
        #     for j in range(n):
        #         print('%3d'%test_board[i][j], end='')
        #     print()
        # print()
        return
    else:
        # 전체바이러스 개수중에 m개 선택하기
        for i in range(S,len(virus)):
            activate_virus.append(virus[i])
            dfs(L+1,i+1)
            activate_virus.pop()

if __name__=='__main__':
    n, m = map(int,input().split())     # n = 맵크기, m = 고를 바이러스 수
    board = [list(map(int,input().split())) for _ in range(n)]  # 맵정보
    dir = [(-1,0),(0,1),(1,0),(0,-1)]   # 바이러스 이동방향
    dq = deque()                        # 탐색할 위치 큐
    min_val = 1000000000000             # 빈칸을 모두 채웠을때 최소시간 변수
    flag = False                        # 바이러스를 어떻게 놓아도 빈칸을 모두 채울 수 없는 경우 체크 변수
    virus = []                          # 전체바이러스 위치 배열
    activate_virus = []                 # 활성화할 바이러스 위치 배열

    # 바이러스를 모두 -1로 초기화,
    # 벽을 모두 -3으로 초기화
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                virus.append((i,j))
                board[i][j] = -1
            elif board[i][j] == 1:
                board[i][j] = -3

    # 활성화할 바이러스 조합선택하기
    dfs(0,0)

    # 만약 flag가 True == 빈칸을 모두 채울 수 있는 경우가 한가지라도 있다.
    # 만약 flag가 False == 바이러스를 어떻게 놓아도 빈칸을 모두 채울 수 없다.
    if flag:
        print(min_val)
    else:
        print(-1)
