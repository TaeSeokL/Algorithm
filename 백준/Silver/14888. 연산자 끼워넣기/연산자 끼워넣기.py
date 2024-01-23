def dfs(L,cnt):
    if L == n-1:
        global max_val
        global min_val
        max_val = max(max_val,cnt)
        min_val = min(min_val,cnt)
        return
    else:
        for i in range(4):
            if sign[i] != 0:
                sign[i] -= 1
                if i == 0 : # 덧셈
                    res = cnt + arr[L+1]
                elif i == 1: # 뺄셈
                    res = cnt - arr[L+1]
                elif i == 2:    # 곱셈
                    res = cnt * arr[L + 1]
                else:           # 나눗셈
                    if cnt<0:
                        res = - (abs(cnt)//arr[L+1])
                    else:
                        res = cnt // arr[L + 1]

                dfs(L + 1, res)
                sign[i] += 1

if __name__ == '__main__':
    n = int(input())                        # 수열길이
    arr = list(map(int,input().split()))    # 수열 리스트
    sign = list(map(int,input().split()))   # 연산자 리스트
    max_val = -10000000000                  # 최대값
    min_val = 10000000000                   # 최소값

    dfs(0,arr[0])

    print(max_val)
    print(min_val)