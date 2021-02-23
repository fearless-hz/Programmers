import sys
cnt=0 #현재 그룹 내 인원수
a = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
b.sort() #오름차순으로 정렬
result=0 #최종 그룹 개수
for i in range(a): #인원 수 만큼 반복
    cnt+=1 #인원수 채워넣기
    if b[i]==cnt:
        result+=1 #인워수=공포도이면 여행 떠나는 그룹 1개 증가
        cnt=0 #인원수 초기화

print(result)