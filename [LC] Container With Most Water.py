# sol 2 - two pointers
def maxArea(height):
    answer = 0
    l, r = 0, len(height) - 1

    while l < r:
        tmp = (r - l) * min(height[l], height[r])
        if tmp > answer:
            answer = tmp
        if height[l] >= height[r]:
            r -= 1
        else:
            l += 1

    return answer

print(maxArea([1,8,6,2,5,4,8,3,7]))