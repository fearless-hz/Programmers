import sys
a = sys.stdin.readline().strip()
cnt0=0
cnt1=0
if a[0]=='1':
    cnt0+=1
else :
    cnt1+=1
print(len(a))
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        if a[i+1]=='1':
            cnt0+=1
            print(i)
            print('cnt0:',cnt0)
        else :
            cnt1+=1
            print(i)
            print('cnt1:',cnt1)

print(min(cnt0,cnt1))