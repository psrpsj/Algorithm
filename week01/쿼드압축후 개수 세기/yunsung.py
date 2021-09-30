def solution(arr):
    def check(row,col,size):
        # S 내부에 있는 모든 수가 같은 값인지 확인
        for i in range(row, row+size):
            for j in range(col, col+size):
                if arr[row][col] != arr[i][j]:
                    return False
        return True
    
    def dfs(row, col, size):
        if check(row, col, size):
            answer[arr[row][col]] += 1  # 모든 수가 같은 값이라면 해당 값 +1
        else:
            # 4분면 탐색
            size = size//2
            dfs(row, col, size)
            dfs(row, col+size, size)
            dfs(row+size, col, size)
            dfs(row+size, col+size, size)
            
    answer = [0,0]
    dfs(0,0,len(arr))
    
    return answer