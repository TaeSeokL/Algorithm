if __name__ == '__main__':
    n, k = map(int,input().split())     # n 맵 크기, k 말 갯수

    color_board = [list(map(int,input().split())) for _ in range(n)]    # 보드의 색깔 배열
    chess_board = [[[] for _ in range(n)] for _ in range(n)]            # 체스말 표시 배열

    horse = [0]*(k+1)                       # 체스말 위치 관리 배열
    horse_dir = [0]*(k+1)                   # 체스말 방향 관리 배열
    dir = [0,(0,1),(0,-1),(-1,0),(1,0)]     # 체스말 방향에 따른 위치 업데이트 배열

    # 체스말 만큼 반복문으로 배열에 넣어주고 위치와 방향관리 배열에 넣어준다.
    for i in range(1,k+1):
        r,c,d = map(int,input().split())
        chess_board[r-1][c-1] += [i]
        horse[i] = (r-1,c-1)
        horse_dir[i] = d

    # 턴이 1000넘어가면 종료해야함
    for turn in range(1,1001):
        # 말이 순서대로 이동
        for num in range(1,k+1):
            # 현재 말의 위치와 방향을 받아온다.
            y,x = horse[num]
            d = horse_dir[num]

            # 지금 말이 현재 쌓여있는 탑에서 어디에 위치해있는지 확인
            # tmp는 말의 탑을 옮겨줄 배열이다
            idx = chess_board[y][x].index(num)
            tmp = []

            # 현재 말이 위치해있는 층부터 탑의 꼭대기까지있는 말을 tmp로 옮겨준다.
            for i in range(idx, len(chess_board[y][x])):
                tmp += [chess_board[y][x][i]]

            # 이동방향에 따른 다음 위치 업데이트
            ny,nx = y + dir[d][0], x + dir[d][1]

            # 범위를 벗어나거나 파란색일때
            if ny<0 or ny>=n or nx < 0 or nx >= n or color_board[ny][nx] == 2:
                # 방향이 바뀌어야 되므로 방향을 전환해주고 방향 관리 배열에 업데이트해준다.
                if d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 4
                else:
                    d = 3
                horse_dir[num] = d

                # 바뀐 방향으로 다음 위치를 새로 업데이트해준다.
                ny, nx = y + dir[d][0], x + dir[d][1]

                # 범위를 벗어나거나 파란색일때
                if ny<0 or ny>=n or nx < 0 or nx >= n or color_board[ny][nx] == 2:
                    # 이땐 그자리에 그대로 있어야함.
                    continue
                # 흰색일 때
                elif color_board[ny][nx] == 0:
                    # 다음 위치에 tmp를 쌓아주고
                    chess_board[ny][nx] += tmp

                    # 옮긴 말들을 원배열에서 제거 후 위치 업데이트
                    for z in tmp:
                        chess_board[y][x].remove(z)
                        horse[z] = (ny,nx)

                # 다음이 빨간색일때
                elif color_board[ny][nx] == 1:
                    # 다음 위치에 tmp를 거꾸로해서 쌓아주고
                    tmp.reverse()
                    chess_board[ny][nx] += tmp
                    # 옮긴 말들을 원배열에서 제거 후 위치 업데이트
                    for z in tmp:
                        chess_board[y][x].remove(z)
                        horse[z] = (ny, nx)

            # 다음 체스보드가 흰색일때
            elif color_board[ny][nx] == 0:
                chess_board[ny][nx] += tmp

                # 옮긴 말들을 원배열에서 제거 후 위치 업데이트
                for z in tmp:
                    chess_board[y][x].remove(z)
                    horse[z] = (ny, nx)

            # 다음이 빨간색일때
            elif color_board[ny][nx] == 1:
                tmp.reverse()
                chess_board[ny][nx] += tmp

                # 옮긴 말들을 원배열에서 제거 후 위치 업데이트
                for z in tmp:
                    chess_board[y][x].remove(z)
                    horse[z] = (ny, nx)

            # 하나의 말을 옮길때마다 탑 높이가 4가 넘어가는지 체크해야함.
            # 배열을 모두 탐색하면 오래걸리므로 말들이 위치한 곳의 탑 높이만 확인함.
            for i in range(1,k+1):
                y,x = horse[i]
                if len(chess_board[y][x]) >= 4:
                    print(turn)
                    exit(0)

    # 턴이 1000넘어가도록 4층이 안되면 -1 출력 후 종료
    print(-1)
