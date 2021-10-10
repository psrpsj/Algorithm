def solution(absolutes, signs):
    answer = 0
    for x, y in zip(absolutes, signs):
        if y == False:
            x *= -1
        answer += x

    return answer