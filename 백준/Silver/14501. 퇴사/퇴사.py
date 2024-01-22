def dfs(n,cnt):     # n 현재날짜, cnt 현재수익
    global max_val

    # 현재날짜가 퇴사일보다 같거나 클때 == 더이상 일못함.
    if n >= N:
        max_val = max(max_val,cnt)
        return

    # 현재날짜 + 소요기간이 퇴사일보다 작거나 같을때 == 상담가능
    if n+T[n] <= N:
        dfs(n+T[n], cnt+P[n])

    # 현재날짜에 잡혀있는 상담 안할 때
    dfs(n+1,cnt)

if __name__=='__main__':
    N = int(input())
    T = [0]*N
    P = [0]*N
    for i in range(N):
        T[i], P[i] = map(int,input().split())
    max_val = 0

    dfs(0,0)

    print(max_val)