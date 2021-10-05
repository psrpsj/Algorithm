# 테스트 1 〉	통과 (98.82ms, 10.7MB)
# 테스트 2 〉	통과 (98.96ms, 10.6MB)
# 테스트 3 〉	통과 (111.82ms, 10.9MB)
# 테스트 4 〉	통과 (105.19ms, 10.7MB)
# 테스트 5 〉	통과 (103.61ms, 10.6MB)
# 테스트 6 〉	통과 (98.60ms, 10.6MB)
# 테스트 7 〉	통과 (106.28ms, 10.6MB)

def solution(left, right):
    answer = 0
    
    count = [0] * 100001
    for i in range(1,100001):
        for j in range(1, 100001//i):
            count[i*j] += 1
    
    for i in range(left, right+1):
        if count[i]%2 == 0:
            answer += i
        else:
            answer -= i
    return answer