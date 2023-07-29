# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라

class Solution:
    def trap1(self, height: list[int]) -> int:
        if not height:
            return 0

        vol = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:

            if left_max <= right_max:
                vol += left_max - height[left]
                left += 1
            else:
                vol += right_max - height[right]
                right -= 1

            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
        return vol

    def trap2(self, height: list[int]) -> int:
        pass



c = Solution()

height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result1 = c.trap1(height1)
assert result1 == 6, 'result1 is {}, should return {}'.format(result1, 6)

height2 = [4, 2, 0, 3, 2, 5]
result2 = c.trap1(height2)
assert result2 == 9, 'result2 is {}, should return {}'.format(result2, 9)
