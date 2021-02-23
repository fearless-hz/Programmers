N=int(input())
a=list(map(int,input().split()))
a.sort()
cnt=0
result=0

for i in range(N):
    cnt+=1
    if a[i]==cnt :
        result+=1
        cnt=0

print(result)