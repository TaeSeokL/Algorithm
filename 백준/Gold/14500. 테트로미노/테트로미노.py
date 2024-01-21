
def dfs(L,cnt,tlst):
    global max_val

    # 가지치기
    # 지금까지 계산한것 = cnt, 남은 계산횟수 = 4-L
    # 남은 계산횟수에 전부 맵의 최댓값을 더했는데도
    # 현재 최대합보다 작으면 계산할 필요가 없음
    if cnt+(4-L)*mm <= max_val:
        return

    # 4번계산했을때 최대값 갱신
    if L == 4:
        if cnt > max_val:
            max_val = cnt
            return
        else:
            return
    else:
        # 여기가 중요한 부분인데, 평소 dfs는 상하좌우 탐색 반복문만 썼지만
        # 이문제의 경우 내가 이동한 다음 인덱스에서도 상하좌우를 탐색해야하기 때문에
        # tlst라는 리스트에 내가 이동한 다음 인덱스를 추가해줌으로써
        # 단지 우우우우 >>>> 일방향 탐색을 하는것이아니라
        # 두번째 우 에서도 상하좌우로 탐색할 수 있게 만들어줌.
        for now_position in tlst:
            y,x = now_position
            for i in range(4):
                # 다음 위치 업데이트
                ny,nx = y+dy[i],x + dx[i]
                if 0<=ny<n and 0<=nx<m and check_list[ny][nx] != 1 :
                    cnt += board[ny][nx]
                    check_list[ny][nx] = 1
                    dfs(L+1,cnt,tlst+[(ny,nx)])
                    check_list[ny][nx] = 0
                    cnt -= board[ny][nx]

if __name__=='__main__':
    n,m = map(int,input().split()) # n = 세로크기, m = 가로크기
    board = [list(map(int,input().split())) for _ in range(n)]  # 맵정보
    mm = 0  # 가지치기를 위해 맵의 최댓값 찾기
    for x in board:
        mm = max(max(x),mm)

    # 최대합, 방문체크리스트, 이동방향리스트
    max_val = 0
    check_list = [[0]*m for _ in range(n)]
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    # 맵안의 모든 노드들을 탐색
    # 첫노드를 방문체크해주고 dfs로 넘겨준다.
    for i in range(n):
        for j in range(m):
            check_list[i][j] = 1
            dfs(1,board[i][j],[(i,j)])
            check_list[i][j] = 0

    print(max_val)