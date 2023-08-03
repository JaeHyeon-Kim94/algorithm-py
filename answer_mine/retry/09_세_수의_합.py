#

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)

        i: int = 0

        result: list[list[int]] = []

        for i in range(len(sorted_nums) - 2):
            if sorted_nums[i] > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            j = i + 1
            k = len(sorted_nums) - 1

            while j < k:
                sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]

                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    result.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])

                    while j < k and sorted_nums[j] == sorted_nums[j+1]:
                        j += 1
                    while j < k and sorted_nums[k] == sorted_nums[k-1]:
                        k -= 1

                    k -= 1
                    j += 1

        return result


c = Solution()

print(c.threeSum([-1,0,1,2,-1,-4]))
