
if __name__=='__main__':
    n, m, y,x, k = map(int,input().split())        # n 세로크기 m 가로크기 x,y 초기 주사위 좌표, k 이동횟수
    board = [list(map(int,input().split())) for _ in range(n)]      # 맵정보
    k_arr = list(map(int,input().split()))    # 이동정보
    dy, dx = [0,0,0,-1,1],[0,1,-1,0,0]    # 이동 인덱스 갱신시 사용 동서북남
    n1=n2=n3=n4=n5=n6=0     # 주사위 면 변수 선언
    res_arr = [] # 정답

    for dr in k_arr:
        # 다음 위치 계산
        ny,nx = y + dy[dr], x+dx[dr]
        # 주사위의 이동위치가 인덱스 범위 안일때
        if 0<=ny<n and 0<=nx<m:
            # 이동 방향에 따라 면 업데이트 해줘야함
            if dr == 1: # 동쪽
                n1,n3,n4,n6 = n4,n1,n6,n3
            elif dr == 2: # 서쪽
                n1,n3,n4,n6 = n3,n6,n1,n4
            elif dr == 3 : # 북쪽
                n1,n2,n5,n6 = n5,n1,n6,n2
            else:
                n1,n2,n5,n6 = n2,n6,n1,n5

            if board[ny][nx] == 0:
                # 이동한 칸에 바닥면이 0이면
                # 주사위 바닥면의 숫자가 칸에 복사된다
                board[ny][nx] = n6
            # 이동한 칸에 바닥면이 0이 아니면
            else:
                # 칸에 쓰여진 숫자가 주사위 바닥면으로 복사되고
                # 보드는 0으로 초기화 된다.
                # 이때 기준 형태를 기준으로 n6은 바닥면, n1은 윗면이다
                n6, board[ny][nx] = board[ny][nx], 0

            # 이동 후 윗면에 있는 숫자 저장
            res_arr.append(n1)
            # 이동이 됐으므로 현재 위치 업데이트
            y,x = ny,nx

    print(*res_arr, sep='\n')
