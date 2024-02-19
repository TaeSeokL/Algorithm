from copy import deepcopy

def find_fish(num,board):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == num:
                return (i,j)

def move_fish(sy,sx,board):
    # 물고기 번호 작은 순으로 이동시켜줌
    for fish_num in range(1,17):
        # 물고기의 현재 위치를 전부 배열로 관리해도 되지만 물고기의 위치가 계속 바뀌니 재귀 과정 중 원복을 해줘야할 필요가있음.
        # 그래서 그냥 단순탐색해서 물고기의 현재위치를 찾아줌.
        position = find_fish(fish_num,board)
        # 물고기가 안죽었으면 현재 위치가 리턴됨. 거기서 물고기의 방향을 얻어줌.
        if position:
            y_fish, x_fish = position[0], position[1]
            direction = board[y_fish][x_fish][1]

            # 8번동안 방향을 새로 갱신하며 물고기가 이동가능한곳으로 이동시켜줌.
            # 조건은 범위내이고, 상어가 없는 곳임.
            for _ in range(8):
                next_y_fish, next_x_fish = y_fish + dir[direction][0], x_fish + dir[direction][1]
                if 0<=next_y_fish<4 and 0<=next_x_fish<4:
                    if not (next_y_fish == sy and next_x_fish == sx):
                         # 방향이 계속 갱신되기 때문에 갱신된 방향을 먼저 원래 위치의 배열에 업데이트 해준뒤에 스왑을 해주면 됨.
                         board[y_fish][x_fish][1] = direction
                         board[next_y_fish][next_x_fish], board[y_fish][x_fish] = board[y_fish][x_fish],board[next_y_fish][next_x_fish]
                         break
                # 방향갱신
                direction = (direction+1)%8

# 상어가 이동 가능한 곳을 배열로 리턴해주는 함수
def get_possible_pos(sy,sx,board):
    # 상어의 이동방향을 얻어오기
    direction = board[sy][sx][1]
    position = []

    # 상어의 좌표를 계속 업데이트 하며 상어가 이동 가능한 곳이 있다면 포지션에 추가
    # 이동 조건은 범위내이고 물고기가 존재해야함
    # 상어는 최대 2칸을 움직일 수 있으므로 반복문 범위 설정
    for _ in range(3):
        sy, sx = sy + dir[direction][0], sx + dir[direction][1]
        if 0<=sy<4 and 0<=sx<4 and board[sy][sx][0] != -1:
            position.append((sy,sx))
    return position

def dfs(sy,sx,total_eat,board):
    global max_val
    # 이게 존나 중요함 나중에 재귀가 종료됐을때 원상복구를 해서 같은 상태에서 같은 트리를 탈 수 있게 해줘야함.
    board = deepcopy(board)

    # 상어가 현재위치에 있는 물고기를 먹고, 물고기를 죽었다고 표시하기
    total_eat += board[sy][sx][0]
    board[sy][sx][0] = -1

    # 물고기를 전부 이동시켜 주기
    move_fish(sy,sx,board)

    # 물고기가 이동한뒤에 상어가 이동가능한곳이 있는지 체크하고 리턴받음.
    position = get_possible_pos(sy,sx,board)

    # 이동 가능하다면 그대로 재귀함수 또 타줌.
    if position:
        for next_sy,next_sx in position:
            dfs(next_sy,next_sx,total_eat,board)
    # 없다면 최대값갱신 후 재귀 종료
    else:
        max_val = max(max_val,total_eat)
        return

if __name__=='__main__':
    board = [[None]*4 for _ in range(4)]                               # [물고기번호,방향] 저장, 번호가 -1이면 잡아먹힌것
    dir = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]   # 물고기 방향 갱신 배열
    max_val = 0                                                     # 정답배열

    # 입력받고 보드에다가 표시
    for i in range(4):
        arr = list(map(int, input().split()))
        for j in range(4):
            board[i][j] = [arr[j*2],arr[j*2+1]-1]

    # 상어의 초기 위치
    sy,sx=0,0

    # 재귀함수 시작
    dfs(sy,sx,0,board)

    print(max_val)