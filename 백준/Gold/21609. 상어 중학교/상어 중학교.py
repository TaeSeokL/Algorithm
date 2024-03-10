from collections import deque
from copy import deepcopy

# 문제의 조건을 만족하는 블록 그룹 찾는 함수
def find_block_group():

    check = [[0]*n for _ in range(n)]   # 방문체크배열
    block_group_list = []               # 현재 배열상태에서 블록 그룹들을 저장할 배열
    dq = deque()                        # 탐색큐

    # 반복문으로 배열을 전체 순회하며 한칸마다 bfs를 타줘야함.
    # 이런식으로 반복문과 조건문을 조합하면 기준블록에 대한 조건은 자동으로 충족하게됨.
    # temp의 젤 앞 칸이 기준블록이 되게 된다는 뜻임.
    for i in range(n):
        for j in range(n):
            # 현재칸에서 시작하는 블록 그룹을 저장하는 임시배열
            temp = []

            # 만약 현재칸이 방문안함, 검은 공아님, 무지개공아님, 빈칸아님 일때 탐색가능함.
            if check[i][j] == 0 and board[i][j] != -1 and board[i][j] != 0 and board[i][j] != -5:
                # 현재칸에 저장된 색깔을 기준색깔로 저장해준 뒤 temp, dq에 위치를 추가해주고 방문체크를 해준다.
                std_color = board[i][j]
                temp.append((i,j))
                dq.append((i,j))
                check[i][j] = 1

                # 큐가 빌때까지 탐색을 진행한다.
                while dq:
                    y,x = dq.popleft()

                    for d in range(4):
                        ny,nx = y + dir[d][0], x + dir[d][1]
                        # 탐색기준
                        # 범위안, 방문안함, 검은공아님, 빈칸아님, 기준색깔과 같은색이거나 무지개 공임 => 탐색가능
                        if 0<=ny<n and 0<=nx<n and check[ny][nx] == 0 and board[ny][nx] != -1 and board[ny][nx] != -5 and (board[ny][nx] == std_color or board[ny][nx] == 0):
                            temp.append((ny,nx))
                            dq.append((ny,nx))
                            check[ny][nx] = 1

            # 한칸에 대한 bfs를 돌고 난 뒤 블록 그룹 임시 배열의 길이가 2이상이라면 블록그룹리스트에 추가해줌.
            if len(temp) >= 2:
                block_group_list.append(temp)

            # **중요한 부분 : 무지개공은 기준색깔이 뭐든 간에 접근이 가능하기 때문에, 한칸에 대한 bfs돌고 난 뒤
            # 무지개공에대한 방문처리를 초기화해줘야함.
            for r in range(n):
                for c in range(n):
                    if board[r][c] == 0:
                        check[r][c] = 0

    # 블록그룹리스트에서 적합한 하나의 블록그룹을 얻기위한 과정 = 다중정렬
    # 블록그룹리스트내의 블록그룹들의 정보를 sorting_list에 저장장해줌. = (블록그룹크기, 무지개블록갯수, 기준블록행이가장큰것, 기준블록열이 가장큰것, 현재블록그룹인덱스)
    sorting_list = []
    if block_group_list:
        for i in range(len(block_group_list)):
            rainbow_block = 0
            for y,x in block_group_list[i]:
                if board[y][x] == 0:
                    rainbow_block += 1

            sorting_list.append([len(block_group_list[i]),rainbow_block,block_group_list[i][0][0],block_group_list[i][0][1],i])
    # 만약 블록그룹이 없다면 게임 종료
    else:
        print(ans)
        exit(0)

    # 문제의 조건대로 정렬해준다. 크기가 큰 순 -> 무지개블록이 많은 순 -> 기준블록의 행이 큰 순 -> 기준블록의 열이 큰 순
    # 젤 앞의 블록그룹이 가장 적합한 블록그룹이니, 인덱스를 받아와서 해당 블록그룹만 뽑아준다.
    sorting_list.sort(key = lambda x:(-x[0],-x[1],-x[2],-x[3]))
    proper_list_li = sorting_list[0][4]
    proper_list = block_group_list[proper_list_li]

    return proper_list

# 중력 작용
def gravity():
    # 열별로 적용시켜줌.
    for c in range(n):
        # pp는 현재 열 상태에서 젤 밑에 있는 빈칸을 가르키는 변수
        # np는 pp위로 검은공 제외 다른 공이 나올때까지 탐색하는 변수
        pp, np = n-1, n-1

        # np가 끝까지 탐색을 끝날때까지 무한반복
        while True:
            # 현재 가르키는 위치가 빈칸일때
            if board[pp][c] == -5 :
                # 현재 탐색 위치가 검은색블록이다 == np, pp 모두 업데이트해줘야함.
                if board[np][c] == -1:
                    np -= 1
                    pp = np
                # 현재 탐색 위치가 빈칸이다 == np 위로 더 탐색
                elif board[np][c] == -5 :
                    np -= 1
                # 현재 탐색 위치가 다른 공이다 == 젤 밑의 빈칸과 바꿔줌.
                else:
                    board[pp][c], board[np][c] = board[np][c], board[pp][c]
            # 현재 가르키는 위치가 빈칸이 아닐 경우 np, pp 모두 업데이트
            else:
                pp -= 1
                np = pp
            # 만약 np가 0까지 모두 탐색을 완료 했다면 break
            if np < 0:
                break

# 목적지 기준 배열 회전 구현
def rotate():
    for y in range(n):
        for x in range(n):
            next_board[y][x] = board[x][n-1-y]

if __name__=='__main__':

    n, m = map(int,input().split())                             # n 맵크기, m 색 갯수
    board = [list(map(int,input().split())) for _ in range(n)]  # 맵 정보
    dir = [(-1,0),(0,1),(1,0),(0,-1)]                           # 이동배열
    ans = 0                                                     # 정답변수
    next_board = [[0] * n for _ in range(n)]                    # 임시저장배열
    
    # 제거할 블록 그룹이 없을때까지 무한반복
    while True:
        # 적합한 블록 그룹 찾기
        list = find_block_group()

        # 블록 삭제 및 점수 획득, 삭제된 블록 -5로 저장
        ans += len(list)**2
        for y,x in list:
            board[y][x] = -5

        # 중력 -> 회전 -> 중력
        gravity()

        rotate()
        board = deepcopy(next_board)

        gravity()