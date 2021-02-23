s=input()
result=1

for i in range(len(s)):
    if int(s[i])!=0:
        result*=int(s[i])
    else :
        result+=int(s[i])
print(result)