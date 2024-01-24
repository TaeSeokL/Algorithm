# 갈 수 있는 길인지 판단하는 함수.
def judge(way):
    # 1부터 반복분 시작. 이때 i가 의미하는 바는 현재 위치이다.
    for i in range(1,N):
        if abs(way[i] - way[i-1]) > 1:          # 현재 위치와 이전 위치의 높이차가 1이상일때는 못가는 길임.
            return False

        # 현재 높이 - 이전 높이 = -1 => 현재가 더 낮다는 뜻
        # 현재 위치에서 오른쪽으로 경사로를 설치해야함.
        # 이때 경사로의 길이만큼 같은 높이가 와야 경사로를 설치할 수 있다.
        if way[i] - way[i-1] == -1:
            for j in range(L):
                # 경사로의 길이만큼 반복문 시작
                # 현재위치에서 경사로 길이 더한것이 범위 밖일때 or 이미 방문처리가 되어있을때 or 높이가 다를때
                if i+j >= N or used[i+j] or way[i] != way[i+j] :
                    return False
                # 현재위치와 현재위치에서 경사로길이만큼에 있는 블럭들의 높이가 전부 동일할때 = 방문체크
                if way[i] == way[i+j]:
                    used[i+j] = True

        # 현재 높이 - 이전 높이 = 1 => 현재가 더 높다는 뜻
        # 현재 위치 -1 부터 왼쪽으로 경사로를 설치해야함.
        elif way[i] - way[i-1] == 1 :
            for j in range(L):
                # 여기서는 위와 다르게 시작점이 i-1이다.
                # i-1부터 j를 빼가면서 경사로의 길이만큼 확인한다.
                # 범위를 벗어나거나, 이미 방문을 했거나, 높이가 다를때
                if i-j-1 < 0 or used[i-j-1] or way[i-1] != way[i-j-1]:
                    return False
                # 경사로를 설치할 곳들의 블럭의 높이가 동일할때 = 방문체크
                if way[i-1] == way[i-j-1] :
                    used[i-j-1] = True

    # for문이 정상적으로 종료되면 갈 수 있는 곳
    return True

if __name__=='__main__':
    N, L = map(int,input().split())                                 # N 맵 크기 L 경사로 길이
    board = [list(map(int,input().split())) for _ in range(N)]      # 맵 정보
    res = 0                                                         # 정답

    # 행 먼저 판단한다.
    # 갈 수 있는 길인지 판단하는 함수에 열을 전달한 후 가능하다면 정답 + 1
    for i in range(N):
        used = [False] * N
        if judge(board[i]):
            res += 1

    # 열 판단
    # 배열의 값들을 리스트로 만든 후에 입력으로 전달한다.
    for i in range(N):
        used = [False] * N
        if judge([board[j][i] for j in range(N)]):
            res += 1

    print(res)