if __name__ == '__main__':
    n, m = map(int,input().split())                             # n 격자크기 / m 마법 수행 횟수

    board = [list(map(int,input().split())) for _ in range(n)]  # 초기 맵정보

    magic_dir = [0,(-1,0),(1,0),(0,-1),(0,1)]           # 마법 사용 시 방향
    tornado_dir = [(0,-1),(1,0),(0,1),(-1,0)]           # 토네이도 탐색 방향
    explode_ball = [0,0,0,0]                            # 폭파한 공 갯수 저장

    magic = []
    for _ in range(m):
        d, s = map(int,input().split())         # d, s 마법 시전한 방향과 거리
        magic.append((d,s))

    # 마법 수행
    for d,s in magic:
        # [1] 상어가 마법 수행해서 공 파괴하기
        sy, sx = n//2, n//2
        for _ in range(s):
            ny = sy + magic_dir[d][0]
            nx = sx + magic_dir[d][1]

            if 0<=ny<n and 0<=nx<n :
                board[ny][nx] = 0
                sy, sx = ny, nx

        # [2] 토네이도 배열 1차원으로 펴면서 구슬 빈자리 이동 처리
        flatten = []
        sy,sx,sd = n//2,n//2,0
        for length in range(1,n+1):
            for step in range(1,2*length+1):
                ny = sy + tornado_dir[sd%4][0]
                nx = sx + tornado_dir[sd%4][1]

                if nx < 0:
                    break

                if board[ny][nx] != 0:
                    flatten.append(board[ny][nx])

                if step == length or step == length*2:
                    sd += 1

                sy, sx = ny, nx

        # [3] 구슬 폭파시키기(폭파하는 구슬 없을때까지 반복) (1차원처리)
        flatten.append(0)
        while True:
            pp = 0
            np = pp + 1
            temp = [pp]
            final_delete = []
            while np < len(flatten):

                # 현재 위치와 탐색 위치의 값이 같을때
                if flatten[pp] == flatten[np]:
                    temp.append(np)
                    np += 1
                # 현재 위치와 탐색 위치의 값이 다를때
                else:
                    if len(temp) >= 4:          # 그 전에 4개의 연속하는 공이 있을때
                        temp.sort(reverse=True)
                        final_delete.append(temp)
                        pp = np
                        np = pp + 1
                        temp = [pp]
                    else:                       # 아무것도 없을때
                        pp = np
                        np = pp + 1
                        temp = [pp]

            if final_delete:
                final_delete.sort(reverse=True)
                for li in final_delete:
                    num = flatten[li[0]]
                    explode_ball[num] += len(li)
                    for x in li:
                        flatten.pop(x)
            else:
                break

        # [4] 구슬 변화하기 (1차원처리) -> (2차원 옮기기)
        new_flatten = []
        flatten.append(0)
        pp = 0
        np = pp + 1
        temp = [pp]

        while np < len(flatten):

            if flatten[pp] == flatten[np]:
                temp.append(np)
                np += 1
            else:
                num = flatten[temp[0]]
                quan = len(temp)

                new_flatten += [quan]
                new_flatten += [num]

                pp = np
                np = pp + 1
                temp = [pp]

        sy, sx, sd = n // 2, n // 2, 0
        for length in range(1, n + 1):
            for step in range(1, 2 * length + 1):
                ny = sy + tornado_dir[sd % 4][0]
                nx = sx + tornado_dir[sd % 4][1]

                if nx < 0:
                    break

                if new_flatten:
                    board[ny][nx] = new_flatten.pop(0)
                else:
                    board[ny][nx] = 0

                if step == length or step == length * 2:
                    sd += 1

                sy, sx = ny, nx

    print(explode_ball[1]+explode_ball[2]*2+explode_ball[3]*3)















