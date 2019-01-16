def solution(arrangement):
    answer = 0
    stk=[]
    arrangement = list(arrangement)
    i=0
    while i < len(arrangement):       #len(arrangement)-1 번째 인덱스 까지만 조사
        if arrangement[i] == '(' and arrangement[i+1] == ')':   #()일때 - 레이저
            answer = answer + len(stk)
            i += 1
        elif arrangement[i] == '(':     # (일때 - 층 하나 더 쌓임. 스택에 추가
            stk.append(1)
        elif arrangement[i] == ')':     # )일때 - 층 하나 빠짐. 조각 하나 더 생기고, 스택에서 젤 윗층 하나 제거
            answer += 1
            stk.pop()
        i += 1

    return answer

arrangement="()(((()())(())()))(())"
print(solution(arrangement))