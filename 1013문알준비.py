'''
print([num * 3 for num in range(3)])

print([num * 3 for num in range(10) if num % 2 == 0])

print([x * y for x in range(2, 10) for y in range(1, 10)])
'''
# 실습 1
for i in range(5):  # 혹은 (1,6):
    for j in range(5-i):
        print('*', end='')
    print("")


#실습 2번
print('1번')
num = [1,2,3,4,5,6,7,8,9,10]
result = [n*2 for n in num if n%2]

print(result, '\n')

print('2번')
vowels = 'aeiou'
sentence = 'Do not learn English, but learn Python.'

print(''.join([a for a in sentence if a not in vowels]))
#print(' '.join([a for a in sentence if a.lower() not in vowels]))


#과제 - f
score= [20,55,67,82,45,33,90,87,100,25]
total = 0
count = 0

while len(score) != 0:
    mark = score.pop()
    if mark >= 50:
        total += mark
        count += 1
print('총합: {0}, 평균 {1:0.2f}'.format(total, total/count))
