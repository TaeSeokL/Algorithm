if __name__=='__main__':
    n, m = map(int,input().split())                                 # n 맵크기, m 명령수
    board = [list(map(int,input().split())) for _ in range(n)]      # 맵정보
    dir = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]   # 이동
    water_copy_bug_dir = [(-1,-1),(-1,1),(1,1),(1,-1)]              # 이동
    cloud = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]                       # 초기 구름 위치

    for turn in range(m):
        d, s = map(int,input().split())     # d 방향, s 속도
        previous_cloud = []                 # 물양이 증가한 위치 저장배열

        # 구름 이동 및 비내리기
        for cy,cx in cloud:
            # 다음위치 = (현재위치 + 속력*방향 + n)%n -> n을 더하는 것은 음수를 방지하기 위함.
            ny = (cy+s*dir[d-1][0]+n)%n
            nx = (cx+s*dir[d-1][1]+n)%n
            # 물양 증가
            board[ny][nx] += 1
            # 물양 증가한 곳 저장해두기
            previous_cloud.append((ny,nx))

        # 물복사 버그 마법 -> 물양이 증가한곳만 버그마법이 일어남.
        # 처음엔 line48에서처럼 모든것을 위치로 관리하고 not in을 쓰려고했지만
        # 시간차이가 많이나서 이미 물양이 증가한 곳을 방문배열로 체크해둔뒤 방문체크가 안된곳에만
        # 구름을 생성해주면 됨. 이렇게하면 512ms -> 172ms로 단축됨.
        v = [[0]*n for _ in range(n)]
        for cy, cx in previous_cloud:
            water = 0
            v[cy][cx] = 1
            # 대각선 체크 후 물 있는지 확인. 여기서 처음에는 next_board를 정의후
            # 각 위치에 동시에 물양을 증가시키려고 했음. 왜냐하면, 물양이 0이었다가 순차적으로 처리하면서
            # 1이된 경우가 있을까봐. 하지만 문제조건상 여기서 처리하는 위치들은 물양이 0일수가없음.
            # 그래서 그냥 기존 board에 바로바로 업데이트 해주어도됨.
            for d in range(4):
                ny = cy + water_copy_bug_dir[d][0]
                nx = cx + water_copy_bug_dir[d][1]
                # 범위내이고 물이 있을때
                if 0<=ny<n and 0<=nx<n and board[ny][nx] > 0:
                    water += 1
            # 물복사
            board[cy][cx] += water

        # 구름 리스트 초기화
        cloud = []
        # 배열 전체 순회하면서 방문안한곳과 물양이 2이상인곳에 구름생성해줌.
        for i in range(n):
           for j in range(n):
               # if board[i][j] >= 2 and (i,j) not in previous_cloud:
               if board[i][j] >= 2 and v[i][j] ==0 :
                   cloud.append((i,j))
                   board[i][j] -= 2

    # 정답 출력 : 물의 합
    ans = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 :
                ans += board[i][j]

    print(ans)
