import sys

if __name__ == '__main__':

    n,m = map(int,sys.stdin.readline().split())
    hash = {}

    for _ in range(m):
        id = sys.stdin.readline().strip()        # 학번

        if id in hash:      # 이미 대기열에 있을 경우
            del hash[id]    # 앞 순서 제거 후 다시 추가
            hash[id] = 1
        else:
            hash[id] = 1    # 없으면 순서대로 추가

    i = 0                   # 수강신청 가능 인원까지 학번 출력
    for key, _ in hash.items():
        print(key)
        i += 1

        if i == n:
            break