def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0

    s = "_" + s
    counter_dic, char_list = {}, [0]
    answer = [0] * len(s)

    idx = 1
    while idx < len(s):
        if s[idx] not in counter_dic:
            counter_dic[s[idx]] = idx         # _pwwkew 일 때 -> w: 3
            char_list.append(s[idx]) #
        else:
            # counter_dic_inverse[counter_dic[s[idx]] + 1] : counter_dic[s[idx]] + 1 부터
            # counter_dic_inverse[idx] : idx 까지 세팅
            tmp_idx = counter_dic[s[idx]] + 1
            tmp_dic = {s[idx]:idx}
            while tmp_idx < idx:
                tmp_dic[s[tmp_idx]] = tmp_idx
                tmp_idx += 1
            counter_dic = tmp_dic
            char_list.append(s[idx])

        answer[idx] = max(answer[idx - 1], len(counter_dic))

        idx += 1

    return answer[-1]

"""
def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0

    s = "_" + s
    counter_dic, counter_dic_inverse = {}, {}
    answer = [0] * len(s)

    idx = 1
    while idx < len(s):
        if s[idx] not in counter_dic:
            counter_dic[s[idx]] = idx         # _pwwkew 일 때 -> w: 3
            counter_dic_inverse[idx] = s[idx] # _pwwkew 일 때 -> 3: w
        else:
            # counter_dic_inverse[counter_dic[s[idx]] + 1] : counter_dic[s[idx]] + 1 부터
            # counter_dic_inverse[idx] : idx 까지 세팅
            tmp_idx = counter_dic[s[idx]] + 1
            tmp_counter_dic = {s[idx] : idx}
            while tmp_idx < idx:
                tmp_counter_dic[counter_dic_inverse[tmp_idx]] = tmp_idx
                tmp_idx += 1
            counter_dic = tmp_counter_dic
            counter_dic_inverse[idx] = s[idx]

        answer[idx] = max(answer[idx - 1], len(counter_dic))

        idx += 1

    return answer[-1]
"""

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("dvdf"))