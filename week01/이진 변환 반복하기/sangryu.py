def solution(s):
    deleted_zeros = 0
    step = 0
    
    while s != "1":
        deleted_zeros += s.count('0')
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        step += 1
    
    answer = [step, deleted_zeros]
    return answer