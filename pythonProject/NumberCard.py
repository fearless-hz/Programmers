N, M = map(int,input().split()) #N,M 입력받기
result=0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)