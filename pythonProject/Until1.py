N,K = map(int,input().split())
cnt=0

def until(N,K) :
    global cnt
    while (True):
        if N == 1:
            break
        elif (N % K == 0):
            N /= K
            cnt += 1
        else:
            N -= 1
            cnt += 1
    print(cnt)

until(N,K)
