"""
该题目非常有趣，有几个细节需要注意，
1. 初始化应该为[0]
2. 计算右乘积，range的范围和数组的下标。
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # 数组长度
        length = len(nums)  

        # 初始化左乘积、右乘积和结果数组
        left, right, answer = [0]*length, [0]*length, [0]*length

        # 计算左乘积
        left[0] = 1  # 第一个元素左边没有其他元素，所以乘积为1
        for i in range(1, length):
            left[i] = left[i-1] * nums[i-1]

        # 计算右乘积
        right[length-1] = 1  # 最后一个元素右边没有其他元素，所以乘积为1
        for i in range(length-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        # 计算最终结果
        for i in range(length):
            answer[i] = left[i] * right[i]

        return answer


# 示例测试
print(productExceptSelf([1,2,3,4]))  # 输出 [24,12,8,6]
