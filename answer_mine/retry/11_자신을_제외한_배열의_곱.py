# Given an integer array nums, return an array answer such that answer[i] is equal to
# the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        left_multiply, right_multiply = [1]*len(nums), [1]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                left_multiply[i] = nums[i - 1] * left_multiply[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            else:
                right_multiply[i] = nums[i + 1] * right_multiply[i + 1]

        return [left_multiply[i] * right_multiply[i] for i in range(len(nums))]

s = Solution()

print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))