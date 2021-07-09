class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        s = list(s)
        # 짝수
        idx, n, answer = 1, 0, ''
        while idx < len(s):
            a, b = s[:idx], s[idx:]
            a.reverse()

            l = min(len(a), len(b))
            tmp = ''
            for i in range(l):
                if a[i] != b[i]:
                    break
                else:
                    tmp = a[i] + tmp + b[i]
            if len(tmp) > n:
                answer = tmp
                n = len(answer)
            idx += 1

        # 홀수
        idx = 1
        while idx < len(s):
            a, b = s[:idx], s[idx+1:]
            a.reverse()

            l = min(len(a), len(b))
            tmp = s[idx]
            for i in range(l):
                if a[i] != b[i]:
                    break
                else:
                    tmp = a[i] + tmp +b[i]
            if len(tmp) > n:
                answer = tmp
                n = len(answer)
            idx += 1

        if answer == '':
            return s[0]

        return answer