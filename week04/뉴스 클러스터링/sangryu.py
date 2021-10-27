from collections import Counter


def create_sub(str):
    answer = []
    str = str.lower()
    for idx in range(len(str) - 1):
        if str[idx].isalpha() and str[idx + 1].isalpha():
            answer.append(str[idx] + str[idx + 1])
    return answer


def solution(str1, str2):
    sub_str1 = create_sub(str1)
    sub_str2 = create_sub(str2)

    counter_str1 = Counter(sub_str1)
    counter_str2 = Counter(sub_str2)

    inter = list((counter_str1 & counter_str2).elements())
    union = list((counter_str1 | counter_str2).elements())

    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        return int((len(inter) / len(union)) * 65536)
