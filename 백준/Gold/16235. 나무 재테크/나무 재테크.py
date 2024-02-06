# 내코드
# from collections import deque
#
# def spring():
#     # 현재 나무 위치 개수 만큼 반복문을 돌아줌.
#     tl = len(tree_pos)
#     for i in range(tl):
#         # 중간에 나무가 제거되어 i가 tl이 되면 함수 종료
#         if i == tl:
#             return
#
#         # 첫번째 나무 위치를 받아옴.
#         y,x = tree_pos[i][0], tree_pos[i][1]
#         # L은 0부터 첫 위치의 나무들을 순회해줌. 한 위치에 나무가 여러개일 수 있기 때문.
#         L = 0
#         while L<len(board[y][x]):
#             if board[y][x][L] <= arr[y][x]: # 양분이 충분하다면
#                 arr[y][x] -= board[y][x][L] # 양분 업데이트
#                 board[y][x][L] += 1         # 나이 하나 증가
#                 L += 1                      # 인덱스도 하나 증가
#             else:
#                 dead_tree.append((y, x, board[y][x][L]))  # 죽은나무큐에 추가
#                 board[y][x].remove(board[y][x][L])        # 죽은나무는 나무리스트에서 제거
#                 # 만약 현재위치에 나무가 없다면 나무 위치 배열에서 제거하고 tl -1
#                 if len(board[y][x]) == 0:
#                     tree_pos.remove((y,x))
#                     tl -= 1
#
# # 죽은 나무 하나씩 꺼내서 양분 추가해줌.
# def summer():
#     while dead_tree:
#         y,x,v = dead_tree.popleft()
#         v = v//2
#         arr[y][x] += v
#
# def fall():
#     # 현재 나무 위치 개수만큼 반복문
#     tl = len(tree_pos)
#     for i in range(tl):
#         # 현재 위치받아온 뒤 탐색
#         y,x = tree_pos[i][0], tree_pos[i][1]
#
#         # 현재 위치의 나무들을 탐색
#         # 만약 나이가 5의 배수이면 번식해줌.
#         for j in range(len(board[y][x])):
#             if board[y][x][j] % 5 == 0:
#                 for ry, rx in ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)):
#                     ny, nx = y+ry, x+rx
#                     if 0<=ny<N and 0<=nx<N:
#                         board[ny][nx].insert(0,1)
#                         if (ny,nx) not in tree_pos:
#                             tree_pos.append((ny,nx))
# # 양분 추가해줌.
# def winter():
#     for i in range(N):
#         for j in range(N):
#             arr[i][j] += add_arr[i][j]
#
# if __name__=='__main__':
#     N, M, K = map(int,input().split())                              # N 맵크기, M 초기 나무 수, K 년 수
#     arr = [[5]*N for _ in range(N)]                                 # 초기 양분 상태
#     add_arr = [list(map(int,input().split())) for _ in range(N)]    # 추가 양분 배열
#     board = [[[] for _ in range(N) ] for _ in range(N)]             # 나무나이 배열
#     tree_pos = []                                                   # 나무위치 배열
#     dead_tree = deque()                                             # 죽은나무 배열
#     ans = 0                                                         # 정답 배열
#
#     # 맵에 나무 위치 추가
#     for i in range(M):
#         x,y,z = map(int,input().split())
#         board[y-1][x-1].append(z)
#         tree_pos.append((y-1,x-1))
#
#     # 주어진 년수만큼 반복문 돌아주기
#     for year in range(K):
#         spring()
#         summer()
#         fall()
#         winter()
#
#     # 나무 있는 곳 세어주기
#     for i in range(N):
#         for j in range(N):
#             t = len(board[i][j])
#             if t != 0:
#                 ans += t
#
#     print(ans)

# 답코드
from collections import deque

def spring_summer():
    # 배열의 모든 위치를 돌면서 나무가 있는 곳 탐색
    for i in range(N):
        for j in range(N):
            for k in range(len(board[i][j])):
                # 나무 있는 곳 발견시 현재 땅의 양분과 나무의 나이를 비교해서
                # 먹을 수 있으면 양분과 나이 업데이트
                if board[i][j][k] <= arr[i][j]:
                    arr[i][j] -= board[i][j][k]  # 양분 업데이트
                    board[i][j][k] += 1  # 나이 하나 증가
                else:
                    # 먹을 수 없는 경우 k번째 나무부터는 모두 죽어야함.
                    # 전체 나무 갯수(len(board[i][j])) - k = 죽어야할 나무 갯수이므로 반복문을 이렇게 돌아주ㅗㄱ
                    # 바로 뒤에서 부터 팝해서 여름에 할 역할까지 처리함.
                    for _ in range(k,len(board[i][j])):
                        arr[i][j] += board[i][j].pop() // 2
                    break

def fall():
    # 모두 탐색하며 나무 있는 곳 찾기
    for i in range(N):
        for j in range(N):
            for k in range(len(board[i][j])):
                # 만약 나무 나이가 5의 배수이면 주변에 나무 뿌리기
                if board[i][j][k] % 5 == 0:
                    for ry, rx in ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)):
                        ny, nx = i+ry, j+rx
                        if 0<=ny<N and 0<=nx<N:
                            board[ny][nx].appendleft(1)

# 양분 추가해줌.
def winter():
    for i in range(N):
        for j in range(N):
            arr[i][j] += add_arr[i][j]

if __name__=='__main__':
    N, M, K = map(int,input().split())                              # N 맵크기, M 초기 나무 수, K 년 수
    arr = [[5]*N for _ in range(N)]                                 # 초기 양분 상태
    add_arr = [list(map(int,input().split())) for _ in range(N)]    # 추가 양분 배열
    board = [[deque() for _ in range(N) ] for _ in range(N)]        # 나무나이 배열
    ans = 0                                                         # 정답 배열

    # 맵에 나무 위치 추가
    for i in range(M):
        y,x,z = map(int,input().split())
        board[y-1][x-1].append(z)

    # 주어진 년수만큼 반복문 돌아주기
    for year in range(K):
        spring_summer()
        fall()
        winter()

    # 나무 있는 곳 세어주기
    for i in range(N):
        for j in range(N):
            t = len(board[i][j])
            if t != 0:
                ans += t

    print(ans)



