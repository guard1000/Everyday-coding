# 파이썬 짱..
def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1

print(strStr("hello", "ll"))
print(strStr("aaaaa", "bba"))
print(strStr("", ""))