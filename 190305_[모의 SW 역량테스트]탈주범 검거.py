def left(r, c, board, nxt):
    if board[r][c - 1] in [1, 3, 4, 5] and ([r, c - 1] not in nxt):
        nxt.append([r, c - 1])
    return nxt


def right(r, c, board, nxt):
    if board[r][c + 1] in [1, 3, 6, 7] and ([r, c + 1] not in nxt):
        nxt.append([r, c + 1])
    return nxt


def up(r, c, board, nxt):
    if board[r - 1][c] in [1, 2, 5, 6] and ([r - 1, c] not in nxt):
        nxt.append([r - 1, c])
    return nxt


def down(r, c, board, nxt):
    if board[r + 1][c] in [1, 2, 4, 7] and ([r + 1, c] not in nxt):
        nxt.append([r + 1, c])
    return nxt


def bfs(now, answer, board, l):
    nxt = []
    for n in now:
        if board[n[0]][n[1]] == 1:
            nxt = left(n[0], n[1], board, nxt)
            nxt = right(n[0], n[1], board, nxt)
            nxt = up(n[0], n[1], board, nxt)
            nxt = down(n[0], n[1], board, nxt)
        elif board[n[0]][n[1]] == 2:
            nxt = up(n[0], n[1], board, nxt)
            nxt = down(n[0], n[1], board, nxt)
        elif board[n[0]][n[1]] == 3:
            nxt = left(n[0], n[1], board, nxt)
            nxt = right(n[0], n[1], board, nxt)
        elif board[n[0]][n[1]] == 4:
            nxt = up(n[0], n[1], board, nxt)
            nxt = right(n[0], n[1], board, nxt)
        elif board[n[0]][n[1]] == 5:
            nxt = right(n[0], n[1], board, nxt)
            nxt = down(n[0], n[1], board, nxt)
        elif board[n[0]][n[1]] == 6:
            nxt = left(n[0], n[1], board, nxt)
            nxt = down(n[0], n[1], board, nxt)
        elif board[n[0]][n[1]] == 7:
            nxt = up(n[0], n[1], board, nxt)
            nxt = left(n[0], n[1], board, nxt)
        board[n[0]][n[1]] = -1
    if len(nxt) == 0 or l == 0:  # 끝
        return answer
    return bfs(nxt, answer + len(nxt), board, l - 1)


answer = 1  # 처음 한지점은 있으니까 1부터
T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    board = [[-1 for b in range(M + 2)]]
    for n in range(N):  # 입력 -> 범위 일일히 if문 넣기 귀찮으니까 둘레를 -1로 패딩하자.
        board.append(list(map(int, input().split())))
        board[-1].insert(0, -1)
        board[-1].append(-1)
    board.append([-1 for b in range(M + 2)])
    print('#', end='')
    print(t + 1, end=' ')
    print(bfs([[R + 1, C + 1]], answer, board, L - 1))

