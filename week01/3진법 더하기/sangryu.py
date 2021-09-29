def solution(n):
    three_bit = ""
    while n > 0:
        three_bit += str(n % 3)
        n //= 3
    
    answer = 0
    for i in range(1, len(three_bit) + 1):
        answer += int(three_bit[-i]) * pow(3, i-1)
    return answer