answer = []

def h(n, f, b, t):
    if n == 1:
        answer.append([f, t])
        return
    h(n - 1, f, t, b)
    answer.append([f, t])
    h(n - 1, b, f, t)

def solution(n):
    h(n, 1, 2, 3)
    return answer

print(solution(3))