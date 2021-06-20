def solution(n, money):
    dp = [([1] + [0] * n) for _ in range(len(money))]

    # dp[i][j] = dp[i-1][j] + dp[i][j-money[i]]
    for i in range(len(money)):
        for j in range(1, len(dp[0])):
            if i == 0:  # dp[i-1]이 없는 경우
                dp[i][j] = dp[i][j - money[i]]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - money[i]]

    return dp[-1][-1]


print(solution(5, [1,2,5]))