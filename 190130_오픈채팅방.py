def solution(record):   #해쉬
    answer = []
    n = len(record)
    dic = {}
    for i in range(n):
        record[i] = record[i].split(' ')
        if len(record[i]) == 3:
            dic[record[i][1]] = record[i][2]
    for i in range(n):
        if record[i][0] == 'Enter':
            answer.append(dic[record[i][1]]+'님이 들어왔습니다.')
        elif record[i][0] == 'Leave':
            answer.append(dic[record[i][1]]+'님이 나갔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))