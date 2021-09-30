def solution(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i]*b[i]
    print(result)
    return result
