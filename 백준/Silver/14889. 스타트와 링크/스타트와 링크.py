# 두팀 능력치 차이 계산하는 함수
def calculate(a_team,b_team):
    a_power = 0
    b_power = 0
    # 두팀은 정확히 반으로 나눠졌기 때문에
    # 범위를 이렇게 설정한다.
    for i in range(N//2):
        for j in range(i+1,N//2):
            # 선수들 사이의 관계에 기인한 능력치를 누적해야하기 때문에
            # board[a_team[i]][ateam[j]] 와 같은 형태로 더해준다.
            # 만약 aTeam의 첫번째(i==0)선수가 5번 선수이고 두번째(j==1) 선수가 7번 선수일때
            # 5-7 능력치 = board[5][7], 7-5 능력치 = board[7][5]를 더해주어야하는것이다.
            a_power = a_power + board[a_team[i]][a_team[j]] + board[a_team[j]][a_team[i]]
            b_power = b_power + board[b_team[i]][b_team[j]] + board[b_team[j]][b_team[i]]
            
    return abs(a_power-b_power)

# 팀을 나눠주는 백트래킹
# 두 팀의 리스트를 인자로 받아서 n번째 선수를 두팀 중 하나에 넣는다.
# 그리고 N번째 선수 == 끝선수까지 넣었을때 첫번째 팀에 있는 선수가 정확히 반으로 나눠졌는지 확인한다
# 안나눠졌으면 계산할 필요 없음.
# 그 다음 계산함수로 리스트 두개를 전달해서 최소값을 갱신한다.
def devide(n,alist,blist):
    global min_val
    if n == N :
        if len(alist) == N//2:
            cnt = calculate(alist,blist)
            min_val = min(cnt,min_val)
    else:
        # 이 코드의 하이라이트 부분
        # 첫번째 팀에 넣는 경우는 [n]을 더해서 첫번째 팀 리스트를 전달한다. 두번째 팀은 그대로 전달한다.
        # 이때 재귀함수가 종료되는 시점에는 첫번째팀에는 [n]이 빠져있는 상태이기 때문에
        # 그대로 두번째 팀에 넣어줌으로써 이렇게 간단하게 짤 수 있따.
        devide(n+1,alist + [n], blist)
        devide(n+1,alist, blist + [n])

if __name__=='__main__':
    N = int(input())                                                # 총 사람 수
    board = [list(map(int,input().split())) for _ in range(N)]      # 능력치정보
    min_val = 10000000000                                           # 최소값 변수
    devide(0,[],[])                                    # 함수호출

    print(min_val)
