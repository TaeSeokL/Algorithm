from copy import deepcopy
from collections import deque

def virus(board):
    # 바이러스가 퍼져나가는 함수이다.
    # 우선 dfs를 통해 바이러스 퍼짐을 구현하기 위해
    # 큐를 선언한 후 반복문을 통해 초기 바이러스 지점을 파악하고 인덱스를 추가해준다.
    virus_lst = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                virus_lst.append((i,j))

    # 바이러스 인덱스 리스트가 빌때까지 반복문을 돌아준다.
    while virus_lst:
        # 바이러스 퍼져나가기
        y,x = virus_lst.popleft()
        # 상하좌우로 퍼져나가므로 이렇게 구현.
        for dy,dx in ((-1,0),(0,1),(1,0),(0,-1)):
            ny,nx = y + dy, x + dx
            # 인덱스 범위내이고, 빈칸일 경우에만 바이러스가 퍼질 수 있음.
            # 조건이 맞다면 바이러스로 바꿔주고, 큐에 추가해준다.
            if 0<=ny<n and 0<=nx<m and board[ny][nx] == 0:
                board[ny][nx] = 2
                virus_lst.append((ny,nx))

    # 그 후 바이러스가 다 퍼진 board를 return 해준다.
    # 근데 굳이 return 안하고 바로 calculate_warningzone으로 가도될거같음.
    return board

def calculate_warningzone(board):
    global warning_area
    global safety_area

    safety = 0      # 이번 보드에서 안전지역 넓이
    warning = 0     # 이번 보드에서 위험지역 넓이
    # 반복문을 통해 위험지역이 얼마나 넓은지 파악해준다.
    # 조금이라도 시간을 줄이기 위해 위험지역넓이의 최소값을 계산하도록 로직을 짰다.
    # 배열을 순회하다 위험지역최소넓이(warning_area)변수보다 현재 보드에서 위험지역 넓이가 크다면
    # 더 반복할 필요없는것이므로 함수를 종료한다.
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                warning += 1

                 if warning > warning_area:
                     return

    # 만약 반복문이 끝났다는 건 위험지역최소넓이보다 현재 보드에서 위험지역 넓이가 작다는 뜻이된다.
    # 그럴 경우 최소값을 갱신해주고, 다시 반복문을 돌면서 안전지역의 최대값도 갱신해준다.
    # 여기서 안전지역넓이를 max(safety,safety_area)이렇게 안한 이유는 어차피 위험지역넓이가 최소란 얘기는
    # 안전지역 넓이가 최대란 것과 동일한 소리이기 때문이다.
    if warning<warning_area:
        warning_area = warning
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    safety += 1

        safety_area = safety

if __name__=='__main__':
    n,m = map(int,input().split())                                  # n = 세로크기, m = 가로크기
    board = [list(map(int,input().split())) for _ in range(n)]      # 초기맵정보
    test_board = deepcopy(board)                                    # 벽 세워질 테스트 보드
    empty_index = []                                                # 빈칸 인덱스 리스트
    warning_area = 1000000                                          # 위험지역넓이 최대값 변수
    safety_area = 0                                                 # 안전지역넓이 최소값 변수

    # 반복문을 통해 초기 안전지대 영역을 파악한다
    # 이것들 중에서 벽을 세워야하기 때문이다.
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                empty_index.append((i,j))

    l = len(empty_index)
    # 벽이 3개이므로 3중 반복문을 통해 벽을 하나씩 세워준다.
    # 반드시, 반복문이 한번 돌고나서 벽을 세웠던것을 초기화해주는 것이 필요하다.
    # 또한 벽은 이중으로 세울 수 없으므로 반복문의 범위 또한 신경써야한다.
    for i in range(l):
        wall1_y, wall1_x = empty_index[i]
        test_board[wall1_y][wall1_x] = 1
        for j in range(i+1, l):
            wall2_y, wall2_x = empty_index[j]
            test_board[wall2_y][wall2_x] = 1
            for z in range(j+1,l):
                wall3_y, wall3_x = empty_index[z]
                test_board[wall3_y][wall3_x] = 1

                # 여기까지가 벽을 3개 세운 시점이 되겠다.
                # 이상태에서 바이러스가 퍼져나가는 함수로 진입해야하는데
                # testboard를 입력으로 줘버리면 참조가 되어 벽을 세운 배열이 바뀌므로
                # deepcoopy를 통해 입력해준다.
                # 바이러스 퍼져나가기
                test_board2 = deepcopy(test_board)
                arr = virus(test_board2)

                # 위험지대 계산 and 최소값 갱신
                calculate_warningzone(arr)

                test_board[wall3_y][wall3_x] = 0
            test_board[wall2_y][wall2_x] = 0
        test_board[wall1_y][wall1_x] = 0

    print(safety_area)
