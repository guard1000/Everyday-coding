#프로그래머스_DP로 풀어보기
#https://programmers.co.kr/learn/courses/30/lessons/12905?language=python3
def solution(board):
    rows = len(board)
    cols = len(board[0])
    s = [[0 for col in range(cols)] for row in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if (board[i][j] == 1):
                s[i][j] = min(s[i][j-1], s[i-1][j], s[i-1][j-1])+1
            else:
                s[i][j] = 0
    answer=s[0][0]
    for i in range(rows):
        for j in range(cols):
            if answer < s[i][j]:
                answer = s[i][j]
    return answer**2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))