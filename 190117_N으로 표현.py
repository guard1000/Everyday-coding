def solution(N, number):
    answer = 1
    now = [N]
    nxt = []
    total=[]
    i = 1
    while answer < 9:
        i = i*10+1
        if N*i not in nxt:
            nxt.append(N*i)
        for num in now:
            if num + N not in nxt:
                nxt.append(num + N)
            if num - N not in nxt and num-N > 0:
                nxt.append(num - N)
            if num * N not in nxt:
                nxt.append(num * N)
            if num // N not in nxt:
                nxt.append(num // N)
        total.append(now)
        now = nxt[:]
        nxt.clear()
        answer += 1

    for i in range(4,9):
        for j in range(2, i//2+1):
            for num1 in total[j-1]:
                for num2 in total[i-j-1]:
                    if num1+num2 not in total[i-1]:
                        total[i-1].append(num1+num2)
                    if num1-num2>0 and num1-num2 not in total[i-1]:
                        total[i-1].append(num1-num2)
                    if num1*num2 not in total[i-1]:
                        total[i-1].append(num1*num2)
                    if num2 != 0 and num1//num2 not in total[i-1]:
                        total[i-1].append(num1//num2)
    answer=0
    while answer < 8:
        if number in total[answer]:
            return answer+1
        answer += 1
    return -1

#print(solution(5,12))
#print(solution(5,23))
#print(solution(5,27))
print(solution(5,56))
#print(solution(2,11))
