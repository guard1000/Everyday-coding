def climbStairs(n):
    if n == 1 or n == 2:
        return n

    answer = [1, 2]
    for _ in range(n - 2):
        answer.append(answer[-1] + answer[-2])
    return answer[-1]

print(climbStairs(2))
print(climbStairs(3))