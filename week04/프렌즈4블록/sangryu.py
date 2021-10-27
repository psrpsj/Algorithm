def solution(n, arr1, arr2):
    answer = []
    for idx in range(len(arr1)):
        binary = str(bin(arr1[idx] | arr2[idx])[2:])
        binary = binary.rjust(n, "0")
        binary = binary.replace("1", "#")
        binary = binary.replace("0", " ")
        answer.append(binary)
    return answer
