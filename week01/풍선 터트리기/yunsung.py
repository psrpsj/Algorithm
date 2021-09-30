def solution(a):
    if len(a) <= 2:  # 길이가 2이하인 경우 모든 수를 남길 수 있으므로 길이 return
        return len(a)
    
    answer = 2  # 양 끝쪽의 값은 무조건 남길 수 있으므로 2개 저장
    left_min, right_min = a[0],a[-1]  # 왼쪽최솟값, 오른쪽최솟값
    
    for i in range(1, len(a)-1):
        # left_min 보다 더 작은 수의 경우 left_min 갱신, answer +1
        if left_min > a[i]:
            left_min = a[i]
            answer += 1
            
        # right_min보다 더 작은 수의 경우 right_min 갱신, answer +1
        if right_min > a[-1-i]:
            right_min = a[-1-i]
            answer += 1
            
    # 가장 작은 수가 같다면 중복된 수가 있으므로 answer-1
    return answer if left_min != right_min else answer-1