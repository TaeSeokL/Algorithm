def dfs(n,S):
    global ans
    # 뽑아야할 만큼 다 뽑았다면 뽑힌 조합으로 사다리 조건 만족하는지 check() 함수 호출
    # 만족하면 ans 갱신 후 종료
    if n == cnt:
        if check():
            ans = 1
        return

    # 조합 구현, 전체 갯수 중 cnt 개 뽑는 조합
    # 조건문으로 사다리를 놓을 수 있는 곳만 뽑아준다.
    for i in range(S,length):
        ti, tj = pos[i]
        # 왼쪽, 오른쪽 모두 사다리가 없을때만 가능
        if arr[ti][tj-1] == 0 and arr[ti][tj+1] == 0 :
            arr[ti][tj] = 1
            dfs(n+1,i+1)
            arr[ti][tj] = 0

# 사다리 조건 만족하는지 사다리 타는 함수
def check():
    # j = 세로선(열번호)
    for j in range(1,n+1):
        sj = j
        # i = 가로선(행번호)
        for i in range(1,h+1):
            # 왼쪽으로 한칸
            if arr[i][sj-1] == 1:
                sj -= 1
            # 오른쪽으로 한칸
            elif arr[i][sj] == 1:
                sj += 1

        # 다른 곳으로 나온다면 False
        if sj != j:
            return False
    # 전부 알맞으 곳으로 나왔다 = return False가 실행이 안됐다 = 성공
    return True

if __name__=='__main__':
    n,m,h = map(int,input().split())        # n 세로선갯수 m 연결돼있는 사다리 갯수 h 세로선마다 놓을 수 있는 가로선 갯수

    # [1] 사다리 제작해줌. 양옆에 패딩해주고, 좌표는 (1,1)부터 시작함.
    arr = [[0]*(n+2) for _ in range(h+1)]

    # [2] 이미 놓여진 사다리 표시해줌
    for _ in range(m):
        a,b = map(int,input().split())
        arr[a][b] = 1

    # [3] 사다리 놓을 수 있는 후보지 위치 저장해두기
    pos = []
    for i in range(1,h+1):
        for j in range(1,n+1):
            if arr[i][j] == 0 and arr[i][j-1] == 0 and arr[i][j+1] == 0:
                pos.append((i,j))

    length = len(pos)   # 후보지 위치 수

    # 사다리는 최대 3개 까지 놓을 수 있음. cnt = 놓을 사다리 갯수, 반복문 돌아줌. 3개 초과면 -1 출력
    # 만약 재귀 이후 정답변수가 1이됐따면 그 갯수가 정답이므로 브레이크
    for cnt in range(4):

        ans = 0  # 정답변수(놓은사다리 갯수)

        # [4] 재귀 돌아줌. dfs(n,S) n은 갯수 S는 출발점
        dfs(0,0)

        if ans == 1:
            ans = cnt
            break
    else:
        ans = -1

    print(ans)