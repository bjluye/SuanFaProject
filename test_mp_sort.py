# -*- coding: utf-8 -*-
def mp_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[i]>nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums

nums = [12,35,99,18,76]
print(mp_sort(nums))