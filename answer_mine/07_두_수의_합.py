# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

# input
#   nums = [2, 7, 11, 15], target = 9

# output
#   [0, 1]

class Solution(object):
    def two_sum3_1(self, nums: list[int], target: int) -> list[int]:
        valid_nums = [valid for valid in nums
                      if valid <= target]

        for idx, val in enumerate(valid_nums):
            diff = (target - val)
            if diff in valid_nums and valid_nums.index(diff) != idx:
                return sorted([valid_nums.index(target - val), idx])



    def two_sum3_2(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {}

        for idx, val in enumerate(nums):
            nums_dict[val] = idx

        for idx, val in enumerate(nums):
            if (target - val) in nums_dict and nums_dict[target - val] != idx:
                return [idx, nums_dict[target - val]]


    