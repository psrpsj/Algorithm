def solution(s):
    count = 0
    remove_zero = 0
    while s!="1":
        word = ""
        for x in s:
            if x == "1":
                word += x
            elif x == "0":
                remove_zero += 1
        count += 1
        s = bin(len(word))[2:]
    return [count, remove_zero]