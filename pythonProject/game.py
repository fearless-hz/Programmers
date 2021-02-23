def recursive(i):
    if i<=1 : #i 값이 1 혹은 0이면 그대로 1 출력
        return 1
    return i*recursive(i-1) #i 값이 1보다 클 경우 재귀함수 호출


print(recursive(5))