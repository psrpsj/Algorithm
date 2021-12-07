def get_next(row, col, node_dir, grid):
    if node_dir == 0:
        if grid[row][col] == "S":
            n_row, n_col, n_dir = row - 1, col, node_dir
            if n_row < 0:
                n_row = len(grid) - 1
        elif grid[row][col] == "L":
            n_row, n_col, n_dir = row, col - 1, 2
            if n_col < 0:
                n_col = len(grid[0]) - 1
        elif grid[row][col] == "R":
            n_row, n_col, n_dir = row, col + 1, 3
            if n_col == len(grid[0]):
                n_col = 0
    elif node_dir == 1:
        if grid[row][col] == "S":
            n_row, n_col, n_dir = row + 1, col, node_dir
            if n_row == len(grid):
                n_row = 0
        elif grid[row][col] == "L":
            n_row, n_col, n_dir = row, col + 1, 3
            if n_col == len(grid[0]):
                n_col = 0
        elif grid[row][col] == "R":
            n_row, n_col, n_dir = row, col - 1, 2
            if n_col < 0:
                n_col = len(grid[0]) - 1
    elif node_dir == 2:
        if grid[row][col] == "S":
            n_row, n_col, n_dir = row, col - 1, node_dir
            if n_col < 0:
                n_col = len(grid[0]) - 1
        elif grid[row][col] == "L":
            n_row, n_col, n_dir = row + 1, col, 1
            if n_row == len(grid):
                n_row = 0
        elif grid[row][col] == "R":
            n_row, n_col, n_dir = row - 1, col, 0
            if n_row < 0:
                n_row = len(grid) - 1
    elif node_dir == 3:
        if grid[row][col] == "S":
            n_row, n_col, n_dir = row, col + 1, node_dir
            if n_col == len(grid[0]):
                n_col = 0
        elif grid[row][col] == "L":
            n_row, n_col, n_dir = row - 1, col, 0
            if n_row < 0:
                n_row = len(grid) - 1
        elif grid[row][col] == "R":
            n_row, n_col, n_dir = row + 1, col, 1
            if n_row == len(grid):
                n_row = 0
    return n_row, n_col, n_dir


def solution(grid):
    array = []
    answer = []
    for _ in range(len(grid)):
        array.append([[0, 0, 0, 0] for _ in range(len(grid[0]))])

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for node_dir in range(4):
                if array[row][col][node_dir] == 0:
                    length = 1
                    array[row][col][node_dir] = 1
                    n_row, n_col, n_dir = get_next(row, col, node_dir, grid)
                    while array[n_row][n_col][n_dir] != 1:
                        array[n_row][n_col][n_dir] = 1
                        length += 1
                        n_row, n_col, n_dir = get_next(n_row, n_col, n_dir, grid)
                    answer.append(length)
    return sorted(answer)


# 테스트 1 〉	통과 (0.37ms, 10.4MB)
# 테스트 2 〉	통과 (0.42ms, 10.4MB)
# 테스트 3 〉	통과 (0.45ms, 10.3MB)
# 테스트 4 〉	통과 (19.89ms, 10.7MB)
# 테스트 5 〉	통과 (38.22ms, 11.4MB)
# 테스트 6 〉	통과 (44.50ms, 11.8MB)
# 테스트 7 〉	통과 (622.17ms, 32.4MB)
# 테스트 8 〉	통과 (487.04ms, 29.8MB)
# 테스트 9 〉	통과 (509.75ms, 34.3MB)
# 테스트 10 〉	통과 (668.55ms, 40.2MB)
# 테스트 11 〉	통과 (622.65ms, 41.6MB)
