def solution(arrows):  # 오일러의 다면체 정리(2차원): f = 1+e-v
    nodes = set()
    edges = set()
    (x, y) = (0, 0)
    go = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    nodes.add((x, y))

    for a in arrows:
        for i in range(2):
            (x2, y2) = (x + go[a][0], y + go[a][1])
            nodes.add((x2, y2))
            if (x, y) > (x2, y2):
                edges.add(((x, y), (x2, y2)))
            else:
                edges.add(((x2, y2), (x, y)))
            (x, y) = (x2, y2)

    return 1 + len(edges) - len(nodes)