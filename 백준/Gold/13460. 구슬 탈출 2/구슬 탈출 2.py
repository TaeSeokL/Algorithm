
from collections import deque

def bfs(ry,rx,by,bx):
    global count
    dq = deque() # 공의 위치를 저장하는 큐
    visited = [] # 공이 방문한 곳을 저장해놓는 배열

    dq.append((ry,rx,by,bx)) # 큐에 현재 위치를 추가하고
    visited.append((ry,rx,by,bx)) # 방문처리

    # 큐가 빌때까지 반복 진행
    while dq:
        for  _ in range(len(dq)):
            # 현재 위치를 큐에서 꺼내기
            ry,rx,by,bx = dq.popleft()

            # 10번 이내로 공을 못빼냈을 경우 break
            if count > 10:
                print(-1)
                return

            # 공 위치가 구멍일때
            if board[ry][rx] == 'O':
                print(count)
                return

            # 상하좌우 탐색
            for i in range(4):

                # 빨간공에 현재 위치 저장
                nry = ry
                nrx = rx

                # 공이 멈출때까지 한방향으로 이동
                while True:
                    # 빨간공의 새로운 위치 갱신
                    nry +=  dy[i]
                    nrx +=  dx[i]

                    # 만약 벽일 경우 #
                    if board[nry][nrx] == '#':
                        # 벽에 위치해있으니 한칸씩 이전으로 옮기기
                        nry -= dy[i]
                        nrx -= dx[i]
                        break
                    # 만약 구멍일 경우
                    elif board[nry][nrx] == 'O':
                        break

                # 파란 공에 현재 위치 저장
                nby = by
                nbx = bx
                while True:
                    # 파란공의 새로운 위치 갱신
                    nby += dy[i]
                    nbx += dx[i]

                    # 만약 벽일 경우 #
                    if board[nby][nbx] == '#':
                        # 벽에 위치해있으니 한칸씩 이전으로 옮기기
                        nby -= dy[i]
                        nbx -= dx[i]
                        break
                    # 만약 구멍일 경우
                    elif board[nby][nbx] == 'O':
                        break

                # 새로 움직인 파란공의 위치가 구멍일 때 == 안되는 경우
                # 큐에 추가하지 않고 == 그 다음 루트를 탐색하지 않고 이 경우는 스킵
                if board[nby][nbx] == 'O':
                    continue

                # 한쪽 방향으로 이동 후에 빨간 파란 공의 위치가 같을때
                if nry == nby and nrx == nbx:
                    # 이전위치와 현재위치의 길이를 구해서 절댓값이 큰쪽을 옮겨야함
                    # 즉 더 많은 거리를 이동한쪽이 이전 위치 기준 더 뒤에 있엇으므로 한칸 전으로 땡기기
                    if (abs(ry-nry)+abs(rx-nrx)) > (abs(by-nby)+abs(bx-nbx)): # 빨간공이 더 멀리 있었을 때
                        nry -= dy[i]
                        nrx -= dx[i]
                    else: # 파란공이 더 멀리 있었을때
                        nby -= dy[i]
                        nbx -= dx[i]

                # 새로 이동한 좌표가 방문하지 않았을때
                # 큐에 추가 후 방문 처리
                if (nry,nrx,nby,nbx) not in visited:
                    visited.append((nry,nrx,nby,nbx))
                    dq.append((nry,nrx,nby,nbx))

        count += 1

    # 10번내로 움직였지만 성공한 케이스가 없는 경우
    # 1. 파랑과 빨강 공이 동시에 구멍으로 나온 경우
    # 2. 파랑공이 구멍으로 나온 경우
    # 3. 공을 더이상 움직일 수 없는 경우
    print(-1)


if __name__=='__main__':
    # 입력 받기
    # n, m = map(int,sys.stdin.readline().split()) # n 세로, m 가로
    n, m = map(int,input().split())
    board = []
    count = 0 # 이동횟수
    ry,rx,by,bx = 0,0,0,0
    # 상하좌우
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    for i in range(n):
        # 개행문자제거 후 보드에 한줄씩 추가
        # li = list(sys.stdin.readline().rstrip())
        li = list(input())
        board.append(li)
        # 입력받은 리스트에서 빨간공과 파란공의 위치를 찾아서 저장해두기
        for j in range(m):
            if li[j] == 'R':
                ry, rx = i, j
            if li[j] == 'B':
                by, bx = i, j

    bfs(ry,rx,by,bx)


