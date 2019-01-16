def solution(brown, red):
    answer = []
    xlist = []
    i = 0
    for x in range(1, red + 1):
        if red % x == 0 and x not in xlist:
            xlist.append(red / x)

    for x2 in xlist:
        n = 1
        while 2 * x2 + 2 * (red / x2) - 4 + 8 * n <= brown:
            if 2 * x2 + 2 * (red / x2) - 4 + 8 * n == brown:
                i = x2 + n * 2
                break
            n = n + 1
        if i != 0:
            break

    answer.append(i)
    answer.append((brown + red) / answer[0])
    return answer