
if __name__=='__main__':
    T = int(input())

    for case in range(1,T+1):
        n = int(input())
        arr = list(map(int,input().split()))        # 매매가 리스트
        cnt = 0

        max_val = n-1         # 최대값포인트
        p_val = max_val - 1   # 현재 값 포인터
        while True:

            if arr[max_val] > arr[p_val]:       # 매매해서 이득을 얻을 수 있는 경우
                cnt += arr[max_val] - arr[p_val]

            elif arr[max_val] < arr[p_val] :    # 현재 값이 최대 값보다 크다면
                max_val = p_val
                p_val = max_val - 1

                if p_val < 0:
                    print('#%d %d'%(case,cnt))
                    break
                continue

            p_val -= 1
            if p_val < 0:
                print('#%d %d' % (case, cnt))
                break

