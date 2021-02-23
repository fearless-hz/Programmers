n,m = map(int,input().split())
lis=[]
for i in range(n):
    lis.append(int(input()))
dp = [10001]*(m+1)
dp[0]=0
for i in range(n):
    for j in range(lis[i],m+1):
        print(j,dp[j],lis[i])
        if dp[j-lis[i]]!=10001:
            dp[j]=min(dp[j],dp[j-lis[i]]+1)
            print('dp[',j,']:',dp[j])

if dp[m]==10001 : print(-1)
else: print(dp[m])