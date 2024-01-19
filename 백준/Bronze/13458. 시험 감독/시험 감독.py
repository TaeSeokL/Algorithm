
# 내 코드
# if __name__=='__main__':
#     n = int(input())        # 수험장 수
#     arr = list(map(int,input().split()))    # 수험장마다 있는 응시자 수
#     b, c = map(int,input().split())     # b= 총감독의 능력, c=부감독의 능력
#
#     arr.insert(0,0)     # 필요감독수 배열과 맞추기 위해 삽입
#     res = [0]*1000001       # 필요감독 수 배열, 응시자수 최대만큼 생성, 메모이제이션 위함
#     res_val = 0 # 필요한 최소감독 수
#
#     for i in range(1,n+1):   # arr[i] = 수험장 안의 응시자 수
#         # 이미 앞전에 응시자수에 대한 최소감독을 구해놓았을 경우
#         if res[arr[i]] != 0 :
#             res_val += res[arr[i]]
#         else:
#             tmp = arr[i]
#             arr[i] = arr[i] - b      # 총감독 능력으로 나눈 뒤의 남은 응시자 수
#             cnt = arr[i] / c         # 남은 응시자 수를 부감독 능력으로 나눈 몫 //이거 쓰면 안됨. 소수점을 파악하는게 중요.
#
#             # cnt가 0이하란 소리는 총감독 한번 뺀게 0이하란 소리
#             # 즉 총감독 한명만 있어도 응시자 수 처리 가능하단 소리
#             if cnt <= 0:
#                 res[tmp] = 1
#             elif cnt <= 1:    # 몫이 1보다 작을 경우 부감독 1명만 써도 되니 총감독 1명 + 부감독 1명 해서 res[tmp]에 저장
#                 res[tmp] = 2
#             else:
#                 if arr[i] % c == 0 : # 나머지가 0일때, 남은 응시자가 부감독으로 딱 맞아 떨어질때. 필요한 감독수는 = 몫 + 총감독
#                     res[tmp] = arr[i] // c + 1
#                 else:                # 안나눠떨어질때. 필요한 감독수는 = 몫 + 총감독 + 부감독 1
#                     res[tmp] = arr[i]//c + 2    # 몫이 1보다 클 경우, 나눈 몫 + 총감독 1명 + 부감독 1명 해서 res[tmp]에 저장
#                 # 응시자수가 43명이고 부감독 능력이 20일때
#                 # 나눈 몫은 2명, 나머지를 처리해야하므로 1명 더 필요함 즉, cnt + 1 + 1(총감독)
#
#             res_val += res[tmp]
#
#     print(res_val)
#
#

# 더 간결한 코드
if __name__=='__main__':
    n = int(input())        # 수험장 수
    arr = list(map(int,input().split()))    # 수험장마다 있는 응시자 수
    b, c = map(int,input().split())
    res = 0

    for i in range(n):
        # 총감독 빼고 하나 카운트
        arr[i] = arr[i] - b
        res += 1

        # 남은 응시자 수가 0보다 크다면 부감독이 들어가야함.
        if arr[i] > 0:
            # 남은 응시자 수가 부감독 능력의 배수라면 몫만 더해주면 됨.
            if arr[i] % c == 0:
                res += arr[i] // c
            # 배수가 아니라면 몫 + 1 을 더해줘야함. 한명이 더 필요하기 때문
            else:
                res += arr[i] // c + 1

    print(res)
