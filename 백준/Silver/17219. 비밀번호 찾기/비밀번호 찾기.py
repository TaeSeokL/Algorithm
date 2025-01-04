import sys

if __name__ == '__main__':
    n,m = map(int,sys.stdin.readline().split())     # n 주소, m 찾으려는 갯수

    pwd_hash = {}            # 비밀번호 해시 테이블

    for _ in range(n):
        add, pwd = sys.stdin.readline().split()

        pwd_hash[add] = pwd

    for _ in range(m):
        tar = sys.stdin.readline().strip()

        print(pwd_hash[tar])