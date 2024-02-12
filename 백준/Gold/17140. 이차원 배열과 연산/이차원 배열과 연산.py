from copy import deepcopy

if __name__=='__main__':
    r, c, k = map(int,input().split())                          # board[r][c] = k 가 될때까지 시간 출력
    board = [list(map(int,input().split())) for _ in range(3)]  # 맵정보

    nmax_row = 3
    nmax_col = 3

    # print('-----------원본 배열---------------')
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         print('%3d'%board[i][j], end = '')
    #     print()

    for t in range(101):
        # 정답 조건일때 종료
        # 초반 테케에서 r이랑 c가 3보다 큰 숫자가 들어오는 경우가 있어서 이렇게 해야함
        # 최대 행 갯수와 최대 열 갯수가 r이랑 c보다 큰 경우만 r,c자리에 뭐가 있는지 파악 가능
        if nmax_row > r-1 and nmax_col > c-1 and board[r-1][c-1] == k:
            print(t)
            exit(0)

        # 현 보드의 행 갯수와 열갯수
        n_row = len(board)
        n_col = len(board[0])

        li = []     # 새로 만들어질 행 또는 열
        temp = []   # 새로 만들어질 배열
        # R 연산
        if n_row >= n_col:
            # print('-------------%d턴 R연산------------'%t)
            # 보드를 돌면서 무슨 숫자가 있는지 파악 후에 숫자 갯수를 세준다.
            # 이때 number 배열의 인덱스를 숫자로 생각하고 배열값을 숫자가 몇회 나왔는지로 생각하면서 추가해준다.
            # 또한 li 배열에 어떤 숫자가 나왔는지 저장해둔다.
            for i in range(n_row):
                number = [0] * 101
                for j in range(n_col):
                    if board[i][j] != 0:
                        number[board[i][j]] += 1
                        li.append(board[i][j])

                # 숫자 갯수 만큼 반복문 돌아준다.
                # 숫자 하나씩 빼서 나온 횟수와 함께 다시 어펜드 해준다.
                ln = len(li)
                for j in range(ln):
                    n = li.pop(0)
                    if (n,number[n]) not in li:
                        li.append((n,number[n]))

                # 숫자와 등장횟수가 저장된 리스트를 횟수, 숫자크기 순으로 정렬해준다.
                li.sort(key=lambda x:(x[1],x[0]))

                # li 리스트의 원소를 하나씩 빼서 tmp 리스트를 만들어준다.
                # 다 정렬된 상태이기 때문에 tmp는 문제의 조건에 부합하는 새로운 행이다.
                tmp = []
                while li:
                    number, cnt = li.pop(0)
                    tmp += [number,cnt]

                # 만약 새로 만든 행의 길이가 100보다 크다면 최대 열갯수를 100개로 지정해준다.
                # 그게 아니라면 보드 최대 열 갯수를 갱신해준다.
                if len(tmp) > 100:
                    nmax_col = 100
                elif len(tmp) > nmax_col:
                    nmax_col = len(tmp)

                # 새로운 배열에 새로만든 행을 추가해준다.
                temp.append(tmp)

            # R연산을 마친 배열의 행들을 탐색하며
            # 최대 열갯수보다 길이가 작으면 0을 채워준다.
            for x in temp:
                if len(x) < nmax_col :
                    n = nmax_col - len(x)
                    for _ in range(n):
                        x.append(0)
            # 보드 갱신
            board = deepcopy(temp)

        # C연산
        else:
            # print('-------------%d턴 C연산------------'%t)
            # R 연산과 마찬가지로 숫자와 등장 횟수 파악
            for i in range(n_col):
                number = [0] * 101
                for j in range(n_row):
                    if board[j][i] != 0:
                        number[board[j][i]] += 1
                        li.append(board[j][i])

                # (숫자,등장횟수) 형태로 li에 추가
                ln = len(li)
                for j in range(ln):
                    n = li.pop(0)
                    if (n, number[n]) not in li:
                        li.append((n, number[n]))

                # 정렬 후 리스트 만들기
                li.sort(key=lambda x: (x[1], x[0]))
                tmp = []
                while li:
                    number, cnt = li.pop(0)
                    tmp += [number, cnt]

                # 100보다 클때 제한두기
                # 아니면 현재 최대 행 갯수 갱신
                if len(tmp) > 100:
                    nmax_row = 100
                elif len(tmp) > nmax_row:
                    nmax_row = len(tmp)
                temp.append(tmp)

            # C 연산에서는 열갯수는 안바뀌므로 현재 열 갯수 사용
            # 그리고 여기서는 하나하나 그냥 보드에 옮겨줌.
            board = [[0]*n_col for _ in range(nmax_row)]
            for i in range(nmax_col):
                l = len(temp[i])
                for j in range(l):
                    board[j][i] = temp[i][j]

        # print('------------ 연산 후 ---------------')
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         print('%3d'%board[i][j], end='')
        #     print()

    print(-1)