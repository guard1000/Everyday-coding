#2014313508 박천욱
print('Welcome to Gaussian Elimination!')
print()
print('a1x + b1y +c1z = d1')
print('a2x + b2y +c2z = d2')
print('a3x + b3y +c3z = d3\n')
nodap = 0
inp =[]     #입력
inp.append(list(input('a1 b1 c1 d1을 순서대로 입력해주세요').split()))
inp.append(list(input('a2 b2 c2 d2을 순서대로 입력해주세요').split()))
inp.append(list(input('a3 b3 c3 d3을 순서대로 입력해주세요').split()))

for i in range(3):      #형변환
    for j in range(4):
        inp[i][j] = int(inp[i][j])
print(inp)
print()

print('STEP 1')
for i in range(1,3):
    if inp[0][0] != 0:
        tmp = (inp[i][0] / inp[0][0])
        for j in range(4):
            inp[i][j] = inp[i][j] - (inp[0][j]*tmp)
print(inp)
print()

print('STEP 2')
if inp[1][1] != 0:
    tmp = (inp[2][1] / inp[1][1])
    for j in range(4):
        inp[2][j] = inp[2][j] - (inp[1][j]*tmp)
print(inp)
print()

print('STEP 3')
for i in range(1,-1, -1):
    if inp[2][2] != 0:
        tmp = (inp[i][2] / inp[2][2])
        for j in range(4):
            inp[i][j] = inp[i][j] - (inp[2][j]*tmp)
print(inp)
print()

print('STEP 4')
if inp[1][1] != 0:
    tmp = (inp[0][1] / inp[1][1])
    for j in range(4):
        inp[0][j] = inp[0][j] - (inp[1][j]*tmp)
print(inp)
print()

print('STEP 5 - 완성형')
for i in range(3):
    if inp[i][i] != 0:
        inp[i][3] = inp[i][3] / inp[i][i]
        inp[i][i] = 1.0
        print(inp[i])
    else:
        nodap = 1

print()
if nodap == 0:
    print('x =', inp[0][3])
    print('y =', inp[1][3])
    print('z =', inp[2][3])
else:
    print('해가 없는 식이군요!')
