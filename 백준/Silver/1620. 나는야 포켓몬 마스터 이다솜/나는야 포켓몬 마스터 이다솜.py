import sys
import time

if __name__ == '__main__':
    start_time = time.time()

    n, m = map(int,sys.stdin.readline().split())

    # 포켓몬 저장 해쉬
    name_hash = {}
    number_hash = {}

    for i in range(1,n+1):

        name = sys.stdin.readline().strip()

        # 이름 -> 숫자 / 숫자 -> 이름 으로 key-value 저장
        name_hash[name] = i
        number_hash[i] = name

    # 문제에 맞는 value 값 출력
    for _ in range(m):
        val = sys.stdin.readline().strip()

        if val.isdigit():
            print(number_hash[int(val)])
        else:
            print(name_hash[val])

    # print("프로그램 실행시간 : ",time.time() - start_time)
