'''
n=[21, 212]

n1=[int(str(i).ljust(4,'0')) for i in n]
n = sorted(n, reverse=True, key=lambda  x: int((str(x)+str(x)[0]).ljust(4,'0')))

print(n)

s='12354'
print(s+s[0])
'''

def solution(numbers):
    answer = ''
    numbers = sorted(numbers, reverse=True, key=lambda  x: (str(x)*2).ljust(4,'0'))
    for i in numbers:
        answer += str(i)
    if answer[0] == '0':    #모두 0인 경우 -> 테스트11
        return '0'
    return answer

n1 =[21, 212]
n2 = [3, 30, 34, 5, 9]
n3=[0,0,0,0]

print(solution(n1))
print(solution(n2))
print(solution(n3))
