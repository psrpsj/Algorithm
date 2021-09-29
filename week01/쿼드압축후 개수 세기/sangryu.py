def dfs (x, y, next, arr, ans):
    start = arr[x][y]
    for i in range(x, x+next):
        for j in range(y, y+next):
            if arr[i][j] != start:
                next = next // 2
                dfs(x, y, next, arr, ans)
                dfs(x+next, y, next, arr, ans)
                dfs(x, y+next, next, arr, ans)
                dfs(x+next, y+next, next, arr, ans)
                return
    ans[start] += 1

def solution(arr):
    answer = [0,0]
    dfs(0, 0, len(arr), arr, answer)
    return answer
