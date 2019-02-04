import itertools

def chk(case, relation):
    test = set()
    for r in range(len(relation)):
        tmp = []
        for c in case:
            tmp.append(relation[r][c])
        test.add(tuple(tmp))
    if len(test) == len(relation):
        return True
    return False

def solution(relation):
    n = len(relation[0])
    num = [i for i in range(n)]
    cases = []
    for i in range(1, n + 1):
        combination = itertools.combinations(num, i)
        for comb in combination:
            cases.append(comb)
    answer = 0
    a = [0 for i in range(len(cases))]
    i = 0
    while i < len(cases):
        if a[i] == 1:
            i += 1
        elif chk(cases[i], relation):
            answer += 1
            j = i + 1
            while j < len(cases):
                if set.issubset(set(cases[i]), set(cases[j])):
                    a[j] = 1
                j += 1
            i += 1
        else:
            i += 1
    return answer

print(solution([[100,'ryan','music',2],[200,'apeach','math',2],[300,'tube','computer',3],[400,'con','computer',1],[500,'muzi','music',3],[600,'apeach','music',2]]))