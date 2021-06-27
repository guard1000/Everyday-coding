import itertools
def candi_checker(id1, id2):  # (banned_id, user_id)
    if len(id1) != len(id2):
        return 0
    idx = 0
    while idx < len(id1):
        if id1[idx] != '*' and id1[idx] != id2[idx]:
            return 0
        idx += 1
    return 1


def solution(user_id, banned_id):
    answer = []
    idxs = [_ for _ in range(len(user_id))]
    # make board
    board = [[0 for j in range(len(user_id))] for i in range(len(banned_id))]
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            board[i][j] = candi_checker(banned_id[i], user_id[j])

    mypermutation = itertools.permutations(idxs,len(banned_id))
    for myperm in mypermutation:
        cnt = len(banned_id)
        for _ in range(len(banned_id)):
            if board[_][myperm[_]] == 1:
                cnt -= 1
                if cnt == 0:
                    answer.append(myperm)
            else:
                break

    answer = len(list(set([tuple(set(ans)) for ans in answer])))
    return answer



print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))