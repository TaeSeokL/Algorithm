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

                if nx < 0:                              # 좌표가 (0,-1) 가면 종료
                    break

                if board[ny][nx] != 0:                  # 0이 아닐때만 = 공 있을때만 추가
                    flatten.append(board[ny][nx])

                if step == length or step == length*2:  # 방향전환
                    sd += 1

                sy, sx = ny, nx                         # 위치 갱신

        # [3] 구슬 폭파시키기(폭파하는 구슬 없을때까지 반복) (1차원처리)
        # 마지막에 0을 추가하는 이유는 np는 기본적으로 pp 보다 1 앞서있기때문에
        # 마지막 원소를 처리하려면 배열 끝에 허수가 하나 있어야 한다. 그래서 추가해줌.
        flatten.append(0)
        while True:
            pp = 0                              # 현재위치
            np = pp + 1                         # 탐색위치
            temp = [pp]                         # 동일한 공 발견시 저장 배열
            final_delete = []                   # 최종 삭제해야하는 공 인덱스 배열
            while np < len(flatten):
                # 현재 위치와 탐색 위치의 값이 같을때
                if flatten[pp] == flatten[np]:
                    temp.append(np)             # 탐색 위치 추가
                    np += 1                     # 계속 탐색
                # 현재 위치와 탐색 위치의 값이 다를때
                else:
                    if len(temp) >= 4:              # 그 전에 4개의 연속하는 공이 있을때
                        temp.sort(reverse=True)     # 나중에 pop하기 위해 거꾸로 정렬해서 저장
                        final_delete.append(temp)
                        pp = np                     # 현재위치 갱신
                        np = pp + 1                 # 탐색위치 갱신
                        temp = [pp]
                    else:                           # 아무것도 없을때 : 위치 갱신 후 계속 탐색
                        pp = np
                        np = pp + 1
                        temp = [pp]

            if final_delete:                    # 연속하는 공이 있을때
                final_delete.sort(reverse=True)     # pop하기 위해 거꾸로 정렬
                for li in final_delete:             # 연속하는 공집합을 하나씩 꺼내옴
                    num = flatten[li[0]]            # 폭파하는 공 번호 받기
                    explode_ball[num] += len(li)    # 점수 집계
                    for x in li:                    # 인덱스로 팝해주기
                        flatten.pop(x)
            else:                               # 연속하는 공이 없을 때
                break

        # [4] 구슬 변화하기 (1차원처리) -> (2차원 옮기기)
        # 여기도 동일하게 마지막 원소를 처리해주기 위해 끝에 허수를 하나 추가해준다.
        flatten.append(0)
        new_flatten = []            # 새로운 플랫 배열
        pp = 0                      # 현재위치
        np = pp + 1                 # 탐색 위치
        temp = [pp]                 # 동일한 공 발견시 저장배열

        while np < len(flatten):
            if flatten[pp] == flatten[np]:  # 현재위치와 탐색위치 공 같을때
                temp.append(np)             # 탐색위치 추가
                np += 1                     # 계속 탐색
            else:                           # 현재위치와 탐색위치 공 다를때
                num = flatten[temp[0]]      # 공 번호 정보 받아오기
                quan = len(temp)            # 저장된 공 갯수 받아오기

                new_flatten += [quan]       # 새배열 제작 (공갯수,공번호) -> 문제조건
                new_flatten += [num]

                pp = np                     # 위치 갱신 후 계속 탐색
                np = pp + 1
                temp = [pp]

        # [4] - 1 :  2차원 옮기기 작업
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
