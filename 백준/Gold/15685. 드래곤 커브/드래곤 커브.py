
# 정답 체크
def check():
    global cnt
    for i in range(100):
        for j in range(100):
            if board[i][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1 and board[i+1][j] == 1:
                cnt += 1

# 드래곤 커브 그려주는 함수
def dragon_curve(y,x,d,g,direction):
    # direction 배열은 하나의 드래곤커브를 그릴때 다음 방향을 찾기위한 리스트임
    global end_y, end_x
    # 총 세대수 g까지 for문을 돌면서 0, 1, 2 --- g 세대까지의 드래곤 커브를 그려줌
    for k in range(g+1):
        # 이전 방향을 direction에 저장하기 위한 임시 변수/ 세대마다 갱신되야함
        temp = []
        # 0세대 드래곤 커브 그려줌
        if k == 0:
            # 현재 위치와 방향에 따른 다음 위치에 방문체크를 해주고
            board[y][x] = 1
            ny, nx = y + dd[d][0], x + dd[d][1]
            board[ny][nx] = 1

            # 현재 세대 방향을 temp에 저장해줌. 기준점도 업데이트 시켜줌.
            temp.insert(0, d)
            end_y,end_x = ny,nx
        else:
            # 1세대 부터는 반복문을 돌아야함
            # 현재 시점에서 이동해야할 방향의 공식은 기준점 부터 처음까지 방향에 반시계 방향으로 회전하면 됨.
            for i in range(len(direction)):
                # 3일 경우 0으로 나머지는 1 더해줌.
                if direction[i] == 3:
                    new_d = 0
                else:
                    new_d = direction[i] + 1

                # 기준 위치를 잡고 방향에 따른 다음 위치를 구하고 방문체크해줌.
                py,px = end_y,end_x
                ny,nx = py+dd[new_d][0], px + dd[new_d][1]
                board[ny][nx] = 1

                # 현재 세대 방향 저장 변수에 새로 갱신한 방향을 저장해줌. 왜냐?
                # 다음 세대에서도 써야하기 때문에!
                temp.insert(0,new_d)
                end_y,end_x = ny,nx

        # 이렇게 해주는 이유는 세대별 반복문을 돌때 바로 direction 배열을 수정해버리면
        # 그거에 따라 결과가 이상해지기때문에 한 세대의 반복문을 진행할때 direction은 그 전세대
        # 방향들만 저장되게 유지해줌. 그 다음 반복문이 끝나고 난 뒤 현재 세대 + 과거 세대 해서 갱신시켜줌.
        direction = temp + direction


if __name__=='__main__':
    N = int(input())                            # 드래곤커브 갯수
    board = [[0]*101 for _ in range(101)]       # 맵
    dd = [(0,1),(-1,0),(0,-1),(1,0)]            # 방향 순서대로 동 북 서 남
    cnt = 0                                     # 정답 변수
    end_y, end_x = 0, 0                         # 끝난 기준점 변수

    for i in range(N):
        # 드래곤커브 갯수만큼 입력받음.
        x,y,d,g = map(int,input().split())
        dragon_curve(y,x,d,g,[])

    check()
    print(cnt)
