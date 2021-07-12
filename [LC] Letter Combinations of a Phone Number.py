import itertools
class Solution:
    def letterCombinations(digits):
        answer = []
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        answer = []
        digits = list(digits)

        idxs = [0, 1, 2, 3]
        if len(digits) == 1:
            answer = dic[digits[0]]

        elif len(digits) >= 2:
            mypermutation = itertools.product(idxs, repeat=len(digits))
            for myperm in mypermutation:  # (0, 3, 2)
                tmp, idx = '', 0
                while idx < len(digits) and len(dic[digits[idx]]) > myperm[idx]:
                    tmp += dic[digits[idx]][myperm[idx]]
                    idx += 1

                if idx == len(digits):
                    answer.append(tmp)

        return answer