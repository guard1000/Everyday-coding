def exist(board, word):
    m,n = len(board), len(board[0])
    candi, idx = [], 1
    dir_dic = {
        0: [[1,0], [-1,0],[0,-1], [0,1]], # 초기
        1: [[1,0], [0,-1], [0,1]],  # 상
        2: [[-1,0], [0,-1], [0,1]], # 하
        3: [[1,0], [-1,0], [0,1]],  # 좌
        4: [[1,0], [-1,0], [0,-1]]  # 우
    }
    dir_dic_nxt = {'[1, 0]': 1, '[-1, 0]': 2, '[0, 1]': 3, '[0, -1]': 4}

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                candi.append([[i,j,0]])
    # 시작이 없을 경우 제외
    if len(candi) == 0:
        return False
    # word가 1개일 경우
    if len(word) == 1:
        return True

    # 존재하지 않는지 확인
    for _ in range(len(word)):
        exist = False
        for i in range(m):
            if word[_] in board[i]:
                exist = True
                break
        if not exist:
            return False

    while idx < len(word):
        nxt_candi = []
        #print(candi)
        for cand in candi:
            pos_i, pos_j = cand[-1][0], cand[-1][1]
            checklist = dir_dic[cand[-1][-1]] # 확인해야 할 위치 리스트
            for check in checklist:
                nxt_i, nxt_j = pos_i + check[0],  pos_j + check[1]
                # 다음 char 발견
                if (-1 < nxt_i < m) and (-1 < nxt_j <n) and board[nxt_i][nxt_j] == word[idx] and [nxt_i, nxt_j] not in [_[:2] for _ in cand]:
                    nxt_candi.append(cand + [[nxt_i, nxt_j, dir_dic_nxt[str(check)]]])

        if len(nxt_candi) == 0:
            return False
        candi = nxt_candi
        idx += 1

    return True



#print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED'))
#print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'SEE'))
#print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB'))
#print(exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "aaaaaaaaaaaaa"))
#print(exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAB"))
