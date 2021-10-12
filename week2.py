# 음양 더하기
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]:
            answer += abs(absolutes[i])
        else:
            answer -= abs(absolutes[i])
            
    return answer

# 약수의 갯수와 덧셈

def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    
    return answer

# Matching {x} Repetitions

Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'

# Matching {x, y} Repetitions

Regex_Pattern = r'^\d{1,2}[a-zA-z]{3,}[.]{0,3}$'

# Matching Zero Or More Repetitions

Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'

# Matching One Or More Repetitions

Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'