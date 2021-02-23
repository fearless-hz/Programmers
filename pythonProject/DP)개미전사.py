N=int(input())
lis=list(map(int,input().split()))
dp=[0]*100
dp[0]=lis[0]
dp[1]=max(lis[0],lis[1])
for i in range(2,N):
    dp[i]=max(dp[i-1], dp[i-2]+lis[i])
print(dp[N-1])