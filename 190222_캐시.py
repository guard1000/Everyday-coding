def solution(cacheSize, cities):
    if cacheSize==0: return len(cities)*5
    answer = 0
    cache=[-1 for i in range(cacheSize)]
    for c in range(len(cities)):
        cities[c] = cities[c].lower()
    city = list(set(cities))
    for c in range(len(cities)):
        cities[c] = city.index(cities[c])
    for c in cities:
        if c not in cache:
            answer += 5
            cache.append(c)
            cache = cache[1:]
        else:
            answer += 1
            cache.pop(cache.index(c))
            cache.append(c)
    return answer