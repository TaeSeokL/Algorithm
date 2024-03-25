# n = 10개의 눈금 중 현재 진행 중인 눈금
# sum_score = 말이 얻은 점수 누적
def dfs(n,sum_score):
    global ans
    # 눈금을 전부 적용했을때 최대값 갱신
    if n == 10:
        ans = max(ans,sum_score)
        return

    # line19 - line23 예시
    # 현재 위치가 5일 경우 갈 수 있는 위치는 [6, 21]이다.(인접리스트)
    # 이때 출발지가 5일 경우 교차로(21)로 진입해야하기 때문에 한칸을 움직여서 현재 위치를 21로 설정해준다. c = adj[s][-1]
    # 그 다음 for문으로 진입해서 계속 c를 업데이트 하며 위치를 갱신해준다.
    # -- 눈금이 3이 나왔을때 시뮬레이션 --
    # s = 5 (초기 위치) -> c = adj[s][-1] = 21 (한칸이동) -> c = adj[c][0] = 22 (한칸이동) -> c = adj[c][0] = 23 (한칸이동)
    # 5에서 23까지 총 3칸을 이동했다.(굿노트 그림참조) 교차로가 아닐 경우에도 같은 로직으로 계속 위치를 업데이트 시켜줌.

    # 4개의 말 중 하나씩 선택해서 눈금 적용
    for j in range(4):
        s = v[j]                    # 1. 선택한 말의 현재 위치 받아오기
        c = adj[s][-1]              # 2. 선택한 말을 한칸 옮겨주기 -> 이유는 교차로에 있을 경우 교차로로 진입하도록 만들기 위해. 교차로 아닐 경우는 어차피 인접리스트 원소가 하나니까 그냥 한칸 움직이는거로 구현이됨.
        for _ in range(1,lst[n]):   # 3. 위에서 한칸 움직였으니까 여기서는 눈금 -1 만큼 움직여줌.
            c = adj[c][0]           # 4. c를 계속 인접리스트에 대입 -> 갱신하며 한칸씩 움직여줌.

        # 눈금만큼 다 움직이고 난 뒤 거기로 갈 수 있는지 판단 -> 목적지이거나 도착지점에 말이 없을때
        # 말을 그 위치로 움직여주고, 도착지점의 점수를 더해서 넘겨줌. 다시 돌아 왔을때는 꼭 위치를 원상 복구 해줘야함.
        if c == 32 or c not in v:
            v[j] = c
            dfs(n+1,sum_score+score[c])
            v[j] = s

if __name__=='__main__':
    lst = list(map(int,input().split()))    # 나올 눈금 갯수들

    # 인접리스트 : index(현재위치) value(갈수있는곳) -> 윷놀이판에 위치를 부여해서 다음에 갈 수 있는 곳들을 리스트로 만들었음.
    # 도착지(32) 이후로 36까지 있는것은, 20위치에서 눈금이 5가 나왔을때를 대비해서 20 -> 32 -> 33 -> 34 -> 35 -> 36 전부 32로 돌아가게끔 구현한것임.
    #     [0] [1] [2] [3] [4] [5]    [6] [7] [8] [9] [10]     [11] [12] [13] [14] [15]    [16] [17] [18] [19] [20] [21] [22] [23] [24] [25] [26] [27] [28] [29] [30] [31] [32] [33] [34] [35] [36]
    adj =[[1],[2],[3],[4],[5],[6,21],[7],[8],[9],[10],[11,27],[12],[13],[14],[15],[16,29],[17],[18],[19],[20],[32],[22],[23],[24],[25],[26],[20],[28],[24],[30],[31],[24],[32],[32],[32],[32],[32]]

    # 점수리스트 : 현재위치에서 얻을 수 있는 점수
    #       [0] [1] [2] [3] [4] [5]    [6] [7] [8] [9] [10]     [11] [12] [13] [14] [15]    [16] [17] [18] [19] [20] [21] [22] [23] [24] [25] [26] [27] [28] [29] [30] [31] [32]
    score = [0,  2,  4,  6,  8,  10,    12, 14, 16, 18, 20,      22,  24,  26,  28,  30,     32,  34,  36,  38,  40,  13,  16,  19,  25,  30,  35,  22,  24,  28,  27,  26,  0]

    v = [0,0,0,0]                    # 네 개의 말의 현재 위치
    ans = 0                          # 정답변수
    dfs(0,0)            # 재귀 출발
    print(ans)