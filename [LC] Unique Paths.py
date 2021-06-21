import math
def uniquePaths(m, n):
    return int(math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1)))

print(uniquePaths(7,3))
print(uniquePaths(3,3))