def find_even(num):
    divisor = []
    for i in range(1, num+1):
        if num % i == 0:
            divisor.append(i)
    if len(divisor) % 2 == 0:
        return True
    else:
        return False

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if find_even(i):
            answer += i
        else:
            answer -= i
    return answer