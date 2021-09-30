def solution(n):
    row, col, ans = -1, 0, 1
    tri_list = [[0] * i for i in range(1, n + 1)]

    for i in range(n):
        for _ in range(n-i):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            tri_list[row][col] = ans
            ans += 1
            
    answer = []
    for lst in tri_list:
        answer += lst
        
    return answer