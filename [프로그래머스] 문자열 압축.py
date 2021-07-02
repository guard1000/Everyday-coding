def counter(s, n):
    s = [s[i:i + n] for i in range(0, len(s), n)]
    idx, tmp_val, tmp_cnt, dic = 0, '', 0, {}
    while idx < len(s):
        if s[idx] != tmp_val:
            key = str(idx) + '_' + s[idx]
            dic[key] = 1
            tmp_val = s[idx]
            tmp_cnt = 1
        else:
            key = str(idx - tmp_cnt) + '_' + s[idx]
            dic[key] += 1
            tmp_cnt += 1
        idx += 1

    countval = 0
    for key in dic:
        countval += len(key.split('_')[-1])
        if dic[key] != 1:
            countval += len(str(dic[key]))

    return countval


def solution(s):
    if len(s) == 1:
        return 1

    answer = 1000
    for n in range(1, len(s)//2 + 1):
        ans = counter(s, n)
        if ans < answer:
            answer = ans

    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
