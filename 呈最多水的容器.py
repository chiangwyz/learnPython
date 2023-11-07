"""
初始化两个指针，一个在数组的开始位置（left），另一个在数组的末尾位置（right）。
初始化一个变量来存储最大的水量（max_water）。
当 left 指针在 right 指针的左边时，执行循环：
计算当前指针所指的两条线与 x 轴形成的容器的水量，它由两条线中较短一条的高度和两条线之间的距离（right - left）决定。
更新 max_water，如果当前水量大于 max_water 则替换。
移动两个指针中指向较短线条的那一个（因为容水量受限于较短的线条），如果两条线条高度相同，则可以同时移动 left 和 right。
当两个指针相遇时，循环结束，max_water 中存储的就是可以储存的最大水量。
"""
class Solution:
    def maxArea(self, height: list[int]) -> int:
        current_water = 0
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            current_water = (right - left) * min(height[right], height[left])

            max_water = max(max_water, current_water)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return max_water
