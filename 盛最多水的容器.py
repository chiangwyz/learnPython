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
        max_water = 0  # 初始化最大水量为0
        left, right = 0, len(height) - 1  # 设置双指针在数组的两端
        
        while left < right:  # 当左指针小于右指针时
            # 计算当前的水量，由较短的边界决定
            current_water = (right - left) * min(height[left], height[right])
            # 更新最大水量
            max_water = max(max_water, current_water)
            
            # 移动较短边界的指针，以寻找可能的更大容器
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water  # 返回最大水量
                
