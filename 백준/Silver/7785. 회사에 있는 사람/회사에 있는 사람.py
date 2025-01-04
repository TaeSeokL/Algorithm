if __name__ == '__main__':
    n = int(input())

    # 출입기록 저장할 해시테이블
    hash = {}

    for _ in range(n):
        name, status = input().split()

        # 만약 출입기록이 이미 있따면 +1 없다면 1로 설정
        if name in hash:
            if hash[name] >= 2:
                hash[name] = 1
            else:
                hash[name] += 1
        else:
            hash[name] = 1

    # 짝수면 퇴근한것, 홀수면 남아있는 것
    sol = []
    for key, value in hash.items():
        if value == 1:
            sol.append(key)

    sol.sort(reverse=True)

    for person in sol:
        print(person)
