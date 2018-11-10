import math
def solution(numbers):
    answer= solution2(numbers, '')
    return answer

def solution2(numbers,answer2):
    fmax = max(numbers, key=lambda x: x // (10 ** int(math.log10(x))))
    fmax = fmax // (10 ** int(math.log10(fmax)))
    tmplist = []
    for i in numbers:
        if (i // (10 ** int(math.log10(i)))) == fmax:
            tmplist.append(i)
    answer2 = answer2 + str(max(tmplist, key=lambda x: x % 10))
    numbers.remove(max(tmplist, key=lambda x: x % 10))
    if len(numbers) == 0:
        print(answer2)
        return answer2
    solution2(numbers,answer2)


numbers=[3, 30, 34, 5, 9]
print(solution(numbers))

'''
def func(hap, flist):
    if len(flist) == 0:
        alist.append(hap)
    else:
        fmax = max(flist, key=lambda x: x // (10 ** int(math.log10(x))))
        fmax = fmax // (10 ** int(math.log10(fmax)))
        tmplist=[]
        for i in flist:
            if (i // (10 ** int(math.log10(i)))) == fmax:
                tmplist.append(i)
        j = max(tmplist, key=lambda x: x %10)
        hap = hap * (10 ** ((int(math.log10(j))) + 1)) + j
        flist.remove(j)
        print(hap)      ##
        print(flist)    ##
        func(hap, flist)



numbers=[3, 30, 34, 5, 9]
solution(numbers)
'''

''' 람다 이용해서 앞자릿수 젤 큰놈 구하기
flist = [5, 6, 80, 91, 594]
fmax = max(flist, key=lambda x: x // (10 ** int(math.log10(x))))
fmax = fmax // (10 ** int(math.log10(fmax)))
for i in flist:
    if i // (10 ** int(math.log10(i))):
print(fmax)
'''