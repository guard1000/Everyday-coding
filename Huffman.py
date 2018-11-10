huff=[]
def huffman(huff, n):

    if len(huff) > 1:
        huff = sorted(huff, key=lambda x:x[len(x)-1])
        print(huff)     #돌아가는 모습 보여줌

        name = huff[0][0] + huff[1][0]
        value = huff[0][1] + huff[1][1]

        for a in huff[0][0]:
            for i in range(n):
                if a in inp[i][0]:
                    inp[i].append(0)
        for a in huff[1][0]:
            for i in range(n):
                if a in inp[i][0]:
                    inp[i].append(1)

        huff.append([name,value])
        huff.pop(0)
        huff.pop(0)

        huffman(huff, n)

    else:
        return 0


n = int(input('몇개의 원소가 있나요?'))  #입력 몇개?
inp = []
for i in range(n):      #입력
    print(i+1, end = '')
    a = input('번째의 입력 : [이름 값] ').split()
    a[1] = float(a[1])
    b = [a[0]]
    inp.append([b,a[1]])

print('처음 입력은\n', inp)
print('Huffman이 돌아갑니다.\n')
huffman(inp, n)

answer = []             #각 [이름, 코드]로 입력될 리스트
for i in range(n):      #값을 만들어 줍니다.
    val=''
    for j in range(len(inp[i])-1, 1, -1):
        val += str(inp[i][j])
    answer.append([inp[i][0][0],val])

print()         #한줄 띄어쓰기
for i in range(n):
    print(answer[i][0],'=',answer[i][1])
