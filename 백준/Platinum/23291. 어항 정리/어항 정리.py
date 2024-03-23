def adjust(arr):
    # 동시에 일어나니까 복사해서 쓰기
    narr = [x[:] for x in arr]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
                ni, nj = i + dy, j + dx
                # 범위내이고, 현재물고기가 더 많을때
                if 0<=ni<len(arr) and 0<=nj<len(arr[ni]) and arr[i][j]>arr[ni][nj]:
                    d = (arr[i][j] - arr[ni][nj])//5

                    # d가 0보다 클때 작은 곳에 추가, 많은 곳에 감소
                    if d > 0 :
                        narr[i][j] -= d
                        narr[ni][nj] += d

    return narr

def flatten(arr):
    narr = []

    # 거꾸로 세아르면서 범위 체크하면서 어펜드해주기
    for j in range(len(arr[-1])):
        for i in range(len(arr)-1,-1,-1):
            if j < len(arr[i]):
                narr.append(arr[i][j])

    return narr

if __name__=='__main__':
    n, k = map(int,input().split())         # n 어항 갯수(4의배수), k 최대값 최소값 차이
    arr = list(map(int,input().split()))    # 초기 어항 정보

    ans = 0                                 # 게임 진행 횟수

    # 최대-최소 가 k 보다 작거나 같으면 게임 종료
    while max(arr) - min(arr) > k :

        # [1] 물고기 갯수가 가장 적은 곳들에 물고기 한마리씩 추가하기
        min_v = min(arr)
        for i in range(len(arr)):
            if arr[i] == min_v:
                arr[i] += 1

        # [2] 첫번째 공중부양
        # [2] - 1 먼저 블록 하나 위로 쌓아줌
        arr = [[arr[0]]] + [arr[1:]]

        # [2] - 2 조건에 걸릴때까지 계쏙 공중부양시킴
        while True:
            w = len(arr[-2])                        # 1. 공중부양 시킬 블록의 폭 구하기

            # 만약 공중부양 시켜서 쌓을 길이가 가장 바닥에 있는 길이보다 크면 종료 => 못쌓는거임.
            if len(arr) > len(arr[-1]) - w:
                break

            arr1 = [lst[:w] for lst in arr]         # 2. 공중부양 시킬 블록 만들어줌
            arr2 = list(map(list,zip(*arr1[::-1]))) # 3. 공중부양 시킬 블록 회전시켜줌

            arr = arr2 + [arr[-1][w:]]              # 4. 만든 부분과 남은 부분 합쳐 쌓아줌.

        # [3] 물고기 수 조절 작업
        narr = adjust(arr)

        # [4] 평탄화 작업
        arr = flatten(narr)

        # [5] 두번째 공중부양
        M = len(arr)//2
        narr = [arr[:M][::-1]] + [arr[M:]]          # 1. 중간으로 나눈 뒤 거꾸로 읽으면서(180'회전) 쌓아줌
        M = M//2
        arr1 = [lst[:M] for lst in narr]            # 2. 왼쪽 절반 공중 부양
        arr2 = [lst[::-1] for lst in arr1[::-1]]  # 3. 왼쪽 절반 180'회전
        arr = arr2 + [lst[M:] for lst in narr]      # 4. 나머지 부분 합치기

        # [6] 물고기 수 조절 + 평탄화
        narr = adjust(arr)
        arr = flatten(narr)

        ans += 1

    print(ans)