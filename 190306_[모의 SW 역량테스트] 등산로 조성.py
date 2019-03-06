def bfs(d, candi, N):
    nxt = []
    for c in candi:
        if c[0] < N - 1 and board[c[0]][c[1]] > board[c[0] + 1][c[1]] and [c[0] + 1, c[1]] not in nxt:    nxt.append(
            [c[0] + 1, c[1]])
        if c[0] > 0 and board[c[0]][c[1]] > board[c[0] - 1][c[1]] and [c[0] - 1, c[1]] not in nxt:    nxt.append(
            [c[0] - 1, c[1]])
        if c[1] < N - 1 and board[c[0]][c[1]] > board[c[0]][c[1] + 1] and [c[0], c[1] + 1] not in nxt:    nxt.append(
            [c[0], c[1] + 1])
        if c[1] > 0 and board[c[0]][c[1]] > board[c[0]][c[1] - 1] and [c[0], c[1] - 1] not in nxt:    nxt.append(
            [c[0], c[1] - 1])
    if len(nxt) == 0:
        return d
    return bfs(d + 1, nxt, N)


T = int(input())
for t in range(T):
    N, K = map(int, input().split())  # N, K
    # print(N,K)
    board = []
    for n in range(N):  # board 입력
        board.append(list(map(int, input().split())))
    # print(board)
    M = 0
    start = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > M:    M = board[i][j]
    for i in range(N):
        for j in range(N):
            if board[i][j] == M:    start.append([i, j])
    # print(start)
    answer = 0
    for i in range(N):
        for j in range(N):
            for k in range(1, K + 1):
                board[i][j] -= 1
                if bfs(1, start, N) > answer:    answer = bfs(1, start, N)
            board[i][j] += K

    print('#', end='')
    print(t + 1, end=' ')
    print(answer)


