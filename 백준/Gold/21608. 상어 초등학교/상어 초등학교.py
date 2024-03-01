if __name__=='__main__':
    n = int(input())
    board = [[0] * (n + 1) for _ in range(n + 1)]           # 맵, (1,1)부터 (n,n)까지
    dir = [(-1,0),(0,1),(1,0),(0,-1)]                       # 방향변수
    student_n = n**2                                        # 전체 학생수
    student_order = [0]*student_n                           # 처리해할 학생 순서
    student_like = [[0]*4 for _ in range(student_n+1)]      # 각 학생별 좋아하는 학생 : 인덱스 = 학생번호

    for i in range(student_n):
        sn, a,b,c,d = map(int,input().split())
        student_order[i] = sn
        student_like[sn] = [a,b,c,d]

    # 처리해야할 순서대로 학생 자리 배정하기
    for sn in student_order:
        # 각 학생별로 자리 후보를 저장하는 배열
        temp = []
        for y in range(1,n+1):
            for x in range(1,n+1):
                # 현재 탐색 위치가 빈자리일 경우에만 진입
                if board[y][x] == 0:
                    emtpy_space = 0         # 현재 탐색 위치 기준 주변에 빈칸이 몇개 있는지 파악
                    like_space = 0          # 현재 탐색 위치 기준 주변에 좋아하는 학생이 몇개 있는지 파악
                    for dy,dx in ((-1,0),(0,1),(1,0),(0,-1)):
                        ny, nx = y + dy, x + dx
                        # 범위내
                        if 1<=ny<=n and 1<=nx<=n:
                            # 빈칸일 경우 빈칸 변수 + 1
                            if board[ny][nx] == 0:
                                emtpy_space += 1
                            # 좋아하는 학생일 경우 좋아하는 변수 + 1
                            elif board[ny][nx] in student_like[sn]:
                                like_space += 1
                    # 자리가 될 수 있는 후보 배열에 추가해주기
                    temp.append([y,x,like_space,emtpy_space])

        # 모든 탐색이 종료되면 해당 학생이 앉을 수 있는 후보배열이 완성됨.
        # 이 배열을 처음엔 행, 열 기준으로 오름차순 정렬을 진행해줌.
        # 그러면 행이 작은순 -> 열이 작은순 으로 정렬이 됨.
        # 그 다음 좋아하는 학생이 많은 자리 -> 빈칸이 많은 자리 기준으로 내림차순 정렬을 진행해줌.
        # 그러면 좋아하는 학생이 많은 자리가 제일 앞에오고 그런 자리가 여러개있을시 빈칸이 많은 자리가
        # 젤 앞으로 오게됨. 정렬이 완료되면 배열의 첫번째 요소가 가장 적합한 자리가 되게 됨.
        temp.sort(key=lambda x:(x[0],x[1]))
        temp.sort(key=lambda x:(x[2],x[3]), reverse=True)

        # 가장 적합한 자리에 맵 갱신
        ny,nx,_,_ = temp[0]
        board[ny][nx] = sn

    # 정답 출력
    ans = 0
    for y in range(1,n+1):
        for x in range(1,n+1):
            # 맵을 탐색하며 해당 자리의 학생 번호르 받아옴. 주변에 좋아하는 학생이
            # 있을 경우 cnt + 1 해줌.
            sn = board[y][x]
            cnt = 0
            for dy,dx in ((-1,0),(0,1),(1,0),(0,-1)):
                ny, nx = y + dy, x + dx

                if 1<=ny<=n and 1 <= nx <= n and board[ny][nx] in student_like[sn]:
                    cnt += 1

            # 문제의 조건에 맞게 정답을 갱신해줌.
            if cnt != 0:
                ans += 10**(cnt-1)

    print(ans)
