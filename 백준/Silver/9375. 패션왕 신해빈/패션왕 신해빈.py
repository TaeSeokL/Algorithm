import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())       # TC 갯수

    for _ in range(T):
        n = int(sys.stdin.readline().strip())   # 의상갯수

        hash = {}

        for _ in range(n):
            name, kind = sys.stdin.readline().split()   # 옷 이름, 종류

            # 종류별로 옷 갯수를 저장
            if kind in hash:
                hash[kind] += 1
            else:
                hash[kind] = 1

        cnt = 1                                         # 알몸이 아닌 경우의 수 구하기
        for _, value in hash.items():
            cnt *= (value+1)                            # 안입은 경우를 세기 위해 종류수 + 1 해서 구하기

        print(cnt-1)                                    # 아무것도 안입은 경우의 수 -1