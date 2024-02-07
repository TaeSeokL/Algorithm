from copy import deepcopy

# 미세먼지 확산
def dust():
    # 반복문으로 배열 전부 탐색
    for i in range(n):
        for j in range(m):
            cnt = 0     # 확산 몇번 됐는지 계산하는 변수
            # 공기 청정기나 빈칸이 아닐때만 확산이 됨.
            # 4방향으로 반복문 시작
            if board[i][j] != -1 and board[i][j] != 0:
                for z in range(4):
                    ny, nx = i + dy[z], j + dx[z]
                    # 다음 위치가 범위 안이고, 공기청정기가 아닐때에만 확산이 됨.
                    # 문제에 주어진 조건대로 원배열안의 먼지를 5로 나눈 몫을 dust_board에 누적해줌.
                    # 확산 횟수도 +1 해줌.
                    if 0<=ny<n and 0<=nx<m and board[ny][nx] != -1:
                        dust_board[ny][nx] += board[i][j] // 5
                        cnt += 1
                # 확산이 일어난 지점에도 먼지 양을 업데이트 해줌.여기서도 누적해줘야함.
                # 확산은 동시에 일어나기 때문에 모두 누적
                dust_board[i][j] += board[i][j] - (board[i][j]//5) * cnt

def air_conditioner():
    # 배열을 그려서 공기청정기 윗부분, 아랫부분 나눠서 구현했음.
    # 스왑이 잘 되기 때문에, pv에 우선 0을 저장해두고 다음 위치에 넣고
    # pv에 다음 위치에 있던 값을 넣는 식으로 범위 계산을 해서 구현해주었음.
    # 주의할 점은 공기청정기 인덱스까지 갔을때 pv에 그 전 먼지양이 저장되어 있을텐데
    # 이값은 스왑하지 않고 그냥 버려버려야함. 공기가 청정되는 과정임.

    # 공기청정기 위쪽
    pv = 0
    # 오른쪽 진행
    for i in range(1,m):
        dust_board[top_y][i], pv = pv, dust_board[top_y][i]
    # 위쪽 진행
    for i in range(top_y-1,-1,-1):
        dust_board[i][m-1], pv = pv, dust_board[i][m-1]
    # 왼쪽 진행
    for i in range(m-2,-1,-1):
        dust_board[0][i], pv = pv, dust_board[0][i]
    # 아래쪽 진행
    for i in range(1, top_y+1):
        if i == top_y:
            continue
        dust_board[i][0], pv = pv, dust_board[i][0]

    # 공기청정기 아래쪽
    pv = 0
    for i in range(1,m):
        dust_board[bottom_y][i], pv = pv, dust_board[bottom_y][i]
    # 아래쪽 진행
    for i in range(bottom_y+1, n):
        dust_board[i][m-1], pv = pv, dust_board[i][m-1]
    # 왼쪽 진행
    for i in range(m-2,-1,-1):
        dust_board[n-1][i], pv = pv, dust_board[n-1][i]
    # 위쪽 진행
    for i in range(n-2,bottom_y-1,-1):
        if i == bottom_y:
            continue
        dust_board[i][0], pv = pv, dust_board[i][0]

if __name__=='__main__':
    n,m,t = map(int,input().split())                            # nxm, t 초
    board = [list(map(int,input().split())) for _ in range(n)]  # 초기배열
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    # 공기청정기의 위치 저장해놓기
    condi = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == -1 :
                condi.append((i,j))
    top_y, top_x, bottom_y, bottom_x = condi[0][0], 0, condi[1][0], 0

    # t초동안 반복문 돔.
    # 원배열에 미세먼지 확산을 구현하면 반복문 도는 중에 원배열이 바뀌어서 이상하게 되므로
    # 원배열은 유지하고 dust_board에 미세머지 확산과 공기청정기 영향을 전부 구현
    # 그 후 원배열 변수에 dust_board를 카피해주고 공기청정기를 표시해서 다음 단계를 위한 준비를 함.
    for _ in range(t):
        dust_board = [[0] * m for _ in range(n)]
        dust()
        air_conditioner()
        board = deepcopy(dust_board)
        board[top_y][top_x] = -1
        board[bottom_y][bottom_x] = -1

    # 정답 계산
    ans = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] != -1:
                ans += board[i][j]
    print(ans)

