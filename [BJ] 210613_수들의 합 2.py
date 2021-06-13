N, M = map(int, input().split())
A = list(map(int, input().split()))
A.append(0)

answer = 0
start, end = 0, 0

while end < N:
    if sum(A[start:end+1]) < M:
        end += 1
    elif sum(A[start:end+1]) > M:
        if start < end:
            start += 1
        elif start == end:
            start += 1
            end += 1
    else:
        answer += 1
        end += 1

print(answer)
