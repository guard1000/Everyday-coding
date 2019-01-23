def solution(money):
    answer = 0
    n = len(money)
    if n == 3:  # 3개뿐이면 젤큰놈
        return max(money)
    start0 = [money[0], money[0]]  # 0번부터ㄱㄱ 하는 경우(맨 마지막 못먹음)
    start1 = [0, money[1]]  # 1번부터 ㄱㄱ 하는 경우

    # 2번 ~ n-2번 집까지는 2전과 지금을 먹는것과 직전을 먹는것 중 큰것을 택함
    for i in range(2, n - 1):
        start0.append(max(start0[i - 1], money[i] + start0[i - 2]))
        start1.append(max(start1[i - 1], money[i] + start1[i - 2]))

    # 마지막 집은 0번을 먹고 출발했을 경우 못먹음
    start1.append(max(start1[n - 2], money[n - 1] + start1[n - 3]))

    return max(start0[n - 2], start1[n - 1])


print(solution([1,2,3,1]))