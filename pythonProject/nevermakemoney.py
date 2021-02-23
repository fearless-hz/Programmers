import sys
a=int(sys.stdin.readline()) #동전의 개수
b = list(map(int, sys.stdin.readline().split())) #동전의 단위
b.sort() #오름차순으로 정렬
target=1 #초기 target=1
for i in b :
    if target<i : #target값이 화폐단위보다 작으면 break
        break
    target+=i
    print(target)
print(target)
