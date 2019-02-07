def solution(s):    #Dp연습
    n = len(s)
    memo =[[0 for cols in range(n)] for rows in range(n)]
    for i in range(n):
        memo[i][i] = 1
    maxLength=1
    i = 0
    while i < n - 1:
        if (s[i] == s[i + 1]):
            memo[i][i + 1] = True
            maxLength = 2
        i = i + 1
    k = 3
    while k <= n:
        i = 0
        while i < (n - k + 1):
            j = i + k - 1
            if (memo[i + 1][j - 1] and s[i] == s[j]):
                memo[i][j] = True
                if (k > maxLength):
                    maxLength = k
            i = i + 1
        k = k + 1
    return maxLength

'''
def lps(seq, i, j):
    if (i == j):
        return 1

    if (seq[i] == seq[j] and i + 1 == j):
        return 2

    if (seq[i] == seq[j]):
        return lps(seq, i + 1, j - 1) + 2

    return max(lps(seq, i, j - 1),lps(seq, i + 1, j))

def solution(s):    #recusive method
    n = len(s)
    return lps(s, 0, n - 1)
'''


'''
def solution(s):    #Dp연습
    n = len(s)
    memo =[[0 for cols in range(n)] for rows in range(n)]
    for i in range(n):
        memo[i][i] = 1
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            if s[i] == s[j] and l == 2:
                memo[i][j] = 2
            elif s[i] == s[j]:
                memo[i][j] = memo[i+1][j-1] +2
            else:
                memo[i][j] = max(memo[i][j-1], memo[i+1][j])

    return memo[0][n-1]

print(solution('abcdcba'))
'''
print(solution('abcdcba'))