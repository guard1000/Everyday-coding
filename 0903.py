n, t, m, p = map(int, input().split())
# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p

def convert(n, base):               # 재귀를 활용해 10진수를 n진법으로 변환하는 함수
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

alist = []
answer = ""

for i in range(t*m):                # alist에 숫자열 append
    blist = list(convert(i, n))     # 각 숫자의 자릿수별로 삽입
    for j in range(len(blist)):
        alist.append(blist[j])

n = p-1                             # 튜브의 순서가 p니까 리스트 인덱스상으론 p-1번째부터!
for a in range(t):                  # t개의 숫자를 구해서 answer문자열에 이어붙임(+)
    answer = answer+alist[n]
    n = n+m                         # m명이 참여하고 있으므로 다음번은 n+m번째 인덱스의 값

print(answer)
