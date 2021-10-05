import numpy as np

def solution(a, b):
    x = np.array(a)
    y = np.array(b)
    answer = int(x.dot(y))
    return answer