def solution(numbers):
    answer = set()
    for i in range(len(numbers) -1):
        for j in range(i + 1, len(numbers)):
            sum = numbers[i] + numbers[j]
            answer.add(sum)
    answer = sorted(list(answer))
    return answer