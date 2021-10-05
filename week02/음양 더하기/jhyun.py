# 테스트 1 〉	통과 (0.12ms, 10.2MB)
# 테스트 2 〉	통과 (0.14ms, 10.2MB)
# 테스트 3 〉	통과 (0.08ms, 10.3MB)
# 테스트 4 〉	통과 (0.08ms, 10.3MB)
# 테스트 5 〉	통과 (0.08ms, 10.2MB)
# 테스트 6 〉	통과 (0.14ms, 10.3MB)
# 테스트 7 〉	통과 (0.08ms, 10.2MB)
# 테스트 8 〉	통과 (0.14ms, 10.3MB)
# 테스트 9 〉	통과 (0.08ms, 10.3MB)
import time

def solution(absolutes, signs):
    answer = 0
    length = len(absolutes)
    for i in range(length):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer