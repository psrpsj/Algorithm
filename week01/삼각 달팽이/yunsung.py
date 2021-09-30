def solution(n):
    graph = [[0]*i for i in range(1,n+1)]
    
    # (위->아래, 왼쪽-> 오른쪽, 아래->위) 순서로 dx,dy 설정
    dx = [1,0,-1]
    dy = [0,1,-1]

    size, direction = n,0   # 변의 길이, 이동방향
    start,row,col = 1,-1,0  # 시작숫자, 시작행, 시작열

    while size > 0:  # 변의 길이가 0보다 작아지면 중단

        for i in range(start, start+size):  # 방향에 맞춰 숫자 채우기
            row += dx[direction%3]
            col += dy[direction%3]
            graph[row][col] = i

        start = graph[row][col] + 1  # 다음 시작 숫자 설정
        size -= 1                    # 다음 변의 길이는 (현재 변의 길이 - 1)
        direction += 1               # 방향 변경
    
    answer = []
    for row in graph:
        answer += row
    
    return answer