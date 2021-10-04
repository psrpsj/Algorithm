def helper(s):
    if len(s) % 2 == 1:
        return False
    start = ["(", "{", "["]
    stack = []
    for letter in s:
        if letter in start:
            stack.append(letter)
        else:
            if not stack:
                return False
            compare = stack.pop()
            if letter == ")" and compare != "(":
                return False
            elif letter == "}" and compare != "{":
                return False
            if letter == "]" and compare != "[":
                return False
    return True


def solution(s):
    answer = 0
    sentence = s
    for i in range(len(s)):
        if helper(sentence):
            answer += 1
        sentence = sentence[1:] + sentence[0]        
    return answer