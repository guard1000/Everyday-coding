def threeSum(nums):
    answer, sorted_num = [], sorted(nums)
    idx = 0
    while idx <= len(nums) - 3:
        l, r = idx + 1, len(nums) - 1
        if sorted_num[idx] + sorted_num[-1] + sorted_num[-2] < 0:
            idx += 1
            continue

        while l != r:
            if sorted_num[l] + sorted_num[r] < -sorted_num[idx]:
                l += 1
            else:
                if sorted_num[l] + sorted_num[r] == -sorted_num[idx] and [sorted_num[idx], sorted_num[l],
                                                                              sorted_num[r]] not in answer:
                    answer.append([sorted_num[idx], sorted_num[l], sorted_num[r]])
                r -= 1

        idx += 1

    return answer


print(threeSum([-1,0,1,2,-1,-4]))