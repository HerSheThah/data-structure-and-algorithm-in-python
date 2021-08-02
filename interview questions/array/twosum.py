# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

def twoSum(nums, target):
    pairs={}
    for i in range(len(nums)):
        try:
            index=pairs[nums[i]]
            return [index, i]
        except KeyError:
            n=target-nums[i]
            pairs[n]=i
    return None


twoSum([3, 2, 4], 6)

# time --> o(n)
# space --> o(n)
