def solution(numbers):
    from itertools import combinations
    answer = set()
    for c in combinations(numbers,2):  # 두 가지 수로 만들 수 있는 조합 모두 탐색
        answer.add(sum(c))
    answer = sorted(list(answer))
    return answer