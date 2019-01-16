'''
Nlist = []
Mlist = []


def solution(M, N):
    tmp = []
    tmp2 = []
    for j in range(len(M)):  # M리스트의 원소로 tmp리스트를 만듬
        if M[j] != 0:
            for k in range(M[j]):
                tmp.append(j + 1)

    l = len(tmp)
    for j in range(len(N) - l + 1):
        tmp2 = N[j:j + l]
        tmp2.sort()
        if tmp == tmp2:
            return j + 1
    return 0


# 메인
n = int(input())  # 테스트케이스 몇개인지 입력받음
for i in range(n):
    N, M = map(int, input().split())  # N M 입력
    Mlist.append(list(map(int, input().split())))
    Nlist.append(list(map(int, input().split())))

for i in range(n):
    print('#', end='')
    print(i + 1, solution(Mlist[i], Nlist[i]))
'''

l = ['ede', 'ded']
if l[0] > l[1]:
    print(1)
else:
    print(2)