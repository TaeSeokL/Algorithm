if __name__=='__main__':
    n, k = map(int,input().split())         # n 벨트수, k 조건
    belt = list(map(int,input().split()))   # 벨트정보
    robot = [0]*n                           # 로봇위치
    ans = 1                                 # 단계

    while True:
        # 1번 과정 : 벨트 회전, 로봇 위치 하나씩 증가
        belt.insert(0,belt.pop(-1))
        robot.pop(-1)
        robot.insert(0,0)

        # 2번과정
        # 로봇배열의 마지막부터 시작해서 끝에 로봇이 있으면 내리기
        # 나머지칸과 해당칸 +1 칸을 검사하며 해당칸에 로봇이 있고, 다음칸에 로봇이 없고
        # 내구도가 1이상일때 로봇 이동시켜주기
        for i in range(n-1,-1,-1):
            if i == n-1 and robot[i] == 1:
                robot[i] = 0
            elif robot[i] == 1 and robot[i+1] == 0 and belt[i+1]>=1:
                belt[i+1] -= 1
                robot[i] = 0
                robot[i+1] = 1

        # 3번과정
        # 올리는 위치에 로봇이 없다면 로봇 올려주고 내구도 감소
        if belt[0] != 0:
            robot[0] = 1
            belt[0] -= 1

        # 4번과정
        # 내구도 0인 칸 세어주고, k 이상이면 코드 종료
        # 아니면 계속 진행
        res = 0
        for x in belt:
            if x == 0:
                res += 1

        if res >= k:
            print(ans)
            break
        else:
            ans += 1

# 이건 리스트 대신 큐를 이용해본건데 오히려 시간이 더 오래 걸렸음.
# from collections import deque
# if __name__=='__main__':
#     n, k = map(int,input().split())         # n 벨트수, k 조건
#     belt = deque(map(int,input().split()))  # 벨트정보
#     robot = deque([0]*n)                    # 로봇위치
#     ans = 1                                 # 단계
# 
#     while True:
#         # 1번 과정 : 벨트 회전, 로봇 위치 하나씩 증가
#         belt.appendleft(belt.pop())
#         robot.pop()
#         robot.appendleft(0)
# 
#         # 2번과정
#         # 로봇배열의 마지막부터 시작해서 끝에 로봇이 있으면 내리기
#         # 나머지칸과 해당칸 +1 칸을 검사하며 해당칸에 로봇이 있고, 다음칸에 로봇이 없고
#         # 내구도가 1이상일때 로봇 이동시켜주기
#         for i in range(n-1,-1,-1):
#             if i == n-1 and robot[i] == 1:
#                 robot[i] = 0
#             elif robot[i] == 1 and robot[i+1] == 0 and belt[i+1]>=1:
#                 belt[i+1] -= 1
#                 robot[i] = 0
#                 robot[i+1] = 1
# 
#         # 3번과정
#         # 올리는 위치에 로봇이 없다면 로봇 올려주고 내구도 감소
#         if belt[0] != 0:
#             robot[0] = 1
#             belt[0] -= 1
# 
#         # 4번과정
#         # 내구도 0인 칸 세어주고, k 이상이면 코드 종료
#         # 아니면 계속 진행
#         res = 0
#         for x in belt:
#             if x == 0:
#                 res += 1
# 
#         if res >= k:
#             print(ans)
#             break
#         else:
#             ans += 1
