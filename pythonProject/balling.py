import sys
N,K=(map(int,sys.stdin.readline().split()))
M=list(map(int,sys.stdin.readline().split()))
cnt=0
print(M)
for i in range(N):
    for j in range(i,N):
        if M[i]!=M[j]:
            print(M[i],M[j])
            cnt+=1
print(cnt)