def printPost(inn, pre, inStrt, inEnd):
    global preIndex, hm
    if (inStrt > inEnd):
        return
    # Find index of next item in preorder traversal in
    # inorder.
    inIndex = hm[pre[preIndex]]
    preIndex += 1

    # traverse left tree
    printPost(inn, pre, inStrt, inIndex - 1)

    # traverse right tree
    printPost(inn, pre, inIndex + 1, inEnd)

    # prroot node at the end of traversal
    print(inn[inIndex], end=" ")


def printPostMain(inn, pre, n):
    for i in range(n):
        hm[inn[i]] = i

    printPost(inn, pre, 0, n - 1)
    print()

inp_cnt, inp_pre, inp_in = [], [], []

N = int(input())
for _ in range(N):
    inp_cnt.append(int(input()))
    inp_pre.append(list(map(int, input().split())))
    inp_in.append(list(map(int, input().split())))

for _ in range(N):
    hm = {}
    preIndex = 0
    inn, pre = inp_in[_], inp_pre[_]
    n = len(pre)
    printPostMain(inn, pre, n)


'''
2
4
3 2 1 4
2 3 4 1
8
3 6 5 4 8 7 1 2
5 6 8 4 3 1 2 7
'''