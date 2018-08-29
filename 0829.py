import itertools # 사전식배열을 위해 임포트

N = int(input())
tlist=input().split()
answer = 0
tmp = 0

for i in range(N):
    answer += (N-i)*int(tlist[i])

mypermuatation = itertools.permutations(tlist)
for s in mypermuatation:
    for j in range(N):
        tmp += (N-j)*int(s[j])

    if tmp < answer:
        answer = tmp
    tmp = 0

print(answer)