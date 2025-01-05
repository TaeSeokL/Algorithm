import sys

if __name__ == '__main__':

    n, m = map(int,sys.stdin.readline().split())        # n 걸그룹수 , m 문제수

    team_hash = {}              # 팀 : 멤버
    member_hash = {}            # 멤버 : 팀

    for _ in range(n):
        team_name = sys.stdin.readline().strip()
        member = int(sys.stdin.readline().strip())

        for i in range(member):
            name = sys.stdin.readline().strip()

            if i == 0 :                                 # 처음 멤버를 넣을때 리스트 형으로 넣기 위함.
                team_hash[team_name] = [name]
            else:
                team_hash[team_name].append(name)       # 그 후로 계속 append

            member_hash[name] = team_name               # 멤버 해쉬 팀 이름 저장

    for _ in range(m):
        tar = sys.stdin.readline().strip()
        quiz = int(sys.stdin.readline().strip())

        if quiz == 0:                       # 팀에 속한 멤버 사전순 출력
            team_hash[tar].sort()

            for val in team_hash[tar]:
                print(val)

        else:                               # 멤버가 속한 팀 출력
            print(member_hash[tar])