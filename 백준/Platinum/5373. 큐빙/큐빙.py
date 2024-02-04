# 그냥 쌩 노가다
def rotate(p,d):
    # 앞면
    if p == 'F':
        # 시계 방향
        if d == '+':
            # 앞면 시계방향 회전
            front[0][0], front[0][1], front[0][2], front[1][0], front[1][1], front[1][2], \
            front[2][0], front[2][1], front[2][2] = front[2][0], front[1][0], front[0][0], \
            front[2][1], front[1][1], front[0][1], front[2][2], front[1][2], front[0][2]
            # 나머지 면 처리
            up[2][0], up[2][1], up[2][2],right[0][0],right[1][0],right[2][0],\
            down[2][0], down[2][1], down[2][2], left[0][2], left[1][2], left[2][2] = \
            left[2][2], left[1][2], left[0][2], up[2][0], up[2][1], up[2][2], \
            right[0][0], right[1][0], right[2][0], down[2][2], down[2][1], down[2][0]
        else:
            # 앞면 반시계 방향 회전
            front[0][0], front[0][1], front[0][2], front[1][0], front[1][1], front[1][2], \
            front[2][0], front[2][1], front[2][2] = front[0][2], front[1][2], front[2][2], \
            front[0][1], front[1][1], front[2][1], front[0][0], front[1][0], front[2][0]
            # 나머지 면 처리
            up[2][0], up[2][1], up[2][2], right[0][0], right[1][0], right[2][0], \
            down[2][0], down[2][1], down[2][2], left[0][2], left[1][2], left[2][2] = \
            right[0][0], right[1][0], right[2][0], down[2][0], down[2][1], down[2][2], \
            left[2][2], left[1][2], left[0][2], up[2][2], up[2][1], up[2][0]
    # 뒷면
    elif p == 'B':
        # 시계 방향
        if d == '+' :
            # 뒷면 시계방향 회전
            back[0][0], back[0][1], back[0][2], back[1][0], back[1][1], back[1][2], \
            back[2][0], back[2][1], back[2][2] = back[2][0], back[1][0], back[0][0], \
            back[2][1], back[1][1], back[0][1], back[2][2], back[1][2], back[0][2]
            # 나머지면 처리
            up[0][0], up[0][1], up[0][2], right[0][2], right[1][2], right[2][2], \
            down[0][0], down[0][1], down[0][2], left[2][0],left[1][0], left[0][0] = \
            right[0][2], right[1][2], right[2][2], down[0][0], down[0][1], down[0][2], \
            left[2][0], left[1][0], left[0][0], up[0][0], up[0][1], up[0][2]
        else:
            # 뒷면 반시계 방향 회전
            back[0][0], back[0][1], back[0][2], back[1][0], back[1][1], back[1][2], \
            back[2][0], back[2][1], back[2][2] = back[0][2], back[1][2], back[2][2], \
            back[0][1], back[1][1], back[2][1], back[0][0], back[1][0], back[2][0]
            # 나머지면 처리
            up[0][0], up[0][1], up[0][2], right[0][2], right[1][2], right[2][2], \
            down[0][0], down[0][1], down[0][2], left[2][0], left[1][0], left[0][0] = \
            left[2][0], left[1][0], left[0][0], up[0][0], up[0][1], up[0][2], \
            right[0][2], right[1][2], right[2][2], down[0][0], down[0][1], down[0][2]
    # 왼쪽면
    elif p == 'L':
        # 시계 방향
        if d == '+':
            # 왼쪽면 시계방향 회전
            left[0][0], left[0][1], left[0][2], left[1][0], left[1][1], left[1][2], \
            left[2][0], left[2][1], left[2][2] = left[2][0], left[1][0], left[0][0], \
            left[2][1], left[1][1], left[0][1], left[2][2], left[1][2], left[0][2]
            # 나머지면 처리
            up[0][0], up[1][0], up[2][0], front[0][0], front[1][0], front[2][0], \
            down[0][2], down[1][2], down[2][2], back[0][2], back[1][2], back[2][2] = \
            back[2][2], back[1][2], back[0][2], up[0][0], up[1][0], up[2][0], \
            front[2][0], front[1][0], front[0][0], down[0][2], down[1][2], down[2][2]
        else:
            # 왼쪽면 반시계 방향 회전
            left[0][0], left[0][1], left[0][2], left[1][0], left[1][1], left[1][2], \
            left[2][0], left[2][1], left[2][2] = left[0][2], left[1][2], left[2][2], \
            left[0][1], left[1][1], left[2][1], left[0][0], left[1][0], left[2][0]
            # 나머지면 처리
            up[0][0], up[1][0], up[2][0], front[0][0], front[1][0], front[2][0], \
            down[2][2], down[1][2], down[0][2], back[0][2], back[1][2], back[2][2] = \
            front[0][0], front[1][0], front[2][0], down[2][2], down[1][2], down[0][2], \
            back[2][2], back[1][2], back[0][2], up[2][0], up[1][0], up[0][0]
    # 오른쪽면
    elif p == 'R':
        # 시계 방향
        if d == '+':
            # 오른면 시계방향 회전
            right[0][0], right[0][1], right[0][2], right[1][0], right[1][1], right[1][2], \
            right[2][0], right[2][1], right[2][2] = right[2][0], right[1][0], right[0][0], \
            right[2][1], right[1][1], right[0][1], right[2][2], right[1][2], right[0][2]
            # 나머지면 처리
            up[2][2], up[1][2], up[0][2], front[2][2], front[1][2], front[0][2], \
            down[0][0], down[1][0], down[2][0], back[0][0], back[1][0], back[2][0] = \
            front[2][2], front[1][2], front[0][2], down[0][0], down[1][0], down[2][0], \
            back[0][0], back[1][0], back[2][0], up[2][2], up[1][2], up[0][2]
        else:
            # 오른면 반시계 방향 회전
            right[0][0], right[0][1], right[0][2], right[1][0], right[1][1], right[1][2], \
            right[2][0], right[2][1], right[2][2] = right[0][2], right[1][2], right[2][2], \
            right[0][1], right[1][1], right[2][1], right[0][0], right[1][0], right[2][0]
            # 나머지면 처리
            up[2][2], up[1][2], up[0][2], front[2][2], front[1][2], front[0][2], \
            down[0][0], down[1][0], down[2][0], back[0][0], back[1][0], back[2][0] = \
            back[0][0], back[1][0], back[2][0], up[2][2], up[1][2], up[0][2], \
            front[2][2], front[1][2], front[0][2], down[0][0], down[1][0], down[2][0]
    # 윗면
    elif p == 'U':
        # 시계 방향
        if d == '+':
            # 윗면 시계방향 회전
            up[0][0], up[0][1], up[0][2], up[1][0], up[1][1], up[1][2], \
            up[2][0], up[2][1], up[2][2] = up[2][0], up[1][0], up[0][0], \
            up[2][1], up[1][1], up[0][1], up[2][2], up[1][2], up[0][2]
            # 나머지면 처리
            front[0][0], front[0][1], front[0][2], left[0][0], left[0][1], left[0][2], \
            back[0][0], back[0][1], back[0][2], right[0][0], right[0][1], right[0][2] = \
            right[0][0], right[0][1], right[0][2], front[0][0], front[0][1], front[0][2], \
            left[0][0], left[0][1], left[0][2], back[0][0], back[0][1], back[0][2]
        else:
            # 윗면 반시계 방향 회전
            up[0][0], up[0][1], up[0][2], up[1][0], up[1][1], up[1][2], \
            up[2][0], up[2][1], up[2][2] = up[0][2], up[1][2], up[2][2], \
            up[0][1], up[1][1], up[2][1], up[0][0], up[1][0], up[2][0]
            # 나머지면 처리
            front[0][0], front[0][1], front[0][2], left[0][0], left[0][1], left[0][2], \
            back[0][0], back[0][1], back[0][2], right[0][0], right[0][1], right[0][2] = \
            left[0][0], left[0][1], left[0][2], back[0][0], back[0][1], back[0][2], \
            right[0][0], right[0][1], right[0][2], front[0][0], front[0][1], front[0][2]
    # 아랫면
    elif p == 'D':
        # 시계 방향
        if d == '+':
            # 아랫면 시계방향 회전
            down[0][0], down[0][1], down[0][2], down[1][0], down[1][1], down[1][2], \
            down[2][0], down[2][1], down[2][2] = down[2][0], down[1][0], down[0][0], \
            down[2][1], down[1][1], down[0][1], down[2][2], down[1][2], down[0][2]
            # 나머지면 처리
            front[2][0], front[2][1], front[2][2], left[2][0], left[2][1], left[2][2], \
            back[2][0], back[2][1], back[2][2], right[2][0], right[2][1], right[2][2] = \
            left[2][0], left[2][1], left[2][2], back[2][0], back[2][1], back[2][2], \
            right[2][0], right[2][1], right[2][2], front[2][0], front[2][1], front[2][2]
        else:
            # 아랫면 반시계 방향 회전
            down[0][0], down[0][1], down[0][2], down[1][0], down[1][1], down[1][2], \
            down[2][0], down[2][1], down[2][2] = down[0][2], down[1][2], down[2][2], \
            down[0][1], down[1][1], down[2][1], down[0][0], down[1][0], down[2][0]
            # 나머지면 처리
            front[2][0], front[2][1], front[2][2], left[2][0], left[2][1], left[2][2], \
            back[2][0], back[2][1], back[2][2], right[2][0], right[2][1], right[2][2] = \
            right[2][0], right[2][1], right[2][2], front[2][0], front[2][1], front[2][2], \
            left[2][0], left[2][1], left[2][2], back[2][0], back[2][1], back[2][2]

if __name__=='__main__':
    # 전체 테스트 케이스 갯수
    T = int(input())

    for i in range(T):
        # up, down, front, back, left, right, 각 테스트 케이스 마다 초기화 해줘야함
        up = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
        down = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
        front = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
        back = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
        left = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
        right = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]

        # 입력을 리스트 + 스트링으로 받고 스트링에 인덱스로 접근하여 면과 방향 추출
        n = int(input())
        orders = input().split()
        for order in orders:
            side, turn = order[0], order[1]
            rotate(side,turn)

        for j in up:
            print(''.join(j))

