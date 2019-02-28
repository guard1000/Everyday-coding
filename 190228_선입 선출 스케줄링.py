def solution(n, cores):
    m = min(cores)
    start = m * n // len(cores)
    end = m * n
    mid = (start + end) // 2

    while (start < end):
        cnt = 0
        available = 0
        for i in cores:
            cnt += (mid // i) + 1
            if mid % i == 0:
                available += 1
                cnt -= 1

        if cnt >= n:
            end = mid
        elif cnt + available < n:
            start = mid + 1
        else:
            for i in range(len(cores)):
                if mid % cores[i] == 0:
                    cnt += 1
                if cnt == n:
                    return i + 1
        mid = (start + end) // 2

print(solution(6,[1,2,3]))
print(solution(22,[1,2,3,4,5]))
