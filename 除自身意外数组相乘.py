"""
该题目非常有趣，有几个细节需要注意，
1. 初始化应该为[0]
2. L[0] = 1 \ R[length - 1] = 1
"""
def productExceptSelf(nums: list[int]) -> list[int]:
    length = len(nums)
    # L 和 R 分别表示左侧所有元素的乘积和右侧所有元素的乘积
    L, R, answer = [0]*length, [0]*length, [0]*length

    # L[i] 为索引 i 左侧所有元素的乘积
    L[0] = 1
    for i in range(1, length):
        L[i] = nums[i - 1] * L[i - 1]

    # R[i] 为索引 i 右侧所有元素的乘积
    R[length - 1] = 1
    for i in reversed(range(length - 1)):
        R[i] = nums[i + 1] * R[i + 1]

    # 对于索引 i，除 nums[i] 之外其余各元素的乘积就是 L[i] 和 R[i] 的乘积
    for i in range(length):
        answer[i] = L[i] * R[i]

    return answer

# 示例测试
print(productExceptSelf([1,2,3,4]))  # 输出 [24,12,8,6]
