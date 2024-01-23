def dfs(L,cnt):
    # 종료조건일때 최대와 최소를 갱신 후 종료
    if L == n-1:
        global max_val
        global min_val
        max_val = max(max_val,cnt)
        min_val = min(min_val,cnt)
        return
    else:
        # 연산자 리스트 길이만큼 반복문
        # 할당된 연산자 수가 0이 아닐때만 사용가능함
        # 1개 사용했으니 -1 해주고 연산자에 맞춰 연산실행
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
                    # 음수 나눗셈의 경우 문제의 조건에서 양수로 변환 후
                    # 나누고 다시 음수로 변환하라는 조건이 있어 조건 추가
                    if cnt<0:
                        res = - (abs(cnt)//arr[L+1])
                    else:
                        res = cnt // arr[L + 1]

                # 연산결과와 다음 수열을 위한 인덱스를 전달
                # 그리고 재귀가 종료될때는 꼭 사용한 연산자를 다시 추가시켜주는게 중요하다.
                dfs(L + 1, res)
                sign[i] += 1

if __name__ == '__main__':
    n = int(input())                        # 수열길이
    arr = list(map(int,input().split()))    # 수열 리스트
    sign = list(map(int,input().split()))   # 연산자 리스트
    max_val = -10000000000                  # 최대값
    min_val = 10000000000                   # 최소값

    dfs(0,arr[0])                        # 백트래킹

    print(max_val)
    print(min_val)
