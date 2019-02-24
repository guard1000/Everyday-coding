def solution(dartResult):
    tmp=[0]
    dartsplit=[]
    calc=[]
    i=2
    while i < len(dartResult):  #문자열 쪼개기
        if '0' <= dartResult[i] <= '9':
            dartsplit.append(dartResult[tmp[-1]:i])
            tmp.append(i)
            if len(dartsplit) == 2:
                dartsplit.append(dartResult[i:])
                break
            i += 2
        else:
            i += 1
    for i in range(3):
        if dartsplit[i][1] =='0':   #10
            calc.append(10)
        else:   #0-9
            calc.append(int(dartsplit[i][0]))
        if 'D' in dartsplit[i]: #double
            calc[i] **= 2
        elif 'T' in dartsplit[i]: #triple
            calc[i] **= 3
        if '#' in dartsplit[i]: # -
            calc[i] *= -1
        elif '*' in dartsplit[i] and i != 0: # *
            calc[i-1] *= 2
            calc[i] *= 2
        elif '*' in dartsplit[i]:
            calc[i] *= 2
    return sum(calc)