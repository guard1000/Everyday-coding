def trap(height):
    idx, answer = 0, 0
    while idx < len(height):
        now_h = height[idx]
        l_top = max(height[:idx]) if len(height[:idx]) > 0 else 0
        r_top = max(height[idx + 1:]) if len(height[idx + 1:]) > 0 else 0

        s = max(min(l_top, r_top) - now_h, 0)
        answer += s

        idx += 1

    return answer


"""
# 초안
# stack을 두고 단방향으로 서치하려 했음
# -> 320개 중 319개 통과, 마지막 Time Limit 

def trap(height):
    answer, idx, stack, tmp = 0, 0, [], {}

    while idx < len(height) and height[idx] == 0:
        idx += 1
    if idx == len(height):
        return 0

    while idx < len(height):
        if len(stack) == 0 and height[idx] != 0:
            for _ in range(height[idx], 0, -1):
                stack.append(_)
                tmp[_] = 0

        elif height[idx] == 0:
            for t in tmp:
                tmp[t] += 1

        else:
            while len(stack) != 0 and stack[-1] <= height[idx]:
                # 작은 것들 제거, answer +
                answer += tmp[stack[-1]]
                del (tmp[stack[-1]])
                stack.pop(-1)

                # 기존것들 보다 높은 것이 들어온 경우
                if len(stack) == 0:
                    for _ in range(height[idx], 0, -1):
                        stack.append(_)
                        tmp[_] = 0
                    break

                # 들어온 것보다 큰 것이 존재하던 경우
                if stack[-1] > height[idx]:
                    for t in tmp:
                        tmp[t] += 1
                    for _ in range(height[idx], 0, -1):
                        stack.append(_)
                        tmp[_] = 0
                    break

        print(idx, stack, tmp, answer)
        idx += 1

    return answer
"""
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
