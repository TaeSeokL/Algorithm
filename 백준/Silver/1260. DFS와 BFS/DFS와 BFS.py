from collections import deque

## DFS는 방문 가능한곳 나오면 바로 거기로 점프해서 깊게 들어감.
def DFS(V):
    # 현재 노드 출력
    print(V, end =' ')

    # 노드만큼 for문
    # 노드 순서대로 반복하기 때문에, 방문할 수 있는 정점이 여러개인 경우
    # 제일 번호가 작은 정점부터 방문하게 된다.
    for i in range(1,N+1):
        # i 노드에 방문을 안했고, 간선이 연결되어 있을때
        if visit1[i] == 0 and graph[V][i] == 1:
            # i 노드 방문처리해준 뒤 V로 넘겨준다.
            visit1[i] = 1
            DFS(i)

## BFS는 방문 가능한곳 나와도 append 시키면서 노드의 갯수만큼 반복문을 돌면서
## 방문 가능한 곳이 더 있나 찾아봄. 즉 레벨 탐색을 함.
def BFS(V):
    # 현재 노드 dq에 추가해주기
    dq = deque([V])

    # dq가 빌때까지 반복 == 모두 방문
    while dq:
        # 젤 앞에 있는거 꺼내기
        n = dq.popleft()
        print(n, end = ' ')
        # 노드 갯수만큼 for문
        for i in range(1,N+1):
            # 만약 i 노드에 방문을 안했고, 간선이 연결되어 있을때
            # 큐에 어펜드하고 방문처리
            if visit2[i] == 0 and graph[n][i] == 1:
                dq.append(i)
                visit2[i] = 1

if __name__=="__main__":
    N, M, V = map(int,input().split())
    # 노드 사이 간선의 정보를 저장하기 위해 그래프를 만든다.
    # 이때 0번 인덱스는 사용하지 않기때문에 노드의 갯수보다 +1 해서 생성해준다.
    graph = [[0]*(N+1) for _ in range(N+1)]

    # 간선의 수만큼 입력을 받은 뒤
    # 양방향으로 정보를 저장해준다.
    for _ in range(M):
        a, b = map(int,input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    # 방문 표시를 할 배열을 선언해준다.
    # 이때도 0번 인덱스는 사용하지 않기 때문에 노드 갯수보다 1개 더 많게 정의
    # 1 = DFS, 2 = BFS
    visit1 = [0] * (N + 1)
    visit2 = [0] * (N + 1)
    visit1[V] = 1
    visit2[V] = 1

    # 함수실행
    DFS(V)
    print()
    BFS(V)