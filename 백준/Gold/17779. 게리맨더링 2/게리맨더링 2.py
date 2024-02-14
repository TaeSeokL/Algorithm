# 이런문제는 처음이라 생소했는데 조건을 잘 분석하고
# 인덱스와 범위를 헷갈리지 않고 조건문을 잘 작성하면 쉽게 풀 수 있는거 같다.
def calculate(x,y,d1,d2):
    # 선거구 인구를 누적할 배열과
    # 선거구를 나누어줄 이차원 배열을 선언해준다.
    elec = [0] * 5
    arr = [[0]*(n+1) for _ in range(n+1)]

    # 경계선의 조건을 참고해서 경계선을 5구역으로 먼저 표시해준다.
    for i in range(d1+1):
        arr[x+i][y-i] = 5
        arr[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):
        arr[x+i][y+i] = 5
        arr[x+d1+i][y-d1+i] = 5

    # 경계선 내부를 5구역으로 표시해준다.
    # flag를 사용해서 경계선을 만나면 거기서부터 5구역 표시를 계속해준다.
    # 그러면 반대쪽 경계선에서 flag가 또 바뀌게 되므로 내부가 자연스럽게 표시된다.
    for i in range(x+1,x+d1+d2):
        flag = False
        for j in range(1,n+1):
            if arr[i][j] == 5 :
                flag = not flag
            if flag:
                arr[i][j] = 5

    # 문제에 있는 각 선거구의 조건문을 작성하여 elec배열에 누적해준다.
    # 마지막으로 최댓값과 최소값의 차이를 리턴시켜준다.
    for r in range(1,n+1):
        for c in range(1,n+1):
            if r < x + d1 and c <= y and arr[r][c] == 0:
                elec[0] += board[r][c]
            elif r<=x+d2 and y <= c <= n and arr[r][c] == 0:
                elec[1] += board[r][c]
            elif x+d1 <= r <= n and c < y-d1+d2 and arr[r][c] == 0:
                elec[2] += board[r][c]
            elif x+d2 < r <= n and y-d1+d2 <=c <=n and arr[r][c] == 0:
                elec[3] += board[r][c]
            elif arr[r][c] == 5:
                elec[4] += board[r][c]
    return max(elec) - min(elec)

if __name__=='__main__':
    n = int(input())
    # 인덱스를 (1,1) 부터 시작하기 위해 보드의 바깥면을 만들어준다.
    board = [[]]
    for i in range(n):
        board.append([0]+list(map(int,input().split())))

    # 정답변수
    result = 1000000000

    # x,y,d1,d2는 1<=변수<=n의 범위를 갖기 때문에
    # 4중 반복문과 문제에서 나온 조건문을 이용해서 만족하는 숫자들을 찾아준다.
    # 주의할점이 이문제 자체에서 x가 행, y가 열으로 사용했기 때문에 유의하자.
    for x in range(1,n+1):
        for y in range(1,n+1):
            for d1 in range(1,n+1):
                for d2 in range(1,n+1):
                    if 1<=x<x+d1+d2<=n and 1<=y-d1<y<y+d2<=n:
                        result = min(result,calculate(x,y,d1,d2))

    print(result)