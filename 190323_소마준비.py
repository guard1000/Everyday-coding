import re
print(re.sub('[^A-Za-z]+', '', input()).swapcase())

'''
item=[[1,4,7],[1,2,8],[7,2,4],[7,3,5],[7,3,2],[4,5,5]]
print(sorted(item, reverse=True, key=lambda x: (x[0],x[1],x[2])))
'''

'''
W = 6
item=[[4,7],[1,2],[2,4],[4,5]]

dp = [[0 for i in range(W+1)] for j in range(len(item)+1)]
for i in range(1,len(item)):
    for j in range(1,W+1):
        if item[i-1][0] < j:
            dp[i][j] = max(item[i-1][1]+dp[i][j-item[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[len(item)-1][W])
'''


'''
#이진
target =int(input())
left,right =0,1000000
cnt = 0
while left < right:
    mid = (left+right)//2
    print(left, mid, right)
    if mid == target:   break
    elif mid > target:
        right = mid-1
    elif mid < target:
        left = mid+1
    cnt += 1
print((left+right)//2)
print(cnt)
'''


'''
#삽입정렬
a= [5,3,1,7,4,98,10,15,47,91,46,53,74,11]
for i in range(1,len(a)):
    for j in range(i):
        if a[j] > a[i]:
            a[i],a[j]=a[j],a[i]
    print(i,a)
'''

'''
#선택정렬
a= [5,3,1,7,4,98,10,15,47,91,46,53,74,11]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]: a[i],a[j]=a[j],a[i]
    print(a)
'''
'''
#퀵소트
def bs(a):
    if len(a) <= 1: return a
    p = a[0]
    left,mid,right=[],[],[]
    for i in a:
        if i == p:  mid.append(i)
        elif i < p: left.append(i)
        else:   right.append(i)
    return bs(left)+mid+bs(right)

a= [1,3,5,7,4,98,10,15,47,91,46,53,74,11]
print(bs(a))
'''




'''
#다이아
N = int(input())
for i in range(1,N+1):
    for j in range(N-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*',end='')
    print()
for i in range(N-1,-1,-1):
    for j in range(N-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*',end='')
    print()
'''

'''
n = int(input())
answer=[]
while n > 0:
    a = n//2
    b = n%2
    answer.append(str(b))
    n = a
answer.reverse()
answer=''.join(answer)
print(answer)
'''



'''
#대소문자 바꾸기
str = input()
print(str.swapcase())
print(str.upper())
print(str.lower())
'''

'''
#소수 갯수 구하기
cnt = 0
for i in range(2,N+1):
    j=2
    while j<i:
        if i%j == 0:
            break
        j += 1
    if j == i:
        cnt += 1
print(cnt)
'''


'''
#다이아
for i in range(1,N+1):
    for j in range(N-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*',end='')
    print()
for i in range(N-1,-1,-1):
    for j in range(N-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*',end='')
    print()
'''