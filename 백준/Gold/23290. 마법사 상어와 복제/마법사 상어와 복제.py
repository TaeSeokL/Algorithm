def move_fish():
    # 물고기를 꺼낸다.
    for i in range(len(fish)):
        y,x,d,cnt = fish[i]

        for k in range(8):
            # 반시계방향으로 회전하며 이동 가능한 곳 찾기
            ny = y + fish_dir[(d-k)%8][0]
            nx = x + fish_dir[(d-k)%8][1]
            # 범위 내이고, 상어가 없고, 물고기 냄새가 없는 곳
            if (ny,nx) in boundary and (ny,nx) != (sy,sx) and fish_smell[ny][nx] == 0:
                # 물고기 이동 시켜주고 브레이크 (다른곳으로 이동할수도 있으니)
                fish[i] = [ny,nx,(d-k)%8,cnt]
                break

def move_shark():
    # 재귀함수 대신 4개의 이동방향중 3개를 선택하는 3중 포문을 사용해줌.
    # (상 좌 하 우) 우선 순위로 이동해야함. fish_dir에서 보면 (2, 0, 6, 4)임
    max_v = -1
    del_set = set()
    for d1 in (2,0,6,4):
        r1, c1 = sy + fish_dir[d1][0], sx + fish_dir[d1][1]
        if (r1,c1) not in boundary: continue  # 범위 벗어나면 다음 방향으로.
        for d2 in (2,0,6,4):
            r2, c2 = r1 + fish_dir[d2][0], c1 + fish_dir[d2][1]
            if (r2,c2) not in boundary: continue  # 범위 벗어나면 다음 방향으로
            for d3 in (2,0,6,4):
                r3, c3 = r2 + fish_dir[d3][0], c2 + fish_dir[d3][1]
                if (r3,c3) not in boundary: continue    # 범위 벗어나면 다음 방향으로

                # --여기까지가 4개중 3개를 뽑은 상황임--
                # 이제부터 이 3개를 뽑은 경우의 수 중 물고기를 가장 많이 먹은 경로로 상어를 이동시켜야함.
                # 물고기를 불러와서 경로안에 물고기가 있으면 먹은 물고기를 계산해줌.
                shk_v = set(((r1,c1),(r2,c2),(r3,c3)))
                f_cnt = 0

                for i in range(len(fish)):
                    # 만약 물고기가 상어 이동 경로에 있으면 잡아먹은 물고기로 더해줌.
                    if (fish[i][0],fish[i][1]) in shk_v:
                        f_cnt += fish[i][3]

                # 현재 뽑은 경로에서 잡아먹은 물고기 수가 최대 물고기수보다 클때
                # 최대물고기수 갱신해주고, 상어 위치 갱신해주고, 삭제해야할 위치를 전달해줌
                if max_v < f_cnt:
                    max_v = f_cnt
                    yy, xx = r3,c3
                    del_set = shk_v

    # --위에서 구한 경로에 있는 물고기를 모두 삭제해주고 냄새남겨줌.--
    # 삭제는 물고기 배열에 반대로 접근하며 pop 메서드를 사용해줌.
    for i in range(len(fish)-1,-1,-1):
        if (fish[i][0],fish[i][1]) in del_set:
            fish_smell[fish[i][0]][fish[i][1]] = 3
            fish.pop(i)

    return yy,xx

def merge(fish):
    # 같은 좌표, 같은 방향으로 우선 정렬
    fish.sort(key=lambda x:(x[0],x[1],x[2]))

    # 합치는 로직은 i 초기값을 1로 두고 i-1과 위치, 방향을 비교하며 같으면
    # i의 카운트를 i-1의 카운트에 합쳐주고 i를 pop 하는 로직임.
    # 만약 같지 않다면 i를 +1 하며 끝까지 비교해줌
    i = 1
    while i < len(fish):
        if fish[i][:3] == fish[i-1][:3]:        # 카운트전까지, 즉 위치 방향이 같을때
            fish[i-1][3] += fish[i][3]
            fish.pop(i)
        else:
            i += 1

if __name__=='__main__':
    m, s = map(int,input().split())     # m 물고기 수, s 연습횟수

    fish = []
    # 물고기들을 군집으로 관리 [1] 행 [2] 열 [3] 방향 [4] 갯수
    # 같은 위치에 같은 방향을 가진 물고기들을 갯수로 관리한다.
    for _ in range(m):
        r, c, d = map(int,input().split())      # (r,c) d 방향
        fish.append([r-1,c-1,d-1,1])

    # 상어 위치
    sy, sx = map(int,input().split())
    sy, sx = sy-1 , sx - 1

    fish_dir = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]  # 물고기 이동방향
    fish_smell = [[0]*4 for _ in range(4)]                              # 물고기 냄새 배열

    # 격자가 4x4로 작으니 바운더리를 정의해서 not in or in 으로 범위를 확인할 것임.
    boundary = set([(i,j) for j in range(4) for i in range(4)])

    # 연습횟수만큼 게임 진행
    for turn in range(s):
        # 복제마법 시전
        copy_fish = [x[:] for x in fish]

        # 물고기 이동
        move_fish()

        # 상어 이동, 물고기 잡아먹음, 물고기 냄새 남김.
        sy,sx = move_shark()

        # 물고기 냄새 사라짐
        for r in range(4):
            for c in range(4):
                if fish_smell[r][c] > 0:
                    fish_smell[r][c] -= 1

        # 복제마법 적용 후 같은 위치 같은 방향의 물고기들 갯수 합쳐주기
        fish += copy_fish
        merge(fish)

    ans = 0
    for i in range(len(fish)):
        ans += fish[i][3]
    print(ans)