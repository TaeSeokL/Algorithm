def isPrime(num):
    for j in range(2,int(num**0.5)+ 1):
        # 2부터 루트 num까지의 범위안에 숫자들로
        # num을 나눴을때 나머지가 0이면 소수가 아님.
        if num%j == 0 :
            return False
    # for문이 break 안됐을때 else 실행 -> 소수란 뜻
    else:
        return True

if __name__=='__main__':
    # n~m까지의 범위에서 소수를 출력
    n,m = map(int,input().split())

    for i in range(n,m+1):
        if i == 1:
            continue

        if isPrime(i):
            print(i)
