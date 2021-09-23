def solution(a, b):
    ans = 0 # 0으로 초기값 설정
    length = len(a) # 순환 횟수
    
    for i in range(length):
        ans += a[i] * b[i] # 연산
        
    return ans
