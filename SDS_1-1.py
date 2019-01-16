answer = []

def card():
    n = int(input())  # #몇개의 카드인지 저장
    inp = input().split()  # 카드 정보 저장
    ans = inp[0]
    for i in range(1, len(inp)):
        if ans + inp[i] > inp[i] + ans:
            ans = ans + inp[i]
        else:
            ans = inp[i] + ans
    return ans

# 메인
N = int(input())  # N개의 인풋
for i in range(N):
    answer.append(card())

for i in range(N):
    print('#', end='')
    print(i + 1, answer[i])