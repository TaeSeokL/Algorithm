## 풀이법 ##
# 도시의 치킨집 중 폐업 시키지 않을 치킨집을 m개 dfs로 고른다. 이때 조합구하는 법으로 고른다. 중복 허용 x, 순서 상관 x
# m개 골랐다면, 모든 집의 인덱스와 고른 치킨집의 인덱스를 비교하며 각 집의 최소 치킨 거리를 구하고, 최소 도시 치킨 거리를 구한다.

def dfs(L,S):
    # m개의 치킨집을 골랐을때
    if L == m :
        global min_val
        # 고른 res에 대한 도시 치킨 거리 변수 cnt
        cnt = 0
        # 모든 집에 대하여 최소 치킨 거리를 구한다.
        for i in range(len(house)):
            # 한집에 대한 치킨거리, 모든 치킨집과의 거리를 구해서 최소값을 구해야한다.
            min_distance = 1000000
            hy, hx = house[i]
            for j in res:
                cy, cx = j
                dis = abs(cy-hy) + abs(cx-hx)
                # 만약 m개의 치킨집 중에 현재 치킨집과의 치킨 거리가 작다면 최소 치킨 거리 갱신
                if dis<min_distance:
                    min_distance = dis
            # 위의 반복문에서 각 집에 대한 최소 치킨 거리를 구했기 때문에 그냥 더해줘도 최소 도시 치킨 거리 이다.
            cnt += min_distance
        # m개 고른 res가 더 작다면 정답 갱신
        if cnt < min_val:
            min_val = cnt
        return
    else:
        # 치킨집 배열을 접근하여 골라준다.
        # i에 있는 치킨집을 골랐다면 다음 재귀에서는 i+1부터 반복문을 시작해주면서 골랐던 치킨집을 제외시켜준다.
        for i in range(S,len(chiken_house)):
            res.append(chiken_house[i])
            dfs(L+1,i+1)
            res.pop()

if __name__=='__main__':
    n,m = map(int,input().split())                              # n 맵크기 m 골라야할 치킨 집 갯수
    board = [list(map(int,input().split())) for _ in range(n)]  # 맵 정보
    house = []                                                  # 집 인덱스 배열
    chiken_house = []                                           # 치킨집 인덱스 배열
    res = []                                                    # m개의 치킨집 배열
    min_val = 100000000                                         # 최소 도시 치킨 거리

    # 치킨집과 집의 인덱스 정보를 구해준다.
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                house.append((i,j))
            elif board[i][j] == 2:
                chiken_house.append((i,j))

    # L은 고른 치킨집 갯수, S는 현재 고른 치킨집 보다 +1 값을 전달해줌으로써 다음 치킨집부터 고를 수 있게 해준다.
    dfs(0,0)
    print(min_val)

