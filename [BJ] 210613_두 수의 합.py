# Sol2 - Two Pointers
n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

answer = 0
a = [_ for _ in a if _ < x]
l, r = 0, len(a)-1

while l != r:
    if a[l] + a[r] < x:
        l += 1
    else:
        if a[l] + a[r] == x:
            answer += 1
        r -= 1

print(answer)


"""
# Sol1 - combinations -> time limit!
import itertools

n = int(input())
a = list(map(int, input().split()))
x = int(input())

answer = 0
idxs = [_ for _ in range(n) if a[_] < x]
mycomb = itertools.combinations(idxs, 2)
for comb in mycomb:
    if a[comb[0]] + a[comb[1]] == x:
        answer += 1

print(answer)
"""

"""
9
5 12 7 10 9 1 2 3 11
13
"""
