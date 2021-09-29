def solution(n):
    answer = 0
    three = ''
    while n!=0:
        three = str(n%3) + three
        n = n//3
    
    for i in range(len(three)):
        answer += int(three[i]) * 3**i
        
    return answer