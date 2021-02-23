import sys
N = int(sys.stdin.readline())
m=str(N)

a=list(map(int,m))
sum1,sum2=0,0
for i in range(len(m)//2):
    sum1+=a[i]
    sum2+=a[(len(m)//2)+i]
if sum1==sum2 :
    print("LUCKY")
else :
    print("READY")