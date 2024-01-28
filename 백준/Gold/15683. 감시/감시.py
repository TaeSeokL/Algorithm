from copy import deepcopy

def fill(board,dir,y,x):
    # 각 씨씨티비별 뻗어나가야할 방향 == dir
    # 그 방향으로 계속 업데이트 해준다.
    for i in dir:
        ny = y
        nx = x
        while True:
            ny = ny + dy[i]
            nx = nx + dx[i]
            # 만약 인덱스 범위 밖이거나, 벽이 있으면 break
            # 아니면 그 자리를 -1로 채워준다.
            if ny<0 or nx<0 or ny>=n or nx>=m:
                break
            elif board[ny][nx] == 6:
                break
            elif board[ny][nx] == 0 :
                board[ny][nx] = -1

def dfs(depth,arr):
    global min_val
    # depth는 cctv 배열을 탐색하는 인데스이다.
    # 종료조건은 depth가 cctv를 다 사용했을 때 즉 depth == len(cctv)이다
    if depth == len(cctv):
        # 여기서 최소값을 갱신해준다
        cnt = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0 :
                    cnt += 1
        min_val = min(min_val,cnt)
        return

    # 씨씨티비를 사용해야할때
    # 원배열의 유지와 재귀호출에서의 복원을 위해 입력받은 배열을 deepcopy해준다.
    # cctv 배열에서 위치와 씨씨티비 번호를 가져와준다.
    temp = deepcopy(arr)
    y,x,cctv_number = cctv[depth]
    # 각 cctv번호에 알맞게 회전방향 중 택일을 하여 감시를 시작한 후 재귀호출을 실행해준다.
    for i in mode[cctv_number]:
        # 여기서 따로 배열을 리턴안받아도 주소값을 board와 temp가 공유하기 때문에 temp가 자동업데이트됨
        fill(temp,i,y,x)
        dfs(depth+1,temp)
        # 이 코드 다음 다른 방향을 갈때는 그 전 씨씨티비 까지 돌았던 상태의 맵을 불러와야한다.
        # 즉 입력받은 arr이 그 전 씨씨티비 감시가 이루어진 배열이니 그걸 temp에 복사해줌으로써
        # 바로 다음 반복문에서도 반복문 시작과 동일한 효과를 낼 수 있게해준다.
        temp = deepcopy(arr)

if __name__=='__main__':
    n,m = map(int,input().split())      # 맵크기
    ori_board = [list(map(int,input().split())) for _ in range(n)]      # 맵정보
    cctv = []       # cctv 정보 배열
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    min_val = 100   # 정답변수

    # 순서대로 1번,2번 -- 감시카메라가 갈 수 있는 방향
    mode = [
        [],
        [[0],[1],[2],[3]],
        [[0,2],[1,3]],
        [[0,1],[1,2],[2,3],[3,0]],
        [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
        [[0,1,2,3]]]

    # 만약 씨씨티비가 발견된다면 그 인덱스와 씨씨티비 번호를 배열에 저장한다.
    for i in range(n):
        for j in range(m):
            if ori_board[i][j] != 6 and ori_board[i][j] != 0:
                cctv.append((i,j,ori_board[i][j]))

    dfs(0,ori_board)
    print(min_val)


