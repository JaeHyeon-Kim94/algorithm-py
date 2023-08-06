# Given an integer array nums of 2n integers,
# group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
# such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

# 1 <= n <= 104
# nums.length == 2 * n
# -104 <= nums[i] <= 104

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)

        pairs: list[tuple] = []
        for i in range(0, len(sorted_nums)-1, 2):
            pairs.append((sorted_nums[i], sorted_nums[i+1]))

        sum: int = 0
        for pair in pairs:
            sum += pair[0]


        return sum


s = Solution()
print(s.arrayPairSum([6,2,6,5,1,2]))
