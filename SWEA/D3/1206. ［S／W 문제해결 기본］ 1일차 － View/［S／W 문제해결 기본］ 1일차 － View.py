
if __name__=='__main__':
    for case in range(1,11):
        n = int(input())
        arr = list(map(int,input().split()))

        cnt = 0
        for i in range(2,n-2):
            left_gap = 256
            right_gap = 256
            now_val = arr[i]        # 현재 건물 높이

            # 좌우로 비교
            for j in range(1,3):
                if arr[i]-arr[i-j] > 0 :        # 현재 건물이 더 높을때
                    if (arr[i] - arr[i-j]) < left_gap:
                        left_gap = arr[i]-arr[i-j]  # 갭기록
                else:
                    left_gap = 256
                    break
            for j in range(1,3):
                if arr[i] - arr[i+j] > 0 :
                    if (arr[i] - arr[i+j]) < right_gap:
                        right_gap = arr[i] - arr[i+j]
                else:
                    right_gap = 256
                    break

            if left_gap != 256 and right_gap != 256:
                if left_gap < right_gap:
                    cnt += left_gap
                else:
                    cnt += right_gap

        print('#%d %d'%(case,cnt))

