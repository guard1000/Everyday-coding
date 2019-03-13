dir = {1: [-1, 0], 2: [1, 0], 3: [0, -1], 4: [0, 1]}


def round(N, hives):
    hives = move(hives)
    hives = meet_check(hives)
    hives = end_check(N, hives)
    return hives


def move(hives):  # 이동방향으로 한칸씩 움직이게 한다
    for h in range(len(hives)):
        hives[h][0], hives[h][1] = dir[hives[h][3]][0] + hives[h][0], dir[hives[h][3]][1] + hives[h][1]
    return hives


def end_check(N, hives):  # 없어지는것은 여기서만 가능. 수 반으로 떨구고 방향 바꿔줌
    h = 0
    while h < len(hives):
        if hives[h][0] in [0, N - 1] or hives[h][1] in [0, N - 1]:
            if hives[h][3] in [1, 2]:    hives[h][3] = 3 - hives[h][3]
            if hives[h][3] in [3, 4]:    hives[h][3] = 7 - hives[h][3]
            hives[h][2] = hives[h][2] // 2
            if hives[h][2] == 0:
                hives.pop(h)
                h -= 1
        h += 1
    return hives


def meet_check(hives):  # 만나면 반갑다고 뽀뽀뽀
    h = 0
    while h < len(hives):
        tmp = []
        i = 0
        for i in range(len(hives)):
            if hives[h][:2] == hives[i][:2]:
                tmp.append(hives[i])
        if len(tmp) > 1:  # 혼자가 아니야
            tmp = sorted(tmp, key=lambda x: x[2])  # 수 기준 정렬
            for j in range(len(tmp) - 1):
                tmp[-1][2] += tmp[j][2]
                hives.remove(tmp[j])
            h -= 1
        h += 1
    return hives


T = int(input())
for t in range(T):
    answer = 0
    hives = []
    N, M, K = map(int, input().split())
    for k in range(K):
        hives.append(list(map(int, input().split())))
    for m in range(M):
        hives = round(N, hives)
    for hive in hives:
        answer += hive[2]
    print('#', end='')
    print(t + 1, end=' ')
    print(answer)