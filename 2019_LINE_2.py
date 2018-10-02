import sys

Matrix = [[0] * 100 for i in range(100)]
Max = 0

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        split = sys.stdin.readline().strip().split(' ')
        x = int(split[0])
        y = int(split[1])
        w = int(split[2])
        h = int(split[3])
        for i in range(x, x + w + 1):
            for j in range(y, y + h + 1):
                Matrix[i][j] += 1

    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            if Matrix[i][j] > Max:
                Max = Matrix[i][j]

print(Max)