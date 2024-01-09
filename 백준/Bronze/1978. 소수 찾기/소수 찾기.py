def sosu():
    cnt = 0
    for x in arr:
        # 1을 제외하고 자기자신으로만 나눠지는 수 = 소수
        if x == 1:
            continue
        v = 2
        while True:
            # 소수일 경우
            if x == v:
                cnt += 1
                break
            # 소수가 아닐경우
            if x % v == 0:
                break
            v += 1
            
    return cnt
if __name__=='__main__':
    n = int(input()) # 주어진 숫자 갯수
    arr= list(map(int,input().split())) # 주어진 숫자
    print(sosu())