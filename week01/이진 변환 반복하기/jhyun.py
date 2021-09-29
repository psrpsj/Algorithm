def solution(s):
    answer = []
    zero_count = 0
    count = 0
    while s != "1":
        zero_count += s.count("0")
        s = int(len(s.replace("0", "")))
        s = format(s, 'b')
        count += 1
    
    return count, zero_count