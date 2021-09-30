def solution(n):
    answer = ''
    while n > 0: # 앞뒤 반전된 3진법 수 구하기
        answer += str(n%3)
        n = n//3
    answer = int(answer, 3) # 10진법으로 표현
    return answer