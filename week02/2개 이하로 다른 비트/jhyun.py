# 테스트 1 〉	통과 (0.77ms, 10.4MB)
# 테스트 2 〉	통과 (92.70ms, 26.1MB)
# 테스트 3 〉	통과 (0.08ms, 10.2MB)
# 테스트 4 〉	통과 (0.70ms, 10.4MB)
# 테스트 5 〉	통과 (0.80ms, 10.4MB)
# 테스트 6 〉	통과 (0.77ms, 10.3MB)
# 테스트 7 〉	통과 (140.00ms, 25.3MB)
# 테스트 8 〉	통과 (116.38ms, 24.8MB)
# 테스트 9 〉	통과 (117.24ms, 24.3MB)
# 테스트 10 〉	통과 (161.10ms, 26.9MB)
# 테스트 11 〉	통과 (144.80ms, 26.9MB)

def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            binary_num = list(bin(number)[2:])
            binary_num[-1] = "1"
        else:
            binary_num = bin(number)[2:]
            binary_num = "0" + binary_num
            one_idx = binary_num.rfind("0")
            binary_num = list(binary_num)
            binary_num[one_idx] = "1"
            binary_num[one_idx + 1] = "0"

        ans_num = int("".join(binary_num), 2)
        answer.append(ans_num)
    return answer
