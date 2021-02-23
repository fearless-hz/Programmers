N=input()
row=int(N[1])
cnt=0
column=int(ord(N[0]))-96
move=[(-2,-1),(-1,-2),(2,1),(1,2),(2,-1),(1,-2),(-2,1),(-1,2)] #움직일 수 있는 8가지 경우의 수
for i in move :
    n_row=row+i[0]
    n_c=column+i[1]
    if n_row>=1 and n_c>=1 and n_row<=8 and n_c<=8 :
        cnt+=1

print(cnt)
print(ord('A'),ord('a'))