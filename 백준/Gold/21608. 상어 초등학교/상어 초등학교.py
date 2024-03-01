

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
        max_emtpy_space = 0         # 주변 빈칸 갯수
        max_like_space = 0          # 주변 좋아하는 학생 갯수
        py, px = 50,50              # 적합한 위치 저장
        ey, ex = 50,50
        temp = []
        for y in range(1,n+1):
            for x in range(1,n+1):
                if board[y][x] == 0:
                    emtpy_space = 0
                    like_space = 0
                    for dy,dx in ((-1,0),(0,1),(1,0),(0,-1)):
                        ny, nx = y + dy, x + dx

                        # 범위내
                        if 1<=ny<=n and 1<=nx<=n:
                            if board[ny][nx] == 0:
                                emtpy_space += 1

                            elif board[ny][nx] in student_like[sn]:
                                like_space += 1

                    temp.append([y,x,like_space,emtpy_space])
                    
        temp.sort(key=lambda x:(x[0],x[1]))
        temp.sort(key=lambda x:(x[2],x[3]), reverse=True)

        ny,nx,_,_ = temp[0]
        board[ny][nx] = sn


    ans = 0
    for y in range(1,n+1):
        for x in range(1,n+1):
            sn = board[y][x]
            cnt = 0
            for dy,dx in ((-1,0),(0,1),(1,0),(0,-1)):
                ny, nx = y + dy, x + dx

                if 1<=ny<=n and 1 <= nx <= n and board[ny][nx] in student_like[sn]:
                    cnt += 1

            if cnt != 0:
                ans += 10**(cnt-1)

    print(ans)