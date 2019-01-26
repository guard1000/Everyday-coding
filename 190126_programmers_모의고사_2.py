def binarysearch(s,e,v):
    mid = (s+e)//2
    if e == s+1:
        return s+1
    i = 0
    while i < len(v)-1:
        if i == len(v)-2 and v[i+1]-v[i] > mid:
            break
        if v[i+1] - v[i] > mid*2:
            break
        i += 1
    if i == len(v)-1:
        return binarysearch(s,mid,v)
    return binarysearch(mid,e,v)

def solution(l, v):
    v.sort()
    v += [l]
    return binarysearch(v[0]-1,l,v)


print(solution(15,[15,5,3,7,9,14,0]))
print(solution(5,[2,5]))