if __name__=='__main__':
    R, C, m = map(int,input().split())      # (r,c) 격자 크기, m 상어수

    # 상어 군집 정보 저장
    shark = []
    for _ in range(m):
        a,b,s,d,z = map(int,input().split())
        shark.append([a-1,b-1,s,d-1,z])

    dir = [(-1,0),(1,0),(0,1),(0,-1)]   # 상어 이동 방향 상 하 우 좌
    ans = 0                             # 낚시왕이 잡은 상어 크기 합

    left_right_idx = [i for i in range(C)] + [i for i in range(C-2,0,-1)]   # 좌우방향상어 위치업데이트 배열
    up_down_idx = [i for i in range(R)] + [i for i in range(R-2,0,-1)]      # 위아래방향상어 위치업데이트 배열

    # 낚시왕 시작
    for j in range(C):
        # [1] 가장 가까운 상어 찾기 -> 행기준으로 정렬
        shark.sort(key=lambda x:x[0])
        # 정렬 후 상어왕과 열이 같은 상어를 찾으면 그 상어가 가장 가까이 있는 상어이다. 바로 제거 후 ans 갱신
        for sh in range(len(shark)):
            r,c,s,d,z = shark[sh]
            if c == j:
                shark.pop(sh)
                ans += z
                break

        # [2] 상어 이동
        # 여기서 말하는 인덱스 처리란 어차피 상어는 배열을 왔다갔다 하기 때문에 굿노트에 분석한 것처럼
        # 계산 후에 원래 격자 크기를 넘어가는 인덱스는 우리가 만든 확장배열에 그 값을 넣어서
        # 실제 상어의 인덱스(위치)를 찾아오는 과정을 의미함. 그리고 이때 방향도 함께 반전됨. 궁금하면 개념노트 57p보기
        for sh in range(len(shark)):
            y,x,s,d,z = shark[sh]

            if d == 2 or d == 3:     # 좌우 방향 상어 이동
                x = (x+dir[d][1]*s)%(2*C-2)

                if x >= C:           # C보다 크면 방향 반대 처리, 인덱스 처리
                    x = left_right_idx[x]
                    if d == 2 :
                        d = 3
                    else:
                        d = 2

            elif d == 0 or d == 1:  # 상하 방향 상어 이동
                y = (y+dir[d][0]*s)%(2*R-2)

                if y >= R:          # R보다 크면 방향 반대 처리, 인덱스 처리
                    y = up_down_idx[y]

                    if d == 0:
                        d = 1
                    else:
                        d = 0

            # 위치 및 방향 업데이트
            shark[sh] = [y,x,s,d,z]

        # [3] 위치가 겹치는 상어 잡아먹기 -> 행과 열 기준으로 오름차순 정렬, 크기 기준으로 내림차순 정렬
        shark.sort(key=lambda x:(x[0],x[1],-x[4]))

        # 상어 배열을 거꾸로 돌아주면서 그 전꺼랑 위치가 겹치면 현재꺼를 pop 해주기
        for i in range(len(shark)-1,0,-1):
            if (shark[i][0],shark[i][1]) == (shark[i-1][0],shark[i-1][1]) :
                shark.pop(i)

    print(ans)
