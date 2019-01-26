def solution(board, nums):
    answer = 0
    n = len(board)
    table = [[0 for i in range(n)] for j in range(n)]
    dic={}  #해쉬
    for i in range(n):
        for j in range(n):
            dic[board[i][j]] = [i,j]
    for i in nums:
            table[dic[i][0]][dic[i][1]] = 1
    for i in table: #가로
        if sum(i) == n:
            answer += 1
    for j in range(n): #세로
        tmp=0
        for i in range(n):
            if table[i][j] == 1:
                tmp += 1
            else: break
        if tmp == n:
            answer += 1
    tmp =0
    for i in range(n):  #대각선 \
        if table[i][i] == 1:
            tmp += 1
        else: break
    if tmp == n:
        answer += 1
    tmp = 0
    for i in range(n):  #대각선/
        if table[i][n-1-i] == 1:
            tmp += 1
        else:
            break
    if tmp == n:
        answer += 1

    return answer

print(solution([[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]], [14,3,2,4,13,1,16,11,5,15]))
print(solution([[6,15,17,14,23],[5,12,16,13,25],[21,4,2,1,22],[10,20,3,18,8],[11,9,19,24,7]],[15,7,2,25,9,16,12,18,5,4,10,13,20]))