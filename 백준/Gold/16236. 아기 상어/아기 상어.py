# https://great-park.tistory.com/26 문제해설블로그

from collections import deque

# 이동경로 찾는 BFS
def BFS():
    # 현재 상어 위치를 먼저 추가해놓는다.
    dq = deque([(fy,fx)])

    # 방문 체크 배열도 만들고 현재 위치 체크
    visited = [[-1]*n for _ in range(n)]
    visited[fy][fx] = 0

    # 큐가 빌때까지 반복
    while dq:
        # 하나 빼서 상하좌우 네 곳 방문한다.
        y, x = dq.popleft()
        for i in range(4):
            ny, nx = y+ dy[i], x + dx[i]
            # 인덱스 범위 내이고ㅗ
            # 다음 위치의 있는 물고기가 상어 크기보다 작거나 같고, 방문 안했을때. 갈 수 있음.
            if 0<=ny<n and 0<=nx<n:
                if shark_size >= board[ny][nx] and visited[ny][nx] == -1 :
                    # 이때 그전 방문 체크한 값의 +1로 해주어야 함.
                    # 그 위치까지 가는데 걸리는 경로 길이를 표시하는거임.
                    # 큐에 추가후 계속 탐색
                    visited[ny][nx] = visited[y][x] + 1
                    dq.append((ny,nx))

    # 전부 탐색했으면 체크 배열 전달.
    return visited

# 먹을 물고기를 찾는 함수
def solve(visited):
    # 상어 최종 위치 변수와 최단거리 변수
    y, x = 0, 0
    min_distance = 100000000
    # 반복문을 통해 전부 탐색한다.
    for i in range(n):
        for j in range(n):
            # 이때 방문 배열 값이 -1 이면 BFS로 닿지않은곳이므로 가면안되고
            # 물고기 크기가 1보다 크고 상어 크기보다 작아야 물고기 먹을 수 있음.
            # 그 다음 먹을 수 있는 물고기 중에서 현재 상어 위치에서 최단 거리에 위치한 물고기를 찾아야함.
            # min_distance 업데이트 해주면서 찾기. 상어 위치 업데이트
            if visited[i][j] != -1 and 1<=board[i][j]<shark_size:
                if visited[i][j] < min_distance:
                    min_distance = visited[i][j]
                    y, x = i, j

    # 모두 체크했는데 여전히 이거면 False
    if min_distance == 100000000:
        return False
    else:
        # 아니면 최종 상어 위치와 최단 거리 리턴
        return y,x,min_distance

if __name__=='__main__':
    n = int(input())                                                # 맵크기
    board = [list(map(int,input().split())) for _ in range(n)]      # 맵정보
    shark_size = 2          # 상어 초기 나이
    dy = [-1, 0, 1 ,0]      # 이동 변수
    dx = [0, 1, 0, -1]
    fy, fx = 0,0            # 상어 위치 변수
    answer = 0              # 정답변수
    food = 0                # 상어가 물고기 몇마리 먹은지 체크하는 변수

    # 이중 반복문으로 상어 초기 위치를 찾아서 저장하고 그 위치에 0을 넣어준다.
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                fy,fx = i, j
                board[i][j] = 0

    # 무한루프
    while True:
        # BFS를 통해 갈 수 있는 위치를 전부 표시한 Visited 배열을 만든다.
        # 그걸 solve 함수로 전달해서 갈 수 있는 곳중 최단거리를 이동하면서 물고기를 잡아먹는다.
        result = solve(BFS())

        # 만약 결과가 False면 잡아먹을 물고기가 없다는 뜻 == 갈 곳이 없단 뜻
        # 종료
        if not result :
            print(answer)
            break
        else:
            # fy, fx = 물고기 잡아먹고 난 뒤 위치, min_d = 물고기 먹기 위해 이동한 거리
            # 정답에 누적해주고, 현재 상어 위치 0으로 초기화 해주고 물고기 변수 누적해줌.
            fy, fx, min_d = result[0],result[1],result[2]
            answer += min_d
            board[fy][fx] = 0
            food += 1

            # 물고기 변수가 상어사이즈가 되면 상어 나이 +1 물고기 변수 초기화
            if food == shark_size:
                shark_size += 1
                food = 0