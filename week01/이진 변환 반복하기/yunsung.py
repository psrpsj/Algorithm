def solution(s):
    answer = [0,0]  # [이진 변환 횟수, 제거된 0의 개수]
    while s != '1':
        ones = 0  # 0 제거후 남은 1의 개수
        for i in s:
            if i == '1':
                ones += 1
            else:
                answer[1] += 1
        s = bin(ones)[2:]  # 이진법으로 표현
        answer[0] += 1
    
    return answer