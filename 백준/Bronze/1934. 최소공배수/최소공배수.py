def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)

if __name__=='__main__':
    n = int(input())
    for i in range(n):
        a, b = map(int,input().split())
        a, b = min(a,b), max(a,b) # a가 작은 수, b가 큰 수

        print(lcm(a,b))