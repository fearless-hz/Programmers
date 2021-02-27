import sys

n,m,k = sys.stdin.readline()
lis = []
for i in range(n):
    lis.append(int(input))
lis.sort(reverse=True)
cnt=0
sum=0

for i in range(m):
    if(cnt<k) :
        sum+=lis[0]
        cnt+=1
    elif(cnt==k):
        sum+=lis[1]
        cnt=0
    elif(m==0):
        sum=0
print(sum)
