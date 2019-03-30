def lcs(X, Y):
    n = len(X)
    L = [[None] * (n + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L[n][n]

T = int(input())
for t in range(T):
    x = list(map(int, input().split()))
    y = sorted(x)
    n = len(x)
    print('#', end='')
    print(t + 1, end=' ')
    print(lcs(x, y))